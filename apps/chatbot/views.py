from django.shortcuts import render
from django.http import JsonResponse


def chat_message(request):

    return JsonResponse({

        "response":
        "Movie AI is coming soon 🚀"

    })


def new_chat(request):

    return JsonResponse({

        "status":
        "success"

    })