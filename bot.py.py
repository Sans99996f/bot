from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime

# Расписания для двух недель
schedule_week1 = "Расписание на первую неделю:\n1. Понедельник: Глобальная компетенция, Математика, Информатика\n2. Вторник: Физика, Рус яз,Химия,НВП,Кураторский час\n3. Среда: Рус Лит, Физика, Физ_культ\n4. Четверг:Химия,Рус лит, Каз яз, Математика\n5. Пятница: История Кз, Англ яз, География, Информатика"
schedule_week2 = "Расписание на вторую неделю:\n1. Понедельник: Физ-культ, Математика, Каз яз\n2. Вторник: Англ яз, Рус яз,Химия,НВП,Кураторский час\n3. Среда: Рус яз, Физика, Физ_культ\n4. Четверг:Химия,Рус лит, Каз яз, Математика\n5. Пятница: История Кз, Англ яз, География, Информатика"

# Переменные для хранения ссылки и текста
user_link = "https://wa.me/77789369902"
user_link1 = "https://wa.me/77778246574"

def start(update, context):
    update.message.reply_text('Привет! Я ваш бот куратор. Используйте /help для списка команд.')

def help_command(update, context):
    update.message.reply_text('Доступные команды:\n/start - Запустить бота\n/help - Список команд\n/curator - Куратор\n/headman - Староста\n/schedule - Показать расписание')

def get_schedule(update, context):
    current_week = datetime.now().isocalendar()[1]
    if current_week % 2 == 0:
        schedule = schedule_week2
    else:
        schedule = schedule_week1
    update.message.reply_text(schedule)

def curator(update, context):
    global user_link
    user_link = ' '.join(context.args)
    update.message.reply_text(f'Куратор: {user_link}')

def headman(update, context):
    global user_link1
    user_text = ' '.join(context.args)
    update.message.reply_text(f'Староста: {user_link1}')

def main():
    updater = Updater("7925112330:AAGIU5fV8X_Lnva-AhwWYba0nrzfWCgWmWU", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("schedule", get_schedule))
    dp.add_handler(CommandHandler("curator", curator))
    dp.add_handler(CommandHandler("headman", headman))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()