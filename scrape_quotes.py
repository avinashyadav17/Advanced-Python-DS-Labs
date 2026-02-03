import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
response = requests.get(url)

if response.status_code != 200:
    print("Request failed")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

data = []

quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    tags = quote.find("div", class_="tags").find_all("a", class_="tag")
    tag_list = ", ".join([tag.text for tag in tags])  # Excel-friendly

    data.append([text, author, tag_list])

df = pd.DataFrame(data, columns=["Quote", "Author", "Tags"])

# ✅ Save to Excel file
df.to_excel("quotes.xlsx", index=False)
print(df.to_string(index=False))

print("Data successfully saved to quotes.xlsx")
