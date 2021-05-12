from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)
from app.settings import CHANNEL_ACCESS_TOKEN, CHANNEL_SECRET
from api.models import BotResponse, Event
import random
from .flex_gen import *
import threading
import logging

handler_logger = logging.getLogger("api")
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    msg = event.message.text.lower()
    response = None

    if msg == "deadline minggu ini":
        response = flex_answer("Weekly Deadlines", Event.get_weekly_events())
    elif msg == "deadline bulan ini":
        response = flex_answer("Monthly Deadlines", Event.get_monthly_events())
    else:
        response = text_answer(msg)

    if response:
        reply_thread = threading.Thread(target=reply_target, args=(event.reply_token, response,))
        reply_thread.start()

def reply_target(reply_token, response):
    try:
        line_bot_api.reply_message(reply_token, response)
        handler_logger.info("Reply sent")
    except Exception as e:
        handler_logger.error(e)

def text_answer(msg):
    records = BotResponse.objects.filter(question__icontains=msg)
    if records:
        record = random.choice(records)
        return TextSendMessage(record.answer)
    else:
        return None

def flex_answer(title, events):
    header = header_creator(title)
    body = body_creator(events)

    return FlexSendMessage(
        alt_text=title,
        contents=flex_msg_gen(
            header,
            body
        )
    )