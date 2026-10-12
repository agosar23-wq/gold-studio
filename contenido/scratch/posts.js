const { chromium } = require('playwright');
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1350}});
 await p.goto('file:///tmp/claude-0/-home-user/3d6a0a2e-a980-5532-8595-cde247c8de79/scratchpad/posts.html'); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(800);
 for (const el of await p.$$('.s')) { const id=(await el.getAttribute('id')).slice(1); await el.screenshot({path:`/home/user/gold-studio-final/posteos/${id}.png`}); }
 await b.close(); })();
