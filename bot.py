import requests
import time
import os
from datetime import datetime

TD_KEY = os.environ["TD_KEY"]
TG_TOKEN = os.environ["TG_TOKEN"]
TG_CHAT = "1302678674"

last_signal = ""

def get_candles(interval, size=80):
    r = requests.get(f"https://api.twelvedata.com/time_series?symbol=XAU/USD&interval={interval}&outputsize={size}&apikey={TD_KEY}", timeout=10)
    d = r.json()
    if d.get("status") == "error": return None
    return list(reversed([{"o":float(v["open"]),"h":float(v["high"]),"l":float(v["low"]),"c":float(v["close"])} for v in d["values"]]))

def ema(c,p):
    k=2/(p+1);e=[c[0]]
    for i in range(1,len(c)):e.append(c[i]*k+e[-1]*(1-k))
    return e

def rsi(c,p=14):
    g=l=0
    for i in range(1,p+1):
        d=c[i]-c[i-1]
        if d>0:g+=d
        else:l-=d
    ag,al=g/p,l/p;o=[]
    for i in range(p+1,len(c)):
        d=c[i]-c[i-1]
        ag=(ag*(p-1)+max(d,0))/p;al=(al*(p-1)+max(-d,0))/p
        o.append(100 if al==0 else 100-100/(1+ag/al))
    return o

def stoch(c):
    r=rsi(c,14);raw=[]
    for i in range(13,len(r)):
        sl=r[i-13:i+1];mn,mx=min(sl),max(sl)
        raw.append(50 if mx==mn else (r[i]-mn)/(mx-mn)*100)
    def sma(a,p):return[sum(a[i-p+1:i+1])/p for i in range(p-1,len(a))]
    sk=sma(raw,3);sd=sma(sk,3)
    return sk[-1] if sk else 50,sd[-1] if sd else 50

def atr(h,l,c,p=14):
    tr=[max(h[i]-l[i],abs(h[i]-c[i-1]),abs(l[i]-c[i-1]))for i in range(1,len(c))]
    a=sum(tr[:p])/p
    for i in range(p,len(tr)):a=(a*(p-1)+tr[i])/p
    return a

def signal(price
