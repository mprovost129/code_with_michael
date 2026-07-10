from django.contrib.auth.base_user import BaseUserManager
from django.utils.text import slugify


class UserManager(BaseUserManager):
    def _generate_username(self, email):
        base_username = slugify(email.split('@')[0]).replace('-', '_') or 'user'
        candidate = base_username
        suffix = 1

        while self.model.objects.filter(username=candidate).exists():
            suffix += 1
            candidate = f'{base_username}{suffix}'

        return candidate

    def create_user(self, email, password=None, username=None, **extra_fields):
        if not email:
            raise ValueError('Email address is required.')
        email = self.normalize_email(email)
        username = username or extra_fields.pop('username', None) or self._generate_username(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, username=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields['is_staff']:
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields['is_superuser']:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, username=username, **extra_fields)
