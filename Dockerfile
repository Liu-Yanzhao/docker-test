FROM python:3
WORKDIR /test/
RUN pip install Flask 
COPY . /test/.
EXPOSE 80
CMD ["python", "server.py"]

