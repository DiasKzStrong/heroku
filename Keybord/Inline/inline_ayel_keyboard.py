from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

inline_ayel_tan = InlineKeyboardMarkup(row_width=3,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='2 рәкәт сүннет', web_app=WebAppInfo(
                                              url='https://muslim.kz/kz/namaz/woman/4'))

                                      ],
                                      [

                                          InlineKeyboardButton(text='2 рәкәт парыз', web_app=WebAppInfo(
                                              url='https://muslim.kz/kz/namaz/woman/5'))
                                      ]
                                  ]

                                  )

inline_ayel_besin = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='4 рәкәт сүннет', web_app=WebAppInfo(
                                                url='https://muslim.kz/kz/namaz/woman/6'))

                                        ],
                                        [

                                            InlineKeyboardButton(text='4 рәкәт парыз', web_app=WebAppInfo(
                                                url='https://muslim.kz/kz/namaz/woman/7'))
                                        ],
                                        [

                                            InlineKeyboardButton(text='2 рәкәт сүннет', web_app=WebAppInfo(
                                                url='https://muslim.kz/kz/namaz/woman/8'))

                                        ]
                                    ]
                                    )
inline_ayel_ekinti = InlineKeyboardMarkup(row_width=3,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardButton(text='4 рәкәт парыз', web_app=WebAppInfo(
                                                 url='https://muslim.kz/kz/namaz/woman/9'))

                                         ]

                                     ]

                                     )
inline_ayel_aksham = InlineKeyboardMarkup(row_width=3,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardButton(text='3 рәкәт парыз', web_app=WebAppInfo(
                                                 url='https://muslim.kz/kz/namaz/woman/10'))

                                         ],
                                         [

                                             InlineKeyboardButton(text='2 рәкәт сүннет', web_app=WebAppInfo(
                                                 url='https://muslim.kz/kz/namaz/woman/11'))
                                         ]
                                     ]

                                     )
inline_ayel_kuptan = InlineKeyboardMarkup(row_width=3,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardButton(text='4 рәкәт парыз', web_app=WebAppInfo(
                                                 url='https://muslim.kz/kz/namaz/woman/12'))

                                         ],
                                         [

                                             InlineKeyboardButton(text='2 рәкәт сүннет', web_app=WebAppInfo(
                                                 url='https://muslim.kz/kz/namaz/woman/14'))
                                         ]
                                     ]

                                     )
inline_ayel_utir = InlineKeyboardMarkup(row_width=3,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(text='3 рәкәт уәжіп', web_app=WebAppInfo(
                                               url='https://muslim.kz/kz/namaz/woman/15'))

                                       ]
                                   ]

                                   )

inline_ayel_wudu = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Дарет алып уйрену', web_app=WebAppInfo(url='https://muslim.kz/kz/namaz/woman/2'))]
])
inline_ayel_ulken_wudu = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Ғұсыл алып үйрену', web_app=WebAppInfo(url='https://muslim.kz/kz/namaz/woman/1'))]
])
