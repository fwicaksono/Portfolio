import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Inisialisasi Faker untuk data dummy
fake = Faker()

# Fungsi untuk generate dataset
def generate_supply_chain_data(num_records=1000):
    # Daftar produk dan kategori
    products = {
        "Laptop": {"Supplier_Cost": 500, "Holding_Cost": 10},
        "Smartphone": {"Supplier_Cost": 300, "Holding_Cost": 8},
        "Tablet": {"Supplier_Cost": 200, "Holding_Cost": 5}
    }
    
    # Daftar supplier
    suppliers = {
        "S001": "GlobalTech Supplies",
        "S002": "ElectroWorld Distributors",
        "S003": "GadgetHub Inc."
    }
    
    # Inisialisasi list untuk menyimpan data
    data = []
    
    for _ in range(num_records):
        # Pilih produk secara acak
        product_name = random.choice(list(products.keys()))
        product_info = products[product_name]
        
        # Generate data
        product_id = fake.unique.bothify(text="P###")
        demand = random.randint(50, 500)  # Permintaan antara 50-500 unit
        inventory = random.randint(10, 100)  # Stok antara 10-100 unit
        supplier_id = random.choice(list(suppliers.keys()))
        supplier_name = suppliers[supplier_id]
        supplier_cost = product_info["Supplier_Cost"]
        lead_time = random.randint(3, 14)  # Waktu pengiriman antara 3-14 hari
        holding_cost = product_info["Holding_Cost"]
        order_cost = 100  # Biaya pemesanan tetap
        date = fake.date_between(start_date='-1y', end_date='today')  # Tanggal acak dalam 1 tahun terakhir
        
        # Tambahkan ke list
        data.append([
            product_id, product_name, "Electronics", demand, inventory,
            supplier_id, supplier_name, supplier_cost, lead_time,
            holding_cost, order_cost, date
        ])
    
    # Buat DataFrame

    columns = [
        "Product_ID", "Product_Name", "Category", "Demand", "Inventory",
        "Supplier_ID", "Supplier_Name", "Supplier_Cost", "Lead_Time",
        "Holding_Cost", "Order_Cost", "Date"
    ]
    df = pd.DataFrame(data, columns=columns)
    
    return df

# Generate dataset
dataset = generate_supply_chain_data(870)

# Simpan ke file CSV (opsional)
dataset.to_csv("techmart_supply_chain_data.csv", index=False)

# Tampilkan 5 baris pertama
print(dataset.head())