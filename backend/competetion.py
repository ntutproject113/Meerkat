import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import json
options= Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=options)
url="https://bhuntr.com/tw/competitions?page=[page]"
allData = []
for page in range(1, 3):
    driver.get(url)
    time.sleep(5) 
    html=driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    cpTag = soup.find_all("div", class_="bh-container")
    cpTable= soup.find("div", class_="row bh-section bh-card-list")
    cpColumn = soup.find_all("div", class_="col-lg-3 col-md-4 col-sm-6 col-12 bh-card-item")
    for cpBlock in cpColumn:
        cpName = cpBlock.find("a", class_="bh-title").text.strip()
        cpContent = cpBlock.find("span", class_="bh-item is-processing").text.strip()
        cpLink ="https://bhuntr.com"+cpBlock.find("a", class_="bh-title")["href"]
        cpPrizeTag= cpBlock.find("div", class_="bh-item bh-item-top")
        cpPrize = cpPrizeTag.find("span", class_="bh-amount").text.strip() 
        #最高獎金
        cpData = {}
        cpData["competetion"] = cpName
        cpData["content"] = cpContent
        cpData["link"] = cpLink
        cpData["prize"] = cpPrize
        allData.append(cpData)
with open("competition.json", "w", encoding="utf-8") as f:
    json.dump(allData, f, ensure_ascii=False, indent=2)        
driver.quit()
