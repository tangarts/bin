
import requests
from bs4 import BeautifulSoup

base_url = "http://www.websters1913.com/words/"
word = input("enter a word: ")

url = base_url + word

r = requests.get(url)
if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'lxml')
    defn = soup.find('div', {'class' : 'result-content'})
    print()
    print(defn.text)
else:
    print()
    print("word not found")
