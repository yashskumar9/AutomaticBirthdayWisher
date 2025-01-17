# Automatic Birthday Wisher

This Python script automatically sends personalized birthday wishes to people based on their birthdates stored in a `birthdays.csv` file. It randomly selects a quote from a file and sends an email with a custom message using the SMTP protocol. This script is designed to run continuously and can be hosted on platforms like [PythonAnywhere](https://www.pythonanywhere.com/) for 24/7 operation.

## Features
- Automatically checks today's date and compares it with the `birthdays.csv` file.
- Sends personalized birthday wishes via email.
- Randomly selects a birthday quote from a list.
- Easy to customize with a predefined letter template.

## Project Structure

```plaintext
.
├── birthdays.csv           # Stores birthday data (Name, Email, Date, Month)
├── birthday_wishes.txt     # File containing multiple birthday quotes
├── letter.txt              # Template for the birthday wish
├── main.py                 # Python script to send the emails
├── .env                    # Environment variables (Email credentials)

```

## Prerequisites

1. Python 3.x installed.
2. Install the required Python libraries:
   ```bash
   pip install pandas python-dotenv
   ```
3. A Gmail account to send emails (or any other SMTP-compatible email service).
4. An account on PythonAnywhere (optional, for 24/7 hosting).

## Setup Instructions

1. Configure the ``birthdays.csv`` File
   Create a ``birthdays.csv`` file with the following format:
   ```csv
   name,email,day,month
   John Doe,johndoe@gmail.com,15,1
   Jane Doe,janedoe@gmail.com,20,2
   ```
  - name: Name of the person.
  - email: Email Address of the person.
  - day: Day of the person's birthday.
  - month: Month of the person's birthday.

2. Add Birthda Quotes
   Create a ``birthday_wishes.txt file with multiple quotes, each on a new line. Example:
   ```plaintext
   Wishing you a day filled with love, joy, and laughter!
   Hope your birthday is as amazing as you are!
   May your birthday be as special as you make everyone feel!
   ```

3. Create the Letter Template
   Create a ``letter.txt`` file with placeholders for the name and quote. Example:
   ```plaintext
   Dear [NAME],

   Happy Birthday! 🥳🎂
    
   [QUOTE]
    
   Wishing you all the best on your special day!
    
   Best wishes,  
   Your Friend
   ```
  - Use ``[NAME]`` as a placeholder for the recipient's name.
  - Use ``[QUOTE]`` as a placeholder for a randomly selected birthday quote.

4. Add Environment Variables
   Create a ``.env`` file in the root directory and add your email credentials:
   ```plaintext
   MY_EMAIL=youremail@gmail.com
   MY_PASSWORD=yourpassword
   ```

   Important:  For Gmail users, you need to enable "Less Secure App Access" or generate an App Password.

5. Run the Script Locally
   Run teh script using:
   ```bash
   python main.py
   ```

6. Deploy on PythonAnywhere (Optional)
To run this script continuously, upload the project to [PythonAnywhere](https://www.pythonanywhere.com/) and configure a daily scheduled task to execute the script.

## Notes

- Ensure your email service supports SMTP and allows automated emails.
- For privacy and security, do not share your ``.env`` file or email credentials publicly.

  
- Test the script before deploying it live.
   
