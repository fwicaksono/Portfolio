import os
import pandas as pd
import random
from datetime import datetime, timedelta

# Generate synthetic transaction data
def generate_data(num_rows=1000):
    data = []
    start_date = datetime(2023, 1, 1)
    
    for i in range(num_rows):
        order_id = f"ORD{i+1:06d}"
        customer_id = f"CUST{random.randint(1, 50)}"
        order_date = start_date + timedelta(days=random.randint(0, 365))
        amount = round(random.uniform(10, 500), 2)
        
        data.append([order_id, customer_id, order_date.strftime('%Y-%m-%d'), amount])

    # Save in the same folder as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'transactions.csv')

    df = pd.DataFrame(data, columns=['order_id', 'customer_id', 'order_date', 'amount'])
    df.to_csv(file_path, index=False)
    
    print(f"CSV file generated at: {file_path}")

generate_data()

