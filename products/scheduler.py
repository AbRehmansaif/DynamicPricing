# products/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler import util
from django.conf import settings
from .models import Product

def update_prices():
    print("Starting price updates...")
    products = Product.objects.filter(in_stock=True)
    count = 0
    for product in products:
        try:
            product.update_price()
            count += 1
        except Exception as e:
            print(f"Error updating {product.title}: {str(e)}")
    print(f"Updated {count} product prices")

def train_model():
    print("Training pricing model...")
    from .ml.train_model import train_price_model
    train_price_model()
    print("Model training completed")

def start_scheduler():
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")
    
    # Add jobs
    scheduler.add_job(
        update_prices,
        trigger='cron',
        hour=3,
        id="daily_price_update",
        max_instances=1,
        replace_existing=True,
    )
    
    scheduler.add_job(
        train_model,
        trigger='cron',
        day_of_week='mon',
        hour=2,
        id="weekly_model_training",
        max_instances=1,
        replace_existing=True,
    )
    
    try:
        print("Starting scheduler...")
        scheduler.start()
    except KeyboardInterrupt:
        print("Stopping scheduler...")
        scheduler.shutdown()