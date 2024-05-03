from .models import Course, Instructor, Genre  # Import the models from your models.py file
from django.db import transaction

class CourseRepository:
    def get_all_courses(self):
        return Course.objects.all()

    def add_course(self, title, instructor, price, summary):
        return Course.objects.create(title=title, instructor=instructor, price=price, summary=summary)

    def get_course_by_id(self, id):
        return Course.objects.filter(id=id).first()

    def update_course(self, id, **kwargs):
        Course.objects.filter(id=id).update(**kwargs)

    def delete_course(self, id):
        with transaction.atomic():
            course = self.get_course_by_id(id)
            if course:
                course.delete()

class InstructorRepository:
    def get_all_instructors(self):
        return Instructor.objects.all()

    def add_instructor(self, first_name, last_name):
        return Instructor.objects.create(first_name=first_name, last_name=last_name)

    def get_instructor_by_id(self, id):
        return Instructor.objects.filter(id=id).first()

    def update_instructor(self, id, **kwargs):
        Instructor.objects.filter(id=id).update(**kwargs)

    def delete_instructor(self, id):
        with transaction.atomic():
            instructor = self.get_instructor_by_id(id)
            if instructor:
                instructor.delete()

class GenreRepository:
    def get_all_genres(self):
        return Genre.objects.all()

    def add_genre(self, name):
        return Genre.objects.create(name=name)

    def get_genre_by_id(self, id):
        return Genre.objects.filter(id=id).first()

    def update_genre(self, id, **kwargs):
        Genre.objects.filter(id=id).update(**kwargs)

    def delete_genre(self, id):
        with transaction.atomic():
            genre = self.get_genre_by_id(id)
            if genre:
                genre.delete()
