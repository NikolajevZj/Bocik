from telethon import TelegramClient, events
import re
from Pancake_b import trans
from Pancake_s import sellt
import time

api_id = 1231242345647
api_hash = ''
client = TelegramClient('Gilgamesh', api_id, api_hash)

wartosc_kiedy_kupisz = 0
klucz_prywatny = ''
swapowane_bnp = 0
adres_publiczny_portfela = ''
liqudity_kiedy = 0

@client.on(events.NewMessage())
async def my_event_handler(event):
    string = event.raw_text
    hash = re.findall("0x........................................", string)
    hash = hash[0]
    liquidity = re.findall("Liquidity:..[0-998].[0-99][0-99] BNB",string)
    g = re.findall("[0-998].[0-99][0-99]",liquidity[0])
    wartosc_liq = g[0]
    g1 = re.findall("Slippage.*[0-99]",string)
    y = 0
    for n in g1:
        c = re.findall("[0-99]",n)
        o = c[0]
    y += int(o)
    slip = y

    if liqudity_kiedy < wartosc_liq:
        if slip > wartosc_kiedy_kupisz:
            trans(hash,klucz_prywatny,swapowane_bnp,adres_publiczny_portfela)
            time.sleep(50)
            sellt(hash,klucz_prywatny,swapowane_bnp,adres_publiczny_portfela)
            print("Kupione i Sprzedane")














client.start()
client.run_until_disconnected()
