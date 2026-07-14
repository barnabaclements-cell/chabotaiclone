from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Thread, Message
from .services import ask_groq


class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print("REQUEST DATA:", request.data)

        thread_id = request.data.get("thread_id")
        message = request.data.get("message")

        if not thread_id:
            return Response(
                {"error": "thread_id is required"},
                status=400
            )

        if not message:
            return Response(
                {"error": "message is required"},
                status=400
            )

        try:
            thread = Thread.objects.get(
                id=thread_id,
                user=request.user
            )
        except Thread.DoesNotExist:
            return Response(
                {"error": "Thread not found"},
                status=404
            )

        # Save user message
        Message.objects.create(
            thread=thread,
            role="user",
            content=message
        )

        # Load entire conversation
        conversation = []

        messages = thread.messages.all().order_by("created")

        for msg in messages:
            conversation.append({
                "role": msg.role,
                "content": msg.content
            })

        # Ask Groq
        answer = ask_groq(conversation)

        # Save assistant reply
        Message.objects.create(
            thread=thread,
            role="assistant",
            content=answer
        )

        return Response({
            "response": answer
        })


class ThreadListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        threads = Thread.objects.filter(
            user=request.user
        ).order_by("-created")

        data = []

        for thread in threads:
            data.append({
                "id": thread.id,
                "title": thread.title
            })

        return Response(data)


class CreateThreadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        title = request.data.get("title", "New Chat")

        thread = Thread.objects.create(
            user=request.user,
            title=title
        )

        return Response({
            "id": thread.id,
            "title": thread.title
        })


class ThreadMessagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, thread_id):

        try:
            thread = Thread.objects.get(
                id=thread_id,
                user=request.user
            )
        except Thread.DoesNotExist:
            return Response(
                {"error": "Thread not found"},
                status=404
            )

        messages = thread.messages.all().order_by("created")

        data = []

        for message in messages:
            data.append({
                "id": message.id,
                "role": message.role,
                "content": message.content,
                "created": message.created,
            })

        return Response(data)