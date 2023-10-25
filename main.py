import requests
from bs4 import BeautifulSoup
import csv

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
        }

    def make_request(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()  # Lanza una excepción si hay un error en la solicitud HTTP
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud HTTP: {e}")
            return None

    def parse_content(self, content):
        if content:
            soup = BeautifulSoup(content, "html.parser")
            return soup
        return None

    def extract_title(self, soup):
        if soup:
            title = soup.find("title").text
            return title
        return None

    def extract_links(self, soup):
        if soup:
            links = soup.find_all("a")
            return links
        return []

    def export_to_csv(self, title, links):
        if title and links:
            filename = "data.csv"
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Title", "Link"])
                for link in links:
                    link_text = link.text
                    link_url = link["href"]
                    writer.writerow([title, link_text, link_url])
            print(f"Datos exportados exitosamente a {filename}")
        else:
            print("No hay datos para exportar")

    def run(self):
        content = self.make_request()
        soup = self.parse_content(content)
        title = self.extract_title(soup)
        links = self.extract_links(soup)

        if title:
            print(f"Title: {title}")

        if links:
            for link in links:
                link_text = link.text
                link_url = link["href"]
                print(f"Link: {link_text} - {link_url}")

        self.export_to_csv(title, links)


# Uso de la clase WebScraper
url = "https://www.mercadolibre.cl/ofertas?container_id=MLC779365-1&category=MLC1051#filter_applied=category_id&origin=qcat&filter_position=4"
scraper = WebScraper(url)
scraper.run()