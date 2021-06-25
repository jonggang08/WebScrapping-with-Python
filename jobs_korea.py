import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = "https://www.saramin.co.kr/zf_user/jobs/list/domestic?"

def getjob(result):
    title = result.find("a",{"class":"str_tit"}).text
    sector = result.find("span",{"class":"job_sector"}).text.strip()
    condition = result.find("div",{"class":"col recruit_condition"}).text.strip()
    try:
        location = result.find("p",{"class":"work_place"}).text
    except:
        location = "No Location"
    type = result.find("p",{"class":"employment_type"}).text
    return {"Title": title, "Sector": sector, "Condition": condition, "Location": location, "Type":type}

def get_jobs(lastpage):
    joblist = []
    for page in range(lastpage):
        print(f"Scrapping SO:Page:{page+1}")
        result = requests.get(f"{url}&page={page+1}")
        soup = BeautifulSoup(result.text,'html.parser')
        results = soup.find_all("div",{"class":"list_item"})
        for jobs in results:
            job = getjob(jobs)
            joblist.append(job)
    return joblist
    
lastpage = 20

data = pd.DataFrame(get_jobs(lastpage))
data.to_csv("jobs_Korea.csv")

print(data)






