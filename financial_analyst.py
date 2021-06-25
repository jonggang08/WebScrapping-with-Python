import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.jobstreet.com.sg/en/job-search/financial-analyst-jobs/"

def extract_job(result):
    title = result.find("div",{"class":"FYwKg _2j8fZ_0 sIMFL_0 _1JtWu_0"}).text
    company = result.find("span",{"class":"FYwKg _3MPd_ _2Bz3E And8z"}).text
    skills = result.find_all("dd",{"class":"FYwKg PrHFr"})
    skill = []
    for i in skills:
        data = i.text
        skill.append(data)
    return {'title': title, 'company': company,'Skills': skill[:-1] , 'Job Type': skill[-1]}


def extract_jobs(lastpage):
    joblist=[]
    for page in range(lastpage):
        print(f"Scrapping SO:Page:{page}")
        result = requests.get(f'{url}{page}/')
        soup = BeautifulSoup(result.text,'html.parser')
        results = soup.find_all("div",{"class":"FYwKg _17IyL_0 _2-ij9_0 _3Vcu7_0 MtsXR_0"})
        for result in results:
            job = extract_job(result)
            joblist.append(job)
    return joblist

data = extract_jobs(10)

df = pd.DataFrame(data)
df.to_csv('financial_analyst.csv')