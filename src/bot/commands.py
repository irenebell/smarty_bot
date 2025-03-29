from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import config

from bot.resource_loader import load_image
from config import TG_BOT_API_KEY
from bot.message_sender import send_html_message, send_image_bytes, show_menu
from bot.resource_loader import load_message, load_image, load_menu

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = await load_message("main")
    image_bytes = await load_image("main")
    menu_commands = await load_menu("main")

    await send_image_bytes(
        update=update,
        context=context,
        image_bytes=image_bytes,
    )

    await send_html_message(
        update=update,
        context=context,
        text=text,
    )

    await show_menu(
        update=update,
        context=context,
        commands=menu_commands
    )




app = ApplicationBuilder().token(TG_BOT_API_KEY).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()

