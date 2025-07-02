
import smtplib

try:
    # Connect to the Gmail SMTP server
    server = smtplib.SMTP("smtp.gmail.com", port=587)
    server.starttls()  # Start TLS encryption

    # Receiver email
    receiver_mail = input("Enter the receiver email: ")

    # Sender credentials
    sender_mail = 'iammohit3520@gmail.com'  # Corrected email
    password = "ufzd tqca lkjw wjaf"  # App password (not regular password)

    # Login to the server
    server.login(sender_mail, password)

    # Mail content
    subject = input("Enter the subject of the mail: ")
    body = input("Enter the body of the mail: ")
    message = f'Subject: {subject}\n\n{body}'

    # Send the email
    server.sendmail(sender_mail, receiver_mail, message)
    print("Mail sent successfully.")

    server.quit()  # Close the server connection

except Exception as e:
    print(f"An error occurred: {e}")
