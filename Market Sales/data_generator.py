import pandas as pd
import random
import faker
from datetime import datetime, timedelta

fake = faker.Faker()

# Parameter dataset
num_customers = 5000
num_products = 200
num_transactions = 50000

# Produk dan kategori
categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Books', 'Beauty', 'Toys', 'Sports']
products = {f'Product_{i}': random.choice(categories) for i in range(1, num_products + 1)}

# Data pelanggan
customers = [
    {
        'customer_id': i,
        'name': fake.name(),
        'email': fake.email(),
        'city': fake.city(),
        'country': fake.country()
    }
    for i in range(1, num_customers + 1)
]

# Data transaksi
transactions = []
for _ in range(num_transactions):
    product = random.choice(list(products.keys()))
    category = products[product]
    price = round(random.uniform(5, 500), 2)
    discount = round(random.uniform(0, 0.3) * price, 2)  # Diskon 0-30%
    total_price = price - discount
    payment_method = random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer'])
    transaction_date = datetime.today() - timedelta(days=random.randint(0, 365))
    transactions.append(
        {
            'transaction_id': fake.uuid4(),
            'customer_id': random.randint(1, num_customers),
            'product': product,
            'category': category,
            'price': price,
            'discount': discount,
            'total_price': total_price,
            'payment_method': payment_method,
            'transaction_date': transaction_date.strftime('%Y-%m-%d')
        }
    )

# Simpan dataset sebagai CSV
customers_df = pd.DataFrame(customers)
transactions_df = pd.DataFrame(transactions)

customers_df.to_csv('customers.csv', index=False)
transactions_df.to_csv('transactions.csv', index=False)

print("Dataset berhasil dibuat: customers.csv & transactions.csv")
