import os
import smtplib
from openpyxl import Workbook
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders


def get_item_data():
    item_name = input("Enter item name: ")
    quantity = int(input(f"Enter quantity of {item_name}: "))
    price_per_item = float(input(f"Enter price per item of {item_name}: "))
    total_cost = quantity * price_per_item
    return [item_name, quantity, price_per_item, total_cost]


def send_email(sender_email, receiver_email, subject, body, filename):
    """Sends an email with the Excel file attached."""
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Date'] = formatdate(localtime=True)
    message['Subject'] = subject
    message.attach(MIMEText(body))

    part = MIMEBase('application', "octet-stream")
    with open(filename, "rb") as attachment:
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="items.xlsx"')
    message.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)  
    server.starttls()
    server.login(sender_email, "teez ayih rfrx nmgd")  
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()


def main():
    wb = Workbook() 
    ws = wb.active
    ws.title = "Items"

    headers = ["Item Name", "Quantity", "Price per Item", "Total Cost"]
    ws.append(headers)

    items = []
    while True:
        item = get_item_data()
        items.append(item)
        more_items = input("Do you want to add another item? (yes/no): ")
        if more_items.lower() not in ['yes', 'y']:
            break

    for item in items:
        ws.append(item)

    total_cost = sum(item[3] for item in items)
    ws.append(["", "", "Total Cost", total_cost])

    file_name = os.path.join(current_directory, "items.xlsx")
    wb.save(file_name)

    print(f"Data has been saved to {file_name}")

    user_email = input("Enter your email address: ")

    sender_email = "salman39302@gmail.com"  
    subject = "Items List - from xyz market"
    body = "This email contains the list of items that you purchased in xyz market."

    send_email(sender_email, user_email, subject, body, file_name)

    print(f"Data has been saved to {file_name} and sent to your email.")


if __name__ == "__main__":
    current_directory = os.getcwd()
    print(f"Files will be saved in: {current_directory}")
    main()
    