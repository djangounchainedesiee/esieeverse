FROM python:3.9.13

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_DEBUG=False
RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "esieeverse.wsgi", "--bind", "0.0.0.0:8000"]