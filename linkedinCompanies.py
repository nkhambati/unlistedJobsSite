from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Creating webdriver instance
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# Open linkedIn URL in our browser
driver.get("https://www.linkedin.com")

# LinkedIn is being difficult so we can't go straight to the search site -- we will need to login first and go from there
# Also, LinkedIn is being super difficult -- taking the browser to one of three pages where there may be a sign up button, or only a link
# We'll have to account and try for both of these
try:
    signInBtn = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-btn--full-width")
    signInBtn.click()
except:
    print("No sign in Button, try link")
    try:
        signInLink = driver.find_element(By.LINK_TEXT, "Sign in")
        signInLink.click()
    except:
        print("No sign in link either...")

# Now, assuming that our efforts paid off, we need to fill in the email + password

# Fill in the email
try:
    emailInput = driver.find_element(By.ID, "session_key")
    #emailInput.send_keys(email)
except:
    print("Ugh")

# Now fill in the password
try:
    passInput = driver.find_element(By.ID, "session_password")
    #passInput.send_keys(password)
except:
    print("Ugh2")

# Then click the sign in button again
try:
    signInBtn = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-btn--full-width")
    signInBtn.click()
except:
    print("Ugh3")


# UGH ... LI Needs 2F Authentication now, so we've hit a roadblock