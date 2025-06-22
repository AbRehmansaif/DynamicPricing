# products/management/commands/run_scheduler.py
import time
import schedule
import threading
from django.core.management.base import BaseCommand
from django.conf import settings
from products.models import Product

class Command(BaseCommand):
    help = 'Runs the pricing scheduler'
    
    def handle(self, *args, **options):
        def update_prices():
            self.stdout.write("Updating prices...")
            products = Product.objects.filter(in_stock=True)
            count = 0
            for product in products:
                try:
                    product.update_price()
                    count += 1
                except Exception as e:
                    self.stderr.write(f"Error updating {product.title}: {str(e)}")
            self.stdout.write(f"Updated {count} product prices")
        
        def train_model():
            self.stdout.write("Training pricing model...")
            try:
                from products.ml.train_model import train_price_model
                train_price_model()
                self.stdout.write("Model training completed")
            except Exception as e:
                self.stderr.write(f"Training failed: {str(e)}")
        
        # Schedule tasks
        schedule.every().day.at("03:00").do(update_prices)
        schedule.every().monday.at("02:00").do(train_model)
        
        self.stdout.write("Scheduler started. Press Ctrl+C to exit.")
        while True:
            schedule.run_pending()
            time.sleep(60)