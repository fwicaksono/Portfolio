# 🏥 Patient Waiting List Analysis

## 📌 Project Description
This project aims to analyze and track the patient waiting list status over time using Power BI. The analysis covers both inpatient and outpatient categories, providing insights into waiting list trends, specialty-level breakdowns, and age profile distributions. The dataset spans from 2018 to 2021.

## 🎯 Overall Objectives
- 📊 Track the current status of the patient waiting list.
- 📉 Analyze historical monthly trends of waiting lists in inpatient and outpatient categories.
- 🏷️ Provide a detailed specialty-level and age-profile analysis.

## 📅 Data Scope
- 🕒 Timeframe: 2018 – 2021
- 🏥 Categories: Inpatient & Outpatient

## 📊 Key Metrics
- **📈 Average & Median Waiting List**: Provides insights into the typical waiting time for patients.
- **📌 Current Total Wait List**: Tracks the number of patients currently on the waiting list.

## 📂 Dataset Information
### 🏷️ 1. Specialty Mapping
This dataset maps medical specialties to broader specialty groups.
- **Columns:** `Specialty`, `Specialty Group`
- **Example Data:**
  ```
  Specialty       | Specialty Group
  -------------- | ---------------
  Anaesthetics   | Respiratory
  ```

### 🏥 2. Inpatient Data
This dataset includes patients who are admitted and stay in the hospital.
- **Columns:** `Archive_Date`, `Specialty_HIPE`, `Specialty_Name`, `Case_Type`, `Adult_Child`, `Age_Profile`, `Time_Bands`, `Total`
- **Example Data:**
  ```
  Archive_Date | Specialty_HIPE | Specialty_Name             | Case_Type | Adult_Child | Age_Profile | Time_Bands  | Total
  ------------|---------------|---------------------------|-----------|------------|-------------|------------|------
  31-01-2018  | 0             | Small Volume Specialities | Inpatient | Child      | 0-15        | 6-9 Months | 1
  ```

### 🏠 3. Outpatient Data
This dataset includes patients who receive medical treatment without being admitted to the hospital.
- **Columns:** `Archive_Date`, `Specialty_HIPE`, `Specialty`, `Adult_Child`, `Age_Profile`, `Time_Bands`, `Total`
- **Example Data:**
  ```
  Archive_Date | Specialty_HIPE | Specialty   | Adult_Child | Age_Profile | Time_Bands  | Total
  ------------|---------------|------------|------------|-------------|------------|------
  31-01-2018  | 100           | Cardiology | Child      | 0-15        | 0-3 Months | 167
  ```

## 🛠️ Tools Used
- **📊 Power BI**: For data visualization and analysis.

## 🔍 Expected Outcomes
- 📌 Interactive dashboards showcasing waiting list trends.
- 📉 Insights into how waiting times vary across specialties and age groups.
- 🎯 Data-driven recommendations for healthcare process improvements.
