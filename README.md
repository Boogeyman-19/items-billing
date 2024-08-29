

# Items List Script

This Python script allows users to input item details (name, quantity, price per item) and generates an Excel sheet that summarizes the entered data. The script also calculates the total cost and sends the Excel file as an email attachment to a specified email address.

## Features

- **Item Data Entry**: Collect item details from the user (item name, quantity, price per item).
- **Excel File Generation**: Store the entered item details in an Excel sheet using the `openpyxl` library. The sheet includes columns for item name, quantity, price per item, and total cost.
- **Email with Attachment**: The generated Excel file is sent as an email attachment using the `smtplib` and `email` libraries.

## Requirements

This script requires the following Python libraries:
- `os`
- `smtplib`
- `openpyxl`
- `email.mime`
- `email.utils`

To install the necessary libraries, you can use `pip`:

```bash
pip install openpyxl
```

## Usage

1. **Run the Script**: Execute the Python script using the command below:

   ```bash
   python items.py
   ```

2. **Input Data**: You will be prompted to input the following information for each item:
   - Item name
   - Quantity
   - Price per item

3. **Save Data**: After entering the items, the script will save the data in an Excel file named `items.xlsx`.

4. **Email**: The script will then ask for your email address. It will send the Excel file as an attachment to the provided email.

## Email Configuration

The script uses Gmail's SMTP server to send emails. Make sure to adjust the following email configuration in the code:

```python
sender_email = "your_email@gmail.com"
sender_password = "your_password"
```

**Note**: For security reasons, you should generate an App Password in your Google Account rather than using your regular password. You can generate an App Password by going to your Google Account settings under "Security."

## Example

Here's an example of how the script works:

1. **Item Entry**:
   ```
   Enter item name: Apples
   Enter quantity of Apples: 5
   Enter price per item of Apples: 1.20
   ```

2. **Another Item**:
   ```
   Do you want to add another item? (yes/no): yes
   Enter item name: Bananas
   Enter quantity of Bananas: 8
   Enter price per item of Bananas: 0.50
   ```

3. **Finish**:
   ```
   Do you want to add another item? (yes/no): no
   ```

4. **Email**:
   ```
   Enter your email address: example@example.com
   Data has been saved to /path/to/items.xlsx and sent to your email.
   ```

Feel free to customize this README file according to your specific needs and requirements!
