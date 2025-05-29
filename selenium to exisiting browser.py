# untuk menjalankan browser yang biasa kita pakai, paste kode berikut ke command prompt. pastika port 9222 kosong dan tidak digunakan proses lain.
# "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="C:\edge-dev-profile"
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --profile-directory="Profile 6"

from selenium import webdriver
from selenium.webdriver.edge.options import Options  # Use Edge Options

def connect_to_existing_edge():
    edge_options = Options()
    edge_options.add_experimental_option("debuggerAddress", "localhost:9222")
    driver = webdriver.Edge(options=edge_options)

    driver.get("https://www.google.com/search?q=playwright+by+testers+talk")
    links = driver.find_elements("xpath", "//a[contains(text(), 'Playwright by Testers Talk')]")
    if links:
        links[0].click()
    input("Press Enter to quit...")

if __name__ == "__main__":
    connect_to_existing_edge()