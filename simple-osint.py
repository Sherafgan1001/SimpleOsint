import base64
import datetime
import requests
from bs4 import BeautifulSoup
import json
from colorama import Fore
import sys

osintInstagram = base64.b64decode("aHR0cHM6Ly9zaGVyYWZnYW4uY2xvdWR1ei5ydS9hcGkvb3NpbnRncmFtL2FwaS5waHA/dXNlcj0=").decode()
ipOsint = base64.b64decode("aHR0cHM6Ly9zaGVyYWZnYW4uY2xvdWR1ei5ydS9hcGkvaXAvYXBpLnBocD9pcD0=").decode()

time_h = datetime.datetime.now().hour 
if time_h == 0:
    time = 'Шаб ба хайр'
elif time_h == 1:
    time = 'Шаб ба хайр'
elif time_h == 2:
    time = 'Шаб ба хайр'
elif time_h == 3:
    time = 'Шаб ба хайр'
elif time_h == 4:
    time = 'Шаб ба хайр'
elif time_h == 5:
    time = 'Шаб ба хайр'
elif time_h == 6:
    time = 'Субҳ ба хайр'
elif time_h == 7:
    time = 'Субҳ ба хайр'
elif time_h == 8:
    time = 'Субҳ ба хайр'
elif time_h == 9:
    time = 'Субҳ ба хайр'
elif time_h == 10:
    time = 'Рўз ба хайр'
elif time_h == 11:
    time = 'Рўз ба хайр'
elif time_h == 12:
    time = 'Рўз ба хайр'
elif time_h == 13:
    time = 'Рўз ба хайр'
elif time_h == 14:
    time = 'Рўз ба хайр'
elif time_h == 15:
    time = 'Рўз ба хайр'
elif time_h == 16:
    time = 'Рўз ба хайр'
elif time_h == 17:
    time = 'Шом ба хайр'
elif time_h == 18:
    time = 'Шом ба хайр'
elif time_h == 19:
    time = 'Шом ба хайр'
elif time_h == 20:
    time = 'Шаб ба хайр'
elif time_h == 21:
    time = 'Шаб ба хайр'
elif time_h == 22:
    time = 'Шаб ба хайр'
elif time_h == 23:
    time = 'Шаб ба хайр'

def ip(ip):
    try:
        response = requests.get(url=f"{ipOsint}{ip}").json()
        result = {
            "[IP-addres]":response['result']['ip'],
            "[Timezone]":response['result']['timezone'],
            "[Offset]":response['result']['offset'],
            "[Вакти хозира]":response['result']['localtime'],
            "[Europe]":response['result']['eu'],
            "[Материк]":response['result']['continent'],
            "[Номи материк]":response['result']['continent_name'],
            "[Кишвар]":response['result']['country'],
            "[Номи кишвар]":response['result']['country_name'],
            "[Номи шахр]":response['result']['city'],
            "[Вилоят]":response['result']['state'],
            "[Минтақа]":response['result']['district'],
            "[Пайвастшави]":response['result']['connection'],
            "[Zipcode]":response['result']['zipcode'],
            "[Пахнои]":response['result']['latitude'],
            "[Дарози]":response['result']['longitude'],
            "[Интернет провайдер]":response['result']['isp'],
            "[Ташкилот]":response['result']['organization'],
        }
        for k, v in result.items():
                print(Fore.YELLOW + f'{k}: {v}')
    except KeyError:
        print(Fore.RED + "[!] IP addres нодуруст ворид шудааст")
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "[!] Лутфан алокаи интернетро санчед")

def insta(insta):
    if "@" in insta:
        insta = insta.replace("@", "")
    try:
        response = requests.get(url=f"{osintInstagram}{insta}").json()
        result = {
                "[ID]":response['result']['id'],
                "[Username]":response['result']['username'],
                "[Закрытый аккаунт]":response['result']['is_private'],
                "[Profile Pic Url]":response['result']['profile_pic_url'],
                "[Биография]":response['result']['biography'],
                "[Name]":response['result']['full_name'],
                "[Публикация]":response['result']['edge_owner_to_timeline_media']['count'],
                "[Подписчики]":response['result']['edge_followed_by']['count'],
                "[Подписки]":response['result']['edge_follow']['count'],
            }
        for k, v in result.items():
                print(Fore.YELLOW + f'{k}: {v}')
    except KeyError:
        print(Fore.RED + "[!] Аккаунт бо ин гуна username вучуд надорад")
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "[!] Лутфан алокаи интернетро санчед")

def tiktok(user):
    if "@" in user:
        user = user.replace("@", "")
    try:
        url = f'https://tiktok.com/@{user}'
        headers = {
        'Accept-Language': 'ru',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
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
            "[Подписчики]":followers_count,
            "[Подписки]":following_count,
            "[Username]":user,
            "[Profile Pic Url]":image_link,
            "[Биография]":bio,
            "[Name]":name,
            "[Лайки]":likes_count,
        }
        for k, v in result.items():
            print(Fore.YELLOW + f'{k}: {v}')
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "Лутфан алокаи интернетро санчед!")
    except AttributeError:
        print(Fore.RED + "[!] Аккаунт бо ин гуна username вучуд надорад")

logo = r'''   _____ _                 __        ____       _       __ 
  / ___/(_)___ ___  ____  / /__     / __ \_____(_)___  / /_
  \__ \/ / __ `__ \/ __ \/ / _ \   / / / / ___/ / __ \/ __/
 ___/ / / / / / / / /_/ / /  __/  / /_/ (__  ) / / / / /_  
/____/_/_/ /_/ /_/ .___/_/\___/   \____/____/_/_/ /_/\__/  
                /_/                                        
'''

def main():
    print(Fore.CYAN + logo)
    print(Fore.YELLOW + '\n+=====================================================+')
    print(f'|                    {time}                      |')
    print('+=====================================================+')
    print('| 1. Чустучуи маълумот оиди ip-адрес                  |')
    print('| 2. Чустучуи маълумот оиди аккаунти Instagram        |')
    print('| 3. Чустучуи маълумот оиди аккаунти TikTok           |')
    print('| 4. exit - баромадан аз барнома                      |')
    print('+=====================================================+')


if __name__ == "__main__":
    main() 
while True:
    user_input = input(Fore.BLUE + ">>> ")
    if user_input == "1":
        userIP = input(Fore.GREEN + "IP-адресро ворид намоед: ")
        ip(userIP)
    elif user_input == "2":
        userName = input(Fore.GREEN + "Юзернеймро ворид намоед: ")
        insta(userName)
    elif user_input == "3":
        user = input(Fore.GREEN + "Юзернеймро ворид намоед: ")
        tiktok(user)
    elif user_input == "exit" or user_input == "4":
        print("Goodbye")
        sys.exit()
    else:
        print(Fore.RED + "[!] Командаи номаълум")
        user_input
