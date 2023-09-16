from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Database model  for users in the system.

    DESCRIPTION:
    Overrides the default Django user model behavior to authenticate
    user using email field instead of username field
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Custom model manager to create, retrieve, update, and delete user objects using CLI
    objects = UserProfileManager()

    # Overriding default USERNAME_FIELD with email field
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """
        Retrieve fill name of user
        """
        return self.name

    def get_short_name(self):
        """
        Retrieve short name of user
        """
        return self.name

    def __str__(self):
        """
        Return string representation of our user
        """
        return self.email
