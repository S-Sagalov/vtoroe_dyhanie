from bot.constants.links import PROCESSES_LINK

STOP_MESSAGE = "Работа приложения остановлена."
HELP_MESSAGE = "Написать в поддержку"
START_MESSAGE = (
    "Привет! Меня зовут Втордыш,"
    "и я помощник сотрудников фонда ВТОРОЕ ДЫХАНИЕ. "
    "Я создан для того, чтобы помочь новеньким адаптироваться, "
    "но также буду полезен и опытным сотрудникам.\n"
    "Чтобы продолжить, введи секретное слово."
)
FAILED_THE_TEST = (
    "У нас другое секретное слово."
    "Попробуй ввести его еще раз "
    "или обратись в HR-отдел Фонда или на почту hr@vtoroe.ru."
)
PASSED_THE_TEST = (
    "Верно! Выбери интересующую тебя тему из списка "
    "в меню и я помогу тебе найти нужную информацию."
)
STICKER_ID: str = (
    "CAACAgIAAxkBAAIDwGUEItYpuU5DXDRigDA1M9SL-AdcAALTJAACHRAwSj-yFNWnj6hDMAQ"
)
ABOUT_FUND_HISTORY = {
    'part_1': 'Для начала немного предыстории 👀',
    'part_2': (
        'Весной 2013 года во дворе собора St. Andrews прошла '
        'благотворительная распродажа в поддержку Центра равных '
        'возможностей «Вверх». Несколько девушек собрали свою '
        'одежду и продали её, а вырученные средства направили в «Вверх». '
        'С этой акции началась наша история – спустя год её инициатор '
        ' Дарья Алексеева открыла постоянно работающий '
        'магазин Charity Shop, а еще спустя год в ноябре 2015 года был '
        'зарегистрирован фонд ВТОРОЕ ДЫХАНИЕ.'
    ),
    'part_3': (
        'Сегодня фонд Второе дыхание – это крупнейшая некоммерческая '
        'организация в России, занимающаяся сбором, сортировкой, '
        'перераспределением и переработкой одежды на любой стадии ее жизни.'
    )
}

FUND_MISSION = {
    'part_1': 'Здорово, что тебе интересно! Начну рассказ с важных цифр.',
    'part_2': (
        'Ежегодно в России выбрасывают от 60 до 70 миллионов тонн твердых '
        'бытовых отходов. Одежда и текстильные отходы составляют от 3 до 7% '
        'на мусорных полигонах – то есть по меньшей мере 2 миллиона тонн '
        'одежды ежегодно оказывается на свалках. Одежда разлагается до 200 '
        'лет, и в процессе выделяет метан, загрязняет почву и грунтовые воды '
        'и увеличивает объем мусорных полигонов. 😔'
    ),
    'part_3': (
        'Фонд ВТОРОЕ ДЫХАНИЕ старается предотвратить попадание одежды на '
        'полигоны и создаёт инфраструктуру приема ненужных вещей, которые '
        'при грамотном и эффективном использовании могут стать ценным '
        'ресурсом для решения социальных и экологических проблем.'
    ),
    'part_4': (
        'Мы стремимся к развитию системы повторного использования и '
        'переработки текстиля с 1% (столько собиралось в стране в 2022 '
        'году от общей массы выброшенного) до 50%.'
    ),
    'part_5': (
        'Наша миссия – ОСОЗНАННОЕ ПОТРЕБЛЕНИЕ КАК ОБРАЗ ЖИЗНИ.'
    ),
    'part_6': (
        'Хочешь узнать, куда направляются вещи, которые сдают в Фонд?'
    )
}

BACK_TO_MENU = 'Выбери интересующую тебя тему из списка:'

THINGS_PATH = {
    'part_1': 'Мы дарим старым вещам новую жизнь несколькими способами👇',
    'part_2': (
        'Вещи, собранные Фондом и пригодные к повторному использованию, '
        'передаются на благотворительность – нуждающимся семьям и людям, '
        'попавшим в сложную жизненную ситуацию. Мы оказываем '
        'благотворительную помощь в сотрудничестве с организациями, '
        'которые работают с людьми, нуждающимися в поддержке, а также фондами '
        'по защите животных и социальным учреждениями.'
    ),
    'part_3': (
        'Часть вещей продается в магазинах ВТОРОЕ ДЫХАНИЕ (Charity Shop) '
        'в Москве, Ярославле, Костроме, Ростове Великом. Магазины нужны '
        'для обеспечения собственных нужд фонда, выплаты заработной платы '
        'сотрудникам и аренды помещений.'
    ),
    'part_4': (
        'Одежда, непригодная для дальнейшей носки, '
        'отправляется на переработку.'
    ),
    'part_5': (
        'Показать, как выглядит анатомия процессов в Фонде, '
        'чтобы было нагляднее?'
    )
}

PROCESS_ANATOMY = (
    'Иногда лучше 1 раз увидеть, чем 100 раз услышать, да?😄'
    'Посмотри, '
    f'*[как устроен процесс работы с одеждой]({PROCESSES_LINK}) '
    'в Фонде\.\n'
    'Рассказать какие еще проекты реализует наш Фонд?*'
)
