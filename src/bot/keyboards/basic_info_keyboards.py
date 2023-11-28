from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.constants.query_patterns import INFO_PREFIX
from bot.utils.admin_api import get_django_json


# 1. Клавиатура для подраздела "основная информация"
async def basic_information_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/basic_info_keyboards/1:4/')
    result = [
        [
            InlineKeyboardButton(
                messages['basic_information_keyboard_organization_structure'],
                callback_data=f'{INFO_PREFIX}organization_structure',
            )
        ],
        [
            InlineKeyboardButton(
                messages['basic_information_keyboard_our_team'],
                callback_data=f'{INFO_PREFIX}our_team'
            )
        ],
        [
            InlineKeyboardButton(
                messages['basic_information_keyboard_social_networks'],
                callback_data=f'{INFO_PREFIX}social_networks'
            )
        ],
        [
            InlineKeyboardButton(
                messages['basic_information_keyboard_back_to_main_menu'],
                callback_data='back_to_main_menu'
            )
        ],
    ]
    return InlineKeyboardMarkup(result)


# 2. Клавиатура для 'organization_structure'
async def org_structure_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/basic_info_keyboards/5:9/')
    org_structure_keyboard = [
        [
            InlineKeyboardButton(
                messages['org_structure_keyboard_council'],
                callback_data=f'{INFO_PREFIX}council'
            )
        ],
        [
            InlineKeyboardButton(
                messages['org_structure_keyboard_guardian_council'],
                callback_data=f'{INFO_PREFIX}guardian_council',
            )
        ],
        [
            InlineKeyboardButton(
                messages['org_structure_keyboard_about_departments'],
                callback_data=f'{INFO_PREFIX}about_departments'
            )
        ],
        [
            InlineKeyboardButton(
                messages['org_structure_keyboard_basic_information_back'],
                callback_data='basic_information_back'
            )
        ],
        [
            InlineKeyboardButton(
                messages['org_structure_keyboard_back_to_main_menu'],
                callback_data='back_to_main_menu'
            )
        ],
    ]
    return InlineKeyboardMarkup(org_structure_keyboard)


# 3. Клавиатура для "Наша команда"
async def our_team_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/basic_info_keyboards/10:13/')
    our_team_keyboard = [
        [
            InlineKeyboardButton(
                messages['our_team_keyboard_contact_list'],
                callback_data=f'{INFO_PREFIX}contact_list'
            )
        ],
        [
            InlineKeyboardButton(
                messages['our_team_keyboard_org_departmentss'],
                callback_data=f'{INFO_PREFIX}org_departmentss'
            )
        ],
        [
            InlineKeyboardButton(
                messages['our_team_keyboard_basic_information_back'],
                callback_data='basic_information_back')
        ],
        [
            InlineKeyboardButton(
                messages['our_team_keyboard_back_to_main_menu'],
                callback_data='back_to_main_menu'
            )
        ],
    ]
    return InlineKeyboardMarkup(our_team_keyboard)


# 4. Клавиатура для "Соцсети Фонда"
async def social_networks_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/basic_info_keyboards/14:15/')
    social_networks_keyboard = [
        [
            InlineKeyboardButton(
                messages['social_networks_keyboard_basic_information_back'],
                callback_data='basic_information_back'
            )
        ],
        [
            InlineKeyboardButton(
                messages['social_networks_keyboard_back_to_main_menu'],
                callback_data='back_to_main_menu'
            )
        ],
    ]
    return InlineKeyboardMarkup(social_networks_keyboard)


# 5. Клавиатура для "Совет Фонда"
async def council_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/basic_info_keyboards/16:23/')
    council_keyboard = [
        [
            InlineKeyboardButton(
                messages['council_keyboard_council_question_01'],
                callback_data=f'{INFO_PREFIX}council_question_01',
            )
        ],
        [
            InlineKeyboardButton(
                messages['council_keyboard_council_question_02'],
                callback_data=f'{INFO_PREFIX}council_question_02',
            )
        ],
        [
            InlineKeyboardButton(
                messages['council_keyboard_council_question_03'],
                callback_data=f'{INFO_PREFIX}council_question_03',
            )
        ],
        [
            InlineKeyboardButton(
                messages['council_keyboard_council_question_04'],
                callback_data=f'{INFO_PREFIX}council_question_04',
            )
        ],
        [
            InlineKeyboardButton(
                messages['council_keyboard_council_question_05'],
                callback_data=f'{INFO_PREFIX}council_question_05',
            )
        ],
        [
            InlineKeyboardButton(
                messages['council_keyboard_council_question_06'],
                callback_data=f'{INFO_PREFIX}council_question_06',
            )
        ],
        [
            InlineKeyboardButton(
                messages['council_keyboard_organization_structure'],
                callback_data=f'{INFO_PREFIX}organization_structure'
            )
        ],
        [
            InlineKeyboardButton(
                messages['council_keyboard_back_to_main_menu'],
                callback_data='back_to_main_menu'
            )
        ],
    ]
    return InlineKeyboardMarkup(council_keyboard)


# 6. Клавиатура для возвратов из раздела о департаментах
async def departments_final_markup():
    messages = await get_django_json(
        'http://127.0.0.1:8000/basic_info_keyboards/36:37/')
    departments_final_keyboard = [
        [
            InlineKeyboardButton(
                messages['departments_final_keyboard_back_to_main_menu'],
                callback_data='back_to_main_menu'
            )
        ],
        [
            InlineKeyboardButton(
                messages['departments_final_keyboard_about_departments'],
                callback_data=f'{INFO_PREFIX}about_departments'
            )
        ],
    ]
    return InlineKeyboardMarkup(departments_final_keyboard)


# 7. Клавиатура для "Отделы Фонда"
async def func_departments_keyboard_base():
    messages = await get_django_json(
        'http://127.0.0.1:8000/basic_info_keyboards/22:33/')
    departments_keyboard_base = [
        [
            InlineKeyboardButton(
                messages['departments_keyboard_base_department_01'],
                callback_data=f'{INFO_PREFIX}department_01',
            )
        ],
        [
            InlineKeyboardButton(
                messages['departments_keyboard_base_department_02'],
                callback_data=f'{INFO_PREFIX}department_02',
            )
        ],
        [
            InlineKeyboardButton(
                messages['departments_keyboard_base_department_03'],
                callback_data=f'{INFO_PREFIX}department_03',
            )
        ],
        [
            InlineKeyboardButton(
                messages['departments_keyboard_base_department_04'],
                callback_data=f'{INFO_PREFIX}department_04',
            )
        ],
        [
            InlineKeyboardButton(
                messages['departments_keyboard_base_department_05'],
                callback_data=f'{INFO_PREFIX}department_05',
            )
        ],
        [
            InlineKeyboardButton(
                messages['departments_keyboard_base_department_06'],
                callback_data=f'{INFO_PREFIX}department_06',
            )
        ],
        [
            InlineKeyboardButton(
                messages['departments_keyboard_base_department_07'],
                callback_data=f'{INFO_PREFIX}department_07',
            )
        ],
        [
            InlineKeyboardButton(
                messages['departments_keyboard_base_department_08'],
                callback_data=f'{INFO_PREFIX}department_08',
            )
        ],
        [
            InlineKeyboardButton(
                messages['departments_keyboard_base_department_09'],
                callback_data=f'{INFO_PREFIX}department_09',
            )
        ],
        [
            InlineKeyboardButton(
                messages['departments_keyboard_base_department_10'],
                callback_data=f'{INFO_PREFIX}department_10',
            )
        ],
        [
            InlineKeyboardButton(
                messages['council_keyboard_organization_structure'],
                callback_data=f'{INFO_PREFIX}organization_structure'
            )
        ],
        [
            InlineKeyboardButton(
                messages['council_keyboard_back_to_main_menu'],
                callback_data='back_to_main_menu'  # ?
            )
        ],
    ]
    return InlineKeyboardMarkup(departments_keyboard_base)


# 7.5. Клавиатура для 'departmentss'
async def departmentss_markup():
    # response = requests.get(
    #     'http://127.0.0.1:8000/basic_info_keyboards/24:39/')
    messages = await get_django_json(
        'http://127.0.0.1:8000/basic_info_keyboards/24:39/')
    departments_keyboard = [
            [
                InlineKeyboardButton(
                    messages['departments_keyboard_base_department_01'],
                    callback_data=f'{INFO_PREFIX}department_01',
                )
            ],
            [
                InlineKeyboardButton(
                    messages['departments_keyboard_base_department_02'],
                    callback_data=f'{INFO_PREFIX}department_02',
                )
            ],
            [
                InlineKeyboardButton(
                    messages['departments_keyboard_base_department_03'],
                    callback_data=f'{INFO_PREFIX}department_03',
                )
            ],
            [
                InlineKeyboardButton(
                    messages['departments_keyboard_base_department_04'],
                    callback_data=f'{INFO_PREFIX}department_04',
                )
            ],
            [
                InlineKeyboardButton(
                    messages['departments_keyboard_base_department_05'],
                    callback_data=f'{INFO_PREFIX}department_05',
                )
            ],
            [
                InlineKeyboardButton(
                    messages['departments_keyboard_base_department_06'],
                    callback_data=f'{INFO_PREFIX}department_06',
                )
            ],
            [
                InlineKeyboardButton(
                    messages['departments_keyboard_base_department_07'],
                    callback_data=f'{INFO_PREFIX}department_07',
                )
            ],
            [
                InlineKeyboardButton(
                    messages['departments_keyboard_base_department_08'],
                    callback_data=f'{INFO_PREFIX}department_08',
                )
            ],
            [
                InlineKeyboardButton(
                    messages['departments_keyboard_base_department_09'],
                    callback_data=f'{INFO_PREFIX}department_09',
                )
            ],
            [
                InlineKeyboardButton(
                    messages['departments_keyboard_base_department_10'],
                    callback_data=f'{INFO_PREFIX}department_10',
                )
            ],
            [
                InlineKeyboardButton(
                    messages['departmentss_keyboard_our_team'],
                    callback_data=f'{INFO_PREFIX}our_team'  # ?
                )
            ],
            [
                InlineKeyboardButton(
                    messages['departmentss_keyboard_back_to_main_menu'],
                    callback_data='back_to_main_menu'
                )
            ],
        ]
    return InlineKeyboardMarkup(departments_keyboard)


# 8. Клавиатура для 'guardian_council'
async def guardian_council_markup():
    # response = requests.get('http://127.0.0.1:8000/basic_info_keyboards/34/')
    messages = await get_django_json(
        'http://127.0.0.1:8000/basic_info_keyboards/34/')
    guardian_council_keyboard = [
        [
            InlineKeyboardButton(
                messages['guardian_council_keyboard'],
                callback_data=f'{INFO_PREFIX}organization_structure',
            )
        ],
    ]
    return InlineKeyboardMarkup(guardian_council_keyboard)


# 9. Клавиатуры для 'contact_list'
contact_list_download_keyboard = [
    (
        InlineKeyboardButton(
            'Скачать справочник',
            url='https://docs.google.com/spreadsheets/d/'
            '1m_y8rtod0VEGBAmhmqxK3ax-ulOUfeJNlvMApluhBFM/edit',
        ),
    ),
]
contact_list_download_markup = InlineKeyboardMarkup(
    contact_list_download_keyboard
)
contact_list_exit_keyboard = [
    (
        InlineKeyboardButton(
            'В главное меню', callback_data='exit_from_contact_search'
        ),
    ),
]
contact_list_exit_markup = InlineKeyboardMarkup(contact_list_exit_keyboard)


# from feature33
# async def contact_list_markup():
#     # response = requests.get('http://127.0.0.1:8000/basic_info_keyboards/35/')
#     messages = await get_django_json(
#         'http://127.0.0.1:8000/basic_info_keyboards/35/')
#     contact_list_keyboard = [
#         [
#             InlineKeyboardButton(
#                messages['contact_list_keyboard'],
#                url='https://docs.google.com/spreadsheets/d/'
#                '1m_y8rtod0VEGBAmhmqxK3ax-ulOUfeJNlvMApluhBFM/edit',
#             ),
#         ],
#     ]
#     return InlineKeyboardMarkup(contact_list_keyboard)
