from selenium import webdriver
import pandas as pd
import pandas as pd
import os.path
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from database import *
options = Options()
# options.add_argument('--remote-debugging-port=9222')
# Set a common window size
# options.add_argument("--headless")
# options.headless = True
options.add_argument("--window-size=1920,1080")
# Initialize ChromeDriver with the specified options1
# driver = webdriver.Chrome(options=options,executable_path='/usr/local/bin/chromedriver')
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)  # Adjust the timeout as needed
def get_company_link(company_url):
    # Open the company URL in a new tab
    driver.execute_script("window.open(arguments[0]);", company_url)

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[1])
    wait.until(EC.presence_of_element_located((By.XPATH,'.//a[@data-tn-element="companyLink[]"]')))

    # Get the data you need from the new tab
    # For example, you can get the company name from the new tab
    company_link = driver.find_element(By.XPATH, './/a[@data-tn-element="companyLink[]"]').get_attribute('href')
    print(company_link)
    # Close the new tab
    driver.close()

    # Switch back to the original tab
    driver.switch_to.window(driver.window_handles[0])
    return company_link

# Read the Excel file
df = pd.read_excel("Tech Job Titles and Search Operators.xlsx", sheet_name="Indeed Operator Strings")


# Extract all rows
all_rows = df.values.tolist()

print("All rows:")

for row in all_rows:
    
    
    if not isinstance(row[1], float):
        print(row)
        job_category=row[0].split('-')[0]
        Prompt_Name	=row[0]
        Prompt	=row[1]
        Location	=row[2]
      									

       
        
        driver.get(f'https://ca.indeed.com/jobs?q={Prompt}&l=British+Columbia&start=0')
       
        wait = WebDriverWait(driver, 30)  # Adjust the timeout as needed
        element = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='jobsearch-JobCountAndSortPane-jobCount css-13jafh6 eu4oa1w0']/span")))

        No_of_Jobs=driver.find_element(By.XPATH,"//div[@class='jobsearch-JobCountAndSortPane-jobCount css-13jafh6 eu4oa1w0']/span").text
        pagecount=No_of_Jobs.split(' ')[0].strip()
        pagecount=int(int(pagecount)/10)
        print(pagecount)
        data = []
        job_links=[]
        
        for i in range(0,2):
            print(f'page {i}')
            url=f'https://ca.indeed.com/jobs?q={Prompt}&l=British+Columbia&start={i}'
            driver.get(url)
            print(url)
            element = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='jobsearch-JobCountAndSortPane-jobCount css-13jafh6 eu4oa1w0']/span")))
            # driver.save_screenshot("indeed.png")
            try:
                driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]').click()
            except:
                print('skip cookies')
            
            cards = driver.find_elements(By.XPATH, ".//td[@class='resultContent css-1qwrrf0 eu4oa1w0']")

            

            for card in cards:
                link=card.find_element(By.XPATH, './/div/h2/a').get_attribute('href')
                print(link)
                job_links.append(link)
        print(len(job_links))
        columns=[]
        for link in job_links:
            driver.get(link)
            element = wait.until(EC.presence_of_element_located((By.XPATH,".//h1")))
            job_title=driver.find_element(By.XPATH, ".//h1").text
            
            company=driver.find_element(By.XPATH, './/span[@class="css-1saizt3 e1wnkr790"]').text
            company_url=driver.find_element(By.XPATH, './/span[@class="css-1saizt3 e1wnkr790"]/a').get_attribute('href')
            # date=datetime.now()
            company_link=get_company_link(company_url)

            # formatted_date = date.strftime("%d %B %Y")
            
            salery_jobtype=driver.find_element(By.XPATH, './/div[@id="salaryInfoAndJobType"]').text
            if '-' in salery_jobtype:
                Salary_range=salery_jobtype.split('-')[0]
                Job_Type=salery_jobtype.split('-')[1]
            else:
                Salary_range=''
                Job_Type=salery_jobtype

          
            location=driver.find_element(By.XPATH, '//*[@data-testid="inlineHeader-companyLocation"]/div').text
            if 'remote' in location.lower():
                Work_Type='Remote'
            else:
                Work_Type=''
            City = location.split(',')[-2].strip()
            State = location.split(',')[-1].strip()
            try:
                description = driver.find_element(By.XPATH, '//*[@id="jobDescriptionText"]').text
            except:
                description=''

            
            review=driver.find_element(By.XPATH,'//*[@id="viewJobSSRRoot"]/div/div[3]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div/span/a').text
           
            Rating=driver.find_element(By.XPATH,'//*[@id="companyRatings"]').get_attribute("aria-label")
            Rating=Rating.split('out')[0].strip()
            Indeed_Link	=link

            columns.append({
                "Job Category": job_category,
                "Prompt Name": Prompt_Name,
                "Prompt": Prompt,
                "Indeed Location": Location,
                "No of Jobs": No_of_Jobs,
                "Job Title": job_title,
                "Company Name": company,
                "Rating": Rating,
                "Reviews": review,
                "Company Link": company_link,
                "Location City": City,
                "Location State/Province": State,
                "Job Type": Job_Type,
                "Work Type": Work_Type,
                "Salary range": Salary_range,
                "JD": description,
                "Indeed Link": Indeed_Link
            })
           
        # Define the Excel file name
        excel_file = "output.xlsx"

        # Check if the Excel file exists
        if os.path.isfile(excel_file):
            # Load existing data from Excel file
            df_existing = pd.read_excel(excel_file)
            
            # Create a DataFrame from the new data
            df_new = pd.DataFrame(columns)
            
            # Append new data to existing DataFrame
            df = pd.concat([df_existing, df_new], ignore_index=True)
        else:
            # Create a DataFrame from the new data if the file doesn't exist
            df = pd.DataFrame(columns)

        # Write the DataFrame to an Excel file
        df.to_excel(excel_file, index=False)
        print("Data successfully saved to", excel_file)
        
        # print('finish')
driver.quit()
print('complete')
