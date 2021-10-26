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
    sell = re.findall("Slippage...........", string)
    buy = re.findall("Slippage..........", string)

    buy_v = re.findall("[0-99]%", buy[0])
    buy_slippage = buy_v[0]

    sell_v = re.findall("[0-99]%", sell[0])
    sell_slippage = sell_v[0]
    slip =  sell_slippage + buy_slippage

    if liqudity_kiedy < wartosc_liq:
        if slip > wartosc_kiedy_kupisz:
            trans(hash,klucz_prywatny,swapowane_bnp,adres_publiczny_portfela)
            time.sleep(50)
            sellt(hash,klucz_prywatny,swapowane_bnp,adres_publiczny_portfela)
            print("Kupione i Sprzedane")














client.start()
client.run_until_disconnected()
