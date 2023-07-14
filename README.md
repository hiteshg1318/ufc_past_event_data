# ufc_past_event_data
This is a web-scrapping script to scrape UFC past event data.

1. First thing first, Check the number of pages that exist for the past events. When this script was written, there are 81 pages in total that contained the past events.
# How to check the number of pages
Go the the below URL and relpace the +str(i) with number ex 91 and check if the the page exist. If the page exist try a greater number else try a smaller number. Find that number were the last page exist. Replace 81 with the number in the for loop. And you are good to go. 
url = 'https://www.ufc.com/events?page='+str(i)

2. If the above step is done. Run the Code block by block. Scrapping may take time as there are thousands of records.
