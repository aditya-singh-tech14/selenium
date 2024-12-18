from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set the path for Chrome and Chromedriver
chrome_path = "/usr/bin/google-chrome"
chromedriver_path = "/usr/local/bin/chromedriver"

# Set the Chrome options to use the given Chrome path
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/usr/bin/google-chrome"
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")



service = Service(chromedriver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

# Open a webpage to test the setup
driver.get("https://www.google.com")

# Print the title of the page
print("Page Title:", driver.title)

# Close the browser
driver.quit()
