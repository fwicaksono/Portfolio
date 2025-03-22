# Short-Term Rental Data Analysis

## 📌 Project Overview
This project analyzes short-term rental properties across different locations to optimize revenue, pricing, and occupancy rates. It provides actionable insights for revenue management, demand forecasting, and guest satisfaction improvement.

---

## 🛠️ Dataset Overview
The dataset includes:
- **Location:** City where the property is located
- **Property_Type:** Type of property (Apartment, Villa, Studio, House)
- **Bedrooms:** Number of bedrooms
- **Amenities:** Available features (WiFi, Pool, Kitchen, etc.)
- **Price_Per_Night:** Cost per night in USD
- **Occupancy_Rate:** Percentage of booked days per month
- **Total_Revenue:** Estimated revenue per month
- **Month:** Month of the year (1-12)
- **Holiday_Season:** Indicator for peak season (1 = High Season, 0 = Regular)
- **Rating:** Guest rating (1-5 scale)
- **Num_Reviews:** Number of customer reviews

---

## 📊 SQL Queries for Analysis

### **1️⃣ Revenue & Occupancy Insights**
**Q1: What is the total revenue generated per location?**
```sql
SELECT Location, SUM(Total_Revenue) AS Total_Revenue
FROM rental_data
GROUP BY Location
ORDER BY Total_Revenue DESC;
```

**Q2: What is the average occupancy rate per property type?**
```sql
SELECT Property_Type, AVG(Occupancy_Rate) AS Avg_Occupancy_Rate
FROM rental_data
GROUP BY Property_Type
ORDER BY Avg_Occupancy_Rate DESC;
```

**Q3: Which property type generates the highest revenue per night?**
```sql
SELECT Property_Type, AVG(Price_Per_Night) AS Avg_Price, SUM(Total_Revenue) AS Total_Revenue
FROM rental_data
GROUP BY Property_Type
ORDER BY Total_Revenue DESC;
```

---

### **2️⃣ Pricing & Demand Optimization**
**Q4: How does pricing change across different months?**
```sql
SELECT Month, AVG(Price_Per_Night) AS Avg_Price
FROM rental_data
GROUP BY Month
ORDER BY Month;
```

**Q5: What is the impact of holidays on revenue and occupancy rates?**
```sql
SELECT
    Holiday_Season,
    AVG(Occupancy_Rate) AS Avg_Occupancy,
    AVG(Total_Revenue) AS Avg_Revenue
FROM rental_data
GROUP BY Holiday_Season;
```

---

### **3️⃣ Guest Experience & Ratings**
**Q6: What is the average rating per location?**
```sql
SELECT Location, AVG(Rating) AS Avg_Rating
FROM rental_data
GROUP BY Location
ORDER BY Avg_Rating DESC;
```

**Q7: How do amenities affect guest ratings?**
```sql
SELECT Amenities, AVG(Rating) AS Avg_Rating
FROM rental_data
GROUP BY Amenities
ORDER BY Avg_Rating DESC;
```

**Q8: Which properties have the highest number of reviews?**
```sql
SELECT Location, Property_Type, Num_Reviews
FROM rental_data
ORDER BY Num_Reviews DESC
LIMIT 10;
```

---

## 📈 Power BI Visualizations

### **1️⃣ Revenue & Occupancy Insights**
✅ **Bar Chart:** Total Revenue per Location  
✅ **Line Chart:** Seasonality of Price Per Night  
✅ **Heatmap:** Occupancy Rate by Month & Property Type  

### **2️⃣ Pricing & Demand Optimization**
✅ **Box Plot:** Price Distribution per Property Type  
✅ **Scatter Plot:** Relationship Between Price Per Night & Rating  
✅ **KPI Cards:** Revenue & Occupancy Rate by Holiday Season  

### **3️⃣ Guest Experience & Ratings**
✅ **Bar Chart:** Top 10 Properties by Number of Reviews  
✅ **Word Cloud:** Most Common Amenities  
✅ **Gauge Chart:** Overall Average Rating  

---

## 🚀 Next Steps
1️⃣ Run the SQL queries to extract insights.  
2️⃣ Import the dataset into Power BI and create visualizations.  
3️⃣ Interpret findings to optimize pricing and revenue strategies.  

💡 Need help? Let’s collaborate! 🔥

