from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
zhynys_menu = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text="Ер адам🧔🏻‍♂️")
        ],
        [
            KeyboardButton(text="Әйел адам🧕🏻")
        ]
    ],
)

kb_er_menu = ReplyKeyboardMarkup(

    keyboard=
    [
        [
            KeyboardButton(text='Намаз окып уйрену🧔🏻‍♂️')
        ],
        [
            KeyboardButton(text='Дарет алып уйрену🧔🏻‍♂️',web_app=WebAppInfo(url='https://muslim.kz/kz/namaz/man/2')),
            KeyboardButton(text='Ғұсыл алып үйрену🧔🏻‍♂️',web_app=WebAppInfo(url='https://muslim.kz/kz/namaz/man/1')),
            KeyboardButton(text='Құран☪️',web_app=WebAppInfo(url ='https://kitap.kuran.kz/#!/bet/1/kk')),
            KeyboardButton(text='Намаз уакыты🕌')

        ],
        [
            KeyboardButton(text="Қайта тіркелу◀️")
        ]
    ]

)

kb_er_menu_namaz = ReplyKeyboardMarkup(keyboard=
[
    [
        KeyboardButton(text='Таң намазы🧔🏻‍♂️'),
        KeyboardButton(text='Бесін намазы🧔🏻‍♂️')
    ], [

    KeyboardButton(text='Екінті намазы🧔🏻‍♂️'),
    KeyboardButton(text='Ақшам намазы🧔🏻‍♂️')
], [
    KeyboardButton(text='Құптан намазы🧔🏻‍♂️'),
    KeyboardButton(text='Үтір намазы🧔🏻‍♂️')
],
    [
        KeyboardButton(text="Менюға артқа қайту◀️")
    ]
]

)

kb_ayel_menu = ReplyKeyboardMarkup(

    keyboard=
    [
        [
            KeyboardButton(text='Намаз окып уйрену🧕🏻')
        ],
        [
            KeyboardButton(text='Дарет алып уйрену🧕🏻',web_app=WebAppInfo(url ='https://muslim.kz/kz/namaz/woman/2')),
            KeyboardButton(text='Ғұсыл алып үйрену🧕🏻',web_app=WebAppInfo(url ='https://muslim.kz/kz/namaz/woman/1')),
            KeyboardButton(text='Құран☪️',web_app = WebAppInfo(url ='https://kitap.kuran.kz/#!/bet/1/kk')),
            KeyboardButton(text='Намаз уакыты🕌')

        ],
        [
            KeyboardButton(text="Қайта тіркелу⏪️")
        ]
    ]

)

kb_ayel_menu_namaz = ReplyKeyboardMarkup(keyboard=
[
    [
        KeyboardButton(text='Таң намазы🧕🏻'),
        KeyboardButton(text='Бесін намазы🧕🏻')
    ], [

    KeyboardButton(text='Екінті намазы🧕🏻'),
    KeyboardButton(text='Ақшам намазы🧕🏻')
], [
    KeyboardButton(text='Құптан намазы🧕🏻'),
    KeyboardButton(text='Үтір намазы🧕🏻')
],
    [
        KeyboardButton(text="Менюға артқа қайту⏪️")
    ]
]

)


kb_namaz_time = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="Қаланы өзгерту")
        ],
        [
            KeyboardButton(text="Менюға артқа қайту◀")
        ]

    ],
    resize_keyboard=True


)