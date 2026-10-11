# ---- Стадия 1: сборка зависимостей ----
FROM python:3.12-alpine AS builder

RUN apk add --no-cache gcc musl-dev libffi-dev postgresql-dev

WORKDIR /app

COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt


# ---- Стадия 2: финальный образ ----
FROM python:3.12-alpine AS final

# libpq нужна в рантайме, если используешь psycopg2 (не -binary) или psycopg
RUN apk add --no-cache libpq

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder /wheels /wheels
COPY requirements.txt .
RUN pip install --no-cache-dir --no-index --find-links=/wheels -r requirements.txt \
    && rm -rf /wheels requirements.txt

# manage.py, папка проекта (где settings.py), все приложения
COPY . .

# staticfiles — сюда collectstatic кладёт статику, оттуда её раздаёт nginx
RUN mkdir -p /app/staticfiles && chown -R appuser:appgroup /app
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
    CMD python -c "import urllib.request,sys; sys.exit(0) if urllib.request.urlopen('http://localhost:8000/healthz/', timeout=3).status == 200 else sys.exit(1)"

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]

