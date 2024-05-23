import asyncio
import os
from playwright.async_api import async_playwright

HEADLESS = False

async def main():
    async with async_playwright() as p:
        
        try:
            # Launch the browser
            browser = await p.chromium.launch(headless=HEADLESS)
            # Create a new browser context
            context = await browser.new_context()
            # Open a new page
            page = await context.new_page()
            page.set_default_timeout(0)
            # Go to the website
            url = 'https://api.factorialhr.com/en/users/sign_in/'
            await page.goto(url)
            
            #Login
            await page.get_by_title('Continue with Google').click()
            
            await page.locator('input[type="email"]').fill(os.getenv("USER"))
            await page.get_by_text('Siguiente').click()
            await page.locator('input[type="password"]').fill(os.getenv("PASSWORD"))
            await page.get_by_text('Siguiente').click()
            
            locator = page.locator('#factorialRoot')
            await locator.wait_for()
            
            nav = page.get_by_role('navigation')
            
            await nav.get_by_text('Fichaje').click()
            
            table = page.get_by_role('table').first
            await table.wait_for()
            
            for row in await table.get_by_role('row').filter(has_text='-8h').all():
                open_row_button = row.get_by_role("button").last
                await open_row_button.click()
                new_row = table.get_by_role('row').filter(has_text='Añadir').first
                await new_row.get_by_text('Añadir').click()
                popover = page.locator('[data-radix-popper-content-wrapper]').first
                await popover.get_by_placeholder('--:--').first.fill('09:00')
                await popover.get_by_placeholder('--:--').last.fill('17:00')
                await popover.get_by_text('Aplicar').click()
                await open_row_button.click()

            # Close the browser
            await browser.close()
        except Exception as e:
            print(e)
            await browser.close()

# Run the main function
asyncio.run(main())
