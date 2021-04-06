import math
import requests
from bs4 import BeautifulSoup

baseURL = "https://ae.indeed.com/jobs?l=Abu+Dhabi&limit=50"

r = requests.get(baseURL)

soup = BeautifulSoup(r.text, features="html.parser")
countElement = soup.find("div", {"id": "searchCountPages"})
jobsCount = int(countElement.text.strip().split(' ')[3].replace(',', ''))
pageCount = math.ceil(jobsCount / 50)

for i in range(pageCount):
    page = requests.get(baseURL + "&start={}".format(i * 50))
    pageSoup = BeautifulSoup(page.text, features="html.parser")
    jobs = pageSoup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    print("Page no: {}".format(i), jobs)
# print(jobsCount, pageCount)
