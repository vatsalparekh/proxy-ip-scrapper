# proxy-ip-scrapper
A scrapper for scrapping Proxy-IP list from different websites

# Goal
To create an API, which gives list of Proxy IPs, scrapped from various open lists such as hidemyass and more. 

# Design
Run a celery task for each sites on our list, then to scrap that result and push that latests dump into a db, or a cache such as redis. 
For GET API requests, give that dump from the cache. 
