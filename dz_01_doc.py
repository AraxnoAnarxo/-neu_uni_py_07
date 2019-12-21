# 1) Вручную создать текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).

# f = open('data_event.txt')
# content = f.read()
# print(content)
# f.close

with open ('data_event.txt') as f:
    content = f.read()
    print(content)

# 2) Создать doc шаблон, где будут использованы данные параметры.
# 3) Автоматически сгенерировать отчет о машине в формате doc (как в видео 7.2).

import datetime
import time

from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

def get_context(event, city, date, band_name, band_lineup, duration, set, price):
    return {
        'event': event,
        'city': city,
        'date': date,
        'band_name': band_name,
        'band_lineup': band_lineup,
        'duration': duration,
        'set': set,
        'price': price
    }

def from_template(event, city, date, band_name, band_lineup, duration, set, price, template, signature):
    template = DocxTemplate(template)
    context = get_context(event, city, date, band_name, band_lineup, duration, set, price)

    img_size = Cm(10)  # sets the size of the image
    my_pic = InlineImage(template, signature, img_size)

    context['my_pic'] = my_pic  # adds the InlineImage object to the context

    template.render(context)
    template.save('music_performance' + '_' + str(datetime.datetime.now().date()) + '_offer.docx')

def generate_report(event, city, date, band_name, band_lineup, duration, set, price):
    template = 'my_band_wishlist.docx'
    signature = 'my_pic.png'
    document = from_template(event, city, date, band_name, band_lineup, duration, set,  price, template, signature)

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

start = time.clock()
generate_report('wedding', 'Moscow', '31.01.2020', 'ACDC', ['vocalist', 'lead guitarist', 'rhytm guitarist', 'bassist', 'drummer'], 3 , ["Hard As A Rock",
"Rock N Roll Train", "Stiff Upper Lip",
"Dirty Deeds Done Dirt Cheap",
"For Those About To Rock (We Salute You)",
"Thunderstruck", "Satellite Blues",
"Cover You In Oil", "Let's Get It Up",
"Highway To Hell", "Are You Ready",
"Back In Black", "Safe In New York City",
"You Shook Me All Night Long",
"Ballbreaker", "Flick Of The Switch",
"That's The Way I Wanna Rock N Roll",
"Rock Or Bust", "Anything Goes",
"Guns For Hire", "Put The Finger On You",
"Hell's Bells", "T.N.T.", "Shoot To Thrill",
"Who Made Who", "Heatseeker",
"Have A Drink On Me", "Moneytalks",
"Dirty Eyes", "Big Jack", "Play Ball",
"Big Balls", "Big Gun", "Jail Break",
"Meltdown"], 1000000000)
stop = time.clock()
time_gen = stop - start
print(time_gen)

#generate_report('business meeting', 'Kiev', '01.01.2020', 'Verka Serduchka', ['vocalist', 'keyborad player'], 2, ['Dancing Lasha Tumbai', 'Toy', 'Bohemian Rhapsody', 'Dolce Gabanna', 'Trali Vali'], 280000 )


#4) Создать csv файл с данными.

import csv

# csv.writer
event_data = [['event', 'city', 'date', 'band_name', 'band_lineup', 'duration', 'set', 'price'],['wedding', 'Moscow', '31.01.2020', 'ACDC', ['vocalist', 'lead guitarist', 'rhytm guitarist', 'bassist', 'drummer'], 3 , ["Hard As A Rock",
"Rock N Roll Train", "Stiff Upper Lip",
"Dirty Deeds Done Dirt Cheap",
"For Those About To Rock (We Salute You)",
"Thunderstruck", "Satellite Blues",
"Cover You In Oil", "Let's Get It Up",
"Highway To Hell", "Are You Ready",
"Back In Black", "Safe In New York City",
"You Shook Me All Night Long",
"Ballbreaker", "Flick Of The Switch",
"That's The Way I Wanna Rock N Roll",
"Rock Or Bust", "Anything Goes",
"Guns For Hire", "Put The Finger On You",
"Hell's Bells", "T.N.T.", "Shoot To Thrill",
"Who Made Who", "Heatseeker",
"Have A Drink On Me", "Moneytalks",
"Dirty Eyes", "Big Jack", "Play Ball",
"Big Balls", "Big Gun", "Jail Break",
"Meltdown"], 1000000000],['business meeting', 'Kiev', '01.01.2020', 'Verka Serduchka', ['vocalist', 'keyborad player'], 2, ['Dancing Lasha Tumbai', 'Toy', 'Bohemian Rhapsody', 'Dolce Gabanna', 'Trali Vali'], 280000]]

with open('music_for_event' + '_' + str(time_gen) + '.csv', 'w') as f:
    writer = csv.writer(f, delimiter = '&') #
    writer.writerows(event_data)
print('Writing complete!')



# 5) Создать json файл с данными.

import json

dict_event = {'event': 'wedding', 'city': 'Moscow', 'date': '31.01.2020', 'band_name': 'ACDC', 'band_lineup': ['vocalist', 'lead guitarist', 'rhytm guitarist', 'bassist', 'drummer'], 'duration': 3, 'set': ["Hard As A Rock", "Rock N Roll Train", "Stiff Upper Lip", "Dirty Deeds Done Dirt Cheap", "For Those About To Rock (We Salute You)", "Thunderstruck"], 'price': 1000000000}

#dump, dumps

dict_event_to_json = json.dumps(dict_event)

print(type(dict_event_to_json), dict_event_to_json)

with open('dict_event_to_json' + str(time_gen), 'w') as f:
    json.dump(dict_event, f)

#load, loads

# with open('dict_event_to_json') as f:
#     data = json.load(f)
#
# print(data)