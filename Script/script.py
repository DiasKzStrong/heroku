import datetime
import requests
import json
from datetime import date
from Keybord.Default import kb_namaz_time

with open(r'C:\Users\eeone\PycharmProjects\pythonProject11\Script\data.json', 'r', encoding='utf-8') as file:
    city_list = json.load(file)

def get_namaz_time(inpp):
    c1 = ""
    c2 = ""
    for i in range(len(city_list)):
        if city_list[i]["title"] == inpp:
            c1 = city_list[i]["lat"]
            c2 = city_list[i]["lng"]
    req1 = requests.request("GET", url=f'https://api.muftyat.kz/prayer-times/2023/{c1}/{c2}')
    today = str(date.today())
    count = 0
    city_namaz = json.loads(req1.text)
    for i in range(len(city_namaz["result"])):
        if city_namaz["result"][i]["Date"] == today:
            count = i
            break
    return city_namaz["result"][count]

def get_city(answer):
    new = ''
    for i in range(len(city_list)):
        if answer == city_list[i]["title"]:
            new = city_list[i]['timezone']
    return new

def del_dot(inp):
    d = ''
    for i in inp:
        if i != ':':
            d += i
    return int(d)

def print_namaz_time(inpp,call):
    answer = get_namaz_time(inpp)
    current_time = datetime.datetime.now()
    timer: int = 0
    if get_city(inpp) == '6':
        timer = int((current_time.hour*100)+current_time.minute)
    elif get_city(inpp) == '5':
        timer = int(((current_time.hour-1) * 100) + current_time.minute)
    if del_dot(answer['fajr']) < timer < del_dot(answer['sunrise']):
        return call.message.answer(f" <b>{call.data}</b> \n\n<b>Намаз уақыты:</b> \n\n <b><u>Таң намазы: {answer['fajr']}</u></b> \n Күн шығуы: {answer['sunrise']} \n Бесін: {answer['dhuhr']} \n Аср: {answer['asr']} \n Ақшам: {answer['maghrib']} \n Құптан: {answer['isha']} \n\n <b>Қазір Таң намазының уақыты,қаза қылдырмай оқып үлгерініз!!!</b>")
    elif del_dot(answer['sunrise']) < timer < del_dot(answer['dhuhr']):
        return call.message.answer(f" <b>{call.data}</b> \n\n<b>Намаз уақыты:</b> \n\n Таң намазы: {answer['fajr']} \n <b><u>Күн шығуы: {answer['sunrise']} </u></b>\n Бесін: {answer['dhuhr']} \n Аср: {answer['asr']} \n Ақшам: {answer['maghrib']} \n Құптан: {answer['isha']}\n\n<b>Қазір намаз уақыты емес!!!</b>")
    elif del_dot(answer['dhuhr']) < timer < del_dot(answer['asr']):
        return call.message.answer(f" <b>{call.data}</b> \n\n<b>Намаз уақыты:</b> \n\n Таң намазы: {answer['fajr']} \n Күн шығуы: {answer['sunrise']} \n <b><u>Бесін: {answer['dhuhr']}</u></b> \n Аср: {answer['asr']} \n Ақшам: {answer['maghrib']} \n Құптан: {answer['isha']}\n\n<b>Қазір Бесін намазының уақыты,қаза қылдырмай оқып үлгерініз!!!</b>")
    elif del_dot(answer['asr']) < timer < del_dot(answer['maghrib']):
        return call.message.answer(f" <b>{call.data}</b> \n\n<b>Намаз уақыты:</b> \n\n Таң намазы: {answer['fajr']} \n Күн шығуы: {answer['sunrise']} \n Бесін: {answer['dhuhr']} \n<b><u> Аср: {answer['asr']} </u></b>\n Ақшам: {answer['maghrib']} \n Құптан: {answer['isha']}\n\n<b>Қазір Аср намазының уақыты,қаза қылдырмай оқып үлгерініз!!!</b>")
    elif del_dot(answer['maghrib']) < timer < del_dot(answer['isha']):
        return call.message.answer(f" <b>{call.data}</b> \n\n<b>Намаз уақыты:</b> \n\n Таң намазы: {answer['fajr']} \n Күн шығуы: {answer['sunrise']} \n Бесін: {answer['dhuhr']} \n Аср: {answer['asr']} \n <b><u>Ақшам: {answer['maghrib']}</u></b> \n Құптан: {answer['isha']}\n\n<b>Қазір Ақшам намазының уақыты,қаза қылдырмай оқып үлгерініз!!!</b>")
    else:
        return call.message.answer(f" <b>{call.data}</b> \n\n<b>Намаз уақыты: </b> \n\n Таң намазы: {answer['fajr']} \n Күн шығуы: {answer['sunrise']} \n Бесін: {answer['dhuhr']} \n Аср: {answer['asr']} \n Ақшам: {answer['maghrib']} \n <b><u>Құптан: {answer['isha']}</u></b> \n\n<b>Қазір Құптан намазының уақыты,қаза қылдырмай оқып үлгерініз!!!</b>")

def print_namaz_time_message(inpp,message):
    answer = get_namaz_time(inpp)
    current_time = datetime.datetime.now()
    timer: int = 0
    if get_city(inpp) == '6':
        timer = int((current_time.hour*100)+current_time.minute)
    elif get_city(inpp) == '5':
        timer = int(((current_time.hour-1) * 100) + current_time.minute)
    if del_dot(answer['fajr']) < timer < del_dot(answer['sunrise']):
        return message.answer(f" <b>{inpp}</b> \n\n<b>Намаз уақыты:</b> \n\n <b><u>Таң намазы: {answer['fajr']}</u></b> \n Күн шығуы: {answer['sunrise']} \n Бесін: {answer['dhuhr']} \n Аср: {answer['asr']} \n Ақшам: {answer['maghrib']} \n Құптан: {answer['isha']} \n\n <b>Қазір Таң намазының уақыты,қаза қылдырмай оқып үлгерініз!!!</b>",reply_markup = kb_namaz_time)
    elif del_dot(answer['sunrise']) < timer < del_dot(answer['dhuhr']):
        return message.answer(f" <b>{inpp}</b> \n\n<b>Намаз уақыты:</b> \n\n Таң намазы: {answer['fajr']} \n <b><u>Күн шығуы: {answer['sunrise']} </u></b>\n Бесін: {answer['dhuhr']} \n Аср: {answer['asr']} \n Ақшам: {answer['maghrib']} \n Құптан: {answer['isha']}\n\n<b>Қазір намаз уақыты емес!!!</b>",reply_markup = kb_namaz_time)
    elif del_dot(answer['dhuhr']) < timer < del_dot(answer['asr']):
        return message.answer(f" <b>{inpp}</b> \n\n<b>Намаз уақыты:</b> \n\n Таң намазы: {answer['fajr']} \n Күн шығуы: {answer['sunrise']} \n <b><u>Бесін: {answer['dhuhr']}</u></b> \n Аср: {answer['asr']} \n Ақшам: {answer['maghrib']} \n Құптан: {answer['isha']}\n\n<b>Қазір Бесін намазының уақыты,қаза қылдырмай оқып үлгерініз!!!</b>",reply_markup = kb_namaz_time)
    elif del_dot(answer['asr']) < timer < del_dot(answer['maghrib']):
        return message.answer(f" <b>{inpp}</b> \n\n<b>Намаз уақыты:</b> \n\n Таң намазы: {answer['fajr']} \n Күн шығуы: {answer['sunrise']} \n Бесін: {answer['dhuhr']} \n<b><u> Аср: {answer['asr']} </u></b>\n Ақшам: {answer['maghrib']} \n Құптан: {answer['isha']}\n\n<b>Қазір Аср намазының уақыты,қаза қылдырмай оқып үлгерініз!!!</b>",reply_markup = kb_namaz_time)
    elif del_dot(answer['maghrib']) < timer < del_dot(answer['isha']):
        return message.answer(f" <b>{inpp}</b> \n\n<b>Намаз уақыты:</b> \n\n Таң намазы: {answer['fajr']} \n Күн шығуы: {answer['sunrise']} \n Бесін: {answer['dhuhr']} \n Аср: {answer['asr']} \n <b><u>Ақшам: {answer['maghrib']}</u></b> \n Құптан: {answer['isha']}\n\n<b>Қазір Ақшам намазының уақыты,қаза қылдырмай оқып үлгерініз!!!</b>",reply_markup = kb_namaz_time)
    else:
        return message.answer(f" <b>{inpp}</b> \n\n<b>Намаз уақыты: </b> \n\n Таң намазы: {answer['fajr']} \n Күн шығуы: {answer['sunrise']} \n Бесін: {answer['dhuhr']} \n Аср: {answer['asr']} \n Ақшам: {answer['maghrib']} \n <b><u>Құптан: {answer['isha']}</u></b> \n\n<b>Қазір Құптан намазының уақыты,қаза қылдырмай оқып үлгерініз!!!</b>",reply_markup = kb_namaz_time)

