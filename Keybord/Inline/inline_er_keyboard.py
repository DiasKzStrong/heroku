from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

inline_tan = InlineKeyboardMarkup(row_width=3,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='2 рәкәт сүннет', web_app=WebAppInfo(
                                              url='https://muslim.kz/kz/namaz/man/4'))

                                      ],
                                      [

                                          InlineKeyboardButton(text='2 рәкәт парыз', web_app=WebAppInfo(
                                              url='https://muslim.kz/kz/namaz/man/5'))
                                      ]
                                  ]

                                  )

inline_besin = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='4 рәкәт сүннет', web_app=WebAppInfo(
                                                url='https://muslim.kz/kz/namaz/man/6'))

                                        ],
                                        [

                                            InlineKeyboardButton(text='4 рәкәт парыз', web_app=WebAppInfo(
                                                url='https://muslim.kz/kz/namaz/man/7'))
                                        ],
                                        [

                                            InlineKeyboardButton(text='2 рәкәт сүннет', web_app=WebAppInfo(
                                                url='https://muslim.kz/kz/namaz/man/8'))

                                        ]
                                    ]
                                    )
inline_ekinti = InlineKeyboardMarkup(row_width=3,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardButton(text='4 рәкәт парыз', web_app=WebAppInfo(
                                                 url='https://muslim.kz/kz/namaz/man/9'))

                                         ]

                                     ]

                                     )
inline_aksham = InlineKeyboardMarkup(row_width=3,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardButton(text='3 рәкәт парыз', web_app=WebAppInfo(
                                                 url='https://muslim.kz/kz/namaz/man/10'))

                                         ],
                                         [

                                             InlineKeyboardButton(text='2 рәкәт сүннет', web_app=WebAppInfo(
                                                 url='https://muslim.kz/kz/namaz/man/11'))
                                         ]
                                     ]

                                     )
inline_kuptan = InlineKeyboardMarkup(row_width=3,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardButton(text='4 рәкәт парыз', web_app=WebAppInfo(
                                                 url='https://muslim.kz/kz/namaz/man/12'))

                                         ],
                                         [

                                             InlineKeyboardButton(text='2 рәкәт сүннет', web_app=WebAppInfo(
                                                 url='https://muslim.kz/kz/namaz/man/14'))
                                         ]
                                     ]

                                     )
inline_utir = InlineKeyboardMarkup(row_width=3,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(text='3 рәкәт уәжіп', web_app=WebAppInfo(
                                               url='https://muslim.kz/kz/namaz/man/15'))

                                       ]
                                   ]

                                   )

inline_wudu = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Дарет алып уйрену', web_app=WebAppInfo(url='https://muslim.kz/kz/namaz/man/2'))]
])
inline_ulken_wudu = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Ғұсыл алып үйрену', web_app=WebAppInfo(url='https://muslim.kz/kz/namaz/man/1'))]
])

inline_Quran = InlineKeyboardMarkup(
    inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            InlineKeyboardButton(
                        text = "Құран☪️",web_app=WebAppInfo(url = 'https://kitap.kuran.kz/#!/bet/1/kk')
                                )
                        ]
    )
)