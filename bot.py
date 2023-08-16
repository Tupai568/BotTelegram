from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest, SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty
from telethon.errors import SessionPasswordNeededError
from time import sleep
from pprint import pprint
import requests, json, re, sys, os, random, time, colorama, wikipedia
from colorama import Fore
from googletrans import Translator


os.system('cls')

api_id = 'xxxxxx'  #api_id
api_hash = 'xxxxxxx' #api_hash
phone = 'xxxxx' #nomer_hp_telegram

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
mengetik(Fore.BLUE +'\r█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ \n█  '+Fore.GREEN+'██▓▒­░⡷⠂Bot V1.00⠐⢾░▒▓██  '+Fore.BLUE+'█ \n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n')



def read_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines
   
if not os.path.exists('session'): #cek apakah ada file session
    os.makedirs('session')

client = TelegramClient('session/'+phone,api_id,api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone)
        me = client.sign_in(phone,input('Masukan Code Anda >> '))
    except SessionPasswordNeededError:
        password = input('Masukan Password 2fa Anda >> ')
        me = client.start(phone,password)

dir = open('data.json', encoding="utf8") #direct data dari file data.json anda bisa menambahkan data tambahan di data.json
data = json.loads(dir.read())
async def main():
	@client.on(events.NewMessage(chats=['@xxxxxxx'])) #username chanel telegram. Contoh: @anonyim
	async def my_event_handler(event):
		for curhat in data["data"]:
			if curhat in event.raw_text.lower():
				if curhat == "milo": #jika ada yang menulis text milo maka bot akan otomatis menjawab,
					if "$translate" in event.raw_text.lower():  #jika ada yang mulis milo $translate maka milo harus mengecek terlebih dahulu
						if event.reply_to: #milo akan mengecek apakah yang menggunakan $translate suda mereply apa yang harus ditranslate
							cek = await event.get_reply_message()
							translator = Translator()
							translation = translator.translate(cek.message, dest='id')
							sender = await event.get_sender()
							user = sender.to_dict()
							msg = event.message.to_dict()
							time.sleep(5)
							print(Fore.BLUE+'name: {}'.format(user['first_name']), Fore.YELLOW+'֍', Fore.GREEN+msg['message'])
							await event.reply('traslate( '+translation.text+' )')
							break;
						else: #jika belum mereply maka milo akan memberi notife untuk mereply terlebih dahulu
							sender = await event.get_sender()
							user = sender.to_dict()
							msg = event.message.to_dict()
							time.sleep(5)
							print(Fore.BLUE+'name: {}'.format(user['first_name']), Fore.YELLOW+'֍', Fore.GREEN+msg['message'])
							await event.reply('reply yang mau ditranslate')
							break;
					elif "$wikipedia" in event.raw_text.lower(): #fitur untuk mencari data lewat wikipedia
						sender = await event.get_sender()
						user = sender.to_dict()
						msg = event.message.to_dict()
						cek = "{}".format(msg['message'])
						one = cek.find("(")
						two = cek.find(")")
						if one == int("-1"):
							print(Fore.BLUE+'name: {}'.format(user['first_name']), Fore.YELLOW+'֍', Fore.GREEN+msg['message'])
							await event.reply('Contoh: Milo $wikipedia (apa yng mau dicari)')
						else:
							if two == int(-1):
								print(Fore.BLUE+'name: {}'.format(user['first_name']), Fore.YELLOW+'֍', Fore.GREEN+msg['message'])
								await event.reply('Contoh: Milo $wikipedia (apa yng mau dicari)')
							else:
								one1 = cek.split("(")
								two1 = one1[1].split(")")
								text = two1[0]
								try:
									wikipedia.set_lang("id")
									search = wikipedia.summary(text, sentences=5)
									result = search.replace('0', 'O')
									time.sleep(5)
									print(Fore.BLUE+'name: {}'.format(user['first_name']), Fore.YELLOW+'֍', Fore.GREEN+msg['message'])
									await event.reply(result)
								except:
									print(Fore.BLUE+'name: {}'.format(user['first_name']), Fore.YELLOW+'֍', Fore.GREEN+msg['message'])
									await event.reply("wikipedia tidak mengetahui informasi tersebut")
					else:
						for curhat in data["milo"]:
							if curhat in event.raw_text.lower():
								sender = await event.get_sender()
								user = sender.to_dict()
								msg = event.message.to_dict()
								time.sleep(5)
								print(Fore.BLUE+'name: {}'.format(user['first_name']), Fore.YELLOW+'֍', Fore.GREEN+msg['message'])
								await event.reply(data['milo'][curhat][random.randint(0, 4)])
								break;
						else:
							sender = await event.get_sender()
							user = sender.to_dict()
							msg = event.message.to_dict()
							time.sleep(5)
							print(Fore.BLUE+'name: {}'.format(user['first_name']), Fore.YELLOW+'֍', Fore.GREEN+msg['message'])
							await event.reply(data['respon']['res'][random.randint(0, 4)])
							break;
							pass
				
				else:
					sender = await event.get_sender()
					user = sender.to_dict()
					msg = event.message.to_dict()
					time.sleep(5)
					print(Fore.BLUE+'name: {}'.format(user['first_name']), Fore.YELLOW+'֍', Fore.GREEN+msg['message'])
					await event.reply(data['data'][curhat][random.randint(0, 4)])
					break;
			pass
with client:
	client.loop.run_until_complete(main())
	time.sleep(5)
	client.run_until_disconnected()



