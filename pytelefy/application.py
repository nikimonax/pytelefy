from fastapi import FastAPI

from .telegram import TelegramClient, TelegramLifespan

class PyTeleFyApp(FastAPI):
    def __init__(
        self,
        telegram_client: TelegramClient,
        telegram_lifespan: TelegramLifespan
    ):
        super().__init__(lifespan=telegram_lifespan)
        self.telegram_client = telegram_client
        self.add_api_route("/sendMessage", self.send_message, methods=["POST"])

    async def send_message(self, username: str, text: str):
        await self.telegram_client.send_message(username, text)
        return { "status": "ok" }