FROM python:3.12

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir \
    && pip install "django-phonenumber-field[phonenumbers]" \
    && pip install requests

COPY . .
