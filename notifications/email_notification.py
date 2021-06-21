import smtplib
import configparser
from email.message import EmailMessage
from notifications.notification import Notification
from clients.client import Client


class EmailNotification(Notification):

    @staticmethod
    def notify(title: str, content: str, client: Client):
        msg = EmailMessage()
        msg.set_content(content)

        msg['Subject'] = f'{title} is available'
        msg['From'] = "Availability-checker@do-not-reply"
        msg['To'] = client.email

        print(content)
        config = configparser.ConfigParser()
        config.read('./notifications/email_credentials.ini')
        email_username = config['default']['username']
        email_password = config['default']['password']

        
        # server = smtplib.SMTP('localhost', 8025)
        # con = server
        # con.ehlo()
        # con.starttls()
        # con.ehlo()
        # server.login(USERNAME, PASSWORD)
        # server.sendmail(USERNAME, client.email, content)
        # con.sendmail(email_from, email_to, email_body)
        # con.quit()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo_or_helo_if_needed()
        server.starttls()
        server.ehlo_or_helo_if_needed()
        server.login(email_username, email_password)
        # server.sendmail(USERNAME, client.email, content)
        server.send_message(msg)
        server.quit()
