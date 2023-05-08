FROM python:3.10

COPY ./smart_home/requirements.txt /src/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt

COPY . /src

ENV PYTHONUNBUFFERED=1

WORKDIR src

EXPOSE 6060

CMD ["python3", "-u", "manage.py", "--host", "0.0.0.0", "--port", "6060"]

