import os
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587  # 587 is the default for TLS
EMAIL_ADDRESS = 'sarbtech123@gmail.com'
EMAIL_PASSWORD = 'fpaibhjdkuifdifs'
TO_EMAIL = 'bmathew208@gmail.com'

# Path to the Python script
SCRIPT_PATH = '/root/sarbdeol/categories.py'
PYTHON_ENV_PATH = '/root/venv/bin/python'

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Email sent: {subject}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def is_script_running():
    try:
        # Check if the script is running
        result = subprocess.run(['pgrep', '-f', SCRIPT_PATH], stdout=subprocess.PIPE)
        return result.stdout.strip() != b''  # Returns True if script is running
    except Exception as e:
        print(f"Error checking script: {e}")
        return False

def restart_script():
    try:
        # Restart the script
        subprocess.Popen([PYTHON_ENV_PATH, SCRIPT_PATH])
        return True
    except Exception as e:
        print(f"Error restarting script: {e}")
        return False

def main():
    # Check the script status
    if not is_script_running():
        if restart_script():
            subject = "Script Restarted"
            body = f"The script {SCRIPT_PATH} has been restarted."
        else:
            subject = "Script Failed to Restart"
            body = f"The script {SCRIPT_PATH} is not running and failed to restart."
    else:
        subject = "Script Running"
        body = f"The script {SCRIPT_PATH} is running ."

    send_email(subject, body)

if __name__ == "__main__":
    main()
