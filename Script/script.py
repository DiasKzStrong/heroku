import datetime
import requests
import json
from datetime import date

with open(r'C:\Users\eeone\PycharmProjects\pythonProject11\Script\data.json', 'r', encoding='utf-8') as file:
    city_list = json.load(file)


# array = []
# for i in range(len(city_list)):
#     array.append(city_list[i])
def get_namaz_time(inpp):
    c1 = ""
    c2 = ""
    for i in range(len(city_list)):
        if city_list[i]["title"] == inpp:
            c1 = city_list[i]["lat"]
            c2 = city_list[i]["lng"]
    req1 = requests.request("GET", url=f'https://api.muftyat.kz/prayer-times/2022/{c1}/{c2}')
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
        print(timer)
    if del_dot(answer['fajr']) < timer < del_dot(answer['sunrise']):
        return call.message.answer(f" <b>{call.data}</b> \n\n<b>Намаз уақыты:</b> \n\n <u>Таң намазы: {answer['fajr']}</u> \n Күн шығуы: {answer['sunrise']} \n Бесін: {answer['dhuhr']} \n Аср: {answer['asr']} \n Ақшам: {answer['maghrib']} \n Құптан: {answer['isha']} \n\n <b>Қазір Таң намазының уақыты,қаза қылдырмай оқып үлгерініз!!!</b>")
    elif del_dot(answer['sunrise']) < timer < del_dot(answer['dhuhr']):
        return call.message.answer(f" <b>{call.data}</b> \n\n<b>Намаз уақыты:</b> \n\n Таң намазы: {answer['fajr']} \n <u>Күн шығуы: {answer['sunrise']} </u>\n Бесін: {answer['dhuhr']} \n Аср: {answer['asr']} \n Ақшам: {answer['maghrib']} \n Құптан: {answer['isha']}\n\n<b>Қазір намаз уақыты емес!!!</b>")
    elif del_dot(answer['dhuhr']) < timer < del_dot(answer['asr']):
        return call.message.answer(f" <b>{call.data}</b> \n\n<b>Намаз уақыты:</b> \n\n Таң намазы: {answer['fajr']} \n Күн шығуы: {answer['sunrise']} \n <u>Бесін: {answer['dhuhr']}</u> \n Аср: {answer['asr']} \n Ақшам: {answer['maghrib']} \n Құптан: {answer['isha']}\n\n<b>Қазір Бесін намазының уақыты,қаза қылдырмай оқып үлгерініз!!!</b>")
    elif del_dot(answer['asr']) < timer < del_dot(answer['maghrib']):
        return call.message.answer(f" <b>{call.data}</b> \n\n<b>Намаз уақыты:</b> \n\n Таң намазы: {answer['fajr']} \n Күн шығуы: {answer['sunrise']} \n Бесін: {answer['dhuhr']} \n<u> Аср: {answer['asr']} </u>\n Ақшам: {answer['maghrib']} \n Құптан: {answer['isha']}\n\n<b>Қазір Аср намазының уақыты,қаза қылдырмай оқып үлгерініз!!!</b>")
    elif del_dot(answer['maghrib']) < timer < del_dot(answer['isha']):
        return call.message.answer(f" <b>{call.data}</b> \n\n<b>Намаз уақыты:</b> \n\n Таң намазы: {answer['fajr']} \n Күн шығуы: {answer['sunrise']} \n Бесін: {answer['dhuhr']} \n Аср: {answer['asr']} \n <u> Ақшам: {answer['maghrib']}</u> \n Құптан: {answer['isha']}\n\n<b>Қазір Ақшам намазының уақыты,қаза қылдырмай оқып үлгерініз!!!</b>")
    else:
        return call.message.answer(f" <b>{call.data}</b> \n\n<b>Намаз уақыты: </b> \n\n Таң намазы: {answer['fajr']} \n Күн шығуы: {answer['sunrise']} \n Бесін: {answer['dhuhr']} \n Аср: {answer['asr']} \n Ақшам: {answer['maghrib']} \n <u>Құптан: {answer['isha']}</u> \n\n<b>Қазір Құптан намазының уақыты,қаза қылдырмай оқып үлгерініз!!!</b>")

