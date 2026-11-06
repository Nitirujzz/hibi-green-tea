// usage: node render_mg.js <outdir> <fps> <T> [times...]  (times given => preview frames only)
const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
(async()=>{const [out,fps,T,...ts]=process.argv.slice(2);fs.mkdirSync(out,{recursive:true});
 const b=await chromium.launch();const N=4;const pages=[];
 for(let k=0;k<N;k++){const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+path.resolve(__dirname,'mg.html'));await p.evaluate(()=>document.fonts.ready);pages.push(p);}
 const frames=ts.length?ts.map(Number):[...Array(Math.ceil(T*fps)).keys()].map(i=>i/fps);
 let idx=0;await Promise.all(pages.map(async p=>{while(true){const i=idx++;if(i>=frames.length)break;
   await p.evaluate(t=>render(t),frames[i]);
   await p.screenshot({path:`${out}/${ts.length?('t'+frames[i].toFixed(1)):String(i).padStart(5,'0')}.png`,omitBackground:true});}}));
 await b.close();})();
