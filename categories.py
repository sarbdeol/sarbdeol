
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import traceback
import smtplib
from email.message import EmailMessage
import mimetypes
main=['Tiptree',
    'Satu',
    'Billericay',
    'Braxted',
    'Baddow',
    'lister',
    'Writtle',
    'Jhon ray',
    'Felsted',
    'Tollsbery', 
    'Bardfield',
    'Stock',
    # 'Terling',
    'Rayne',
    'Mayflower',
    'Notley'
    'Frailty'
    ]
def mailsent(message_body, recipient_email, attachment_path):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # 587 is the default for TLS
    smtp_username = 'sarbtech123@gmail.com'
    smtp_password = 'fpaibhjdkuifdifs'
    sender_email = 'sarbtech123@gmail.com'

    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = 'Subject of the Email'
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg.set_content(message_body)

    # Attach the file
    with open(attachment_path, 'rb') as attachment_file:
        attachment_data = attachment_file.read()
        attachment_name = attachment_path.split('/')[-1]
        attachment_type, _ = mimetypes.guess_type(attachment_path)
        attachment_main_type, attachment_sub_type = attachment_type.split('/')

        msg.add_attachment(
            attachment_data,
            maintype=attachment_main_type,
            subtype=attachment_sub_type,
            filename=attachment_name
        )

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
def read_existing_entries(filename):
    entries = set()
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                entries.add(tuple(row))
    except FileNotFoundError:
        pass
    return entries

def write_to_csv(filename, data):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Read existing entries
existing_openings = read_existing_entries('openings.csv')
existing_openings2 = read_existing_entries('allopenings.csv')
existing_errors = read_existing_entries('errors.csv')
# Set up the WebDriver
from selenium.webdriver.chrome.options import Options

# Create Chrome options
options = Options()
# options.add_argument('--remote-debugging-port=9222')
# Set a common window size
options.add_argument("--headless")
# options.headless = True
options.add_argument('--no-sandbox')  # Bypass OS security model
options.add_argument("--window-size=1920,1080")
# Initialize ChromeDriver with the specified options1
from selenium.webdriver.chrome.service import Service

# Specify the path to the ChromeDriver executable
chrome_driver_path = '/usr/local/bin/chromedriver'

# Create a Service object with the specified path
chrome_service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.maximize_window()
# Open the website
driver.get('https://mse.allocate-cloud.co.uk/EmployeeOnlineMobile/MSELIVE/#/home')

# Wait for the username field to be present and enter the username
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "Username"))
).send_keys('Pezhumkattil31948952')

# Wait for the password field to be present and enter the password
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "Password"))
).send_keys('Jinubinoy4321')

# Wait for the login button to be clickable and click it
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "btnLogin"))
).click()

# Wait for the page to load after login
WebDriverWait(driver, 10).until(
    EC.url_contains('home')
)

# Navigate to the bank shifts page
driver.get('https://mse.allocate-cloud.co.uk/EmployeeOnlineMobile/MSELIVE/#/bankshifts/shifts')

# Define a function to check for openings
def check_openings():
    try:
        listdata = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="item sticky"]/div'))
        )
        
        # Click each element found
        count=0
        for i in listdata:
            message_body = "Here is the screenshot."
            recipient_email = 'bmathew208@gmail.com'
            day=i.find_element(By.XPATH,'.//div/span[@class="sub"]')
            date=i.find_element(By.XPATH,'.//div/span[@class="title"]')
            detaildata = WebDriverWait(i, 5).until(
                    EC.presence_of_all_elements_located((By.XPATH, './/div[@class="details"]'))
                )
            print(len(detaildata))
            
            for j, item in enumerate(detaildata):
                name = item.find_element(By.XPATH, './/h2').text
                timed = item.find_element(By.XPATH, ".//span[@class='time-display']/span").text
                print(f"Name: {name}, Time: {timed},day :{day.text}")
                entry = (name, timed,day.text,date.text)
                
                if entry not in existing_openings2 :
    
                    write_to_csv('allopenings.csv', entry)
                    existing_openings2.add(entry)
                
                check_time=int(timed.split(':')[0])
                for i in main:
                    if i.lower() in name.lower():
                        print(f'{i} Found')
                        item.click()
                        if entry not in existing_openings :
                    
                            print("Clicked on an opening")
                            print(f"Name: {name}, Time: {timed} ,day :{day.text}")
                            write_to_csv('openings.csv', entry)
                            existing_openings.add(entry)
                            message_body = "Here is the screenshot."
                            recipient_email = 'bmathew208@gmail.com'  # Replace with the actual recipient email
                            attachment_path = 'triptree.png'  # Replace with the path to your screenshot
                            driver.save_screenshot(attachment_path)
                            mailsent(message_body, recipient_email, attachment_path)
                            
                            if day.text.lower()=='sunday' or day.text.lower()=='saturday' and check_time>=17:
                                print('weekoff')
                                time.sleep(1)
                                print(count)
                                # item.find_element(By.XPATH, '//div[@class="a-section booking"]/button').click()
                                book_button = WebDriverWait(driver, 10).until(
                                    EC.presence_of_all_elements_located((By.XPATH, "//button[contains(text(), 'Book')]"))
                                )
                                
                                # Click the button
                                
                                book_button[count].click()
                                print("click book button")
                                button = WebDriverWait(driver, 10).until(
                                    EC.element_to_be_clickable((By.XPATH, ".//button[contains(text(), 'Book Bank')]"))
                                )

                                # Click the button
                                button.click()
                                print('booked')
                                
                                time.sleep(2)
                                
                                try:
                                    bookpop=driver.find_element(By.XPATH,'//div[@class="booking-confirmation-dialog"]').text
                                    write_to_csv('bookpop.csv', [bookpop])
                                    button = WebDriverWait(driver, 10).until(
                                        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Close')]"))
                                    )

                                    # Click the button
                                    button.click()
                                    item.click()
                                except:
                                    
                                    item.click()
                                    pass
                                attachment_path = 'week_off_book.png'  # Replace with the path to your screenshot
                                driver.save_screenshot(attachment_path)
                                mailsent(message_body, recipient_email, attachment_path)
                                time.sleep(1)
                                buttonclose = WebDriverWait(driver, 10).until(
                                        EC.element_to_be_clickable((By.XPATH, ".//button[contains(text(), 'Close')]"))
                                    )

                                # Click the button
                                buttonclose.click()
        
                            else:
                                
                                if check_time>=17 :
                                    print('job time after 17:00')
                                    time.sleep(1)
                                    print(count)
                                    book_button = WebDriverWait(driver, 15).until(
                                        EC.presence_of_all_elements_located((By.XPATH, "//button[contains(text(), 'Book')]"))
                                    )
                                    
                                    # Click the button
                                    book_button[count].click()
                                    print("click book button")
                                    button = WebDriverWait(driver, 10).until(
                                        EC.element_to_be_clickable((By.XPATH, ".//button[contains(text(), 'Book Bank')]"))
                                    )

                                    # Click the button
                                    button.click()
                                    print('booked')
                                    
                                    time.sleep(2)
                                    attachment_path = 'job_book.png'  # Replace with the path to your screenshot
                                    driver.save_screenshot(attachment_path)
                                    mailsent(message_body, recipient_email, attachment_path)
                                    time.sleep(1)
                                    bookpop=driver.find_element(By.XPATH,'//div[@class="booking-confirmation-dialog"]').text
                                    write_to_csv('bookpop2.csv', [bookpop])
                                    buttonclose = WebDriverWait(driver, 10).until(
                                        EC.element_to_be_clickable((By.XPATH, ".//button[contains(text(), 'Close')]"))
                                    )

                                    # Click the button
                                    buttonclose.click()
                                
                                    time.sleep(1)
                                else:
                                    item.click()
                        else:
                            item.click()
                count+=1
            
            print("There are openings")
        return True
       
    except Exception as e:
        driver.save_screenshot('k.png')
        print("No job found")
        error_entry = (str(e))
        print(error_entry)
        if error_entry not in existing_errors:
            write_to_csv('errors.csv', [error_entry])
            existing_errors.add(error_entry)
        return False

# Refresh and check for openings at 5-second intervals
while True:  # Refresh and check for 1 minute (12 times with 5-second intervals)
    driver.refresh()
    if check_openings():
        pass
    time.sleep(4)

# Close the WebDriver
# driver.quit()
