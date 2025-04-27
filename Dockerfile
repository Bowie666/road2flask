FROM python:3.9
# FROM --platform=linux/amd64 python:3.9

WORKDIR /code

COPY . /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
# CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--workers", "1", "--worker-class", "gevent", "--worker-connections", "10", "--timeout", "200", "app:app"]
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5001"]
# gunicorn \
#       --bind "${DIFY_BIND_ADDRESS:-0.0.0.0}:${DIFY_PORT:-5001}" \
#       --workers ${SERVER_WORKER_AMOUNT:-1} \
#       --worker-class ${SERVER_WORKER_CLASS:-gevent} \
#       --worker-connections ${SERVER_WORKER_CONNECTIONS:-10} \
#       --timeout ${GUNICORN_TIMEOUT:-200} \
#       app:app