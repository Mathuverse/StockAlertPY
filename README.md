# Stock News Alert

Welcome to Stock News Alert! This application fetches stock data and relevant news articles based on predefined criteria and sends email alerts to the user.

## Getting Started

To use the Stock News Alert, you'll need Python installed on your computer. You can download Python from the [official website](https://www.python.org/).

Once you have Python installed, ensure you have the required dependencies installed using the following command:

```bash
pip install requests
```
## How it Works (Continued)

The Stock News Alert application performs the following steps:

1. Retrieves daily stock data for a predefined stock symbol from the Alpha Vantage API.
2. Calculates the difference in closing price between yesterday and the day before yesterday.
3. If the percentage difference is above 0%, fetches the top news articles related to the company associated with the stock symbol from the News API.
4. Sends an email alert to the user with the stock update and the top three news articles.

## Features

- Retrieves daily stock data and news articles from APIs.
- Calculates percentage difference in stock price and sends email alerts if above 0%.
- Fetches top news articles related to the company associated with the stock symbol.
- Sends email alerts using the user's Gmail account.

## Technologies Used

- Python: Programming language used to build the application.
- Requests: Python library used to make HTTP requests to APIs.
- SMTP: Protocol used for sending email messages.

## Configuration

Before running the application, make sure to update the following variables in the code:

- `MY_EMAIL`: Your Gmail email address.
- `MY_PASS`: Your Gmail account password.
- `STOCK_NAME`: The stock symbol for which you want to receive alerts.
- `COMPANY_NAME`: The name of the company associated with the stock symbol.
- `MY_API_NEWS`: Your API key for the News API.
- `MY_API_STOCKS`: Your API key for the Alpha Vantage API.


