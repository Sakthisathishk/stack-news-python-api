STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
import  smtplib
import  requests
apikey="3BZYP29FS0R7BYKK"
parameter={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":apikey
}
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
is_true=False
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
responce=requests.get(url="https://www.alphavantage.co/query",params=parameter)
responce.raise_for_status()
daily=responce.json()
stock=daily["Time Series (Daily)"]

dates = list(stock.keys())
yesterday=dates[0]
before=dates[1]
print(stock[yesterday])
open=stock[yesterday]["4. close"]
close=stock[before]["4. close"]
diffrent=abs(float(open)-float(close))
percentage=diffrent/float(close)*100
if percentage>=1:
    print("get news")
    is_true=True



#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
price=[key for (key, value) in stock.items()]
print(["1.open"])

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if is_true:

    param={
        "qInTitle":COMPANY_NAME,
        "apiKey":"d30cd1d982f34fac9b0a79c398e8cfff",
        
    }
    news=requests.get(url=NEWS_ENDPOINT,params=param)
    news.raise_for_status()
    art=news.json()
    article=art["articles"][:3]
    print(article)


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted=[f"headline:{aot['title']},brief:{aot['description']}" for aot in article]
print(formatted)
#TODO 9. - Send each article as a separate message via Twilio.
if is_true:


    my_email = "ksakthimurugan8@gmail.com"
    password = "ksny zcjb rxrt kipr"
    a=[]
    for i in formatted:
        a.append(i)
    message = " ".join(a)



    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="greyraven@myyahoo.com",
                            msg=f"Subject:hello\n\n{message}".encode('utf-8'))


#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

