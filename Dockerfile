FROM python:3.10

COPY req.txt req.txt
RUN pip install --no-cache-dir -r req.txt

COPY . code
WORKDIR /code

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]