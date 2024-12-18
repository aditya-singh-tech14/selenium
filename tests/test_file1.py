from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Disable sandbox (useful in CI environments)
options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage (useful for Docker)
driver = webdriver.Chrome(options=options)


# Start Chrome browser
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.google.com")
print("Title:", driver.title)

# Close the browser
driver.quit()
