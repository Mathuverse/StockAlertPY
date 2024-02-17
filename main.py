import requests
import datetime
import smtplib
import tkinter as tk
#Welcome
#All the variables and constants
MY_EMAIL="Mathudeals@gmail.com"
MY_PASS="ngzjeqhpuqfwbqja"

STOCK_NAME = "ATD.TO"
COMPANY_NAME = "COUCHE TARD"

MY_API_NEWS = "5d12d240957247eeb7c1f0055528a9c1"
MY_API_STOCKS = "PU5549K5KHK695KN"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": MY_API_STOCKS
}

#The date from yesturday and the day before yesturday
yesturday_date = (str(datetime.datetime.now() - datetime.timedelta(days=1)).split(" "))[0]
before_yesturday_date = (str(datetime.datetime.now() - datetime.timedelta(days=2)).split(" "))[0]

#Request to API Stock for all the values daily
response_stock = requests.get(url="https://www.alphavantage.co/query", params=params)
dic_time = response_stock.json()["Time Series (Daily)"]

#Make a list for the time
list_time = [value for (key,value) in dic_time.items()]

#Choose the closing price for yesturday and the before yesturday
yesturday = float(list_time[0]["4. close"])
before_yesturday =  float(list_time[1]["4. close"])

##Difference in price
difference = abs(yesturday-before_yesturday)

#Percentage difference
percentage = round((difference / yesturday) * 100,1)

#SendEmail if difference is above 5%
if percentage > 0:
    print("Get News")
    params = {
        "q":COMPANY_NAME,
        "from": yesturday_date,
        "sortBy": "publishedAt",
        "apikey": MY_API_NEWS,
    }
    #Resquest to API News to get all top news
    response_news = requests.get(url = "https://newsapi.org/v2/everything" ,params=params)
    news_dic = response_news.json()

    #Keep the top 3 news in a list of dictionaries of title and description
    list_news = [value for (key,value) in news_dic.items()]
    top_news = []
    for _ in range(3):
        top_news.append(list_news[2][_])
        print(top_news[_])
    three_news =  [{'title': dictionary['title'], 'description': dictionary['description']} for dictionary in top_news[:3]]
    print(three_news)

    # See if the difference is positive or negative
    emo = " "
    if (yesturday - before_yesturday) >0:
        emo = f"🔺{percentage}% "
    else:
        emo = f"🔻{percentage}% "

    #Sends all 3 articles Seperately
    for article in three_news:
        #Prepare message to send by email
        msg =f"Subject: {COMPANY_NAME} Stock Update\n\n {STOCK_NAME} :{emo}\n Headline: {article['title']}\nBrief: {article['description']}"
        msg = msg.encode("utf-8")

        #Send email to User
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASS)
            connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=msg
        )