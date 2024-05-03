from django.test import TestCase, Client
from django.urls import reverse
from .models import Course

class CourseIntegrationTest(TestCase):
    def setUp(self):
        # Set up test data
        self.course = Course.objects.create(title='Test Course', price=10)

    def test_course_list_view(self):
        # Test the course list view
        response = self.client.get(reverse('course-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Course')

    def test_purchase_course_view(self):
        # Test the purchase course view
        response = self.client.get(reverse('purchase', args=[self.course.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Course')
