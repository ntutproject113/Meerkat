import bs4
from major import getMajor
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

options = Options()
options.add_argument("--headless")  
options.add_argument("--disable-gpu")
service = Service(EdgeChromiumDriverManager().install())

# 建立 driver
driver = webdriver.Edge(service=service, options=options)

majorInfo = getMajor(driver)
courseTypeCH = {
    "○": "部訂共同必修",
    "△": "校訂共同必修",
    "☆": "共同選修",
    "●": "部訂專業必修",
    "▲": "校訂專業必修",
    "★": "專業選修"
}
allData = []

for majorURL, majorName in majorInfo:
    driver.get(majorURL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
    html = driver.page_source
    courseRoot = bs4.BeautifulSoup(html, "html.parser")
    table=courseRoot.find("table")
    courseData = []
    trs=table.find_all("tr")
    for tr in trs:
        tds = tr.find_all("td")
        if len(tds) >= 5:
            courseYear=tds[0].text.strip()
            courseSemester=tds[1].text.strip()
            courseTypeSymbol=tds[2].text.strip()
            courseType=courseTypeCH.get(courseTypeSymbol, "未知類別")
            courseName=tds[4].text.strip()
            courseData.append({
            "year":courseYear,
            "semester":courseSemester,
            "type":courseType,
            "name":courseName
            })
          
    allData.append({
        "major": majorName,
        "course": courseData
    })

try:
    with open("courses.json", "w", encoding="utf-8") as f:
        json.dump(allData, f, ensure_ascii=False, indent=4)
    print("資料已成功儲存到 courses.json！")
except Exception as e:
    print("轉換 JSON 時出錯：", e)

driver.quit()
