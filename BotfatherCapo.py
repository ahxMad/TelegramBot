from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower()
    greetings = ['hi', 'hello', 'hey']
    if text.startswith(('hi', 'hello','hey')) and any(word in text for word in ('capo', 'boss', 'sir')):
        update.message.reply_text('How can I help you?')
    elif text in greetings:
        update.message.reply_text("Hey, I expect a bit more respect around here. It's BOSS, SIR or CAPO. GOT IT?")

def main() -> None:
    updater = Updater("6738976032:AAEiu535SBYwH9p-6Eedx8FZVU54DxQoJPA", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
