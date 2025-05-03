# "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="C:\edge-dev-profile"
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --profile-directory="Profile 6"

from playwright.async_api import async_playwright
import asyncio

async def test_run_in_already_opened_browser():
    async with async_playwright() as playwright:
        # Connect to already opened browser
        browser = await playwright.chromium.connect_over_cdp('http://127.0.0.1:9222')
        
        # Get the default context
        default_context = browser.contexts[0]
        
        # Get the first page
        page = default_context.pages[0]
        
        # Tulis alamat web yang di protect cloudflare misal chat gpt
        await page.goto('https://chatgpt.com/')
        
        await asyncio.sleep(3)
        
        await page.locator('xpath=//*[@id="prompt-textarea"]/p').fill('Halo, ini pesan otomatis dari playwright')
        
        await asyncio.sleep(3)
        
        await page.keyboard.press('Enter')

# Run it
asyncio.run(test_run_in_already_opened_browser())
