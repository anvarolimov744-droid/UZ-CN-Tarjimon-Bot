import os
import asyncio
from aiohttp import web

from config import run_bot


# ==============================
# SOZLAMALAR
# ==============================

BOT_TOKEN = os.getenv("BOT_TOKEN", "8605594453:AAECMTUJ-j9FcBuXIvVaB4Aq25SlyUICEXw")
ADMIN_ID = int(os.getenv("ADMIN_ID", "8197690967"))

PORT = int(os.getenv("PORT", "10000"))


# ==============================
# RENDER HEALTH SERVER
# ==============================

async def health(request):
    return web.Response(
        text="UZ CN Tarjimon ishlayapti!"
    )


async def start_web_server():
    app = web.Application()
    app.router.add_get("/", health)
    app.router.add_get("/health", health)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(
        runner,
        "0.0.0.0",
        PORT
    )

    await site.start()

    print(f"🌐 Web server: 0.0.0.0:{PORT}")


# ==============================
# BOT
# ==============================

async def main():
    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN topilmadi! Render Environment Variables "
            "ichida BOT_TOKEN ni sozlang."
        )

    await start_web_server()

    print("===================================")
    print("🇺🇿🇨🇳 UZ CN TARJIMON")
    print("===================================")
    print(f"👤 Admin ID: {ADMIN_ID}")
    print("🤖 Bot ishga tushmoqda...")
    print("===================================")

    # config.py dagi run_bot funksiyasini ishga tushirish
    result = run_bot(
        token=BOT_TOKEN,
        admin_id=ADMIN_ID
    )

    if asyncio.iscoroutine(result):
        await result


if __name__ == "__main__":
    asyncio.run(main())