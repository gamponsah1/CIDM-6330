from django.contrib import admin
from .models import Instructor, Genre, Course

class CourseAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the admin form
    list_display = ('title', 'instructor', 'display_genre', 'price')

    # Define the form fields and their properties
    fieldsets = (
        (None, {
            'fields': ('title', 'instructor', 'summary', 'genre', 'price')
        }),
    )

    # Define the behavior when displaying genres in the admin form
    def display_genre(self, obj):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([genre.name for genre in obj.genre.all()])

    # Set the display name for the genre column
    display_genre.short_description = 'Genre'

class InstructorAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the admin form
    list_display = ('last_name', 'first_name')    

class GenreAdmin(admin.ModelAdmin):
    list_filter=('genre')

admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor,InstructorAdmin)
admin.site.register(Genre)


#from django.contrib import admin


#from .models import Instructor, Genre, Course
#admin.site.register(Course)
#admin.site.register(Instructor)
#admin.site.register(Genre)




