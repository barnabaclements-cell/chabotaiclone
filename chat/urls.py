from django.urls import path
from .views import (
    ChatView,
    ThreadListView,
    CreateThreadView,
    ThreadMessagesView,
)

urlpatterns = [
    # Send message to AI
    path("chat/", ChatView.as_view(), name="chat"),

    # Get all threads
    path("threads/", ThreadListView.as_view(), name="threads"),

    # Create new thread
    path("threads/create/", CreateThreadView.as_view(), name="create-thread"),

    # Get all messages of a thread
    path(
        "threads/<int:thread_id>/messages/",
        ThreadMessagesView.as_view(),
        name="thread-messages",
    ),
]