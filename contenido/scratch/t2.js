const { chromium } = require('playwright');
(async()=>{
 const b = await chromium.launch(); const pg = await b.newPage({viewport:{width:1100,height:900}});
 const errs=[]; pg.on('pageerror',e=>errs.push(e.message));
 await pg.goto('file:///home/user/app-nutri/demo.html');
 await pg.click('button.link:has-text("Creá tu cuenta")');
 await pg.fill('#s-name','Ana Prueba'); await pg.fill('#s-email','ana@x.com'); await pg.fill('#s-pass','12345678'); await pg.fill('#s-pass2','12345678');
 await pg.click('button:has-text("Crear cuenta")');
 console.log(await pg.textContent('h2'));
 await pg.click('text=Volver a ingresar');
 await pg.click('text=Entrar como nutricionista');
 await pg.screenshot({path:'nutri2.png'});
 await pg.click('.req:has-text("Ana") >> text=Aprobar');
 await pg.click('text=Salir');
 await pg.fill('#l-email','ana@x.com'); await pg.fill('#l-pass','12345678'); await pg.click('button[type=submit]');
 console.log(await pg.textContent('.hello'));
 console.log('errors', errs); await b.close();
})();
