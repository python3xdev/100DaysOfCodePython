import requests
import smtplib

my_email = EMAIL 
my_password = PASSWORD 
recipient = EMAIL 

STOCK_NAME = "TSLA"
# STOCK_NAME = "IDT"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = YOUR_API_KEY

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = YOUR_API_KEY

up_chart = "📈"
down_chart = "📉"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
    }

stock_response = requests.get(STOCK_ENDPOINT, stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

days = stock_data['Time Series (Daily)']
dates = list(days)[:2]

one_day_ago_low = float(days[dates[0]]["3. low"])
print(f"Yesterday: {one_day_ago_low}")

two_days_ago_low = float(days[dates[1]]["3. low"])
print(f"Day before Yesterday: {two_days_ago_low}")

difference = abs(one_day_ago_low - two_days_ago_low)
difference = round(difference, 2)

diff_percentage = ((one_day_ago_low - two_days_ago_low) / two_days_ago_low) * 100
print(f"% diff: {diff_percentage}")
print("-"*50)

# diff_percentage = 5.68  # for testing purposes
# diff_percentage = -6.41  # for testing purposes

if abs(diff_percentage) >= 5:
    print("Getting news...")
    news_parameters = {
        "q": COMPANY_NAME,
        "from": dates[1],
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,
    }

    news_response = requests.get(NEWS_ENDPOINT, news_parameters)
    news_data = news_response.json()

    first_three_articles = news_data["articles"][:3]

    headlines_and_description = [[article["title"], article["description"], article["url"]] for article in first_three_articles]

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        print("Logging in with email...")
        connection.login(my_email, my_password)
        if diff_percentage >= 5:
            chart = up_chart
            text = "up"
        elif diff_percentage <= -5:
            chart = down_chart
            text = "down"
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg=(
                f"Subject:{COMPANY_NAME} is {text} {abs(diff_percentage)}% {chart}! Here is the news.\n\n"
                f"Here are the three articles that could possibly have something to do with this price change.\n"
                f"{'-' * 50}\n"
                f"Headline: {headlines_and_description[0][0]}\n"
                f"Brief: {headlines_and_description[0][1]}\n"
                f"Continue reading here: {headlines_and_description[0][2]}\n"
                f"{'-' * 50}\n"
                f"Headline: {headlines_and_description[1][0]}\n"
                f"Brief: {headlines_and_description[1][1]}\n"
                f"Continue reading here: {headlines_and_description[1][2]}\n"
                f"{'-' * 50}\n"
                f"Headline: {headlines_and_description[2][0]}\n"
                f"Brief: {headlines_and_description[2][1]}\n"
                f"Continue reading here: {headlines_and_description[2][2]}\n"
                f"{'-' * 50}\n"
            ).encode('utf-8')
        )
        print("Email Sent Successfully!")
else:
    print("No big fluctuations in price...")

# Optional: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

