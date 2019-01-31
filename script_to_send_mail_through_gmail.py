from smtplib import SMTP, SMTPAuthenticationError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Specify the HOST, PORT, username, password, froma and to list
host = "smtp.gmail.com"
port = 587
username = "aamirhussain.bil@gmail.com"
password = "asima123"
from_mail = "aamirhussain.bil@gmail.com"
to_list = ["aamir222686@yahoo.com"]

try:
    email_conn = SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)
    the_msg = MIMEMultipart("alternative")
    the_msg["subject"] = "Hello There!"
    the_msg["From"] = from_mail
    #the_msg["To"] = to_list
    plain_txt = "Testing the message"
    html_txt = """\
    <html>
      <head></head>
      <body>
        <p>Hey!<br>
          Testing this email <b>message</b>. Made by <a href='http://joincfe.com'>Team CFE</a>.
        </p>
      </body>
    </html>
    """
    part_1 = MIMEText(plain_txt, "plain")
    part_2 = MIMEText(html_txt, "html")
    the_msg.attach(part_1)
    the_msg.attach(part_2)
    email_conn.sendmail(from_mail, to_list, the_msg.as_string())
    email_conn.quit()
except SMTPAuthenticationError:
    print("Can't Send Mail")
