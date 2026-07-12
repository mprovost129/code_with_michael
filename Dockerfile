FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# LOGGING's file handler writes to logs/django.log and won't create the
# directory itself. logs/ is excluded from the build context (.dockerignore)
# since the host's accumulated log file shouldn't be baked into the image.
RUN mkdir -p logs

# collectstatic only needs Django to boot, not real secrets or a live
# database — these placeholders satisfy the required settings so the build
# doesn't depend on secrets being present in the build context. Real values
# are supplied at container runtime (docker run -e / compose env_file) and
# always take precedence over these image defaults.
ENV DJANGO_SETTINGS_MODULE=config.Settings.prod \
    SECRET_KEY=build-time-placeholder-not-used-at-runtime \
    ALLOWED_HOSTS=localhost \
    DB_NAME=build \
    DB_USER=build \
    DB_PASSWORD=build

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]
