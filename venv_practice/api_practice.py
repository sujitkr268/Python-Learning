import requests

try:
    response = requests.get("https://httpbin.org/get", timeout=5)

    response.raise_for_status()
    data = response.json()

    print("Status:", response.status_code)
    print("URL:", data["url"])

except requests.exceptions.Timeout:
    print("Time out")

except requests.exceptions.HTTPError:
    print("Error in HTTP")

except requests.exceptions.RequestException:
    print("Something went wrong with the request")
