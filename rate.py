import math
import requests
from bs4 import BeautifulSoup
import time

start_time = time.time()

baseURL = "https://ae.indeed.com/jobs?l=Abu+Dhabi&limit=50"

i = 0
while True:
    i = i + 1
    try:
        r = requests.get(baseURL)
        soup = BeautifulSoup(r.text, features="html.parser")
        title = soup.find("title").text
        if "Captcha" in title:
            print(title, " Index: ", i)
            break
        print(title, " Index: ", i)
        time.sleep(4)
    except Exception as e:
        print(e)
        end_time = time.time() - start_time

        print("Total requests: ", i, "In total time: ", end_time)
        print("Requests/min: ", i / end_time * 60)
end_time = time.time() - start_time
print("Total requests: ", i, "In total time: ", end_time)
print("Requests/min: ", i / end_time / 60)
# print(jobsCount, pageCount)
