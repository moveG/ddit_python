import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:5000/emp'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    trs = soup.select("table")[0].select("tr")
    
    for idx, tr in enumerate(trs):
        if idx > 0:
            nm = tr.select("td")[1].text
            tel = tr.select("td")[4].text
            
            print("이름    : {}".format(nm))
            print("전화번호 : {}".format(tel))
            print("======================")
    
else : 
    print(response.status_code)