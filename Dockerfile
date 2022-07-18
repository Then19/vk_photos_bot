FROM python:3.9

WORKDIR /bot

ENV CLICKHOUSE_DSN="" \
    BOT_TOKEN="" \
    ADMIN_ID="" \
    API_URL=""

COPY ./requirements.txt /bot/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["python", "-m", "bot"]
