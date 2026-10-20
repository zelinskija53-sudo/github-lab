import requests
TOKEN = "8883942720:AAF6xx6cCm_4Svgr9S2tLZIDImZ2INxfVFc"
print(requests.get(f"https://api.telegram.org/bot{TOKEN}/getMe", timeout=10).json())