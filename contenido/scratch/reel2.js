const { chromium } = require('playwright');
const [,, html, dur, out] = process.argv;
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1920}});
 await p.goto('file://'+html); await p.evaluate(async()=>{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>0)));await document.fonts.ready;}); await p.waitForTimeout(500);
 const N=Math.round(+dur*30);
 for(let i=0;i<N;i++){ await p.evaluate(async t=>{ await window.render(t); }, i/30); await p.screenshot({path:`${out}/${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:90}); }
 await b.close(); })();
