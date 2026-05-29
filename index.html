<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1"/>
<meta name="apple-mobile-web-app-capable" content="yes"/>
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"/>
<meta name="apple-mobile-web-app-title" content="GoldSignals"/>
<title>GoldSignals · Sniper</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/umd/react.production.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0/umd/react-dom.production.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/7.23.2/babel.min.js"></script>
<style>
*{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}
body{background:#0a0a0f;color:#f0f0f5;font-family:'Inter',sans-serif;overscroll-behavior:none}
input{box-sizing:border-box;width:100%;font-family:'Inter',sans-serif}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
@keyframes glow{0%,100%{box-shadow:0 0 10px rgba(245,166,35,0.3)}50%{box-shadow:0 0 25px rgba(245,166,35,0.6)}}
::-webkit-scrollbar{display:none}
</style>
</head>
<body>
<div id="root"></div>
<script type="text/babel">
const {useState,useEffect,useCallback,useRef}=React;

const C={
  bg:"#0a0a0f",card:"#12121a",card2:"#1a1a24",
  border:"#252535",
  gold:"#f5a623",goldSoft:"rgba(245,166,35,0.12)",
  red:"#f06060",redSoft:"rgba(240,96,96,0.1)",
  green:"#4cd97b",greenSoft:"rgba(76,217,123,0.1)",
  blue:"#5b9cf6",blueSoft:"rgba(91,156,246,0.1)",
  purple:"#a78bfa",purpleSoft:"rgba(167,139,250,0.1)",
  muted:"#4a4a62",text:"#e8e8f0",text2:"#7070a0",text3:"#4a4a6a"
};

const TG_TOKEN="8838875779:AAF-aOqavtRj5lZr9BdrNR0AZoP_X4KmB8w";
const TG_CHAT="1302678674";

const PAIRS=[
  {symbol:"XAU/USD",emoji:"🥇",cat:"Métaux"},
  {symbol:"BTC/USD",emoji:"₿",cat:"Crypto"},
  {symbol:"EUR/USD",emoji:"💶",cat:"Majeurs"},
  {symbol:"GBP/USD",emoji:"💷",cat:"Majeurs"},
  {symbol:"USD/JPY",emoji:"💴",cat:"Majeurs"},
  {symbol:"USD/CHF",emoji:"🇨🇭",cat:"Majeurs"},
  {symbol:"USD/CAD",emoji:"🇨🇦",cat:"Majeurs"},
  {symbol:"AUD/USD",emoji:"🇦🇺",cat:"Majeurs"},
  {symbol:"NZD/USD",emoji:"🇳🇿",cat:"Majeurs"},
  {symbol:"EUR/JPY",emoji:"🇯🇵",cat:"Croisées"},
  {symbol:"GBP/JPY",emoji:"🇯🇵",cat:"Croisées"},
  {symbol:"AUD/JPY",emoji:"🇯🇵",cat:"Croisées"},
  {symbol:"CAD/JPY",emoji:"🇯🇵",cat:"Croisées"},
  {symbol:"NZD/JPY",emoji:"🇯🇵",cat:"Croisées"},
  {symbol:"EUR/GBP",emoji:"🇬🇧",cat:"Croisées"},
];
const CATS=["Métaux","Crypto","Majeurs","Croisées"];

// ── MATH ──
function calcEMA(c,p){var k=2/(p+1);var e=[c[0]];for(var i=1;i<c.length;i++)e.push(c[i]*k+e[i-1]*(1-k));return e;}
function calcSMA(a,p){var o=[];for(var i=p-1;i<a.length;i++)o.push(a.slice(i-p+1,i+1).reduce(function(a,b){return a+b;},0)/p);return o;}
function calcRSI(c,p){p=p||14;var g=0,l=0;for(var i=1;i<=p;i++){var d=c[i]-c[i-1];if(d>0)g+=d;else l-=d;}var ag=g/p,al=l/p;var o=[];for(var i=p+1;i<c.length;i++){var d=c[i]-c[i-1];ag=(ag*(p-1)+Math.max(d,0))/p;al=(al*(p-1)+Math.max(-d,0))/p;o.push(al===0?100:100-100/(1+ag/al));}return o;}
function calcStoch(c){var rsi=calcRSI(c,14);var raw=[];for(var i=13;i<rsi.length;i++){var sl=rsi.slice(i-13,i+1);var mn=Math.min.apply(null,sl),mx=Math.max.apply(null,sl);raw.push(mx===mn?50:((rsi[i]-mn)/(mx-mn))*100);}var sk=calcSMA(raw,3);var sd=calcSMA(sk,3);return{k:sk[sk.length-1]||50,d:sd[sd.length-1]||50};}
function calcATR(h,l,c,p){p=p||14;var tr=[];for(var i=1;i<c.length;i++)tr.push(Math.max(h[i]-l[i],Math.abs(h[i]-c[i-1]),Math.abs(l[i]-c[i-1])));var atr=tr.slice(0,p).reduce(function(a,b){return a+b;},0)/p;for(var i=p;i<tr.length;i++)atr=(atr*(p-1)+tr[i])/p;return atr;}

// ── FIBONACCI ──
function findSwing(highs,lows,lookback){
  lookback=lookback||20;
  var n=highs.length;
  var swingHigh=highs[n-lookback];
  var swingLow=lows[n-lookback];
  for(var i=n-lookback;i<n;i++){
    if(highs[i]>swingHigh)swingHigh=highs[i];
    if(lows[i]<swingLow)swingLow=lows[i];
  }
  return{high:swingHigh,low:swingLow};
}

function calcFibLevels(swing,isBuy){
  var range=swing.high-swing.low;
  if(isBuy){
    return{
      entry:swing.low+range*0.382,
      sl:swing.low-range*0.1,
      tp1:swing.high+range*0.272,
      tp2:swing.high+range*0.618,
      tp3:swing.high+range*1.618,
      r382:swing.low+range*0.382,
      r618:swing.low+range*0.618,
    };
  } else {
    return{
      entry:swing.high-range*0.382,
      sl:swing.high+range*0.1,
      tp1:swing.low-range*0.272,
      tp2:swing.low-range*0.618,
      tp3:swing.low-range*1.618,
      r382:swing.high-range*0.382,
      r618:swing.high-range*0.618,
    };
  }
}

function getPipSize(symbol){
  if(symbol.includes("XAU"))return 0.10;
  if(symbol.includes("BTC"))return 1;
  if(symbol.includes("JPY"))return 0.01;
  return 0.0001;
}
function getPipDecimals(symbol){
  if(symbol.includes("XAU")||symbol.includes("BTC"))return 0;
  if(symbol.includes("JPY"))return 2;
  return 5;
}

// ── SIGNAL SNIPER ──
function computeSniperSignal(price,c4h,c1h,c15,highs4h,lows4h){
  var e20_4h=calcEMA(c4h,20);var e50_4h=calcEMA(c4h,50);
  var rsi1h=calcRSI(c1h,14);var stoch15=calcStoch(c15);
  var swing=findSwing(highs4h,lows4h,20);
  var trend4h=e20_4h[e20_4h.length-1]>e50_4h[e50_4h.length-1]?"buy":"sell";
  var rsi=rsi1h[rsi1h.length-1];
  var rsiOk=rsi>35&&rsi<65;
  var isBuy=trend4h==="buy";
  var stochOk=isBuy?(stoch15.k>stoch15.d&&stoch15.k<80):(stoch15.k<stoch15.d&&stoch15.k>20);
  var fib=calcFibLevels(swing,isBuy);
  var range=swing.high-swing.low;
  var nearFib=isBuy?Math.abs(price-fib.r382)<range*0.05||Math.abs(price-fib.r618)<range*0.05:Math.abs(price-fib.r382)<range*0.05||Math.abs(price-fib.r618)<range*0.05;
  var conditions=[trend4h!=="neutral",rsiOk,stochOk,nearFib];
  var score=conditions.filter(Boolean).length;
  var direction=score>=3?(isBuy?"buy":"sell"):"neutral";
  var label,color,bg,advice;
  if(direction==="buy"){label="SNIPER BUY 🎯";color=C.green;bg=C.greenSoft;advice="Conditions sniper réunies — entrée précise";}
  else if(direction==="sell"){label="SNIPER SELL 🎯";color=C.red;bg=C.redSoft;advice="Conditions sniper réunies — vente précise";}
  else{label="EN ATTENTE";color=C.gold;bg=C.goldSoft;advice="Pas encore de setup sniper";}
  return{direction,label,color,bg,advice,score,conditions:{trend:trend4h!=="neutral",rsi:rsiOk,stoch:stochOk,fib:nearFib},fib,swing};
}

function buildSniperPlan(price,atr,signal,symbol){
  if(!signal||signal.direction==="neutral")return null;
  var isBuy=signal.direction==="buy";
  var pip=getPipSize(symbol);
  var dp=getPipDecimals(symbol);
  var fib=signal.fib;
  var entry=parseFloat(price.toFixed(dp));
  var sl=parseFloat(fib.sl.toFixed(dp));
  var tp1=parseFloat(fib.tp1.toFixed(dp));
  var tp2=parseFloat(fib.tp2.toFixed(dp));
  var tp3=parseFloat(fib.tp3.toFixed(dp));
  var slPips=Math.round(Math.abs(entry-sl)/pip);
  var tp1Pips=Math.round(Math.abs(tp1-entry)/pip);
  var tp2Pips=Math.round(Math.abs(tp2-entry)/pip);
  var tp3Pips=Math.round(Math.abs(tp3-entry)/pip);
  // Garantir un R/R minimum de 1:2
  if(tp1Pips<slPips){tp1=isBuy?entry+slPips*pip:entry-slPips*pip;tp1Pips=slPips;}
  if(tp2Pips<slPips*2){tp2=isBuy?entry+slPips*pip*2.8:entry-slPips*pip*2.8;tp2Pips=Math.round(slPips*2.8);}
  if(tp3Pips<slPips*4){tp3=isBuy?entry+slPips*pip*5.8:entry-slPips*pip*5.8;tp3Pips=Math.round(slPips*5.8);}
  var rr=Math.round(tp3Pips/slPips);
  return{isBuy,symbol,entry:entry.toFixed(dp),sl:sl.toFixed(dp),tp1:tp1.toFixed(dp),tp2:tp2.toFixed(dp),tp3:tp3.toFixed(dp),slPts:slPips,tp1Pts:tp1Pips,tp2Pts:tp2Pips,tp3Pts:tp3Pips,rr1:(tp1Pips/slPips).toFixed(1),rr2:(tp2Pips/slPips).toFixed(1),rr3:rr};
}

async function sendTG(msg){try{await fetch("https://api.telegram.org/bot"+TG_TOKEN+"/sendMessage",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({chat_id:TG_CHAT,text:msg})});}catch(e){}}

// ── MINI CHART ──
function MiniChart(props){
  var ref=useRef(null);
  useEffect(function(){
    if(!ref.current||!props.candles.length)return;
    var cv=ref.current,dpr=window.devicePixelRatio||1;
    var W=Math.max(cv.parentElement.clientWidth-32,200),H=160;
    cv.width=W*dpr;cv.height=H*dpr;cv.style.width=W+"px";cv.style.height=H+"px";
    var ctx=cv.getContext("2d");ctx.scale(dpr,dpr);
    var rc=props.candles.slice(-40),re20=props.ema20.slice(-40),re50=props.ema50.slice(-40);
    var ps=rc.reduce(function(a,c){return a.concat([c.h,c.l]);},[]);
    var mn=Math.min.apply(null,ps),mx=Math.max.apply(null,ps),rng=mx-mn||1,pad=12;
    var py=function(p){return H-pad-((p-mn)/rng)*(H-pad*2);};
    ctx.fillStyle=C.card;ctx.fillRect(0,0,W,H);
    ctx.strokeStyle=C.border;ctx.lineWidth=0.5;
    for(var i=1;i<=3;i++){var y=pad+(H-pad*2)*i/4;ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke();}
    // Fibonacci levels
    if(props.swing){
      var fibLevels=[0.236,0.382,0.5,0.618,0.786];
      var range=props.swing.high-props.swing.low;
      fibLevels.forEach(function(f){
        var lvl=props.swing.low+range*f;
        if(lvl>=mn&&lvl<=mx){
          ctx.strokeStyle="rgba(167,139,250,0.3)";ctx.lineWidth=0.5;ctx.setLineDash([3,3]);
          ctx.beginPath();ctx.moveTo(0,py(lvl));ctx.lineTo(W,py(lvl));ctx.stroke();ctx.setLineDash([]);
        }
      });
    }
    var step=W/rc.length,cw=Math.max(2,step-1.5);
    rc.forEach(function(c,i){var x=i*step+step/2,bull=c.c>=c.o;ctx.strokeStyle=bull?"rgba(76,217,123,0.6)":"rgba(240,96,96,0.6)";ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(x,py(c.h));ctx.lineTo(x,py(c.l));ctx.stroke();ctx.fillStyle=bull?"rgba(76,217,123,0.85)":"rgba(240,96,96,0.85)";var bt=py(Math.max(c.o,c.c)),bb=py(Math.min(c.o,c.c));ctx.fillRect(x-cw/2,bt,cw,Math.max(1,bb-bt));});
    function dl(arr,color,dash){if(!arr||arr.length<2)return;ctx.beginPath();ctx.strokeStyle=color;ctx.lineWidth=1.5;ctx.setLineDash(dash||[]);arr.forEach(function(v,i){var x=i*step+step/2;i===0?ctx.moveTo(x,py(v)):ctx.lineTo(x,py(v));});ctx.stroke();ctx.setLineDash([]);}
    dl(re20,C.gold);dl(re50,C.blue,[5,3]);
  },[props.candles,props.ema20,props.ema50,props.swing]);
  return React.createElement("canvas",{ref:ref,style:{display:"block",borderRadius:10}});
}

// ── CONDITIONS CHECKER ──
function ConditionRow(props){
  var ok=props.ok;
  return React.createElement("div",{style:{display:"flex",alignItems:"center",gap:10,padding:"10px 0",borderBottom:"1px solid "+C.border}},
    React.createElement("div",{style:{width:22,height:22,borderRadius:"50%",background:ok?C.green+"25":C.red+"25",display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0}},
      React.createElement("span",{style:{fontSize:12,color:ok?C.green:C.red}},ok?"✓":"✗")),
    React.createElement("div",null,
      React.createElement("div",{style:{fontSize:13,color:C.text,fontWeight:500}},props.label),
      React.createElement("div",{style:{fontSize:11,color:C.text2}},props.detail)));
}

// ── PLAN CARD ──
function PlanCard(props){
  var plan=props.plan,signal=props.signal;
  if(!plan)return React.createElement("div",{style:{background:C.card,border:"1px solid "+C.border,borderRadius:16,padding:"24px 20px",textAlign:"center"}},
    React.createElement("div",{style:{fontSize:28,marginBottom:10}},"🎯"),
    React.createElement("div",{style:{fontSize:15,fontWeight:600,color:C.text,marginBottom:8}},"En attente d'un setup sniper"),
    React.createElement("div",{style:{fontSize:13,color:C.text2,lineHeight:1.7}},"Le signal se déclenchera quand 3 conditions sur 4 seront réunies simultanément."),
    signal&&React.createElement("div",{style:{marginTop:16,background:C.card2,borderRadius:12,padding:"12px 16px"}},
      React.createElement("div",{style:{fontSize:11,color:C.text2,marginBottom:8,fontWeight:600,textTransform:"uppercase",letterSpacing:0.5}},"Conditions actuelles"),
      React.createElement(ConditionRow,{ok:signal.conditions.trend,label:"Tendance 4H",detail:"EMA 20 au-dessus/dessous EMA 50"}),
      React.createElement(ConditionRow,{ok:signal.conditions.rsi,label:"RSI 1H neutre",detail:"RSI entre 35 et 65 — pas en extrême"}),
      React.createElement(ConditionRow,{ok:signal.conditions.stoch,label:"Stoch RSI 15min",detail:"Croisement dans la bonne direction"}),
      React.createElement(ConditionRow,{ok:signal.conditions.fib,label:"Zone Fibonacci",detail:"Prix proche du niveau 0.382 ou 0.618"})));

  var col=plan.isBuy?C.green:C.red;
  function row(label,val,sub,c){return React.createElement("div",{style:{display:"flex",justifyContent:"space-between",alignItems:"center",padding:"11px 0",borderBottom:"1px solid "+C.border}},React.createElement("span",{style:{fontSize:13,color:C.text2}},label),React.createElement("div",{style:{textAlign:"right"}},React.createElement("div",{style:{fontSize:14,fontWeight:700,color:c||C.text}},val),sub&&React.createElement("div",{style:{fontSize:11,color:C.text3}},sub)));}
  return React.createElement("div",{style:{animation:"fadeIn 0.4s ease"}},
    React.createElement("div",{style:{background:col+"15",border:"1px solid "+col+"30",borderRadius:16,padding:"14px 18px",marginBottom:10,display:"flex",justifyContent:"space-between",alignItems:"center",animation:"glow 2s infinite"}},
      React.createElement("div",null,
        React.createElement("div",{style:{fontSize:11,color:col,fontWeight:600,letterSpacing:0.8,marginBottom:2}},"🎯 SNIPER SIGNAL"),
        React.createElement("div",{style:{fontSize:20,fontWeight:700,color:col}},plan.isBuy?"🔹 ACHAT "+plan.symbol:"🔸 VENTE "+plan.symbol)),
      React.createElement("div",{style:{textAlign:"center",background:col+"20",borderRadius:10,padding:"8px 12px"}},
        React.createElement("div",{style:{fontSize:10,color:C.text3,marginBottom:2}},"R/R"),
        React.createElement("div",{style:{fontSize:24,fontWeight:700,color:col}},"1:"+plan.rr3))),
    React.createElement("div",{style:{background:C.card,border:"1px solid "+C.border,borderRadius:16,padding:"4px 16px",marginBottom:10}},
      row("📍 Entrée",plan.entry,"Prix d'entrée sniper",C.text),
      row("🛑 Stop Loss",plan.sl,plan.slPts+" pips · Fibonacci SL",C.red)),
    React.createElement("div",{style:{background:C.card,border:"1px solid "+C.border,borderRadius:16,padding:"4px 16px",marginBottom:10}},
      React.createElement("div",{style:{fontSize:11,fontWeight:600,color:C.text2,padding:"12px 0 8px",textTransform:"uppercase",letterSpacing:0.5}},"Extensions Fibonacci"),
      row("🎯 TP1 (1.272)",plan.tp1,plan.tp1Pts+" pips · R/R "+plan.rr1,C.green),
      row("🎯 TP2 (1.618)",plan.tp2,plan.tp2Pts+" pips · R/R "+plan.rr2,C.green),
      row("🎯 TP3 (2.618)",plan.tp3,plan.tp3Pts+" pips · R/R "+plan.rr3,C.green)),
    React.createElement("div",{style:{background:C.purpleSoft,border:"1px solid "+C.purple+"30",borderRadius:14,padding:"14px 16px"}},
      React.createElement("div",{style:{fontSize:12,fontWeight:600,color:C.purple,marginBottom:8}},"🎯 Gestion Sniper"),
      [{t:"TP1",c:"Ferme 40% → déplace SL à l'entrée"},{t:"TP2",c:"Ferme 40% → laisse courir 20%"},{t:"TP3",c:"Objectif Fibonacci 2.618 — laisser courir"}]
      .map(function(x,i){return React.createElement("div",{key:i,style:{display:"flex",gap:10,marginBottom:i<2?8:0}},React.createElement("span",{style:{fontSize:12,color:C.purple,fontWeight:600,flexShrink:0}},x.t+" :"),React.createElement("span",{style:{fontSize:12,color:C.text2,lineHeight:1.5}},x.c));})));
}

// ── PAIR SELECTOR ──
function PairSelector(props){
  var _c=useState("Métaux");var cat=_c[0],setCat=_c[1];
  return React.createElement("div",{style:{position:"fixed",top:0,left:0,right:0,bottom:0,background:"rgba(0,0,0,0.9)",zIndex:100,display:"flex",flexDirection:"column"}},
    React.createElement("div",{style:{background:C.card,borderBottom:"1px solid "+C.border,padding:"18px 20px 12px",display:"flex",justifyContent:"space-between",alignItems:"center"}},
      React.createElement("div",{style:{fontSize:16,fontWeight:700,color:C.text}},"Choisir une paire"),
      React.createElement("button",{onClick:props.onClose,style:{background:C.border,border:"none",borderRadius:8,color:C.text,fontSize:13,padding:"6px 14px",cursor:"pointer"}},"Fermer")),
    React.createElement("div",{style:{display:"flex",gap:6,padding:"12px 16px",background:C.card,borderBottom:"1px solid "+C.border,overflowX:"auto"}},
      CATS.map(function(c){return React.createElement("button",{key:c,onClick:function(){setCat(c);},style:{flexShrink:0,padding:"6px 14px",borderRadius:16,cursor:"pointer",border:"1px solid "+(cat===c?C.gold:C.border),background:cat===c?C.goldSoft:C.bg,color:cat===c?C.gold:C.text2,fontSize:12,fontWeight:cat===c?600:400}},c);})),
    React.createElement("div",{style:{flex:1,overflowY:"auto",padding:"10px 16px"}},
      PAIRS.filter(function(p){return p.cat===cat;}).map(function(p){
        var active=p.symbol===props.current;
        return React.createElement("div",{key:p.symbol,onClick:function(){props.onSelect(p);props.onClose();},style:{display:"flex",alignItems:"center",justifyContent:"space-between",padding:"14px 16px",background:active?C.goldSoft:C.card,border:"1px solid "+(active?C.gold+"44":C.border),borderRadius:12,marginBottom:8,cursor:"pointer"}},
          React.createElement("div",{style:{display:"flex",alignItems:"center",gap:12}},
            React.createElement("span",{style:{fontSize:22}},[p.emoji]),
            React.createElement("div",{style:{fontSize:14,fontWeight:600,color:active?C.gold:C.text}},[p.symbol])),
          active&&React.createElement("span",{style:{fontSize:12,color:C.gold,fontWeight:600}},"Actif ✓"));})));
}

function SetupScreen(props){
  var _s=useState("");var key=_s[0],setKey=_s[1];
  return React.createElement("div",{style:{minHeight:"100vh",display:"flex",flexDirection:"column",alignItems:"center",justifyContent:"center",padding:"32px 24px",background:C.bg}},
    React.createElement("div",{style:{fontSize:48,marginBottom:8}},"🎯"),
    React.createElement("div",{style:{fontSize:28,fontWeight:700,color:C.text,marginBottom:4}},"Sniper Signals"),
    React.createElement("div",{style:{fontSize:13,color:C.text2,marginBottom:8}},"Fibonacci · Multi-TF · Alertes Telegram"),
    React.createElement("div",{style:{width:"100%",maxWidth:360,background:C.card,border:"1px solid "+C.border,borderRadius:20,padding:"28px 24px",marginTop:24}},
      React.createElement("div",{style:{fontSize:12,fontWeight:600,color:C.text2,marginBottom:8,textTransform:"uppercase",letterSpacing:0.5}},"Clé API Twelvedata"),
      React.createElement("input",{value:key,onChange:function(e){setKey(e.target.value);},placeholder:"Colle ta clé ici...",style:{background:C.bg,border:"1px solid "+C.border,borderRadius:10,color:C.text,fontSize:14,padding:"14px 16px",outline:"none",marginBottom:10}}),
      React.createElement("div",{style:{fontSize:12,color:C.text3,marginBottom:24,lineHeight:1.8}},"Gratuit sur ",React.createElement("span",{style:{color:C.gold}},"twelvedata.com")," · Dashboard → API Keys"),
      React.createElement("button",{onClick:function(){if(key.trim())props.onLaunch(key.trim());},style:{width:"100%",background:C.gold,color:"#0a0a0f",border:"none",borderRadius:12,padding:"16px",fontSize:15,fontWeight:700,cursor:"pointer"}},"Lancer →")));
}

// ── APP ──
function App(){
  var _ak=useState(function(){return localStorage.getItem("td_key")||"";});var apiKey=_ak[0],setApiKey=_ak[1];
  var _la=useState(false);var launched=_la[0],setLaunched=_la[1];
  var _lo=useState(false);var loading=_lo[0],setLoading=_lo[1];
  var _er=useState("");var error=_er[0],setError=_er[1];
  var _pr=useState(function(){var s=localStorage.getItem("selected_pair");if(s)try{return JSON.parse(s);}catch(e){}return PAIRS[0];});var selectedPair=_pr[0],setSelectedPair=_pr[1];
  var _sp=useState(false);var showPairs=_sp[0],setShowPairs=_sp[1];
  var _p=useState(null);var price=_p[0],setPrice=_p[1];
  var _ch=useState(null);var change=_ch[0],setChange=_ch[1];
  var _sig=useState(null);var sniperSig=_sig[0],setSniperSig=_sig[1];
  var _plan=useState(null);var tradePlan=_plan[0],setTradePlan=_plan[1];
  var _cd=useState({candles:[],ema20:[],ema50:[],swing:null});var chartData=_cd[0],setChartData=_cd[1];
  var _lu=useState("");var lastUpdate=_lu[0],setLastUpdate=_lu[1];
  var _at=useState("plan");var activeTab=_at[0],setActiveTab=_at[1];
  var _pu=useState(0);var pullDist=_pu[0],setPullDist=_pu[1];
  var timerRef=useRef(null);var wsRef=useRef(null);var lastNotifRef=useRef("");var startYRef=useRef(0);var THRESHOLD=70;

  var fmtPrice=function(p,sym){if(!p)return "-.--";var dp;if(sym&&sym.includes("BTC"))dp=0;else if(sym&&sym.includes("XAU"))dp=2;else if(sym&&sym.includes("JPY"))dp=2;else dp=5;return p.toFixed(dp).replace(/\B(?=(\d{3})+(?!\d))/g," ");};

  var sendTelegram=useCallback(async function(plan,sig){
    var key=sig.direction+plan.symbol;
    if(lastNotifRef.current===key)return;
    lastNotifRef.current=key;
    var symClean=plan.symbol.replace("/","");
    var dir=plan.isBuy?"🔹 ACHAT "+symClean:"🔸 VENTE "+symClean;
    var msg="🎯 SIGNAL SNIPER\n\n"+dir+"\n\n"+
      "Prix d'entrée ➡️ "+plan.entry+" ( exécution immédiate )\n\n"+
      "SL ➡️ "+plan.sl+" ( "+plan.slPts+" pips pertes )\n"+
      "TP1 ➡️ "+plan.tp1+" ( "+plan.tp1Pts+" pips gains )\n"+
      "TP2 ➡️ "+plan.tp2+" ( "+plan.tp2Pts+" pips gains )\n"+
      "TP3 ➡️ "+plan.tp3+" ( "+plan.tp3Pts+" pips gains )\n\n"+
      "💠 Risk reward ratio ≈ 1:"+plan.rr3+"\n"+
      "📐 Niveaux Fibonacci 1.272 / 1.618 / 2.618\n\n"+
      "Ceci n'est pas un conseil d'investissement, c'est juste mon investissement personnel que je vous partage.";
    await sendTG(msg);
  },[]);

  var testTelegram=useCallback(async function(){
    try{var r=await fetch("https://api.telegram.org/bot"+TG_TOKEN+"/sendMessage",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({chat_id:TG_CHAT,text:"🎯 SIGNAL SNIPER\n\n📲 Test de notification — système actif !\n\n🧪 Ceci est un message de test"})});var d=await r.json();if(d.ok)alert("✅ Message envoyé sur Telegram !");else alert("❌ Erreur : "+d.description);}catch(e){alert("❌ Erreur réseau");}
  },[]);

  var refresh=useCallback(async function(){
    try{
      setError("");
      var sym=selectedPair.symbol;
      var results=await Promise.all([
        fetch("https://api.twelvedata.com/time_series?symbol="+sym+"&interval=4h&outputsize=60&apikey="+apiKey).then(function(r){return r.json();}).catch(function(){return null;}),
        fetch("https://api.twelvedata.com/time_series?symbol="+sym+"&interval=1h&outputsize=50&apikey="+apiKey).then(function(r){return r.json();}).catch(function(){return null;}),
        fetch("https://api.twelvedata.com/time_series?symbol="+sym+"&interval=15min&outputsize=50&apikey="+apiKey).then(function(r){return r.json();}).catch(function(){return null;}),
      ]);
      function parseCandles(d){if(!d||d.status==="error"||!d.values)return null;return d.values.reverse().map(function(c){return{o:parseFloat(c.open),h:parseFloat(c.high),l:parseFloat(c.low),c:parseFloat(c.close)};});}
      var c4h=parseCandles(results[0]),c1h=parseCandles(results[1]),c15=parseCandles(results[2]);
      if(!c4h)throw new Error("Données indisponibles");
      var p=c4h[c4h.length-1].c;setPrice(p);
      var closes4h=c4h.map(function(c){return c.c;});
      var highs4h=c4h.map(function(c){return c.h;});
      var lows4h=c4h.map(function(c){return c.l;});
      var ema20a=calcEMA(closes4h,20),ema50a=calcEMA(closes4h,50);
      var atr=calcATR(highs4h,lows4h,closes4h,14);
      setChange(((p-closes4h[closes4h.length-2])/closes4h[closes4h.length-2])*100);
      var closes1h=c1h?c1h.map(function(c){return c.c;}):closes4h;
      var closes15=c15?c15.map(function(c){return c.c;}):closes4h;
      var swing=findSwing(highs4h,lows4h,20);
      var sig=computeSniperSignal(p,closes4h,closes1h,closes15,highs4h,lows4h);
      setSniperSig(sig);
      setChartData({candles:c4h,ema20:ema20a,ema50:ema50a,swing:swing});
      setLastUpdate(new Date().toLocaleTimeString("fr-FR",{hour:"2-digit",minute:"2-digit",second:"2-digit"}));
      var plan=null;
      if(sig.direction!=="neutral")plan=buildSniperPlan(p,atr,sig,sym);
      setTradePlan(plan);
      if(plan)sendTelegram(plan,sig);
    }catch(e){setError("Erreur : "+e.message);}
  },[apiKey,selectedPair,sendTelegram]);

  var startWS=useCallback(function(key,sym){
    if(wsRef.current){wsRef.current.close();wsRef.current=null;}
    var ws=new WebSocket("wss://ws.twelvedata.com/v1/quotes/price?apikey="+key);
    ws.onopen=function(){ws.send(JSON.stringify({action:"subscribe",params:{symbols:sym}}));};
    ws.onmessage=function(e){try{var d=JSON.parse(e.data);if(d.event==="price"&&d.symbol===sym&&d.price){setPrice(parseFloat(d.price));setLastUpdate(new Date().toLocaleTimeString("fr-FR",{hour:"2-digit",minute:"2-digit",second:"2-digit"}));}}catch(err){}};
    ws.onclose=function(){setTimeout(function(){if(wsRef.current===ws)startWS(key,sym);},5000);};
    wsRef.current=ws;
  },[]);

  var selectPair=useCallback(function(pair){if(pair.symbol===selectedPair.symbol)return;setSelectedPair(pair);localStorage.setItem("selected_pair",JSON.stringify(pair));setPrice(null);setChange(null);setSniperSig(null);setTradePlan(null);setLoading(true);lastNotifRef.current="";},[selectedPair]);
  var launch=useCallback(function(key){setApiKey(key);localStorage.setItem("td_key",key);setLaunched(true);setLoading(true);},[]);

  useEffect(function(){if(launched&&apiKey){refresh().finally(function(){setLoading(false);});startWS(apiKey,selectedPair.symbol);timerRef.current=setInterval(refresh,90000);return function(){clearInterval(timerRef.current);if(wsRef.current)wsRef.current.close();};};},[launched,apiKey,selectedPair]);
  useEffect(function(){if(apiKey)setLaunched(true);},[]);

  var onTouchStart=useCallback(function(e){if(window.scrollY===0)startYRef.current=e.touches[0].clientY;},[]);
  var onTouchMove=useCallback(function(e){if(!startYRef.current)return;var dist=e.touches[0].clientY-startYRef.current;if(dist>0&&window.scrollY===0)setPullDist(Math.min(dist,100));},[]);
  var onTouchEnd=useCallback(function(){if(pullDist>=THRESHOLD)refresh();setPullDist(0);startYRef.current=0;},[pullDist,refresh]);

  if(!launched)return React.createElement(SetupScreen,{onLaunch:launch});
  if(loading)return React.createElement("div",{style:{minHeight:"100vh",display:"flex",flexDirection:"column",alignItems:"center",justifyContent:"center",background:C.bg,gap:16}},React.createElement("div",{style:{fontSize:36}},selectedPair.emoji),React.createElement("div",{style:{width:28,height:28,border:"2px solid "+C.border,borderTopColor:C.gold,borderRadius:"50%",animation:"spin 0.8s linear infinite"}}),React.createElement("div",{style:{fontSize:13,color:C.text2}},"Chargement "+selectedPair.symbol+"..."));

  var sig=sniperSig;
  var tabs=[{id:"plan",label:"🎯 Sniper"},{id:"conditions",label:"Conditions"},{id:"chart",label:"Chart"}];

  return React.createElement("div",{onTouchStart:onTouchStart,onTouchMove:onTouchMove,onTouchEnd:onTouchEnd,style:{background:C.bg,minHeight:"100vh",paddingBottom:48}},
    showPairs&&React.createElement(PairSelector,{current:selectedPair.symbol,onSelect:selectPair,onClose:function(){setShowPairs(false);}}),
    pullDist>0&&React.createElement("div",{style:{display:"flex",justifyContent:"center",alignItems:"center",height:pullDist,background:C.bg}},React.createElement("div",{style:{fontSize:12,color:C.text3}},pullDist>=THRESHOLD?"Relâcher ↑":"Tirer ↓")),

    // HEADER
    React.createElement("div",{style:{padding:"14px 16px 12px",borderBottom:"1px solid "+C.border,display:"flex",justifyContent:"space-between",alignItems:"center",position:"sticky",top:0,background:C.bg,zIndex:10}},
      React.createElement("button",{onClick:function(){setShowPairs(true);},style:{display:"flex",alignItems:"center",gap:8,background:C.card,border:"1px solid "+C.border,borderRadius:12,padding:"8px 12px",cursor:"pointer"}},
        React.createElement("span",{style:{fontSize:18}},[selectedPair.emoji]),
        React.createElement("div",{style:{textAlign:"left"}},React.createElement("div",{style:{fontSize:14,fontWeight:700,color:C.text}},[selectedPair.symbol]),React.createElement("div",{style:{fontSize:10,color:C.text3}},"Sniper · Fibonacci")),
        React.createElement("span",{style:{fontSize:10,color:C.text3,marginLeft:4}},"▼")),
      React.createElement("div",{style:{display:"flex",alignItems:"center",gap:8}},
        React.createElement("div",{style:{display:"flex",alignItems:"center",gap:5,background:C.card,borderRadius:20,padding:"5px 10px",border:"1px solid "+C.border}},React.createElement("div",{style:{width:5,height:5,borderRadius:"50%",background:C.green,animation:"pulse 2s infinite"}}),React.createElement("span",{style:{fontSize:10,color:C.text2}},lastUpdate||"--:--")),
        React.createElement("button",{onClick:refresh,style:{background:C.card,border:"1px solid "+C.border,borderRadius:10,color:C.text2,width:32,height:32,display:"flex",alignItems:"center",justifyContent:"center",cursor:"pointer",fontSize:14}},"↻"))),

    error&&React.createElement("div",{style:{margin:"10px 16px",background:C.redSoft,border:"1px solid rgba(240,96,96,0.3)",borderRadius:12,padding:"10px 14px",fontSize:12,color:C.red}},error),

    // PRIX
    React.createElement("div",{style:{padding:"18px 20px 12px",textAlign:"center"}},
      React.createElement("div",{style:{fontSize:44,fontWeight:700,color:C.text,letterSpacing:-1}},fmtPrice(price,selectedPair.symbol)),
      React.createElement("div",{style:{display:"flex",alignItems:"center",justifyContent:"center",gap:6,marginTop:4}},
        React.createElement("span",{style:{fontSize:13,fontWeight:600,color:change!=null?(change>=0?C.green:C.red):C.muted}},change!=null?(change>=0?"+":"")+change.toFixed(2)+"%":"--"),
        React.createElement("span",{style:{fontSize:12,color:C.text3}},"aujourd'hui"))),

    // SIGNAL SNIPER
    sig&&React.createElement("div",{style:{margin:"0 16px 12px",background:sig.bg,border:"1px solid "+sig.color+"30",borderRadius:16,padding:"14px 18px",display:"flex",justifyContent:"space-between",alignItems:"center"}},
      React.createElement("div",null,
        React.createElement("div",{style:{fontSize:10,fontWeight:600,color:sig.color,letterSpacing:0.8,marginBottom:4,textTransform:"uppercase"}},"Signal Sniper"),
        React.createElement("div",{style:{fontSize:20,fontWeight:700,color:sig.color}},sig.label),
        React.createElement("div",{style:{fontSize:12,color:C.text2,marginTop:2}},sig.advice)),
      React.createElement("div",{style:{textAlign:"center",background:sig.color+"20",borderRadius:10,padding:"8px 12px"}},
        React.createElement("div",{style:{fontSize:10,color:C.text3,marginBottom:2}},"CONDITIONS"),
        React.createElement("div",{style:{fontSize:28,fontWeight:700,color:sig.color}},sig.score+"/4"))),

    // TABS
    React.createElement("div",{style:{display:"flex",gap:6,padding:"0 16px 12px",overflowX:"auto",scrollbarWidth:"none"}},
      tabs.map(function(t){return React.createElement("button",{key:t.id,onClick:function(){setActiveTab(t.id);},style:{flexShrink:0,padding:"7px 16px",borderRadius:20,cursor:"pointer",border:"1px solid "+(activeTab===t.id?(sig?sig.color:C.gold):C.border),background:activeTab===t.id?(sig?sig.color:C.gold)+"18":C.card,color:activeTab===t.id?(sig?sig.color:C.gold):C.text2,fontSize:12,fontWeight:activeTab===t.id?600:400}},t.label);})),

    activeTab==="plan"&&React.createElement("div",{style:{padding:"0 16px"}},React.createElement(PlanCard,{plan:tradePlan,signal:sig})),

    activeTab==="conditions"&&sig&&React.createElement("div",{style:{padding:"0 16px"}},
      React.createElement("div",{style:{background:C.card,border:"1px solid "+C.border,borderRadius:16,padding:"4px 16px",marginBottom:12}},
        React.createElement(ConditionRow,{ok:sig.conditions.trend,label:"Tendance 4H alignée",detail:"EMA 20 et EMA 50 dans la même direction"}),
        React.createElement(ConditionRow,{ok:sig.conditions.rsi,label:"RSI 1H neutre",detail:"RSI entre 35-65 — momentum sain"}),
        React.createElement(ConditionRow,{ok:sig.conditions.stoch,label:"Stoch RSI 15min",detail:"Croisement confirme l'entrée"}),
        React.createElement(ConditionRow,{ok:sig.conditions.fib,label:"Zone Fibonacci",detail:"Prix sur niveau 0.382 ou 0.618"})),
      sig.swing&&React.createElement("div",{style:{background:C.card,border:"1px solid "+C.border,borderRadius:16,padding:"16px"}},
        React.createElement("div",{style:{fontSize:12,fontWeight:600,color:C.purple,marginBottom:12}},"📐 Niveaux Fibonacci détectés"),
        [["Swing High",sig.swing.high.toFixed(getPipDecimals(selectedPair.symbol))],
         ["0.786",((sig.swing.high-(sig.swing.high-sig.swing.low)*0.786)).toFixed(getPipDecimals(selectedPair.symbol))],
         ["0.618",((sig.swing.high-(sig.swing.high-sig.swing.low)*0.618)).toFixed(getPipDecimals(selectedPair.symbol))],
         ["0.5",((sig.swing.high-(sig.swing.high-sig.swing.low)*0.5)).toFixed(getPipDecimals(selectedPair.symbol))],
         ["0.382",((sig.swing.high-(sig.swing.high-sig.swing.low)*0.382)).toFixed(getPipDecimals(selectedPair.symbol))],
         ["Swing Low",sig.swing.low.toFixed(getPipDecimals(selectedPair.symbol))]
        ].map(function(x,i){return React.createElement("div",{key:i,style:{display:"flex",justifyContent:"space-between",padding:"6px 0",borderBottom:i<5?"1px solid "+C.border:"none"}},React.createElement("span",{style:{fontSize:12,color:C.purple}},[x[0]]),React.createElement("span",{style:{fontSize:12,fontWeight:600,color:C.text}},[x[1]]));})))),

    activeTab==="chart"&&React.createElement("div",{style:{padding:"0 16px"}},
      React.createElement("div",{style:{background:C.card,border:"1px solid "+C.border,borderRadius:16,padding:"16px"}},
        React.createElement("div",{style:{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:12}},
          React.createElement("span",{style:{fontSize:13,fontWeight:600,color:C.text}},selectedPair.symbol+" · 4H"),
          React.createElement("div",{style:{display:"flex",gap:10}},
            React.createElement("span",{style:{fontSize:10,color:C.gold}},"— EMA20"),
            React.createElement("span",{style:{fontSize:10,color:C.blue}},"-- EMA50"),
            React.createElement("span",{style:{fontSize:10,color:C.purple}},"··· Fib"))),
        React.createElement(MiniChart,{candles:chartData.candles,ema20:chartData.ema20,ema50:chartData.ema50,swing:chartData.swing}))),

    React.createElement("div",{style:{display:"flex",justifyContent:"center",padding:"16px 16px 0"}},React.createElement("button",{onClick:testTelegram,style:{background:C.blueSoft,border:"1px solid "+C.blue+"44",borderRadius:10,color:C.blue,fontSize:12,padding:"10px 20px",cursor:"pointer",fontWeight:600,marginBottom:10}},"📲 Tester Telegram")),
    React.createElement("div",{style:{display:"flex",justifyContent:"center",padding:"8px 16px 0"}},React.createElement("button",{onClick:function(){localStorage.removeItem("td_key");setApiKey("");setLaunched(false);},style:{background:"transparent",border:"1px solid "+C.border,borderRadius:10,color:C.text3,fontSize:12,padding:"8px 18px",cursor:"pointer"}},"⚙ Changer la clé API")));
}

ReactDOM.createRoot(document.getElementById("root")).render(React.createElement(App));
</script>
</body>
</html>