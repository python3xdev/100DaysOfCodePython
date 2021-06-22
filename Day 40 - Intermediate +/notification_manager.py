from twilio.rest import Client
import smtplib

MY_EMAIL = YOUR_GMAIL_ADDRESS
MY_PASSWORD = YOUR_GMAIL_PASSWORD


class NotificationManager:

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr="doej26937@gmail.com",
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
            print("Emails sent successfully.")
