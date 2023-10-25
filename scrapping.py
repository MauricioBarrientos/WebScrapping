import requests
from bs4 import BeautifulSoup

# USER AGENT PARA PROTEGERNOS DE BANEOS
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}

# Define a function to extract the title of a web page
def extract_title(soup):
    title = soup.find("title").text
    return title

# Define a function to extract the links from a web page
def extract_links(soup):
    links = soup.find_all("a")
    return links

# Get the response from the web server
response = requests.get("https://www.mercadolibre.cl/ofertas?container_id=MLC779365-1&category=MLC1051#filter_applied=category_id&origin=qcat&filter_position=4")

# Parse the response as a BeautifulSoup object
soup = BeautifulSoup(response.content, "html.parser")

# Extract the title of the web page
title = extract_title(soup)

# Extract the links from the web page
links = extract_links(soup)

# Print the title of the web page
print(title)

# Print the links from the web page
for link in links:
    link_text = link.text
    link_url = link["href"]
    print(f"{link_text}: {link_url}")