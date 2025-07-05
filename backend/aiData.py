import json
import os

# 最終整合結果
final_data = {
    "competition": [],
    "majorCourse": [],
    "master": [],
    "internship": [],
    "rent": [],
    "scholarship": []
}

# 定義各檔案對應類別
file_map = {
    "competition.json": "competition",
    "course.json": "majorCourse",
    "master.json": "master",
    "intern.json": "internship",
    "rent.json": "rent",
    "schoolarshipLink.json": "scholarship"
}

# 設定資料夾路徑
folder_path = "./data"  # 

# 逐一處理檔案
for filename, category in file_map.items():
    file_path = os.path.join(folder_path, filename)

    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)

                # 如果資料是單筆字典，轉成 list
                if isinstance(data, dict):
                    final_data[category].append(data)
                elif isinstance(data, list):
                    final_data[category].extend(data)
                else:
                    print(f" {filename} 格式不正確，請檢查內容。")

            except Exception as e:
                print(f"讀取 {filename} 時發生錯誤：{e}")

    else:
        print(f" 找不到檔案 {filename}，跳過。")

# 將結果存檔
output_path = os.path.join(folder_path, "aiData.json")
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(final_data, f, ensure_ascii=False, indent=2)

print(" 整合完成，檔案儲存於：", output_path)
