import json
import random
import uuid
from datetime import datetime, timedelta

# Daftar produk
products = ['A', 'B', 'C', 'D']

# Fungsi untuk menghasilkan data transaksi
def generate_transactions(num_transactions=500000):
    transactions = []
    start_date = datetime(2024, 1, 1)
    
    for _ in range(num_transactions):
        transaction = {
            "transaction_id": str(uuid.uuid4()),
            "product": random.choice(products),
            "amount": round(random.uniform(10, 500), 2),  # Jumlah transaksi antara 10 dan 500
            "timestamp": (start_date + timedelta(minutes=random.randint(0, 60*24*30))).isoformat()
        }
        transactions.append(transaction)
    
    return transactions

# Menghasilkan data transaksi
data = generate_transactions()

# Menyimpan ke file JSON
with open("transactions.json", "w") as f:
    json.dump(data, f, indent=4)

print("File transactions.json berhasil dibuat dengan 500000 data transaksi.")