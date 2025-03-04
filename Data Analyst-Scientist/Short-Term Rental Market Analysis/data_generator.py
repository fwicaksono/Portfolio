import pandas as pd
import random
import numpy as np

# Define parameters
num_records = 879  # Number of rental property records
locations = ["Bali", "Jakarta", "Bandung", "Surabaya", "Yogyakarta"]
property_types = ["Apartment", "Villa", "Studio", "House"]
amenities = ["WiFi", "Pool", "Kitchen", "Parking", "Gym", "Air Conditioning"]
months = list(range(1, 13))  # Representing January to December

# Generate synthetic data
data = []
for _ in range(num_records):
    location = random.choice(locations)
    prop_type = random.choice(property_types)
    bedrooms = random.randint(1, 5)
    selected_amenities = random.sample(amenities, random.randint(2, 5))
    price_per_night = round(random.uniform(30, 300), 2)  # In USD
    occupancy_rate = round(random.uniform(0.4, 0.95), 2)  # Percentage of booked days in a month
    total_revenue = round(price_per_night * occupancy_rate * 30, 2)  # Approx. monthly revenue
    month = random.choice(months)
    holiday_season = 1 if month in [6, 7, 12] else 0  # High season during school holidays & December
    
    # Customer reviews
    rating = round(random.uniform(3.0, 5.0), 1)  # Rating from 1 to 5
    num_reviews = random.randint(10, 500)
    
    # Append data
    data.append([location, prop_type, bedrooms, ", ".join(selected_amenities), price_per_night,
                 occupancy_rate, total_revenue, month, holiday_season, rating, num_reviews])

# Create DataFrame
columns = ["Location", "Property_Type", "Bedrooms", "Amenities", "Price_Per_Night",
           "Occupancy_Rate", "Total_Revenue", "Month", "Holiday_Season", "Rating", "Num_Reviews"]
df = pd.DataFrame(data, columns=columns)

# Save dataset to CSV
csv_filename = "D:/Portfolio/Data Analyst-Scientist/Short-Term Rental Market Analysis/short_term_rental_data.csv"  # Windows
df.to_csv(csv_filename, index=False)
print(f"Dataset saved as {csv_filename}")
