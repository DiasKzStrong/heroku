from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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
            KeyboardButton(text='Дарет алып уйрену🧔🏻‍♂️'),
            KeyboardButton(text='Ғұсыл алып үйрену🧔🏻‍♂️'),
            KeyboardButton(text='Құран☪️'),
            KeyboardButton(text='Намаз уакыты🕌')

        ],
        [
            KeyboardButton(text="Артқа қайту◀️")
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
            KeyboardButton(text='Дарет алып уйрену🧕🏻'),
            KeyboardButton(text='Ғұсыл алып үйрену🧕🏻'),
            KeyboardButton(text='Құран☪️'),
            KeyboardButton(text='Намаз уакыты🕌')

        ],
        [
            KeyboardButton(text="Артқа қайту⏪️")
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
            KeyboardButton(text="Менюға артқа қайту◀️")
        ]

    ],
    resize_keyboard=True,
    one_time_keyboard=True


)