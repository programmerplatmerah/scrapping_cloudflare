# untuk menjalankan browser yang biasa kita pakai, paste kode berikut ke command prompt. pastika port 9222 kosong dan tidak digunakan proses lain.
# "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="C:\edge-dev-profile"
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --profile-directory="Profile 6"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def connect_to_existing_chrome():
    # Set up options to connect to existing browser
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
    
    # Connect to the browser
    driver = webdriver.Chrome(options=chrome_options)
    
    # Now you can control the existing browser
    driver.get("https://www.google.com/search?q=playwright+by+testers+talk")
    
    # Find and click link (Selenium syntax differs from Playwright)
    links = driver.find_elements("xpath", "//a[contains(text(), 'Playwright by Testers Talk')]")
    if links:
        links[0].click()
    
    # Keep the driver connection open
    input("Press Enter to quit...")
    
    # Don't call driver.quit() if you want to keep the browser open

if __name__ == "__main__":
    connect_to_existing_chrome()