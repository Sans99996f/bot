from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from datetime import datetime

# Расписания для двух недель
schedule_week1 = 'Расписание на эту неделю!\n \nПонедельник:\nГлобальные компетенции, 713\nМатематика, 303Г\nИнформатика, 611\n \nВторник:\nКураторский час, 303А\nФизика, 303А\nРусский язык, 503А\nХимия, 411\nНВП, 702\n \nСреда:\nРусская литература, 706\nФизика, 303А\nФиз-культура, манеж\n \nЧетверг:\nХимия, 411\nРусская литература, 706\nКазхский язык, 409/304\nМатематика, 303Г\n \nПятница:\nИстория Казахстана, 716\nАнглийский язык, 704/700\nГеография, 717\nИнформатика, 611'
schedule_week2 = 'Расписание на эту неделю!\n \nПонедельник:\nФиз-культура, спорт зал\nМатематика, 303Г\nКазахский язык, 409/304\n \nВторник:\nКураторский час, 305\nАнглийский язык, 704/700\nРусский язык, 503А\nХимия, 411\nНВП, 702\n \nСреда:\nРусский язык, 503А\nФизика, 303А\nФиз-культура, манеж\n \nЧетверг:\nХимия, 411\nРусская литература, 706\nКазхский язык, 409/304\nМатематика, 303Г\n \nПятница:\nИстория Казахстана, 716\nАнглийский язык, 704/700\nГеография, 717\nИнформатика, 611'
# Переменные для хранения ссылки и текста
user_link = "https://wa.me/77789369902"
user_link1 = "https://wa.me/77778246574"

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Помощь", callback_data='help')],
        [InlineKeyboardButton("Расписание", callback_data='schedule')],
        [InlineKeyboardButton("Куратор", callback_data='curator')],
        [InlineKeyboardButton("Староста", callback_data='headman')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Привет! Я ваш бот куратор. Используйте кнопки ниже для выбора команды.', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'help':
        query.edit_message_text(text='Доступные команды:\n/start - Запустить бота\n/help - Список команд\n/curator - Куратор\n/headman - Староста\n/schedule - Показать расписание')
    elif query.data == 'schedule':
        current_week = datetime.now().isocalendar()[1]
        if current_week % 2 == 0:
            schedule = schedule_week2
        else:
            schedule = schedule_week1
        query.edit_message_text(text=schedule)
    elif query.data == 'curator':
        query.edit_message_text(text=f'Куратор: {user_link}')
    elif query.data == 'headman':
        query.edit_message_text(text=f'Староста: {user_link1}')

def main():
    updater = Updater("7925112330:AAGIU5fV8X_Lnva-AhwWYba0nrzfWCgWmWU", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
