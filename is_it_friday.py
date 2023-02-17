import requests

if __name__ == "__main__":
    response = requests.get("https://isitfridayyet.net/")
    print(response.status_code)
    print(response.content)
