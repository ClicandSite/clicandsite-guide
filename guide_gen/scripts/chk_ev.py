from playwright.sync_api import sync_playwright
import re
P=[('http://localhost:8766/cote-d-azur/fete-du-citron-menton/','fr1'),('http://localhost:8767/french-riviera/nice-carnival/','en2'),('http://localhost:8766/cote-d-azur/noel-cote-d-azur/','fr3'),('http://localhost:8766/cote-d-azur/','idx')]
with sync_playwright() as p:
  b=p.chromium.launch(); pg=b.new_page(viewport={'width':420,'height':900})
  bad=[]
  pg.on('response',lambda r: bad.append((r.status,r.url)) if r.status>=400 and 'localhost' in r.url else None)
  for u,n in P:
    pg.goto(u,wait_until='networkidle'); pg.screenshot(path=f'/tmp/ev_{n}.png')
    for a in pg.eval_on_selector_all('a[href]','e=>e.map(x=>x.href)'):
      if 'localhost' in a and '#' not in a:
        r=pg.request.get(a.split('?')[0])
        if r.status>=400: bad.append((r.status,a))
  pg.goto('http://localhost:8766/cote-d-azur/',wait_until='networkidle'); pg.locator('#g-fetes').scroll_into_view_if_needed(); pg.screenshot(path='/tmp/ev_idx2.png')
  print(sorted(set(bad))); b.close()
