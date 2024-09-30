# SMTP Email Sending Application ✉️

## Overview 🌟
The **SMTP Email Sending Application** is a Python-based tool that allows users to send emails with optional attachments (images and PDFs) via Gmail's SMTP server. It leverages environment variables to securely manage email credentials and provides a simple user interface for inputting email details.

## Features 🚀
- Send emails with custom subject and body.
- Attach images and PDF files. 📷📄
- User-friendly input prompts for easy operation. 📝
- Error handling for attachment failures and sending issues. ⚠️

## Requirements 📋
- Python 3.x
- `python-dotenv` package

## Installation ⚙️

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sarveshmscss/SMTP_Mail.git
   cd SMTP_Mail
   ```

2. **Install Dependencies**:
   ```bash
   pip install python-dotenv
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the project root directory with the following content:
   ```plaintext
   mail_id=your_email@gmail.com
   mail_password=your_password
   ```

   **Note**: Replace `your_email@gmail.com` and `your_password` with your actual Gmail credentials. Ensure that you have allowed "Less secure app access" in your Google account settings for SMTP to work.

4. **Ignore the `.env` File**:
   Add the `.env` file to your `.gitignore` to prevent it from being tracked by Git:
   ```plaintext
   .env
   ```

## Usage 📤

1. **Run the Application**:
   Open your terminal or command prompt and execute:
   ```bash
   python app.py
   ```

2. **Provide Input**:
   You will be prompted to enter:
   - **Receiver Email ID**: The recipient's email address. 📧
   - **Subject**: The subject line of the email. 🗒️
   - **Body**: The main content of the email. ✏️
   - **Image Path**: (Optional) The file path of an image to attach. 🌄
   - **PDF Path**: (Optional) The file path of a PDF to attach. 📑

3. **Email Sending**:
   After entering the details, the application will attempt to send the email and will notify you of the success or failure. ✅

## Example 💬
Here’s how the command line interaction may look:

```plaintext
Enter the Receiver Mail id: example@example.com
Enter the subject: Test Email
Enter the Body of the mail: This is a test email.
Enter the Image path (leave blank if not applicable): C:\path\to\image.jpg
Enter the PDF file path (leave blank if not applicable): C:\path\to\file.pdf
Email sent successfully
```

## Error Handling ⚠️
The application provides feedback if:
- An attachment fails to load. ❌
- The email fails to send. 📭


## Author 👨‍💻
- Sarvesh K. - [GitHub Profile](https://github.com/sarveshmscss)

---
