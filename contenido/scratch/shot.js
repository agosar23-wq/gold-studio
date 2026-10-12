const { chromium } = require('playwright');
(async()=>{
 const b = await chromium.launch(); const pg = await b.newPage({viewport:{width:1100,height:900}});
 const errs=[]; pg.on('pageerror',e=>errs.push(e.message));
 await pg.goto('file:///home/user/app-nutri/demo.html');
 await pg.click('text=Entrar como nutricionista');
 await pg.click('text=Lucía Fernández'); await pg.click('button.tab:has-text("Peso")');
 await pg.screenshot({path:'nutri.png'});
 await pg.click('text=Salir'); await pg.click('text=Entrar como paciente');
 await pg.setViewportSize({width:400,height:850});
 await pg.screenshot({path:'pac.png', fullPage:true});
 console.log('errors', errs); await b.close();
})();
