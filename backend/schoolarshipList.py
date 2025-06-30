import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import json

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

service = Service(EdgeChromiumDriverManager().install())

# 建立 driver
driver = webdriver.Edge(service=service, options=options)
html = "https://www.edu.tw/helpdreams/Grants.aspx?n=2BBF7170197CE7D3&sms=0A01A72AAB9E5CD4"
driver.get(html)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')
schoolarshipsData = soup.find_all("td")

schoolarshipTags = [
    "ContentPlaceHolder1_divName",
    "ContentPlaceHolder1_divSchoolSystem",
    "ContentPlaceHolder1_divGrade",
    "ContentPlaceHolder1_divIdentity",
    "ContentPlaceHolder1_divQualification",
    "ContentPlaceHolder1_divAddress",
    "ContentPlaceHolder1_divSchool",
    "ContentPlaceHolder1_divOther",
    "ContentPlaceHolder1_divDate",
    "ContentPlaceHolder1_divContent"
]

schoolarshipSchoolSystem = ["大學院校", "大專院校"]

allData = [] 


for i in range(0, len(schoolarshipsData), 3):
    schoolarshipLink = "https://www.edu.tw/helpdreams/" + schoolarshipsData[i].find("a")["href"].strip()
    driver.get(schoolarshipLink)
    time.sleep(1.5)

    soup2 = BeautifulSoup(driver.page_source, 'html.parser')
    schoolarshipDetails = soup2.find("div", class_="data_midlle")

    schoolarSchool_div = soup2.find("div", id="ContentPlaceHolder1_divSchoolSystem")
    schoolarSchool = schoolarSchool_div.find("div", class_="content").text.strip()

    if any(keyword in schoolarSchool for keyword in schoolarshipSchoolSystem):
        schoolarshipDetailsData = {}

        for tag in schoolarshipTags:
            tag_div = schoolarshipDetails.find("div", id=tag)
            if tag_div:
                content_div = tag_div.find("div", class_="content")
                schoolarshipDetailsData[tag] = content_div.text.strip() if content_div else "無資料"
            else:
                schoolarshipDetailsData[tag] = "無資料"

        url_div = schoolarshipDetails.find("div", id="ContentPlaceHolder1_divtUrl")
        if url_div:
            url_link = url_div.find("a")
            schoolarshipDetailsData["ContentPlaceHolder1_divtUrl"] = url_link.get("href") if url_link else "無資料"
        else:
            schoolarshipDetailsData["ContentPlaceHolder1_divtUrl"] = "無資料"

        allData.append(schoolarshipDetailsData)

with open("schoolarshipLink.json", "w", encoding="utf-8") as f:
    json.dump(allData, f, ensure_ascii=False, indent=4)

driver.quit()
