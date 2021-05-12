from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .libs.message_handler import handler
from linebot.exceptions import InvalidSignatureError
import logging

view_logger = logging.getLogger("api")

# Create your views here.
@require_POST
@csrf_exempt
def bot_callback(request):
    try:
        signature = request.headers['X-Line-Signature']
    except Exception as e:
        view_logger.error(e)
        return JsonResponse({
            'message': 'Provide X-Line-Signature header'
        }, status=400) 

    try:
        body = request.body.decode('utf-8')
        handler.handle(body, signature)
    except InvalidSignatureError as e:
        view_logger.error(e)
        return JsonResponse({
            'message': 'Invalid signature. Please check your channel access token/channel secret.'
        }, status=400)
    except Exception as e:
        view_logger.error(e)
        return JsonResponse({
            'message': 'Unable to handle data'
        }, status=500)

    return JsonResponse({
        'message': 'OK'
    }, status=200)

@require_GET
@csrf_exempt
def hello_world(request):
    return JsonResponse({
        'message': 'hello, world'
    }, status=200)