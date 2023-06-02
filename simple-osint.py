import base64
import datetime
import requests
import sys
from os import system
from bs4 import BeautifulSoup
from colorama import Fore
from fake_useragent import UserAgent

# func for decoding
def base85_decode(encoded_string):
    return base64.a85decode(encoded_string).decode()

# encoded strings 
osintInstagram = base85_decode("BQS?8F#ks-F(f-*@:j.\\DD#F8DfoT5H7j5\\04Ag605koGDKKN3@;RZ+E+pqDBQ-1YF(KAT")
ipOsint = base85_decode("BQS?8F#ks-F(f-*@:j.\\DD#F8DfoT5H7j5\\04Ag6055AY@;op5E+j2TBlH3")

#greetings
time_h = datetime.datetime.now().hour
time = (lambda h: 'Шаб ба хайр' if 0 <= h <= 5 or 20 <= h <= 23 else 'Субҳ ба хайр' if 6 <= h <= 9 else 'Рўз ба хайр' if 10 <= h <= 16 else 'Шом ба хайр')(time_h)

#OSINT IP
def ip(ip):
    try:
        system("clear || cls")
        print(f'[+] IP-СУРОҒА - {ip}\n')
        response = requests.get(url=f"{ipOsint}{ip}").json()
        result = {
            "[ IP-СУРОҒА ]":response['result']['ip'],
            "[ МИНТАҚАИ ВАКТ ]":response['result']['timezone'],
            "[ ОФФСЕТ ]":response['result']['offset'],
            "[ ВАҚТИ ХОЗИРА ]":response['result']['localtime'],
            "[ АВРУПО ]":response['result']['eu'],
            "[ МАТЕРИК ]":response['result']['continent'],
            "[ НОМИ МАТЕРИК ]":response['result']['continent_name'],
            "[ КИШВАР ]":response['result']['country'],
            "[ НОМИ КИШВАР ]":response['result']['country_name'],
            "[ НОМИ ШАХР ]":response['result']['city'],
            "[ ВИЛОЯТ ]":response['result']['state'],
            "[ МИНТАҚА ]":response['result']['district'],
            "[ ПАЙВАСТШАВӢ ]":response['result']['connection'],
            "[ Индекси почтаӣ ]":response['result']['zipcode'],
            "[ ПАҲНОӢ ]":response['result']['latitude'],
            "[ ДАРОЗӢ ]":response['result']['longitude'],
            "[ ИНТЕРНЕТ ПРОВАЙДЕР ]":response['result']['isp'],
            "[ ТАШКИЛОТ ]":response['result']['organization'],
        }
        for k, v in result.items():
                print(Fore.YELLOW + f'{k}: {v}')
    except KeyError:
        print(Fore.RED + "[-] IP-СУРОҒА нодуруст ворид шудааст")
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "[!] Лутфан алоқаи интернетро санчед")

#OSINT INSTA
def insta(insta):
    if "@" in insta:
        insta = insta.replace("@", "")
    try:
        system("cls || clear")
        print(f'[+] САХИФА - {insta}\n')
        response = requests.get(url=f"{osintInstagram}{insta}").json()
        result = {
                "[ ID ]":response['result']['id'],
                "[ НОМИ КОРБАРӢ ]":response['result']['username'],
                "[ САҲИФАИ МАҲКАМ ]":response['result']['is_private'],
                "[ СУРАТИ САҲИФА ]":response['result']['profile_pic_url'],
                "[ БИОГРАФИЯ ]":response['result']['biography'],
                "[ НОМ ]":response['result']['full_name'],
                "[ НАШРҲО ]":response['result']['edge_owner_to_timeline_media']['count'],
                "[ МУШТАРИҲО ]":response['result']['edge_followed_by']['count'],
                "[ ОБУНА ШУДАГИ ]":response['result']['edge_follow']['count'],
            }
        for k, v in result.items():
                print(Fore.YELLOW + f'{k}: {v}')
    except KeyError:
        print(Fore.RED + "[!] Аккаунт бо ин гуна username вучуд надорад")
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "[!] Лутфан алокаи интернетро санчед")

#OSINT TIKTOK
def tiktok(user):
    if "@" in user:
        user = user.replace("@", "")
    try:
        system("clear || cls")
        print(f'[+] САХИФА - {user}\n')
        ua = UserAgent()
        url = f'https://tiktok.com/@{user}'
        headers = {
        'Accept-Language': 'ru',
        'User-Agent': ua.random
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        following_count = soup.find('strong', {'data-e2e': 'following-count'}).text
        followers_count = soup.find('strong', {'data-e2e': 'followers-count'}).text
        likes_count = soup.find('strong', {'data-e2e': 'likes-count'}).text
        img_src = soup.find('img', {'class': 'tiktok-1zpj2q-ImgAvatar'})
        image_link = img_src.get('src')
        bio_tag = soup.find('h2', {'data-e2e': 'user-bio'})
        bio = bio_tag.text
        name_tag = soup.find('h1', {'data-e2e': 'user-subtitle'})
        name = name_tag.text
        result = {
            "[ МУШТАРИҲО ]":followers_count,
            "[ ОБУНА ШУДАГИ ]":following_count,
            "[ НОМИ КОРБАРӢ ]":user,
            "[ СУРАТИ САХИФА ]":image_link,
            "[ БИОГРАФИЯ ]":bio,
            "[ НОМ ]":name,
            "[ ЛАЙКҲО ]":likes_count,
        }
        for k, v in result.items():
            print(Fore.YELLOW + f'{k}: {v}')
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "[!] Лутфан алоқаи интернетро санчед.")
    except AttributeError:
        print(Fore.RED + "[!] Аккаунт бо ин гуна username вучуд надорад.")

banner = r'''   
   _____ _                 __        ____       _       __ 
  / ___/(_)___ ___  ____  / /__     / __ \_____(_)___  / /_
  \__ \/ / __ `__ \/ __ \/ / _ \   / / / / ___/ / __ \/ __/
 ___/ / / / / / / / /_/ / /  __/  / /_/ (__  ) / / / / /_  
/____/_/_/ /_/ /_/ .___/_/\___/   \____/____/_/_/ /_/\__/  
                /_/                                        
    Барнома барои ҷустуҷӯи маълумот бо востаи IP, Instagram ва TikTok.
        https://github.com/Sherafgan1001/SimpleOsint
'''

def main():
    print(Fore.CYAN + banner)
    print(Fore.YELLOW + '+=====================================================+')
    print(f'|                    {time}                      |')
    print('+=====================================================+')
    print('| 1 - ҶУСТУҶӮИ МАЪЛУМОТ ОИДИ IP-АДРЕС                 |')
    print('| 2 - ҶУСТУҶӮИ МАЪЛУМОТ ОИДИ САҲИФАИ ШАХСИИ Instagram |')
    print('| 3 - ҶУСТУҶӮИ МАЪЛУМОТ ОИДИ САҲИФАИ ШАХСИИ TikTok    |')
    print('|-----------------------------------------------------|')
    print('| 4 (EXIT)       БАРОМАДАН АЗ БАРНОМА                 |')
    print('+=====================================================+')


if __name__ == "__main__":
    main() 
while True:
    user_input = input(Fore.BLUE + "\n]>>> ")
    if user_input == "1":
        userIP = input(Fore.GREEN + "[!] IP-адресро ворид намоед: ")
        ip(userIP)
    elif user_input == "2":
        userName = input(Fore.GREEN + "[!] Юзернеймро ворид намоед: ")
        insta(userName)
    elif user_input == "3":
        user = input(Fore.GREEN + "[!] Юзернеймро ворид намоед: ")
        tiktok(user)
    elif user_input == "exit" or user_input == "4" or user_input == "EXIT":
        print("[!] Хуш бошед ")
        sys.exit()
    else:
        print(Fore.RED + "[-] Командаи номаълум ")
        user_input
