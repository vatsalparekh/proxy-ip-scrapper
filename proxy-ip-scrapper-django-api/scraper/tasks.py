from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger


from home.models import IPdata

from selenium import webdriver
from bs4 import BeautifulSoup
import time, re


###################FOR DEMO PURPOSE####################
urls = ["https://free-proxy-list.net"]


    #urls = ["https://free-proxy-list.net","https://free-proxy-list.net/uk-proxy.html",
    #       "https://www.us-proxy.org","https://www.sslproxies.org","https://premproxy.com/list",
    #       "http://nntime.com/","https://hidemy.name/en/proxy-list/","http://free-proxy.cz",
    #       "https://hidester.com/proxylist/","https://nordvpn.com/free-proxy-list/",
    #       "https://www.hide-my-ip.com/proxylist.shtml","http://www.httptunnel.ge/ProxyListForFree.aspx"]



id_tags_name = ["proxylisttable", "proxylisttable", "proxylisttable", "proxylisttable", "proxylist", "proxylist",
                    "", "proxy_list", "", "", "sort-list", "ctl00_ContentPlaceHolder1_GridViewNEW"]

class_name = ["", "", "", "", "", "", "proxy__t", "", "table table-hover",
                  "table table-bordered table-hover table-hover proxy-list-table", "", ""]

ip_seq = [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1]
port_seq = [1, 1, 1, 1, 20, 20, 1, 1, 2, 2, 1, 20, 2, 2, 2]
country_seq = [3, 3, 3, 3, 3, 4, 2, 3, 3, 0, 2, 20, 4, 4, 4]
anon_seq = [4, 4, 4, 4, 1, 2, 5, 6, 7, 20, 5, 20, 3, 3, 5]
https_seq = [6, 6, 6, 6, 20, 20, 4, 2, 4, 3, 4, 20, 6, 6, 6]
pages = [15, 5, 10, 5, 20, 18, 36, 9, 5, 15, 18, 1, 2, 6, 2]



logger = get_task_logger(__name__)

@periodic_task(
    run_every=(crontab(minute='*/3')),
    name="scraping data and pushing to database",
    ignore_result=True)
def main():
    url_index = 0
    while (url_index < len(urls)):
        call_browser(url_index)
        url_index += 1



def extract_data(data, url_index):
    if data:  # if data isn't empty, data exists
        iseq = ip_seq[url_index]
        ps = port_seq[url_index]
        cs = country_seq[url_index]
        aseq = anon_seq[url_index]
        hs = https_seq[url_index]
        i = 0
        while (i < len(data)):
            if data[i] and len(data[i]) > 3:  # length>3 to avoid adsbygoogle

                ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', data[i][iseq])[0]  # [0] to avoid having ip list

                if ps != 20:
                    port = data[i][ps]
                else:
                    s = data[i][iseq].split(":")
                    port = s[len(s) - 1]

                country = data[i][cs] if cs != 20 else "Not specified"
                anon = data[i][aseq] if aseq != 20 else "Not specified"
                if hs != 20:
                    upper = data[i][hs].upper()
                    https = "yes" if upper.find("HTTPS") != -1 or upper.find("YES") != -1 else "no"
                else:
                    https = "Not specified"

                print(ip, port, country, anon, https)
                #writer.writerow([ip, country, port, anon, https, datetime.now()])

                #####################################
                list_of_all_ip = IPdata.objects.values_list('ip_address', flat=True)
                if ip in list_of_all_ip:
                    existing_object = IPdata.objects.filter(ip_address=ip)[0]
                    existing_object.port_no = port
                    existing_object.country = country
                    existing_object.anonymity = anon
                    existing_object.HTTPS = https
                    existing_object.save()
                else:
                    new_object = IPdata()
                    new_object.ip_address = ip
                    new_object.port_no = port
                    new_object.country = country
                    new_object.anonymity = anon
                    new_object.HTTPS = https
                    new_object.save()


            i += 1


def parse(browser, url_index):
    time.sleep(7)
    soup = BeautifulSoup(browser.page_source, "html.parser")

    if not id_tags_name[url_index]:  # if id tag is empty
        attrib = "class"
        value = class_name[url_index]
    else:
        attrib = "id"
        value = id_tags_name[url_index]

    table = soup.find('table', attrs={attrib: value})
    table_body = table.find('tbody')
    rows = table_body.find_all("tr")

    data = []  # to store table here
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols])

    return data


def call_browser(url_index):
    
    browser = webdriver.Chrome()

    browser.get(urls[url_index])
    data = parse(browser, url_index)

    extract_data(data, url_index)

    page_index = 2
    while (page_index <= pages[url_index]):
        try:
            if (url_index == 9):
                browser.find_element_by_link_text('Load more').click()
            else:
                browser.find_element_by_link_text(str(page_index)).click()

            data = parse(browser, url_index)
            extract_data(data, url_index)
        except:
            print("Error: No such element exception.")

        page_index += 1

    browser.quit()
