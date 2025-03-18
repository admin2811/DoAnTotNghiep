import requests
import json
import pandas as pd
import datetime
import time  # Thêm thư viện time để delay

# Thông tin API
API_KEY = "59db8247551b4dad8cdb799e349d7f32"
CITY = "Hanoi"

# Tạo danh sách các khoảng thời gian từ 13/01/2022 đến hiện tại
start_date = datetime.date(2022, 1, 13)
end_date = datetime.date.today()
delta = datetime.timedelta(days=60)  # Lấy từng khoảng 2 tháng để giảm số request

date_ranges = []
while start_date < end_date:
    next_date = start_date + delta
    if next_date > end_date:
        next_date = end_date
    date_ranges.append((start_date, next_date))
    start_date = next_date

# Hàm lấy dữ liệu từ API
def fetch_air_quality(start, end):
    url = f"https://api.weatherbit.io/v2.0/history/airquality?city={CITY}&start_date={start}&end_date={end}&tz=local&key={API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 429:
            print(f"Lỗi 429: Quá nhiều request. Đợi 30 giây trước khi thử lại...")
            time.sleep(30)  # Chờ 30 giây rồi thử lại
            return fetch_air_quality(start, end)
        response.raise_for_status()  # Kiểm tra lỗi HTTP khác
        data = response.json()
        return data.get("data", [])
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi lấy dữ liệu từ {start} đến {end}: {e}")
        return []

# Lấy dữ liệu từ API với delay giữa các request
all_data = []
for start, end in date_ranges:
    print(f"Đang lấy dữ liệu từ {start} đến {end}...")
    all_data.extend(fetch_air_quality(start, end))
    time.sleep(2)  # Chờ 2 giây giữa các request để tránh lỗi 429

# Tạo DataFrame từ dữ liệu thu thập được
if all_data:
    df = pd.DataFrame(all_data)

    # Chuyển đổi thời gian
    df["timestamp_local"] = pd.to_datetime(df["timestamp_local"])

    # Sắp xếp dữ liệu theo thời gian
    df = df.sort_values(by="timestamp_local").reset_index(drop=True)

    # Hiển thị thông tin DataFrame
    print(df.info())
    print(df.head()) 

    # Lưu vào file CSV
    #df.to_csv("air_quality_hanoi_2022_2024.csv", index=False)
    print("Dữ liệu đã được lưu vào air_quality_hanoi_2022_2024.csv")
else:
    print("Không có dữ liệu nào được lấy.")
