######### [ IMPORTING LIBRARIES ] #########
import time
import discord
Jc6D7dNVH = "MTAwNTQ4ODk"
from discord.ext import commands
import os
######### [ WELCOME MESSAGE ] #########
os.system("title ExtremeChat / -_ Version 0.3 -_")
os.system("color c")
def clr(): os.system("cls")
client = commands.Bot(command_prefix = "ec_")
print('''
         _______  ____________  ________  _________________  _____  ______
        / ____/ |/ /_  __/ __ \/ ____/  |/  / ____/ ____/ / / /   |/_  __/
       / __/  |   / / / / /_/ / __/ / /|_/ / __/ / /   / /_/ / /| | / /      Created with love <3
      / /___ /   | / / / _, _/ /___/ /  / / /___/ /___/ __  / ___ |/ /       Developed by TurboKoT#9455
     /_____//_/|_|/_/ /_/ |_/_____/_/  /_/_____/\____/_/ /_/_/  |_/_/     
                                         -_ Version: 0.3 -_                          ''')
yec = "NzU4NA.G7Ow-4.1-pI-TIND"                       
@client.event
async def on_ready():
    clr()
    print("|| Введите ваш ник")
    nickname = input("/> ")
    if nickname == "":
        nickname = "ExtremeUser"
        print("Вы не указали ник, поэтому ваш ник ExtremeUser")
        input("Продолжить (Enter)")
    elif len(nickname)>15:
        print("Ники больше 15 симовлов запрещенны! В вашем нике содержиться " + str(len(nickname)) + " символ(ов)!")
        input()
        exit()
    clr()
    print("|| Введите сервер, на котором хотите переписываться")
    print("|| Доступные сервера: 1, 2, 3")
    global server
    server = int(input("/> "))
    clr()
    if server == 1:
        os.system("title ExtremeChat / -_ Version 0.3 -_ / Server: 1 / NickName: " + nickname)
        channel = client.get_channel(1005487821919887400)
        await channel.send(nickname + " подключился к чату!")
    elif server == 2:
        os.system("title ExtremeChat / -_ Version 0.3 -_ / Server: 2 / NickName: " + nickname)
        channel = client.get_channel(1005535116489130015)
        await channel.send(nickname + " подключился к чату!")
    elif server == 3:
        os.system("title ExtremeChat / -_ Version 0.3 -_ / Server: 3 / NickName: " + nickname)
        channel = client.get_channel(1005535146952376471)
        await channel.send(nickname + " подключился к чату!")
    while True:
        messagee = input("Введите сообщение: ")
        if server == 1:
            await channel.send(nickname + ": " + messagee)
            time.sleep(1)
        elif server == 2:
            await channel.send(nickname + ": " + messagee)
            time.sleep(1)
        elif server == 3:
            await channel.send(nickname + ": " + messagee)
            time.sleep(1)

mar = "xODk4MjAz"
######### [ CATCHING MESSAGES ] #########
@client.event
async def on_message(message):
    if server == 1:
        if message.author.id == 1005488918982037584 or message.author.id == 1001711554003206276:
            if message.channel.id == 1005487821919887400:
                print(message.content)
    elif server == 2:
        if message.author.id == 1005488918982037584 or message.author.id == 1001711554003206276:
            if message.channel.id == 1005535116489130015:
                print(message.content)
    elif server == 3:
        if message.author.id == 1005488918982037584 or message.author.id == 1001711554003206276:
            if message.channel.id == 1005535146952376471:
                print(message.content)

try:
    client.run(Jc6D7dNVH + mar + yec + "MVkOgtMbCZfFTkO3a7Ffh5NWwYuwc")
except:
    clr()
    os.system("color c")
    print("Не удаеться подключиться к серверам ExtremeChat. Возможно, они недоступны, или-же у вас нет интернета ;)")
    input()
