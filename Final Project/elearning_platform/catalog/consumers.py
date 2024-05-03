import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Course, Instructor, Genre
from asgiref.sync import sync_to_async

class ElearningConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass 

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Handling different events when a message is received
        if message == "fetch_courses":
            courses = await self.get_courses()
            await self.send(text_data=json.dumps({
                'message': courses
            }))
        elif message == "fetch_instructors":
            instructors = await self.get_instructors()
            await self.send(text_data=json.dumps({
                'message': instructors
            }))
        elif message == "fetch_genres":
            genres = await self.get_genres()
            await self.send(text_data=json.dumps({
                'message': genres
            }))

    @sync_to_async
    def get_courses(self):
        courses = list(Course.objects.all().values())
        return json.dumps(courses)  # Serialize query to JSON

    @sync_to_async
    def get_instructors(self):
        instructors = list(Instructor.objects.all().values())
        return json.dumps(instructors)  # Serialize query to JSON

    @sync_to_async
    def get_genres(self):
        genres = list(Genre.objects.all().values())
        return json.dumps(genres)  # Serialize query to JSON

    async def elearning_notify(self, event):
        # Send a message to WebSocket
        await self.send(text_data=json.dumps({
            'message': event['text']
        }))
