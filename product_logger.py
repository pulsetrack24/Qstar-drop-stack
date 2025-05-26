import json

def log_product(product):
    log_file = "product_log.json"
    try:
        with open(log_file, "r") as f:
            data = json.load(f)
    except:
        data = []
    data.append(product)
    with open(log_file, "w") as f:
        json.dump(data, f, indent=2)