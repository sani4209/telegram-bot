from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

TOKEN = '8023602290:AAEqaajZNuCi4D23YfOu93rP87-PY4_vRZ0'

CHANNEL_1 = "https://t.me/+UoH0HwPY1nM5Y2M1"
CHANNEL_2 = "https://t.me/+WmLRaXrnnb4yODFl"
CHANNEL_3 = "https://t.me/+MpJNoX1SH1AwZjJl"

def welcome(update: Update, context: CallbackContext):
    new_members = update.message.new_chat_members
    if new_members:
        for member in new_members:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"""🙏 Welcome {member.first_name}!

🔥 हमारे सबसे दमदार चैनल्स जॉइन करो:
👉 [Channel 1]({CHANNEL_1})
👉 [Channel 2]({CHANNEL_2})
👉 [Channel 3]({CHANNEL_3})""",
                parse_mode='Markdown'
            )

def goodbye(update: Update, context: CallbackContext):
    left_member = update.message.left_chat_member
    if left_member:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"""😔 {left_member.first_name} ने ग्रुप छोड़ दिया...

लेकिन तुम ये तीनों चैनल ज़रूर जॉइन करना:
👉 [Channel 1]({CHANNEL_1})
👉 [Channel 2]({CHANNEL_2})
👉 [Channel 3]({CHANNEL_3})""",
            parse_mode='Markdown'
        )

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))
dp.add_handler(MessageHandler(Filters.status_update.left_chat_member, goodbye))

updater.start_polling()
updater.idle()
