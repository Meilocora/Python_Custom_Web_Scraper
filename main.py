from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable

URL = "https://coinmarketcap.com/"

response = requests.get(url=URL)
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

crypto_projects = soup.find_all(name="tr", attrs={'style':'cursor:pointer'})
top_cryptos = []

for project in crypto_projects:
    name = project.findNext(name="p", class_="sc-4984dd93-0 kKpPOn").get_text()
    price = project.findNext(name="td", attrs={'style':'text-align:end'}).findNext(name="span").get_text()
    market_cap = "$" + project.findNext(name="p", class_="sc-4984dd93-0 jZrMxO").get_text().split("$")[2]
    top_cryptos.append({
        "crypto-project": name,
        "price": price,
        "market_cap": market_cap
    })

print("\nTop 10 crypto projects")
table = PrettyTable(header=True)
table.field_names = ["Name", "Price", "Marketcap"]
table.align["Name"] = "c"
table.align["Price"] = "r"
table.align["Marketcap"] = "r"
for project in top_cryptos:
    table.add_row([project["crypto-project"], project["price"], project["market_cap"]])
print(table)



