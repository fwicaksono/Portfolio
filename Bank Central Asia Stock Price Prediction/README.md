# Bank Central Asia (BBCA) Stock Price Prediction

This project focuses on predicting the stock price of **Bank Central Asia (BBCA)** using deep learning models **LSTM (Long Short-Term Memory)** and **GRU (Gated Recurrent Units)**. The dataset consists of historical stock prices, and the models are trained to predict future closing prices based on past trends.

## Dataset
The dataset includes the following columns:
- **Date**: The date of the stock data.
- **Open**: The opening price of the stock.
- **High**: The highest price during the trading session.
- **Low**: The lowest price during the trading session.
- **Close**: The closing price of the stock.
- **Adj Close**: The adjusted closing price considering dividends and splits.
- **Volume**: The number of shares traded.

## Models Used
### 1. Long Short-Term Memory (LSTM)
LSTM is a type of recurrent neural network (RNN) capable of learning long-term dependencies in sequential data, making it well-suited for time series forecasting.

#### **LSTM Model Performance:**
- **Mean Squared Error (MSE)**: 0.001331
- **Root Mean Squared Error (RMSE)**: 0.03648
- **Mean Absolute Error (MAE)**: 0.02894
- **R-squared (R²)**: 0.6837

### 2. Gated Recurrent Unit (GRU)
GRU is a variant of LSTM that simplifies the architecture while maintaining similar performance, making it a strong choice for time series forecasting.

#### **GRU Model Performance:**
- **Mean Squared Error (MSE)**: 0.0008016
- **Root Mean Squared Error (RMSE)**: 0.02831
- **Mean Absolute Error (MAE)**: 0.02215
- **R-squared (R²)**: 0.8095

## Results & Insights
- **GRU outperformed LSTM in terms of R² score**, indicating it captures stock price trends better.
- GRU achieved a lower error rate, making it more suitable for this dataset.
- The models can be fine-tuned further by optimizing hyperparameters and increasing training data.
- Additional features like market sentiment analysis could enhance prediction accuracy.

## Conclusion
- **GRU performed better overall** in terms of error metrics and R² score, making it the preferable model for predicting BBCA stock prices.
- The project demonstrates the potential of deep learning in stock price prediction, though real-world applications should also consider external financial and economic factors.
- Future improvements can include incorporating news sentiment analysis, additional technical indicators, and experimenting with hybrid models for better accuracy.

## Future Improvements
- Experiment with other deep learning architectures like Transformer-based models.
- Incorporate external financial indicators to improve model performance.
- Deploy the model as a web application for real-time predictions.
