import bs4
import time


def getMajor(driver):
    driver.get("https://aps.ntut.edu.tw/course/tw/Cprog.jsp?format=-3&year=114&matric=7")
    time.sleep(2)
    html=driver.page_source
    MajorRoot = bs4.BeautifulSoup(html, "html.parser")
    majorInfo=[]
    excludeKeyword={"課程","學程","備註"}
    #找科系
    pTag=MajorRoot.find_all("p")
    for p in pTag :
        URL=p.find("a")
        #只要有部分內容有符合"課程","學程","備註" 就會剔除
        if URL and not any(keyword in p.text for keyword in excludeKeyword):
            majorName = p.text.strip()
            majorURL = "https://aps.ntut.edu.tw/course/tw/" + URL["href"]
            majorInfo.append((majorURL, majorName))
            print(f"抓取科系: {majorName}, 網址: {majorURL}") 
    return majorInfo
