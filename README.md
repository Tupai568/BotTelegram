# BotTelegram
scrip ini menjadikan akun telgram anda menjadi bot itu sendiri, masukkan bot ke chanel yang anda inginkan.
bot akan membalas ketika ada yang mengirim pesan di chanel dengan text milo,

contoh: milo ngapain? 
maka milo akan menjawab dengan data yang sudah saya sediakan di data.json

# Installing
$ pip install telethon

$ pip install requests

$ pip install colorama

$ pip install googletrans

$ pip install wikipedia

# run python bot.py

api_id = 'xxxxxx'  #api_id

api_hash = 'xxxxxxx' #api_hash

phone = 'xxxxx' #nomer_hp_telegram

edit bagian ini di file bot.py dan masukkan punya anda.

untuk mendapatkan api_id & api_hash, anda perlu membuat nya.

untuk cara pembuatan nya silahkan kunjungi https://tigaputri.asia/membuat-api-telegram/.

# Translate
untuk menggunakan fitur tranlate, 

anda perlu mereply text yang mau anda translate.

dan mereplynya dengan text milo $translate.

# edit bot

@client.on(events.NewMessage(chats=['@xxxxxxx']))  #edit file bot.py dan masukkan username chanel yang anda inginkan.

if curhat == "milo": #ubah kata kunci milo dengan apa yng anda inginkan

if "$translate" in event.raw_text.lower(): #ubah kata kunci $translate dengan apa yang anda inginkan

elif "$wikipedia" in event.raw_text.lower(): #ubah kata kunci wikipedia dengan apa yang anda inginkan




