from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create ChromeOptions object
chrome_options = Options()

# Add argument to use 'Default' profile directory
chrome_options.add_argument('--profile-directory=Default')

# Create WebDriver instance with ChromeOptions
driver = webdriver.Chrome(options=chrome_options)

# Example usage: navigate to a website
driver.get('https://www.example.com')

# Close the browser session
driver.quit()
