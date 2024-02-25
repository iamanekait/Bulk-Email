# Bulk Email Sender

This Python script allows you to send bulk emails with optional attachments using Gmail's SMTP server. It's particularly useful for sending announcements, newsletters, or notifications to a list of recipients stored in an Excel file.

## Prerequisites

Before using this script, ensure you have the following:

- Python installed on your system.
- Necessary Python libraries installed (`pandas`, `smtplib`).
- An Excel file named "Email.xlsx" containing a column named "Emails" with the list of recipient email addresses.
- Access to a Gmail account with "less secure apps" access enabled (if using Gmail's SMTP server).

## Setup

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/yourusername/bulk-email-sender.git
    ```

2. Install the required Python libraries:

    ```bash
    pip install pandas
    ```

3. Ensure your Gmail account allows access to "less secure apps". You can enable this in your [Gmail settings](https://myaccount.google.com/lesssecureapps).

4. Open the script (`bulk_email_sender.py`) in a text editor and follow the instructions to input your email address, password, subject, message, and attachment path (if any).

## Usage

Run the script using Python:

```bash
python bulk_email_sender.py
```

The script will prompt you to input your email address and password. Then, it will read the list of recipient email addresses from the Excel file and ask for the email subject, message, and attachment path. Once you provide all necessary inputs, it will send emails to each recipient.

## Notes

- Make sure to handle sensitive information (like passwords) securely, especially if sharing or storing this script.
- Consider testing with a small list of email addresses before sending to a large audience.
- Be aware of Gmail's sending limits to avoid hitting any restrictions.

## Contribution

Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback and contributions are highly appreciated!

## License

This project is licensed under the [MIT License](LICENSE).
