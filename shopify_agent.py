import json

def publish_to_shopify(product):
    try:
        # Simulate successful upload
        print(f"[Shopify] Pushed: {product['title']} | Margin: {product['margin']}%")
        product['status'] = 'Published'
    except Exception as e:
        product['status'] = f"Error: {str(e)}"