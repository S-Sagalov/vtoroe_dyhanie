from bot.constants.links import FEEDBACK_LINK, URL_KNOWLEDGE_BASE


STOP_MESSAGE = 'Работа приложения остановлена.'
HELP_MESSAGE = 'Если у тебя есть вопрос, присылай его на почту hr@vtoroe.ru'
START_MESSAGE_PART_ONE = (
    'Привет! Меня зовут Втордыш, '
    'и я помощник сотрудников Фонда ВТОРОЕ ДЫХАНИЕ. '
    'Я создан для того, чтобы помочь новеньким адаптироваться, '
    'но также буду полезен и опытным сотрудникам.'
)
START_MESSAGE_PART_TWO = "Чтобы продолжить, введи секретное слово."
FAILED_THE_TEST = (
    'У нас другое секретное слово. '
    'Попробуй ввести его еще раз '
    'или обратись в HR-отдел Фонда или на почту hr@vtoroe.ru.'
)
KNOWLEDGE_BASE_MESSAGE = (
    'Чтобы вся важная и нужная в работе информация была в одном месте, мы'
    rf' создали [Базу знаний]({URL_KNOWLEDGE_BASE}) для сотрудников\.'
    r' В ней собраны регламенты и бизнес\-процессы, по которым мы работаем\.'
)
PASSED_THE_TEST = (
    'Верно! Выбери интересующую тебя тему из списка '
    'в меню, и я помогу тебе найти нужную информацию.'
)

STICKER_ID = (
    'CAACAgIAAxkBAAIDwGUEItYpuU5DXDRigDA1M9SL-AdcAALTJAACHRAwSj-yFNWnj6hDMAQ'
)

FEEDBACK_MESSAGE = (
    'Мы сделали анонимную форму обратной связи для сотрудников Фонда — для '
    'тех, кто работает в бэк\\-офисе, на складах в Москве и Костроме, '
    'в мастерской и в Центре гуманитарной выдачи\\.\n\n'
    'Сообщить о проблеме, поделиться информацией или оставить иную обратную '
    'связь, если ты не хочешь сообщать ее лично, можно по '
    f'[ссылке]({FEEDBACK_LINK})\\.'
)

# Для возвращения в меню раздела
BACK_TO_MENU = 'Выбери интересующую тебя тему из списка:'

PERMISSION_ERROR_MESSAGE = (
    'У вас нет доступа к этому боту.\n' 'Начните с команды /start.'
)
