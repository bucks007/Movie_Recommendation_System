from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.chatbot_view,
        name="chatbot"
    ),

    path(
        "send/",
        views.chat_message,
        name="chat_message"
    ),

    path(
        "new/",
        views.new_chat,
        name="new_chat"
    ),

]