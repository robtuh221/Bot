import telebot
import random
from telebot import types

token = "5262458335:AAF-geM-B7cRl9nWhJ8WmkZvVGwtiakDCIM"
bot = telebot.TeleBot(token)

movies = [
    "Железный человек (2008)",
    "Невероятный халк (2008)",
    "Железный человек 2 (2010)",
    "Тор (2011)",
    "Первый мститель (2011)",
    "Мстители (2012)",
    "Железный человек 3 (2013)",
    "Тор 2: Царство тьмы (2013)",
    "Первый мститель: Другая война (2014)",
    "Стражи галактики (2014)",
    "Мстители. Эра Альтрона (2015)",
    "Человек-Муравей (2015)",
    "Первый мститель: Противостояние (2016)",
    "Доктор Стрэндж (2016)",
    "Человек-паук: Возвращение домой (2017)",
    "Стражи галактики. Часть 2 (2017)",
    "Тор: Рагнарёк (2017)",
    "Чёрная пантера (2018)",
    "Мстители: Война бесконечности (2018)",
    "Человек-муравей и оса (2018)",
    "Капитал Марвел (2019)",
    "Человек-паук: Вдали от дома (2019)",
    "Мстители: Финал (2019)",
    "Чёрная вдова (2021)",
    "Шан-Чи и легенда десяти колец (2021)",
    "Вечные (2021)",
    "Человек-паук: Нет пути домой (2021)"
]
serials = [
    "ВандаВижн - 9  серий (2021)",
    "Сокол и Зимний солдат - 6 серий (2021)",
    "Локи - 6 серий (2021)",
    "Что Если ...? - 9 серий (2021)",
    "Соколиный глаз - 6 серий (2021)"
]

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.resize_keyboard = True
    keyboard.row("Что посмотреть ?")
    keyboard.row("Все фильмы MARVEL", "Сериалы MARVEL")
    keyboard.row("/help", "/god")
    bot.send_message(message.chat.id, 'Привет! Этот бот знает всё о MARVEL.\nКак я могу тебе помочь?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Этот бот даёт ифнормацию про фильмы и сериалы MARVEL, а также может подсказать что посмотреть из этой киновселенной')


@bot.message_handler(commands=['god'])
def god(message):
    bot.send_message(message.chat.id, """Привет, меня зовут Роберт мне 20. Я сделал этого бота, честно я не очень люблю программировать, но для зачёта можно и потерпеть)
Я поклонник спорта в частности хоккея и большого тенниса. Болею за АкБарс, потому что сам с Татарстана.
Сейчас я действующий радиоведущий на радио ЛОЛ, это молодая интернет станция, ей всего год.
Буду дополнять бота разными штуками, ждите новых обновлений ;)""")


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "все фильмы marvel":
        movie = "Фильмы:\n"
        for index, item in enumerate(movies):
            index += 1
            movie += str(index) + " " + item + "\n"
        bot.send_message(message.chat.id, movie)
    elif message.text.lower() == "сериалы marvel":
        serial = "Сериалы:\n"
        for index, item in enumerate(serials):
            index += 1
            serial += str(index) + " " + item + "\n"
        bot.send_message(message.chat.id, serial)
    elif message.text.lower() == "что посмотреть ?":
        ans = random.choice(movies)
        temp_ans1 = ans
        ans2 = random.choice(serials)
        temp_ans2 = ans2
        if temp_ans1 == ans:
            ans = random.choice(movies)
        if temp_ans2 == ans2:
            ans2 = random.choice(serials)
        bot.send_message(message.chat.id, "Посмотри-ка сегодня: " + ans + ",если хочешь фильм\nили\n" + ans2 + ", если в кайф сериал посмотреть")
    else:
        bot.send_message(message.chat.id, "Извини, я пока не шарю за это 🤷‍♂️")


bot.infinity_polling()


