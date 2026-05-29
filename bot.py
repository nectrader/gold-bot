import requests
import time
import os
from datetime import datetime

TD_KEY = os.environ["TD_KEY"]
TG_TOKEN = os.environ["TG_TOKEN"]
TG_CHAT = "1302678674"

last_signal = ""

def get_candles(interval, size=80):
    url = "https://api.twelvedata.com/time_series"
    params = {"symbol":"XAU/USD","interval":interval,"outputsize":size,"apikey":TD_KEY}
    r = requests.get(url, params=params, timeout=10)
    d = r.json()
    if d.get("status") == "error":
        return None
    return list(reversed([{
        "o":float(v["open"]),
        "h":float(v["high"]),
        "l":float(v["low"]),
        "c":float(v["close"])
    } for v in d["values"]]))

def calc_ema(c, p):
    k = 2 / (p + 1)
    e = [c[0]]
    for i in range(1, len(c)):
        e.append(c[i] * k + e[-1] * (1 - k))
    return e

def calc_rsi(c, p=14):
    g = l = 0
    for i in range(1, p + 1):
        d = c[i] - c[i-1]
        if d > 0:
            g += d
        else:
            l -= d
    ag, al = g/p, l/p
    o = []
    for i in range(p + 1, len(c)):
        d = c[i] - c[i-1]
        ag = (ag * (p-1) + max(d, 0)) / p
        al = (al * (p-1) + max(-d, 0)) / p
        o.append(100 if al == 0 else 100 - 100 / (1 + ag/al))
    return o

def calc_stoch(c):
    r = calc_rsi(c, 14)
    raw = []
    for i in range(13, len(r)):
        sl = r[i-13:i+1]
        mn, mx = min(sl), max(sl)
        raw.append(50 if mx == mn else (r[i]-mn)/(mx-mn)*100)
    def sma(a, p):
        return [sum(a[i-p+1:i+1])/p for i in range(p-1, len(a))]
    sk = sma(raw, 3)
    sd = sma(sk, 3)
    return (sk[-1] if sk else 50), (sd[-1] if sd else 50)

def calc_atr(h, l, c, p=14):
    tr = [max(h[i]-l[i], abs(h[i]-c[i-1]), abs(l[i]-c[i-1])) for i in range(1, len(c))]
    a = sum(tr[:p]) / p
    for i in range(p, len(tr)):
        a = (a * (p-1) + tr[i]) / p
    return a

def get_signal(price, c):
    e20 = calc_ema(c, 20)
    e50 = calc_ema(c, 50)
    r = calc_rsi(c, 14)
    sk, sd = calc_stoch(c)
    s = 5
    if price > e20[-1]: s += 1
    else: s -= 1
    if price > e50[-1]: s += 1
    else: s -= 1
    if e20[-1] > e50[-1]: s += 0.5
    else: s -= 0.5
    if sk < 20: s += 2
    elif sk > 80: s -= 2
    elif sk > sd: s += 0.5
    else: s -= 0.5
    if r[-1] < 35: s += 1
    elif r[-1] > 65: s -= 1
    s = max(0, min(10, s))
    if s >= 6: return "buy", s
    if s <= 4: return "sell", s
    return "neutral", s

def send_telegram(msg):
    url = "https://api.telegram.org/bot" + TG_TOKEN + "/sendMessage"
    requests.post(url, json={"chat_id": TG_CHAT, "text": msg}, timeout=10)

def run():
    global last_signal
    c4h = get_candles("4h", 80)
    if not c4h or len(c4h) < 60:
        return
    closes = [c["c"] for c in c4h]
    highs = [c["h"] for c in c4h]
    lows = [c["l"] for c in c4h]
    price = closes[-1]
    a = calc_atr(highs, lows, closes)
    dir4h, score = get_signal(price, closes)
    if dir4h == "neutral":
        return
    time.sleep(3)
    c1h = get_candles("1h", 70)
    time.sleep(3)
    c1d = get_candles("1day", 70)
    if not c1h or not c1d:
        return
    dir1h, _ = get_signal(price, [c["c"] for c in c1h])
    dir1d, _ = get_signal(price, [c["c"] for c in c1d])
    agree = [dir4h, dir1h, dir1d].count(dir4h)
    if agree < 2:
        return
    sig_key = dir4h + "_" + str(round(score, 1))
    if sig_key == last_signal:
        return
    last_signal = sig_key
    is_buy = dir4h == "buy"
    sl_pips = max(100, min(150, round(a / 0.10 * 0.8)))
    tp1_pips = sl_pips
    tp2_pips = round(sl_pips * 2.8)
    tp3_pips = round(sl_pips * 5.8)
    entry = round(price)
    sl = entry - sl_pips * 0.10 if is_buy else entry + sl_pips * 0.10
    tp1 = entry + tp1_pips * 0.10 if is_buy else entry - tp1_pips * 0.10
    tp2 = entry + tp2_pips * 0.10 if is_buy else entry - tp2_pips * 0.10
    tp3 = entry + tp3_pips * 0.10 if is_buy else entry - tp3_pips * 0.10
    rr = round(tp3_pips / sl_pips)
    direction = "ACHAT GOLD / XAUUSD" if is_buy else "VENTE GOLD / XAUUSD"
    emoji = "🔹" if is_buy else "🔻"
    msg = (
        emoji + " " + direction + "\n\n"
        "Prix d'entree ➡️ " + str(entry) + " ( execution immediate )\n\n"
        "SL ➡️ " + str(int(sl)) + " ( " + str(sl_pips) + " pips pertes )\n"
        "TP1 ➡️ " + str(int(tp1)) + " ( " + str(tp1_pips) + " pips gains )\n"
        "TP2 ➡️ " + str(int(tp2)) + " ( " + str(tp2_pips) + " pips gains )\n"
        "TP3 ➡️ " + str(int(tp3)) + " ( " + str(tp3_pips) + " pips gains )\n\n"
        "💠 Risk reward ratio ≈ " + str(rr) + "\n\n"
        "Ceci n'est pas un conseil d'investissement, "
        "c'est juste mon investissement personnel que je vous partage."
    )
    send_telegram(msg)
    print("Signal envoye : " + direction)

send_telegram("🤖 Gold Bot demarre - surveillance active 24h/24")
while True:
    try:
        print("[" + datetime.now().strftime("%H:%M:%S") + "] Verification...")
        run()
    except Exception as e:
        print("Erreur: " + str(e))
    time.sleep(180)
