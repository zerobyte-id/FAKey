FROM python:3

WORKDIR /usr/src/fakey

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "./FAKey.py" ]
