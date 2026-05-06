import requests

url = "https://opensource-demo.orangehrmlive.com"

try:
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        print("Application is UP")
    else:
        print(f"Application returned status: {response.status_code}")

except:
    print("Application is DOWN")