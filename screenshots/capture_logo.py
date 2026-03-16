from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 800, "height": 600})
    page.goto("https://yag.social/login", wait_until="networkidle", timeout=30000)
    page.wait_for_timeout(2000)

    # Try to capture the logo element
    logo = page.locator('img[alt*="Yag"], img[alt*="yag"], .logo, [class*="logo"]').first
    if logo.is_visible():
        logo.screenshot(path="/Users/igoremmanuel/Desktop/yag-lp/img/logo-site.png")
        print("Logo captured from element")

    # Also capture just the header area
    header = page.locator('header, nav, [class*="header"]').first
    if header.is_visible():
        header.screenshot(path="/Users/igoremmanuel/Desktop/yag-lp/img/header-site.png")
        print("Header captured")

    # Login and capture the app header logo
    page.locator('input[placeholder*="usuário" i]').first.fill("admin")
    page.locator('input[type="password"]').first.fill("P3R2ORCUl+bJWAAujxCZYds9")
    page.locator('button[type="submit"]').first.click()
    page.wait_for_timeout(5000)

    # Capture app logo after login
    logo2 = page.locator('img[alt*="Yag"], img[alt*="yag"], .logo, [class*="logo"]').first
    if logo2.is_visible():
        logo2.screenshot(path="/Users/igoremmanuel/Desktop/yag-lp/img/logo-app.png")
        print("App logo captured")

    # Get the logo src
    logos = page.locator('img').all()
    for l in logos:
        try:
            src = l.get_attribute('src')
            alt = l.get_attribute('alt') or ''
            if src and ('logo' in src.lower() or 'yag' in alt.lower() or 'yag' in src.lower()):
                print(f"Found logo: src={src}, alt={alt}")
        except:
            pass

    browser.close()
