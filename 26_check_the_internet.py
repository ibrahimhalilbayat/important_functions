import requests

def check_internet(url="http://www.google.com", timeout=5):
    try:
        print(f"İnternet bağlantısı kontrol ediliyor...")
        response = requests.get(url, timeout=timeout)
        return True if response.status_code == 200 else False
    except requests.ConnectionError:
        return False
