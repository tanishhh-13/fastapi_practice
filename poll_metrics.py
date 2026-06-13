import time
import requests

URL = "http://localhost:9090/api/v1/query"
QUERY = {"query": "http_requests_total"}

while True:
    # Ask Prometheus for the data
    response = requests.get(URL, params=QUERY).json()
    results = response["data"]["result"]

    # Look at the data
    for item in results:
        status = item["metric"].get("status", "200")
        value = item["value"][1]
        log_line = f"Route status: {status}, Total hits: {value}\n"
        print(log_line.strip())

        # If it's a 500 error, save it to a file
        if status.startswith("5"):
            with open("system_alerts.log", "a") as file:
                file.write(f"ALERT! Error detected: {log_line}")

    # Wait 5 seconds 
    time.sleep(5)