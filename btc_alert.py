import requests

BOT_TOKEN = "8721138123:AAFZzQL3_Jk0We0oMyygYEZ9Fz3q22gBLPQ"
CHAT_ID   = "5145100304"

response = requests.get("https://api.kraken.com/0/public/Ticker?pair=XBTUSD")
data     = response.json()
cle      = list(data["result"].keys())[0]
prix     = float(data["result"][cle]["c"][0])

message  = f"₿ Prix BTC/USD : {prix:,.2f} $"
requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    json={"chat_id": CHAT_ID, "text": message}
)

print("Envoyé :", message)
