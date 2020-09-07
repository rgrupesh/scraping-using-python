from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://news.ycombinator.com/").text

soup = BeautifulSoup(source,"lxml")

csv_file = open("hacker_news.csv","w")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["headline", "link"])

for item in soup.find_all("td", "title"):

    try:
        heading = item.a.text
        print(heading)
        links = item.find("a", class_="storylink")["href"]
        print(links)
        print()
    except Exception as e:
        heading = None
        links = None

    csv_writer.writerow([heading,links])    

csv_file.close()    


