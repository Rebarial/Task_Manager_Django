FROM python:3.11.5

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . code
WORKDIR /code

RUN python /code/taskManager/manage.py makemigrations && python /code/taskManager/manage.py migrate

EXPOSE 8000

ENTRYPOINT ["python", "taskManager/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]