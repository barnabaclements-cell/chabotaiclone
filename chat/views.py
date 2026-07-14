import traceback

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Thread, Message
from .services import ask_groq


class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        print("=" * 50)
        print("REQUEST DATA:", request.data)
        print("USER:", request.user)
        print("=" * 50)

        try:

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

            print("Loading thread...")

            thread = Thread.objects.get(
                id=thread_id,
                user=request.user
            )

            print("Thread found:", thread.id)

            Message.objects.create(
                thread=thread,
                role="user",
                content=message
            )

            print("User message saved.")

            conversation = []

            messages = thread.messages.all().order_by("created")

            for msg in messages:
                conversation.append({
                    "role": msg.role,
                    "content": msg.content
                })

            print("Conversation:")
            print(conversation)

            print("Calling Groq...")

            answer = ask_groq(conversation)

            print("Groq replied:")
            print(answer)

            Message.objects.create(
                thread=thread,
                role="assistant",
                content=answer
            )

            print("Assistant message saved.")

            return Response({
                "response": answer
            })

        except Exception as e:

            print("=" * 80)
            print("CHAT ERROR")
            print(e)
            traceback.print_exc()
            print("=" * 80)

            return Response(
                {
                    "error": str(e)
                },
                status=500
            )
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