from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

import json
from .services.chat_service import process_message


def chatbot_view(request):

    return render(
        request,
        "chatbot/chatbot.html"
    )


@require_POST
def chat_message(request):

    data = json.loads(request.body)

    message = data.get(
        "message",
        ""
    )

    response = process_message(
        request.user,
        message
    )

    return JsonResponse({

        "response": response

    })

def new_chat(request):

    return JsonResponse({

        "status":
        "success"

    })