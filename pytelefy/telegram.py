from fastapi import FastAPI
from telethon import TelegramClient

from contextlib import asynccontextmanager

class TelegramLifespan:
    def __init__(self, client: TelegramClient, **kwargs) -> None:
        self.client = client
        self._kwargs = kwargs

    @asynccontextmanager
    async def __call__(self, app: FastAPI):
        async with await self.client.start(**self._kwargs):
            yield