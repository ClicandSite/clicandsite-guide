from playwright.sync_api import sync_playwright
with sync_playwright() as p:
  b=p.chromium.launch(); pg=b.new_page(viewport={'width':420,'height':900})
  for u,o in (('http://localhost:8766/paris/catacombes/','/tmp/eze.png'),('http://localhost:8767/paris/louvre/','/tmp/rcm.png')):
    pg.goto(u); pg.locator('#infos-2026').scroll_into_view_if_needed(); pg.screenshot(path=o)
  b.close()
