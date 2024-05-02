from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_signed_up
from django.contrib.auth.models import User

# Define event listener functions

@receiver(user_logged_in, sender=User)
def user_logged_in_handler(sender, request, user, **kwargs):
    """
    Event listener for user logged in event.
    """
    print(f"User {user.username} logged in.")

@receiver(user_logged_out, sender=User)
def user_logged_out_handler(sender, request, user, **kwargs):
    """
    Event listener for user logged out event.
    """
    print(f"User {user.username} logged out.")

@receiver(user_signed_up, sender=User)
def user_signed_up_handler(sender, user, request, **kwargs):
    """
    Event listener for user signed up event.
    """
    print(f"User {user.username} signed up.")

