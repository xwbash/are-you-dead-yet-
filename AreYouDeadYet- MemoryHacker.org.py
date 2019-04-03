import os
os.system("pip install requests")
os.system("pip install figlet")
import requests
os.system("clear")
os.system("figlet bash")
print("MemoryHackers.org")
url = input(">> Enter The Web Site Name (exp. google.com)~# ")
url = ("https://www.%s"%url)
response = requests.get(url)
ok = response.status_code
if ok == 200:
    print(">> Site is up.")
else:
    print(">> Site is down")
