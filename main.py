import asyncio
from playwright.async_api import async_playwright


HEADLESS = False

async def main():
    async with async_playwright() as p:
        # Launch the browser
        browser = await p.chromium.launch(headless=HEADLESS)
        # Create a new browser context
        context = await browser.new_context()
        # Open a new page
        page = await context.new_page()
        # Go to the website
        url = 'https://api.factorialhr.com/en/users/sign_in/'
        await page.goto(url)
        
        #Login
        await page.get_by_title('Continue with Google').click()
        
        await page.locator('input[type="email"]').fill('julian.fernandez@enzyme.biz')
        await page.get_by_text('Siguiente').click()
        await page.locator('input[type="password"]').fill('yepalooo')
        await page.get_by_text('Siguiente').click()
        
        locator = page.locator('#factorialRoot')
        await locator.wait_for()


        # Get the title of the page
        title = await page.title()
        print(f"Title of the page: {title}")
        # Close the browser
        await browser.close()

# Run the main function
asyncio.run(main())

# option = webdriver.ChromeOptions()
# option.add_argument("start-maximized")


# # Install and set up Chrome WebDriver
# service = Service(ChromeDriverManager().install(), options=option)
# driver = webdriver.Chrome(service=service)




# # Navigate to the webpage
# driver.get(url)


# sso_list_element = driver.find_element(By.CLASS_NAME, 'sso-list')
# sso_list_element.find_elements(By.TAG_NAME, 'a')[0].click()


# # Close the WebDriver
# driver.quit()