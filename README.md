# proxy-ip-scrapper
A scrapper for scrapping Proxy-IP list from different websites

# Goal
1. Scrap data from various sources, which provide open Proxy IP lists, and keep that data into our database
   each IP should have 
```json
[
{
"ip": "1.2.3.4",
"time-last-updated": "141232232", 
"country(if available)": "IND",
"health": "something"
}
{
 "ip": "5.6.7.8",
 "time-last-updated": "141243232", 
 "country(if available)": "USA",
 "health": "something"
}
]
```
   
2. To create an API endpoint, which gives list of Proxy IPs, scrapped from various open lists, also can be queried by country. 

# Design
For each website we track and scrap, we run a worker, which get's the latest website, parse that data, and pushes data to db (or in memory db if we have much higher i/o). 
The API endpoints would get the data for the request from db, and give it. 

# Componenets
Django - for overall framework
djagorestframework - for API endpoint related stuff
celery - for running tasks in workers
selenium - if we can't get data from directly a GET request, we would simulate a browser instance to get the website data
beautifulsoup - to parse the data we get from website
