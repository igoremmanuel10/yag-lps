from playwright.sync_api import sync_playwright
import os

SAVE_DIR = "/Users/igoremmanuel/Desktop/yag-lp/screenshots"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    # Mobile
    ctx_m = browser.new_context(viewport={"width": 390, "height": 844})
    page = ctx_m.new_page()

    page.goto("https://yag.social/login", wait_until="networkidle", timeout=30000)
    page.wait_for_timeout(2000)
    page.locator('input[placeholder*="usuário" i]').first.fill("admin")
    page.locator('input[type="password"]').first.fill("P3R2ORCUl+bJWAAujxCZYds9")
    page.locator('button[type="submit"]').first.click()
    page.wait_for_timeout(5000)
    page.wait_for_load_state("networkidle")

    # Feed mobile
    page.screenshot(path=os.path.join(SAVE_DIR, "10_feed_mobile.png"), full_page=False)
    print("Feed mobile done")

    # Radar
    page.locator('text=Radar').first.click()
    page.wait_for_timeout(3000)
    page.screenshot(path=os.path.join(SAVE_DIR, "09_radar_mobile.png"), full_page=False)
    print("Radar done")

    # Buscar
    page.locator('text=Buscar').first.click()
    page.wait_for_timeout(3000)
    page.screenshot(path=os.path.join(SAVE_DIR, "11_buscar_mobile.png"), full_page=False)
    print("Buscar done")

    # Profile detail
    try:
        page.locator('a[href*="profile"]').first.click()
        page.wait_for_timeout(3000)
        page.screenshot(path=os.path.join(SAVE_DIR, "12_profile_detail_mobile.png"), full_page=True)
        print("Profile done")
    except:
        print("Profile not found")

    # Chat
    page.locator('text=Chat').first.click()
    page.wait_for_timeout(3000)
    page.screenshot(path=os.path.join(SAVE_DIR, "07_chat.png"), full_page=False)
    print("Chat done")

    browser.close()
    print("All done!")
