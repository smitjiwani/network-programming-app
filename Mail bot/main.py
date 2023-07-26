import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()

# server.starttls()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('senders-mail', password) # sender's mail and password (password should be in a text file in hashed format for security purposes)

msg = MIMEMultipart()
msg['From'] = 'sender-username'
msg['To'] = 'recievers-mail'
msg['Subject'] = 'Just a Test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'gff.jpg'

attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('senders-mail', 'recievers-mail', text) # sender's mail and reciever's mail