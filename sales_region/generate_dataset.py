import json
import random
import faker
from datetime import datetime, timedelta

# Initialize Faker
fake = faker.Faker()

# Function to generate customers data
def generate_customers(num_records):
    customers = []
    for i in range(1, num_records + 1):
        customers.append({
            "customer_id": i,
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "address": fake.address(),
            "join_date": fake.date_between(start_date="-5y", end_date="today").isoformat()
        })
    return customers

# Function to generate products data
def generate_products(num_records):
    categories = ["Electronics", "Clothing", "Home Appliances", "Books", "Sports"]
    products = []
    for i in range(1, num_records + 1):
        products.append({
            "product_id": i,
            "product_name": fake.word().capitalize() + " " + random.choice(categories),
            "category": random.choice(categories),
            "price": round(random.uniform(10, 1000), 2),
            "stock_quantity": random.randint(10, 500)
        })
    return products

# Function to generate regions data
def generate_regions():
    regions = ["North", "South", "East", "West"]
    return [{"region_id": i + 1, "region_name": region} for i, region in enumerate(regions)]

# Function to generate salespersons data
def generate_salespersons(num_records):
    salespersons = []
    for i in range(1, num_records + 1):
        salespersons.append({
            "salesperson_id": i,
            "name": fake.name(),
            "region_id": random.randint(1, 4),
            "hire_date": fake.date_between(start_date="-5y", end_date="today").isoformat()
        })
    return salespersons

# Function to generate sales data
def generate_sales(num_records, num_customers, num_products, num_salespersons):
    sales = []
    for i in range(1, num_records + 1):
        sales.append({
            "sale_id": i,
            "customer_id": random.randint(1, num_customers),
            "product_id": random.randint(1, num_products),
            "salesperson_id": random.randint(1, num_salespersons),
            "region_id": random.randint(1, 4),
            "quantity": random.randint(1, 10),
            "sale_date": fake.date_between(start_date="-2y", end_date="today").isoformat()
        })
    return sales

# Generate and save data to JSON
def save_to_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# Main function to generate datasets
def main():
    num_customers = 10000
    num_products = 200
    num_salespersons = 50
    
    num_sales = 100000

    customers = generate_customers(num_customers)
    save_to_json(customers, "customers.json")

    products = generate_products(num_products)
    save_to_json(products, "products.json")

    regions = generate_regions()
    save_to_json(regions, "regions.json")

    salespersons = generate_salespersons(num_salespersons)
    save_to_json(salespersons, "salespersons.json")

    sales = generate_sales(num_sales, num_customers, num_products, num_salespersons)
    save_to_json(sales, "sales.json")

if __name__ == "__main__":
    main()
