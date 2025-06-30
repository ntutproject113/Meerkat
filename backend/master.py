import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import json
import re

url = "https://www.reallygood.com.tw/newExam/inside?str=0AB98C37435A1716A3CA5BFEF5596942"

options = Options()
options.add_argument("--headless")  # 無頭模式，不開啟視窗
options.add_argument("--disable-gpu")
options.use_chromium = True
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=options)
driver.get(url)
time.sleep(5)  # 等待網頁完整載入

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, "html.parser")

exclude_keywords = ["台灣聯合大學系統(中央、政治、清大、陽明交大)𝐍𝐄𝐖"]

# 如果 HTML 中包含排除關鍵字，跳過後續
if any(keyword in soup.prettify() for keyword in exclude_keywords):
    print("包含排除關鍵字，跳過")
else:
    # 先移除所有 <span> 
    for span in soup.find_all("span"):
        span.decompose()
    # 使用正規表達式抓取學校名稱、內容塊、連結
    pattern = re.compile(
        r'<h3.*?>(.*?)</h3>\n(.*?)考試簡章.*?<a href="(.*?)".*?>',
        re.DOTALL
    )
    matches = re.findall(pattern, soup.prettify())
    
    # 清洗HTML
    def clean_html(raw_html):
        clean_text = BeautifulSoup(raw_html, "html.parser").get_text(separator="\n")
        # 去除多餘空白行、前後空白和換行
        lines = [line.strip() for line in clean_text.splitlines() if line.strip() != '']
        return "".join(lines)

    results = []
    for name_raw, content_raw, link in matches:
        name = name_raw.strip()  # 去除前後空白與換行
        content = clean_html(content_raw)
        content_list = [part.strip("▋") for part in content.split("▋") if part.strip()]     
        
        results.append({
            "school": name,
            "content": content_list,
            "link": link.strip()
        })
    json_output = json.dumps(results, ensure_ascii=False, indent=2)
with open("master.json", "w", encoding="utf-8") as f:
    f.write(json_output)
    
 
