# PyTeleFy

Simple service for sending messages in telegram using POST request.

The project was created for educational purposes. For use in real projects, it is recommended to use the official API:

```sh
https://api.telegram.org/bot<BOT_TOKEN>/sendMessage?chat_id=<CHAT_ID>&text=<MESSAGE_TEXT>
```

## Usage

### Prepare config

```
cp example.config.yml config.yml 
```

- get `api_id` and `api_hash` here https://my.telegram.org/
- get `bot_token` here https://t.me/BotFather


### Run manually

```sh
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
uvicorn pytelefy:app
```

### Run via docker

```sh
docker build --tag pytelefy .
docker run -d --rm \
    --name pytelefy \
    -v "$(pwd)/config.yml:/etc/pytelefy/config.yml:ro" \
    -p 8000:8000 \
    pytelefy
```

or using docker compose

```sh
docker compose up -d
```

### Test

```
curl -X "POST" "http://localhost:8000/sendMessage?username=<your username>&text=Hello%2C%20World%21"
```