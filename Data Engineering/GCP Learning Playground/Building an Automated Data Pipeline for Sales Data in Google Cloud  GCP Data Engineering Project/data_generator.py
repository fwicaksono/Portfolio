import csv
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Define product list with prices
products = [
    ("Sedan", 20000),
    ("SUV", 30000),
    ("Truck", 40000),
    ("Convertible", 50000),
    ("Coupe", 35000),
    ("Hatchback", 18000),
    ("Minivan", 25000),
    ("Sports Car", 60000),
    ("Electric Car", 45000),
    ("Luxury Car", 70000)
]

# Define cities
cities = ["New York", "Los Angeles", "Philadelphia"]

# Generate random sales data
def generate_sales_data(num_records=1000):
    for city in cities:
        output_file = f"sales_data_{city.replace(' ', '_').lower()}.csv"
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Transaction_ID", "Date", "Customer_Name", "Product", "Price", "Quantity", "Total_Sale", "Payment_Method", "City"])
            
            for i in range(1, num_records + 1):
                date = fake.date_between(start_date="-1y", end_date="today")
                customer_name = fake.name()
                product, price = random.choice(products)
                quantity = random.randint(1, 2)
                total_sale = price * quantity
                payment_method = random.choice(["Credit Card", "Debit Card", "PayPal", "Cash", "Bank Transfer"])
                
                writer.writerow([i, date, customer_name, product, price, quantity, total_sale, payment_method, city])

        print(f"Generated {num_records} sales records and saved to {output_file}")

# Run the generator
generate_sales_data(500)

