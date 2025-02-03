# Sentiment Analysis of Couvee Seturan Customer Reviews

## 📌 Project Overview
This project analyzes customer reviews of **Couvee Seturan**, a coffee shop in **Seturan, Yogyakarta, Indonesia**, to understand customer sentiment. The dataset consists of **250 reviews** collected from **Google Maps**. By applying **Natural Language Processing (NLP)** techniques, the sentiment of each review is classified as **Positive, Negative, or Neutral**.

## 📂 Dataset
- **Source:** Google Maps reviews
- **Total Reviews:** 250
- **Language:** Indonesian

## 🛠️ Tools & Technologies
- **Python** (pandas, re, nltk, textblob, matplotlib, wordcloud)
- **VADER Sentiment Analysis** (for rule-based sentiment scoring)
- **TextBlob** (for sentiment polarity scoring)
- **Matplotlib & WordCloud** (for data visualization)

## 🔄 Data Preprocessing
1. Convert text to lowercase
2. Remove numbers and punctuation
3. Tokenization (splitting text into words)
4. Remove stopwords (common words that add little meaning)
5. Reconstruct cleaned text


## 📈 Results & Insights
- The majority of reviews are **positive**, indicating high customer satisfaction.
- Negative reviews highlight areas for improvement, such as service speed or pricing.
- The **word cloud** reveals commonly mentioned terms, helping understand customer preferences.