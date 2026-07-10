from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        identifier = username or kwargs.get(user_model.USERNAME_FIELD)

        if not identifier or not password:
            return None

        user = user_model.objects.filter(
            Q(email__iexact=identifier) | Q(username__iexact=identifier)
        ).first()
        if user is not None and user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
