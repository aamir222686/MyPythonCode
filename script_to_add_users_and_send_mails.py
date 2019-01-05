import datetime
from smtplib import SMTP, SMTPException, SMTPAuthenticationError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "aamirhussain.bil@gmail.com"
password = "asima123"
from_email = username

class MessageUser():
	user_details = []
	#to put email id and formatted messages into email_details
	email_details = []
	#just messages which will be saved here
	messages = []
	base_message = """
	Hello {name}!!
	Total Amount : {total}
	Transaction Date : {date}
	"""
	#function to collect user details
	def collect_details(self, name, amount, email=None):
		#format name and amount to capitalize the first letter in name and show only 2 decimal factors in amount
		name = name[0].upper() + name[1:].lower()
		amount = "%.2f" %(amount)
		today = datetime.date.today()
		date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
		#create a dict and append this dict to user_details
		detail = {
			"name": name,
			"amount": amount,
			"date": date_text,
		}
		if email != None:
			detail["email"] = email
		self.user_details.append(detail)
	#function to show the details collected
	def show_users(self):
		return self.user_details
	#function to create messages that we can send to the users and also creating a new dict with just email and the message to be sent
	def make_message(self):
		#need to make sure if there are things added in user_details or if not return a null list
		#and also collect the email and the message once formatted and append it to email_details or else just add it to messages
		if len(self.user_details) > 0:
			for detail in self.show_users():
				#collect the attributes to add into the base message which can be formatted here
				name = detail["name"]
				amount = detail["amount"]
				date = detail["date"]
				message = self.base_message
				user_msg = message.format(name=name, total=amount, date=date)
				#get the email from the detail list and add a if else statement to either add details,
				#in email_details [] or messages []
				#and create a new dict of user date with email and formatted message and then append it to email details
				user_email = detail.get("email")
				if user_email:
					user_data = {
						"user_mail": user_email,
						"user_message": user_msg
					}
					self.email_details.append(user_data)
				else:
					self.messages.append(user_msg)
			return self.messages
		return []
	#a function to use the data and open a email connection and send the mail to teh Users.
	def send_message(self):
		#this will be a contination of the make_message function
		self.make_message()
		#this function will only run if something has been added to the email_details list
		#return tru or false if this fucntion is set
		if len(self.email_details) > 0:
			#start a loop to look into and send a message for every user with a custom pre-formatted message
			#contains all the definations of the email list and the message list to be sent to the users.
			for detail in self.email_details:
				user_mail_id = detail["user_mail"]
				user_message_send = detail["user_message"]
				#try and raise an exception with a custom message if there are any smtp errors
				try:
					email_conn = SMTP(host, port)
					email_conn.ehlo()
					email_conn.starttls()
					email_conn.login(username, password)
					#create a plain message here and create a Subject, From and To attribute with MIMEMultipart
					#create the message and add it into the MIMEMultipart with MIMEText
					the_msg = MIMEMultipart("alternative")
					the_msg["Subject"] = "Your Billing Details"
					the_msg["From"] = from_email
					the_msg["to"] = user_mail_id
					part_1 = MIMEText(user_message_send, "plain")
					the_msg.attach(part_1)
					#send this message to the added number of people(add the thing as a list)
					email_conn.sendmail(from_email, user_mail_id, the_msg.as_string())
					email_conn.quit()
				except SMTPException:
					print("Email Not Sent")
			return True
		return false
			



					
						





