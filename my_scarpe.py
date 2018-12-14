#STEP 1: COMMAND PROMPT
#STEP 2: TYPE PYTHON3 OR PY3 OR PYTHON
#STEP 3: IMPORT REQUESTS
#STEP 4: IF YOU DONT GET ANY ERRORS,SKIP STEP 4 OR ELSE quit() then use command pip3 install requests
#STEP 5: WE USE TWO LIBRARIES HERE REQUEST FOR GETTING CONTENTS OF WEBSITES THEN BEAUTIFULSOUP A GLOBAL USED LIBRARY
#STEP 6: pip3 install requests, pip3 install lxml, pip3 html5lib ,pip3 install beautifulsoup4 or pip3 install bs4
#STEP 7: we will open our target website and convert it into a html file using lxml parser
from bs4 import BeautifulSoup
import requests
#STEP 8: THEN WE CAN VIEW THE WEBSITE HTML FORMAT BY PARSING THE WEBSITE AND USING PREETIFY() METHOD WE CAN GET A INTENDED HTML FILE INTENDED
#with open('') as html_file:
    #soup = BeautifulSoup(html_file,'lxml')
#STEP 9: WE CAN USE ATTRIBUTES TO GET ANY PARTICULAR PARTS OF HTML FROM WEBSITE
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_my_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline'])

for section in soup.find_all('a', href =True ):
    headline = section['href']
    
    if headline.startswith('#'):
        pass;
    elif headline.startswith('https:'):
        print(headline)
    else:
        pass;
    #summary = section.find('div', class_='showcase section-height__medium').text
    #print(summary)
     
    #try:
        #vid_src = article.find('iframe', class_='youtube-player')['src']
        #vid_id = vid_src.split('/')[4]
        #vid_id = vid_id.split('?')[0]
        #yt_link = f'https://youtube.com/watch?v={vid_id}'
    #except Exception as e:
        #yt_link = None

    #print(yt_link)

    print()

    csv_writer.writerow([headline])

csv_file.close()

