import requests
from bs4 import BeautifulSoup
def get_clinique_lipsticks():
    base_url = "https://goldapple.ru/makeup/guby/pomada"
    params = {
        "brands": "clinique",
        "price_min": 1000,
        "price_max": 4000
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    lipsticks = []
    page = 1
    while True:
        params["page"] = page
        response = requests.get(base_url, params=params, headers=headers)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")
        product_cards = soup.find_all("div", class_="product-card")

        if not product_cards:
            break

        for card in product_cards:
            name_tag = card.find("a", class_="product-name")
            price_tag = card.find("span", class_="price")

            if name_tag and price_tag:
                name = name_tag.text.strip()
                price_str = price_tag.text.strip()
                price = int("".join(filter(str.isdigit, price_str)))

                if 1000 <= price <= 4000:
                    lipsticks.append({"name": name, "price": price})
        page += 1
    return lipsticks
if __name__ == "__main__":
    products = get_clinique_lipsticks()
    for idx, product in enumerate(products, 1):
        print(f"{idx}. {product['name']} - {product['price']} руб.")