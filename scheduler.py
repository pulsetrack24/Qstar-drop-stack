from shopify_agent import publish_to_shopify
from product_logger import log_product
import time

def start_automation():
    keywords = ["bio health tracker", "fitness ring", "smart body sensor"]
    for i, kw in enumerate(keywords):
        product = {
            "title": f"{kw.title()} {i+1}",
            "gtin": f"GTIN-BIO-{1000+i}",
            "price": 29.99 + i * 2,
            "compare_price": 49.99 + i * 2,
            "margin": round(((49.99 + i * 2 - (29.99 + i * 2)) / (29.99 + i * 2)) * 100, 1),
            "status": "Draft"
        }
        log_product(product)
        publish_to_shopify(product)
        time.sleep(3)