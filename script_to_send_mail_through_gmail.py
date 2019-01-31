from smtplib import SMTP, SMTPAuthenticationError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Specify the HOST, PORT, username, password, from and to list
host = "smtp.gmail.com"
port = 587
username = "aamirhussain.bil@gmail.com"
password = "asima123"
from_mail = "aamirhussain.bil@gmail.com"
to_list = ["aamir222686@yahoo.com"]
#create a try except block with a SMTPException if anything goes wrong with connection it will throw a error
try:
    #Connect HOST and Port which is already specified, ehlo() will talk to the smtp server and then starttls will start the connection
    email_conn = SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    #login with the already specified username and password
    email_conn.login(username, password)
    #2 parts first MIMEMultipart will have different parts of mails, from, to, subject and the message
    the_msg = MIMEMultipart("alternative")
    the_msg["subject"] = "Hello There!"
    the_msg["From"] = from_mail
    #the_msg["To"] = to_list
    #we will need a html versiona and a plain version, if html is not supported it will render the plain text message  
    plain_txt = "Testing the message"
    html_txt = """\
    <html>
      <head></head>
      <body>
        <p>Hey!<br>
          Testing this email <b>message</b>. Made by <a href='https://vuedigitalmedia.com'>Team VUE</a>.
        </p>
      </body>
    </html>
    """
    #Create 2 parts with the mimetext and attach it to the MULTIPART message
    part_1 = MIMEText(plain_txt, "plain")
    part_2 = MIMEText(html_txt, "html")
    the_msg.attach(part_1)
    the_msg.attach(part_2)
    #Send the message as string
    email_conn.sendmail(from_mail, to_list, the_msg.as_string())
    email_conn.quit()
#except will add an exception and trow a error message    
except SMTPAuthenticationError:
    print("Can't Send Mail")
