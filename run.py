import os

import time

import random

import json

try:

    import colorama

except:

    os.system("pip installl colorama")

    import colorama

try:

    import requests

except:

    os.system("pip installl requests")

    import requests

THIS_VERSION = "0.2"

reset = colorama.Fore.RESET

red = colorama.Fore.LIGHTRED_EX

cyan = colorama.Fore.LIGHTCYAN_EX

green = colorama.Fore.LIGHTGREEN_EX

yellow = colorama.Fore.LIGHTYELLOW_EX

magenta = colorama.Fore.LIGHTMAGENTA_EX

space = "                            "

logo = f"""\n\n   

\t /$$    /$$ /$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$$$ /$$$$$$$$

\t| $$   | $$|_  $$_/| $$  / $$ /$$__  $$| $$_____/|__  $$__/

\t| $$   | $$  | $$  |  $$/ $$/| $$  \__/| $$         | $$   

\t|  $$ / $$/  | $$   \  $$$$/ |  $$$$$$ | $$$$$      | $$   

\t \  $$ $$/   | $$    >$$  $$  \____  $$| $$__/      | $$   

\t  \  $$$/    | $$   /$$/\  $$ /$$  \ $$| $$         | $$   

\t   \  $/    /$$$$$$| $$  \ $$|  $$$$$$/| $$$$$$$$   | $$   

\t    \_/    |______/|__/  |__/ \______/ |________/   |__/\n

\t( {magenta}1{reset} ) > WEBHOOK SPAMMER NORMAL           | ( {magenta}2{reset} ) > WEBHOOK SPAMMER WITH TTS

\t( {magenta}3{reset} ) > WEBHOOK SPAMMER WITH RANDOM PFPS | ( {magenta}4{reset} ) > EXIT

    """.replace("$", magenta+"$"+reset)

    

def clear():

    os.system("cls" if os.name == "nt" else "clear")

def worker():

    os.system(f"title VIXSET TOOL - VERSION : {THIS_VERSION}")

    clear()

    print(logo)

    # Webhoook Spammer ( option 1 )

    try:

        _option = input(f"\t[ {yellow}?{reset} ] ENTER AN OPTION : ")

    except KeyboardInterrupt:

        input(f"\n\t[ {yellow}?{reset} ] PRESS ANY KEY TO EXIT...")

        quit()

        

    if _option == "":

        worker()

    # Webhoook Spammer ( option 2 )

    if _option == "1":

        try:

            Webhook_url = input(f"\t[ {yellow}?{reset} ] WEBHOOK URL : ")

            if not Webhook_url.startswith("https://discord.com/api/webhooks/"):

                 print(f"\t[ {yellow}!{reset} ] INVALID WEBHOOK URL, PLEASE TRY AGAIN")

                 time.sleep(1)

                 worker()

            Webhook_Message = input(f"\t[ {yellow}?{reset} ] WEBHOOK MESSAGE : ")

        except KeyboardInterrupt:

            input(f"\n\t[ {yellow}?{reset} ] PRESS ANY KEY TO EXIT...")

            quit()

        Webhook_Spammer(Webhook_url, Webhook_Message)

    # Webhoook Spammer with tts ( option 2 )

    elif _option == "2":

        try:

            Webhook_url = input(f"\t[ {yellow}?{reset} ] WEBHOOK URL : ")

            if not Webhook_url.startswith("https://discord.com/api/webhooks/"):

                 print(f"\t[ {yellow}!{reset} ] INVALID WEBHOOK URL, PLEASE TRY AGAIN")

                 time.sleep(1)

                 worker()

            Webhook_Message = input(f"\t[ {yellow}?{reset} ] WEBHOOK MESSAGE : ")

        except KeyboardInterrupt:

            input(f"\n\t[ {yellow}?{reset} ] PRESS ANY KEY TO EXIT...")

            quit()

        Webhook_Spammer_tts(Webhook_url, Webhook_Message)

    # Webhoook Spammer with random pfps and name ( option 3 )

    elif _option == "3":

        try:

            Webhook_url = input(f"\t[ {yellow}?{reset} ] WEBHOOK URL : ")

            if not Webhook_url.startswith("https://discord.com/api/webhooks/"):

                 print(f"\t[ {yellow}!{reset} ] INVALID WEBHOOK URL, PLEASE TRY AGAIN")

                 time.sleep(1)

                 worker()

            Webhook_Message = input(f"\t[ {yellow}?{reset} ] WEBHOOK MESSAGE : ")

        except KeyboardInterrupt:

            input(f"\n\t[ {yellow}?{reset} ] PRESS ANY KEY TO EXIT...")

            quit()

        webhook_spammer_random_pfps(Webhook_url, Webhook_Message)

    elif _option == "4":

        input(f"\t[ {yellow}?{reset} ] PRESS ANY KEY TO EXIT...")

        quit()

    else:

        print(f"\t[ {red}X{reset} ] INVALID OPTION, PLEASE TRY AGAIN")

        time.sleep(1)

        worker()

        

def Webhook_Spammer(Webhook_url, Webhook_Message):

    while True:

        try:

            response = requests.post(Webhook_url, json={"content": Webhook_Message, "tts": False})

            if response.status_code == 204 or response.status_code == 200:

                print(f"\t[ {green}+{reset} ] MESSAGE HAS BEEN SENT")

            elif response.status_code == 429:

                print(f"\t[ {yellow}#{reset} ] RATE LIMITED, PLEASE WAIT  {response.json()['retry_after'] / 1000} SECOND")

                time.sleep(response.json()["retry_after"] / 1000)

            else:

                print(f"\t[ {red}X{reset} ] SOMETHING WENT SRONG - {response.status_code}")

            time.sleep(0.01)

        except KeyboardInterrupt:

            break

    input(f"\t[ {yellow}?{reset} ] PRESS ANY KEY TO CONTINUE...")

    worker()

    

def Webhook_Spammer_tts(Webhook_url, Webhook_Message):

    while True:

        try:

            response = requests.post(Webhook_url, json={"content": Webhook_Message, "tts": True})

            if response.status_code == 204 or response.status_code == 200:

                print(f"\t[ {green}+{reset} ] MESSAGE HAS BEEN SENT")

            elif response.status_code == 429:

                print(f"\t[ {yellow}#{reset} ] RATE LIMITED, PLEASE WAIT  {response.json()['retry_after'] / 1000} SECOND")

                time.sleep(response.json()["retry_after"] / 1000)

            else:

                print(f"\t[ {red}X{reset} ] SOMETHING WENT SRONG - {response.status_code}")

            time.sleep(0.01)

        except KeyboardInterrupt:

            break

    input(f"\t[ {yellow}?{reset} ] PRESS ANY KEY TO CONTINUE...")

    worker()

def webhook_spammer_random_pfps(Webhook_url, Webhook_Message):

    while True:

        try:

            _avatar = ["https://pfps.gg/assets/pfps/5477-dog-with-yellow-skin.png", "https://pfps.gg/assets/pfps/1260-unkraine-lover.png", "https://pfps.gg/assets/pfps/4104-wizard-lizard.png", "https://pfps.gg/assets/pfps/5220-swag-cat.png", "https://pfps.gg/assets/pfps/1342-anime.png", "https://pfps.gg/assets/pfps/5939-vaporwave-cat-drinking-in-space.png", "https://pfps.gg/assets/pfps/2555-panda.png", "https://pfps.gg/assets/pfps/5452-sup-dudes.png", "https://pfps.gg/assets/pfps/9605-sad-bart-simpson.png", "https://pfps.gg/assets/pfps/2301-child-pog.png", "https://pfps.gg/assets/pfps/1417-mona-pfp.png", "https://pfps.gg/assets/pfps/7767-rory-mercury-5.png", "https://pfps.gg/assets/pfps/2651-cat80.png", "https://pfps.gg/assets/pfps/5269-sonic-boom.png", "https://pfps.gg/assets/pfps/3660-swag.png", "https://pfps.gg/assets/pfps/3649-gray-haired-healer-faceless.png", "https://pfps.gg/assets/pfps/8506-freddie-dredd-egirl.png", "https://pfps.gg/assets/pfps/7733-anime.png", "https://pfps.gg/assets/pfps/6039-rory-mercury-4.png", "https://pfps.gg/assets/pfps/6721-rimuru-tempest.png", "https://pfps.gg/assets/pfps/4748-fat-lizard.png", "https://pfps.gg/assets/pfps/3671-yor-edit.png", "https://pfps.gg/assets/pfps/3682-drill.gif"]

            _username = ["chilly bidddddd", "quint", "banana from....?", "facal", "yay", "ssr", "Burak", "Wimmy", "Mr. John", "avocado from Maxico", "Big", "GODDD", "h0ny", "Billy", "Rose", "Vert", "hobby", "xdcolor", "brandy jobs", "yuki", "zerkkk", "Lunar", "jackson", "Fork", "Fillip", "Jack", "Steve", "noahh", "seesh", "coralo", "jimmy", "ss+", "bunny girls", "sim", "jane"]

            response = requests.post(Webhook_url, json={"content": Webhook_Message, "username": random.choice(_username), "avatar_url": random.choice(_avatar), "tts": True})

            if response.status_code == 200 or response.status_code == 204:

                print(f"\t[ {green}+{reset} ] MESSAGE HAS BEEN SENT")

            elif response.status_code == 429:

                print(f"\t[ {yellow}!{reset} ] RATE LIMITED, PLEASE WAIT {response.json()['retry_after'] / 1000} SECOND")

                time.sleep(response.json()["retry_after"] / 1000)

            else:

                print(f"\t[ {red}X{reset} ] SOMETHING WENT WRONG, STATUS CODE {response.status_code}")

                time.sleep(1)

                worker()

            time.sleep(0.01)

        except KeyboardInterrupt:

            break

    input(f"\t[ {yellow}?{reset} ] PRESS ANY KEY TO CONTINUE...")

    worker()

if __name__ in "__main__":

    worker()
