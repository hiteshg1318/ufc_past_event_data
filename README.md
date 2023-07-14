# ufc_past_event_data
This is a web-scraping script to scrape UFC past event data.

1. First things first, Check the number of pages that exist for past events. When this script was written, there were 81 pages in total that contained past events.
*How to check the number of pages
Go to the below URL and replace the +str(i) with a number, ex. 91, and check if the page exists. If the page exists, try a greater number; otherwise, try a smaller number. Find the number where the last page exists. Replace 81 with the number in the for loop. And you are good to go. 
url = 'https://www.ufc.com/events?page='+str(i)

3. If the above step is done, Run the Code block by block. Scrapping may take time as there are thousands of records.
