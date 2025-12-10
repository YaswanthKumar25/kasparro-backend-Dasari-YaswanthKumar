import requests
from django.core.management.base import BaseCommand
from products.models import Product

EXTERNAL_API_URL = "https://fakestoreapi.com/products"

class Command(BaseCommand):
    help = "Run ETL: fetch products from external API and load into DB"

    def handle(self, *args, **options):
        self.stdout.write("Starting ETL...")

        response = requests.get(EXTERNAL_API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        created_count = 0
        updated_count = 0

        for item in data:
            external_id = item.get("id")
            title = item.get("title", "")
            price = item.get("price", 0)
            description = item.get("description", "")
            category = item.get("category", "")
            image_url = item.get("image", "")

            obj, created = Product.objects.update_or_create(
                external_id=external_id,
                defaults={
                    "title": title,
                    "price": price,
                    "description": description,
                    "category": category,
                    "image_url": image_url,
                },
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"ETL finished. Created: {created_count}, Updated: {updated_count}"
            )
        )
