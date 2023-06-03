FROM python:3.9.16

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_DEBUG=False
RUN python manage.py collectstatic

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]