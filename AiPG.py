#**this is a sample**
@AiPG
import random
import string
import datetime
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set password expiry time to 24 hours
EXPIRY_TIME_HOURS = 24

def generate_password(length=8, name='', id='', status='ordinary', email=''):
    """Generates a random password consisting of uppercase letters, lowercase letters, symbols, and numbers (at least 3), with a maximum length of 8."""
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    symbols = string.punctuation
    numbers = string.digits
    all_characters = uppercase_letters + lowercase_letters + symbols + numbers
    
    # Make sure there are at least 3 numbers in the password
    numbers_needed = 3
    password = ''.join(random.choice(numbers) for i in range(numbers_needed))
    password += ''.join(random.choice(all_characters) for i in range(length - numbers_needed))
    password = ''.join(random.sample(password, len(password)))
    
    expiry_date = (datetime.datetime.now() + datetime.timedelta(hours=EXPIRY_TIME_HOURS)).strftime("%Y-%m-%d %H:%M:%S")
    
    # Send email confirmation
    sender_email = "your_email@example.com"  # Replace with your own email address
    sender_password = "your_email_password"  # Replace with your own email password
    receiver_email = email
    
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Password Confirmation"
    
    body = f"Hello {name},\n\nYour password is {password} and it expires on {expiry_date}.\n\nThank you for using our service!\n\nBest regards,\nYour Company Name"
    
    message.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print(f"Confirmation email sent to {receiver_email}.")
    except Exception as e:
        print(f"Error: {e}")
    
    return password, expiry_date, name, id, status

# Example usage
payment_confirmed = True  # Replace with actual payment confirmation logic
if payment_confirmed:
    email = "john.doe@example.com"  # Replace with user's email
    password, expiry_date, name, id, status = generate_password(length=12, name='John Doe', id='123456', status='VVIP', email=email)
    print(f"Password: {password}")
    print(f"Password expires on: {expiry_date}")
    print("Password confirmation sent successfully.")
    
    # Save password to CSV file
    with open(f"{name}_{id}.csv", mode='w', newline='') as password_file:
        password_writer = csv.writer(password_file)
        password_writer.writerow(['Name', 'ID', 'Status', 'Password', 'Expiry Date'])
        password_writer.writerow([name, id, status, password, expiry_date])
        
    print("Password downloaded successfully.")
else:
    print("Payment not confirmed.")
