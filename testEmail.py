
# For testing the email and app password
# As google stops allowing the less secure apps
# The solution come into light which is to generate app password that is only one time viewed with any app name.

import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('hari9000kmph@gmail.com', 'brrm dnbr iueu vmlb ')
    print("Login successful")
    server.quit()
except smtplib.SMTPAuthenticationError as e:
    print("Authentication failed:", e)
