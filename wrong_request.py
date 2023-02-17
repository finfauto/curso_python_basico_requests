import requests

if __name__ == "__main__":
    try:
        response = requests.get("http://httpbin.org/status/404")
        response.raise_for_status()
        print(response.status_code)
        print(response.content)
    except requests.HTTPError as exception:
        print("La response viene con un código de error")
        print(exception)
    except requests.exceptions.RequestException as exception:
        print("Excepción general en la request")
        print(exception)

    try:
        response = requests.get("http://httpbin.org/delay/10", timeout=3)
        response.raise_for_status()
        print(response.status_code)
        print(response.content)
    except requests.HTTPError as exception:
        print("La response viene con un código de error")
        print(exception)
    except requests.exceptions.RequestException as exception:
        print("Excepción general en la request")
        print(exception)

    try:
        response = requests.get("http://thisdoesnotexist", timeout=3)
        response.raise_for_status()
        print(response.status_code)
        print(response.content)
    except requests.HTTPError as exception:
        print("La response viene con un código de error")
        print(exception)
    except requests.exceptions.ConnectionError as exception:
        print("Problema con la conexión detectado")
        print(exception)
    except requests.exceptions.RequestException as exception:
        print("Excepción general en la request")
        print(exception)
