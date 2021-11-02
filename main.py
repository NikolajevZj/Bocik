from telethon import TelegramClient, events
import re
from Pancake_b import trans
from Pancake_s import sellt
import time

api_id = 17775638
api_hash = '6d99b66fd5b4400974f72cd8ee8f504d'
client = TelegramClient('anonsperg', api_id, api_hash)

wartosc_kiedy_kupisz = 25
klucz_prywatny = 'a31fe480ba3b30fd5e7962d4581e0b9e161caafcee2bea15cb45575763ac450c'
swapowane_bnp = 0.0004
adres_publiczny_portfela = '0xb1B5d836C3483742684ca6D0468083E72a1f9551'
liqudity_kiedy = 500
traz = 1
def check(traz):
    return traz
def increase(traz):
    traz += 1
def liq1(wartosc_liq):
    if 300 < int(wartosc_liq) < 500:
        liq = 18 - 0.03 * (wartosc_liq - 300)
        return liq
    elif 100 < int(wartosc_liq) < 300:
        liq = 25 - 0.035 * (wartosc_liq - 100)
        return liq
    elif 50 < int(wartosc_liq) < 100:
        liq = 35 - 0.14 * (wartosc_liq - 50)
        return liq


print("Odpalam...")
@client.on(events.NewMessage())
async def my_event_handler(event):
    tra1 = check(traz)
    if tra1 < 5:
        string = event.raw_text
        hash = re.findall("0x........................................", string)
        hash = hash[0]
        liquidity = re.findall("Liquidity:.*[0-998] BNB", string)
        liquidity = liquidity[0]
        g = re.findall("(?<=:.).*[0-9978]", liquidity)
        wartosc_liq = g[0]
        wartosc_liq = wartosc_liq.split(".")
        wartosc_liq = wartosc_liq[0]
        g1 = re.findall("Slippage.*[0-99]", string)
        SLIP_SELL = g1[1]
        y = 0
        for n in g1:
            c = re.findall("(?<=:.).*[0-99]", n)
            o = c[0]
            y += int(o)
        slip = y

        if liqudity_kiedy > int(wartosc_liq) >= 50:
            print("liquid dobry")
            liq = liq1(int(wartosc_liq))
            if int(liq) < wartosc_kiedy_kupisz:
                trans(hash, klucz_prywatny, swapowane_bnp, adres_publiczny_portfela)
                print("Kupione")
                increase(traz)
        else:
            print("Transakcja odrzucona")
















client.start()
client.run_until_disconnected()
