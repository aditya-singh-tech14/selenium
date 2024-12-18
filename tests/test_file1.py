from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_pipeline():
    try:
        # Set up Chrome options for CI/CD pipeline
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome resource constraints

        # Specify the path to ChromeDriver
        service = Service("/usr/local/bin/chromedriver")  # Update the path if necessary

        # Create the WebDriver instance
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Navigate to a test website
        driver.get("https://google.com")

        # Check if the page title is as expected
        assert "Example Domain" in driver.title, "Page title does not match!"

        print("Test passed: Page title is as expected.")

        # Close the browser
        driver.quit()

    except Exception as e:
        print(f"Test failed: {e}")

# Run the test
if __name__ == "__main__":
    test_pipeline()
