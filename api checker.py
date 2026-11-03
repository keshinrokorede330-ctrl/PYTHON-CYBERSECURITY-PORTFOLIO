import requests
from datetime import datetime
urls = [
    "http://api.github.com",
    "http://httpbin.org/status/200",
    "http://httpbin.org/status/401",
    "http://httpbin.org/status/404",
    "http://httpbin.org/status/500",
]
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"API Check Report - {current_time}")
print("=" * 30)
with open(" api_report.txt", "a") as file:
    file.write(f"\n--- Report: {current_time} ---\n")
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            status = response.status_code
            print(f"{url} -> Status: {status}")
            if status == 200:
                message = " OK - API DEY WORK "
            elif status == 401:
                message = " error 401 - AUTH ERROR "
            elif status == 404:
                message = " error 404 - PAGE NOT FOUND "
            elif status == 500:
                message = " error 500 - SERVER ERROR "
            else:
                message = f"problem: {status}"
            print(f" {message}")
            file.write(f"{url} -> Status: {status} | {message}\n")
        except Exception as e:
            print(f"{url} -> Failed: {e}")
            file.write(f"{url} -> Failed: {e}\n")
            print("-" * 40)
            file.write("=" * 40 + "\n")
print("\nreport saved to api_report.txt")