from django.core.management import call_command
from django.utils import timezone
from products.models import Product

def train_model_weekly():
    print(f"{timezone.now()}: Starting weekly model training")
    call_command('train_pricing_model')
    print("Model training completed")

def update_prices_daily():
    print(f"{timezone.now()}: Starting price updates")
    products = Product.objects.filter(in_stock=True)
    count = 0
    for product in products:
        try:
            product.update_price()
            count += 1
        except Exception as e:
            print(f"Error updating {product.title}: {str(e)}")
    print(f"Updated {count} product prices")