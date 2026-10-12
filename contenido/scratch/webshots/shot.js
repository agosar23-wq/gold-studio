const { chromium } = require('playwright');
const F = 'file:///tmp/claude-0/-home-user/3d6a0a2e-a980-5532-8595-cde247c8de79/scratchpad/logo/node_modules/@fontsource/';
(async()=>{
  const b = await chromium.launch(); const p = await b.newPage({viewport:{width:390,height:844}, deviceScaleFactor:2});
  await p.route(/fonts\.(googleapis|gstatic)\.com/, r => r.abort());
  await p.goto('file:///home/user/gold-studio-repo/index.html');
  await p.addStyleTag({content:`
  @font-face{font-family:'Bodoni Moda';src:url(${F}bodoni-moda/files/bodoni-moda-latin-500-normal.woff2);font-weight:400 700}
  @font-face{font-family:'Bodoni Moda';src:url(${F}bodoni-moda/files/bodoni-moda-latin-500-italic.woff2);font-weight:400 700;font-style:italic}
  @font-face{font-family:'Jost';src:url(${F}jost/files/jost-latin-300-normal.woff2);font-weight:300}
  @font-face{font-family:'Jost';src:url(${F}jost/files/jost-latin-400-normal.woff2);font-weight:400}
  @font-face{font-family:'Jost';src:url(${F}jost/files/jost-latin-500-normal.woff2);font-weight:500 600}
  .reveal{opacity:1!important;transform:none!important}`});
  await p.evaluate(async()=>{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>0)));});
  await p.waitForTimeout(500);
  const offs = await p.evaluate(()=>['inicio','servicios','trabajos','paquetes','contacto'].map(i=>{const e=document.getElementById(i);return [i, Math.round(e.getBoundingClientRect().top+window.scrollY)];}));
  console.log(JSON.stringify(offs));
  await p.addStyleTag({content:'html{scroll-behavior:auto!important} header,.nav,.topbar{position:absolute!important}'});
  await p.screenshot({path:'/tmp/claude-0/-home-user/3d6a0a2e-a980-5532-8595-cde247c8de79/scratchpad/webshots/full.png', fullPage:true});
  await b.close();
})();
