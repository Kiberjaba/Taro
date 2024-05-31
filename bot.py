import os
import random
from telegram import Update, InputFile
from telegram.ext import Application, MessageHandler, CallbackContext
from telegram.ext.filters import TEXT

TELEGRAM_TOKEN = '6338270646:AAGLlbcNbBuU8h-RviGA-8YFO32xbCa2sek'

# Список случайных фраз
random_phrases = [
    "Ветер перемен уже дует в твою сторону.",
    "Тени прошлого могут скрывать важные подсказки.",
    "Ответ лежит глубже, чем ты можешь себе представить.",
    "Твоя интуиция приведет тебя к истине.",
    "Судьба плетет свои сети, будь внимателен.",
    "Свет и тьма в гармонии принесут тебе ответы.",
    "Будущее не высечено в камне, твои действия решат всё.",
    "Древние знания откроются тебе в нужный момент.",
    "Внутренний голос всегда говорит правду.",
    "Ожидай неожиданного, и ты будешь готов ко всему.",
    "Скрытые силы работают на твою сторону.",
    "Незримые нити соединяют все события.",
    "Прими изменения, они принесут рост и мудрость.",
    "Каждое испытание – это шаг к твоему предназначению.",
    "Вселенная слышит твои мысли, будь ясным в своих желаниях.",
    "Твоя истинная сила проявится в момент нужды.",
    "Слушай шепот ветра, в нем скрыта истина.",
    "Простота есть ключ к великому пониманию.",
    "Время – это иллюзия, следуй за своим сердцем.",
    "Дорога будет ясна, когда ты осознаешь свою цель."
]

# Путь к директории с изображениями
IMAGE_DIR = 'images'

async def send_random_images(update: Update, context: CallbackContext) -> None:
    image_files = [img for img in os.listdir(IMAGE_DIR) if img.endswith(('.png'))]
    selected_images = random.sample(image_files, min(3, len(image_files)))
    
    for image in selected_images:
        image_path = os.path.join(IMAGE_DIR, image)
        try:
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(image_path, 'rb'))
        except Exception as e:
            print(f"Ошибка при отправке изображения {image_path}: {e}")

async def handle_message(update: Update, context: CallbackContext) -> None:
    message_text = update.message.text
    
    if message_text.endswith('?'):
        await send_random_images(update, context)
    else:
        random_phrase = random.choice(random_phrases)
        await update.message.reply_text(random_phrase)

def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    application.add_handler(MessageHandler(TEXT, handle_message))
    
    application.run_polling()

if __name__ == '__main__':
    main()
