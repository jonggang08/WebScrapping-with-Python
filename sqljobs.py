import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url="https://stackoverflow.com/jobs?q=sql"

def extract_job(job):
    title = job.find("h2", {"class": "mb4"}).text.strip()
    comloc = job.find("span",{"class":"fc-black-500"}).text.strip()
    info = job.find("ul",{"class":"mt4 fs-caption fc-black-500 horizontal-list"}).find_all("li",recursive=False)
    day = info[0].text
    return {'title': title, 'Company': comloc,"Day":day}

def extract_jobs(lastpage):
    joblist = []
    for page in range(lastpage):
        print(f"Scrapping SO:Page:{page}")
        result = requests.get(f"{url}&pg={page+1}")
        soup = BeautifulSoup(result.text,'html.parser')
        results = soup.find_all("div",{"class":"-job"})
        for job in results:
            jobs = extract_job(job)
            joblist.append(jobs)
    return joblist

data = extract_jobs(9)

df=pd.DataFrame(data)
df.to_csv("sql.csv")

print(df)
