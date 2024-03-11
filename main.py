from os import getenv

from aiohttp import web

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application


TOKEN = getenv("BOT_TOKEN")
ADMIN_ID = getenv("ADMIN_ID")


WEB_SERVER_HOST = "127.0.0.1"
WEB_SERVER_PORT = 8080
WEBHOOK_PATH = "/webhook"

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    if message.from_user.id == ADMIN_ID:
        await message.answer(f"Hello!")

def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

    app = web.Application()

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )

    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    setup_application(app, dp, bot=bot)

    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    main()