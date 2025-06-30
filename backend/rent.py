import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import json
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
service = Service(EdgeChromiumDriverManager().install())

# 建立 driver
driver = webdriver.Edge(service=service, options=options)
houseRawData = []
url0="https://rent.houseprice.tw/list/21_usage/5-10-8-12-9-3-7-4-6-1-2-11_zip/?p={page}"
'''1 中正 2 大同 3中山 4松山 5大安 6萬華 7信義 8士林 9北投 10內湖 11南港 12文山
1-2-3-4-5_casetype 1 整層 2獨立 3分租 4雅房 5其他
2-1-3-4-5_building 1大樓 2公寓 3透天 4別墅 5其他'''
for page in range(1, 4):
    url = url0.format(page=page)
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    house_list = soup.find_all("div", class_="flex-1 flex-shrink space-y-2")
    rentlList = soup.find_all("div", class_="items-center self-center flex-shrink-0 w-40 text-end")
    rentHrefList = soup.find_all("a", class_="group")
    houseImgList = soup.find_all("div", class_="h-full overflow-hidden bg-white border rounded-lg border-c-dark-400")

    for i in range(len(house_list)):
        houseData = house_list[i]
        rentalNameTag = houseData.find("h2", class_="text-2xl font-bold text-black line-clamp-1 group-visited:text-c-dark-600 group-hover:text-c-purple-700")
        rentalName = rentalNameTag.text.strip() if rentalNameTag else "無標題"

        transportationList = houseData.find_all("div", class_="flex items-center gap-1")
        if len(transportationList) > 1:
            transportationTag = transportationList[-1]
            transportation = transportationTag.text.strip()
        else:
            transportation = "無交通資訊"

        rentalAddressTag = houseData.find("svg", class_="text-xl iconify iconify--weui")
        rentalAddress = rentalAddressTag.find_next("span").text.strip() if rentalAddressTag else "無地址"

        retalTypeTag = houseData.find("li", class_="flex items-center")
        retalType = retalTypeTag.text.strip("|").replace(" ", "") if retalTypeTag else "無類型"

        rent = rentlList[i].find("span", class_="pr-1 text-2xl font-bold text-c-orange-700").text.strip() if i < len(rentlList) else "無租金"
        rentHref = "https://rent.houseprice.tw" + rentHrefList[i].get("href") if i < len(rentHrefList) else "無連結"
        houseImgTag = houseImgList[i].find("img", class_="w-full h-full object-cover") if i < len(houseImgList) else None
        houseImgSrc = houseImgTag.get("src") if houseImgTag else "沒照片"

        houseRawData.append({
            "rentalName": rentalName,
            "transportation": transportation,
            "rentalAddress": rentalAddress,
            "retalType": retalType,
            "rent": rent,
            "rentHref": rentHref,
            "houseImgSrc": houseImgSrc
        })
with open("rent.json", "w", encoding="utf-8") as file:
    json.dump(houseRawData, file, ensure_ascii=False, indent=4)