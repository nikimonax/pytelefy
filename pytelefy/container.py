from dependency_injector import providers, containers

from .telegram import TelegramClient, TelegramLifespan
from .application import PyTeleFyApp

class Container(containers.DeclarativeContainer):
    config_dir = providers.Configuration()
    data_dir = providers.Configuration()

    config = providers.Configuration()
    data = providers.Configuration()

    telegram_client = providers.Singleton(
        TelegramClient,
        session=data.telegram.session,
        api_id=config.telegram.api_id,
        api_hash=config.telegram.api_hash
    )

    telegram_lifespan = providers.Singleton(
        TelegramLifespan,
        client=telegram_client,
        bot_token=config.telegram.bot_token
    )

    app = providers.Singleton(
        PyTeleFyApp,
        telegram_client=telegram_client,
        telegram_lifespan=telegram_lifespan
    )

def get_container():
    container = Container()

    container.config_dir.from_env("PYTELEFY_CONFIG_DIR", default=".")
    container.data_dir.from_env("PYTELEFY_DATA_DIR", default=".")

    container.config.from_yaml(container.config_dir() + "/config.yml", required=True)
    container.data.telegram.session.from_value(container.data_dir() + "/telegram")

    return container