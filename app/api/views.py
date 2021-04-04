from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .libs.message_handler import handler
from linebot.exceptions import InvalidSignatureError

# Create your views here.
@require_POST
@csrf_exempt
def bot_callback(request):
    try:
        signature = request.headers['X-Line-Signature']
    except:
        return JsonResponse({
            'message': 'Provide X-Line-Signature header'
        }, status=400) 

    try:
        body = request.body.decode('utf-8')
        handler.handle(body, signature)
    except InvalidSignatureError as e:
        return JsonResponse({
            'message': 'Invalid signature. Please check your channel access token/channel secret.'
        }, status=400)
    except:
        return JsonResponse({
            'message': 'Unable to handle data'
        }, status=500)

    return JsonResponse({
        'message': 'OK'
    }, status=200)