import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url="https://www.amazon.com/dp/B098RKWHHZ/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=b25c096d0097183f6c492bcbdcfb6497&content-id=amzn1.sym.552bcbb2-81a1-4e8b-b868-3fba7d5af42a%3Aamzn1.sym.552bcbb2-81a1-4e8b-b868-3fba7d5af42a&hsa_cr_id=9903264740401&pd_rd_plhdr=t&pd_rd_r=c84809db-f989-4b6c-8f13-e66b9e443242&pd_rd_w=VqC4Q&pd_rd_wg=MBWg4&qid=1670024763&ref_=sbx_be_s_sparkle_lsi4d_asin_1_title&sr=1-2-9e67e56a-6f64-441f-a281-df67fc737124", headers=headers)
website = response.text
soup = BeautifulSoup(website, "html.parser")
price = soup.find(name="span", class_="a-offscreen")
# price = soup.find(name="span", class_="priceblock_ourprice")
# Both of the above commands return the same incorrect value, Not sure why
print(price)
