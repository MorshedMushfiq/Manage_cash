from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Check if the username is an email or a normal username
        if username is None:
            return None

        try:
            # Try to get user by username first
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # If not found by username, check if it's an email
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                return None  # If no match, return None

        # Check if the password is correct
        if user.check_password(password):
            return user
        return None
