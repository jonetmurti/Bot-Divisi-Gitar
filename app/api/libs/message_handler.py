from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from app.settings import CHANNEL_ACCESS_TOKEN, CHANNEL_SECRET
from api.models import BotResponse
import random

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    msg = event.message.text.lower()
    response = None

    if msg == "deadline minggu ini":
        pass
    elif msg == "deadline bulan ini":
        pass
    else:
        response = text_answer(msg)

    if response:
        line_bot_api.reply_message(event.reply_token, response)

def text_answer(msg):
    records = BotResponse.objects.filter(question__icontains=msg)
    if records:
        record = random.choice(records)
        return TextSendMessage(record.answer)
    else:
        return None

def flex_answer(msg):
    pass