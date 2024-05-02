# views.py
# views.py
# views.py

from django.shortcuts import render,get_object_or_404,redirect
from .models import Course, Instructor, Genre
from .forms import CreditCardForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_courses = Course.objects.all().count()
    num_instructors = Instructor.objects.all().count()
    
    context = {
        'num_courses': num_courses,
        'num_instructors': num_instructors,
    }
    return render(request, 'index.html', context=context)

def course_list(request):
    """View function to display a list of courses."""
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'course_list.html', context=context)

def instructor_list(request):
    """View function to display a list of instructors."""
    instructors = Instructor.objects.all()
    context = {
        'instructors': instructors,
    }
    return render(request, 'instructor_list.html', context=context)

def purchase_course(request, course_id):
    # Retrieve the course object based on the provided course_id
    course = get_object_or_404(Course, pk=course_id)
    
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            # Process payment (for demonstration purposes, assume success)
            # Add payment processing logic here
            
            # Redirect to purchase confirmation page after successful payment
            return redirect('purchase_confirmation')
    else:
        # If the request method is GET, instantiate a new CreditCardForm
        form = CreditCardForm()
    
    # Pass the course and form to the template
    context = {
        'course': course,
        'form': form,
    }
    return render(request, 'purchase_course.html', context)


def process_purchase(request, course_id):
    # Retrieve the course object based on the provided course_id
    course = Course.objects.get(pk=course_id)
    
    if request.method == 'POST':
        # Process the payment (for demonstration purposes, we assume payment is successful)
        # Add your payment processing logic here
        # After successful payment, redirect to purchase confirmation page
        return redirect('purchase_confirmation')
    else:
        # If the request method is not POST, redirect back to the purchase page
        return redirect('purchase_course', course_id=course_id)

def purchase_confirmation(request):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            # Process payment and handle purchase logic here
            # Redirect to purchase confirmation page after successful payment
            return redirect('purchase_confirmation')
    else:
        form = CreditCardForm()
    return render(request, 'purchase_confirmation.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login_success')  # Redirect to a success page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def login_success(request):
    return render(request, 'login_success.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})