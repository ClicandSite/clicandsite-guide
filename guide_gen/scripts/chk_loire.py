import asyncio
from playwright.async_api import async_playwright
RD={8766:'provence',8767:'provence'}
P=['avignon/','aix-en-provence/','marseille/','calanques/','gordes/','baux-de-provence/','']
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch()
        for port in (8766,8767):
            pg=await b.new_page(viewport={'width':390,'height':844})
            bad=[]
            pg.on('response',lambda r: bad.append((r.status,r.url)) if r.status>=400 else None)
            for s in P:
                await pg.goto(f'http://localhost:{port}/{RD[port]}/{s}',wait_until='networkidle')
                hrefs=await pg.eval_on_selector_all('a[href]','e=>e.map(a=>a.href)')
                for h in set(hrefs):
                    if h.startswith('http://localhost'):
                        r=await pg.request.get(h)
                        if r.status>=400: bad.append((r.status,h))
            await pg.goto(f'http://localhost:{port}/{RD[port]}/marseille/'); await pg.screenshot(path=f'/tmp/s{port}.png')
            await pg.goto(f'http://localhost:{port}/{RD[port]}/'); await pg.screenshot(path=f'/tmp/i{port}.png',full_page=True)
            await pg.goto(f'http://localhost:{port}/'); await pg.evaluate("document.querySelector('.regions').scrollIntoView()"); await pg.screenshot(path=f'/tmp/h{port}.png')
            print(port,sorted(set(bad)))
        await b.close()
asyncio.run(main())
