from django.test import TestCase

# Create your tests here.
from .models import Course, Instructor, Genre

class ModelTests(TestCase):
    def test_course_creation(self):
        # Test course creation
        course = Course.objects.create(title="Test Course", price=100)
        self.assertEqual(course.title, "Test Course")
        self.assertEqual(course.price, 100)

    def test_instructor_creation(self):
        # Test instructor creation
        instructor = Instructor.objects.create(first_name="John", last_name="Doe")
        self.assertEqual(instructor.first_name, "John")
        self.assertEqual(instructor.last_name, "Doe")

    def test_genre_creation(self):
        # Test genre creation
        genre = Genre.objects.create(name="Test Genre")
        self.assertEqual(genre.name, "Test Genre")
