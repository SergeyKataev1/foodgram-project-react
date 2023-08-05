FROM python:3.11-slim
WORKDIR /backend
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
RUN python -m pip install --upgrade setuptools
COPY ../ .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "foodgram.wsgi"]