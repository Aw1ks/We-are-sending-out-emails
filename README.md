# We-are-sending-out-emails
Create a file .env in the root directory of the project and add the following variables:

```
SMTP_SERVER=<address of the smtp_server> # Example: smtp.gmail.com
SMTP_PORT=<port_smtp_server> # Example: 587
EMAIL_USERNAME=<your_mail address>
EMAIL_PASSWORD=<email password>
SENDER_EMAIL=<sender's address> # May match EMAIL_USERNAME
RECEIVER_EMAIL=<recipient's address>
```
Important: Do not store passwords in code! Use environment variables.

how they are used:
```
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = os.getenv('SMTP_PORT')
username = os.getenv('EMAIL_USERNAME')
password = os.getenv('EMAIL_PASSWORD')
sender_email = os.getenv('SENDER_EMAIL')
receiver_email = os.getenv('RECEIVER_EMAIL')
```
