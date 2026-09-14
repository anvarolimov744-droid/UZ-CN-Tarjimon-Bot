
import asyncio
import json
from pathlib import Path
from datetime import datetime

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message


# =========================================================
# SOZLAMALAR
# =========================================================

BOT_TOKEN = "8981896157:AAEfCrds8eG5IASUN5cBDXx0Vh5qFxAfxlg "

ADMIN_ID = 123456789
# Avval 0 qoldiring.
# Botga /myid yuborib ID'ingizni oling,
# keyin shu yerga o'sha ID raqamini yozing.
ADMIN_ID = 0


# =========================================================
# FAYLLAR
# =========================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(exist_ok=True)

USERS_FILE = DATA_DIR / "users.json"
STATS_FILE = DATA_DIR / "stats.json"
HISTORY_FILE = DATA_DIR / "history.json"


# =========================================================
# JSON FUNKSIYALAR
# =========================================================

def load_json(path, default):
    try:
        if not path.exists():
            save_json(path, default)
            return default

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    except Exception:
        return default


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2
        )


# =========================================================
# FAYLLARNI TAYYORLASH
# =========================================================

if not USERS_FILE.exists():
    save_json(USERS_FILE, [])

if not STATS_FILE.exists():
    save_json(
        STATS_FILE,
        {
            "translations": 0,
            "users": 0,
            "subscribers": 0
        }
    )

if not HISTORY_FILE.exists():
    save_json(HISTORY_FILE, [])


# =========================================================
# TARJIMONNI ULASH
# =========================================================

try:
    from translator import translate_text, detect_language
except ImportError:
    translate_text = None
    detect_language = None


# =========================================================
# FOYDALANUVCHINI RO'YXATGA OLISH
# =========================================================

def register_user(message: Message):

    if not message.from_user:
        return

    users = load_json(
        USERS_FILE,
        []
    )

    user_id = message.from_user.id

    exists = any(
        user.get("id") == user_id
        for user in users
    )

    if not exists:

        users.append(
            {
                "id": user_id,
                "username": message.from_user.username,
                "first_name": message.from_user.first_name,
                "last_name": message.from_user.last_name,
                "joined": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            }
        )

        save_json(
            USERS_FILE,
            users
        )

    stats = load_json(
        STATS_FILE,
        {
            "translations": 0,
            "users": 0,
            "subscribers": 0
        }
    )

    stats["users"] = len(users)
    stats["subscribers"] = len(users)

    save_json(
        STATS_FILE,
        stats
    )


# =========================================================
# TARJIMALAR SONINI OSHIRISH
# =========================================================

def increase_translation_count():

    stats = load_json(
        STATS_FILE,
        {
            "translations": 0,
            "users": 0,
            "subscribers": 0
        }
    )

    stats["translations"] = int(
        stats.get("translations", 0)
    ) + 1

    save_json(
        STATS_FILE,
        stats
    )


# =========================================================
# TARJIMA TARIXINI SAQLASH
# =========================================================

def save_history(
    user_id,
    original,
    translation,
    source,
    target
):

    history = load_json(
        HISTORY_FILE,
        []
    )

    history.insert(
        0,
        {
            "user_id": user_id,
            "original": original,
            "translation": translation,
            "source": source,
            "target": target,
            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }
    )

    save_json(
        HISTORY_FILE,
        history[:1000]
    )


# =========================================================
# BOT VA DISPATCHER
# =========================================================

bot = Bot(
    token=BOT_TOKEN
)

dp = Dispatcher()


# =========================================================
# /start
# =========================================================

@dp.message(CommandStart())
async def start_command(message: Message):

    register_user(message)

    name = message.from_user.first_name

    await message.answer(
        f"👋 Salom, {name}!\n\n"
        "🌐 Tarjimon Super Botga xush kelibsiz!\n\n"
        "🇺🇿 O'zbekcha → 🇨🇳 Xitoycha\n"
        "🇨🇳 Xitoycha → 🇺🇿 O'zbekcha\n\n"
        "✍️ Istalgan matnni yuboring.\n"
        "Bot tilni avtomatik aniqlaydi va tarjima qiladi.\n\n"
        "📌 Buyruqlar:\n"
        "/start — Boshlash\n"
        "/help — Yordam\n"
        "/myid — Telegram ID\n"
        "/uzzh — O'zbekcha → Xitoycha\n"
        "/zhuz — Xitoycha → O'zbekcha\n"
        "/admin — Admin statistikasi"
    )


# =========================================================
# /help
# =========================================================

@dp.message(Command("help"))
async def help_command(message: Message):

    register_user(message)

    await message.answer(
        "📖 YORDAM\n\n"
        "Oddiy matn yuboring.\n\n"
        "Masalan:\n"
        "🇺🇿 salom\n"
        "🇺🇿 rahmat\n"
        "🇺🇿 o'zbekiston\n"
        "🇨🇳 你好\n"
        "🇨🇳 谢谢\n"
        "🇨🇳 中国\n\n"
        "Bot tilni avtomatik aniqlaydi."
    )


# =========================================================
# /myid
# =========================================================

@dp.message(Command("myid"))
async def myid_command(message: Message):

    register_user(message)

    await message.answer(
        f"🆔 Sizning Telegram ID'ingiz:\n\n"
        f"{message.from_user.id}\n\n"
        "Bu raqamni telegram_bot.py ichidagi "
        "ADMIN_ID ga yozishingiz mumkin."
    )


# =========================================================
# /uzzh
# =========================================================

@dp.message(Command("uzzh"))
async def uzzh_command(message: Message):

    register_user(message)

    await message.answer(
        "🇺🇿 → 🇨🇳\n\n"
        "O'zbekcha matnni yuboring."
    )


# =========================================================
# /zhuz
# =========================================================

@dp.message(Command("zhuz"))
async def zhuz_command(message: Message):

    register_user(message)

    await message.answer(
        "🇨🇳 → 🇺🇿\n\n"
        "Xitoycha matnni yuboring."
    )


# =========================================================
# /admin
# =========================================================

@dp.message(Command("admin"))
async def admin_command(message: Message):

    register_user(message)

    if message.from_user.id != ADMIN_ID:

        await message.answer(
            "⛔ Sizda admin huquqi yo'q."
        )

        return

    stats = load_json(
        STATS_FILE,
        {
            "translations": 0,
            "users": 0,
            "subscribers": 0
        }
    )

    users = load_json(
        USERS_FILE,
        []
    )

    await message.answer(
        "🔐 ADMIN PANEL\n\n"
        f"👥 Foydalanuvchilar: {len(users)}\n"
        f"📢 Bot foydalanuvchilari: {stats.get('subscribers', 0)}\n"
        f"🌐 Tarjimalar: {stats.get('translations', 0)}\n\n"
        f"🕐 Vaqt: "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )


# =========================================================
# MATN TARJIMASI
# =========================================================

@dp.message(F.text)
async def translate_message(message: Message):

    register_user(message)

    text = message.text.strip()

    if not text:
        return

    if translate_text is None:

        await message.answer(
            "❌ translator.py topilmadi."
        )

        return

    try:

        source = "auto"

        # Xitoycha belgilarni aniqlash
        detected = detect_language(
            text,
            source
        )

        if detected == "zh":
            target = "uz"
        else:
            target = "zh"

        result = translate_text(
            text,
            source,
            target
        )

        if not result:
            result = "❌ Tarjima topilmadi."

        increase_translation_count()

        save_history(
            user_id=message.from_user.id,
            original=text,
            translation=result,
            source=detected,
            target=target
        )

        if detected == "zh":

            await message.answer(
                "🇨🇳 → 🇺🇿\n\n"
                f"📝 Asl matn:\n{text}\n\n"
                f"🔄 Tarjima:\n{result}"
            )

        else:

            await message.answer(
                "🇺🇿 → 🇨🇳\n\n"
                f"📝 Asl matn:\n{text}\n\n"
                f"🔄 Tarjima:\n{result}"
            )

    except Exception as error:

        print(
            "Tarjima xatosi:",
            error
        )

        await message.answer(
            "❌ Tarjima vaqtida xatolik yuz berdi."
        )


# =========================================================
# BOSHQA XABARLAR
# =========================================================

@dp.message()
async def other_message(message: Message):

    register_user(message)

    await message.answer(
        "✍️ Iltimos, matn yuboring.\n\n"
        "Masalan:\n"
        "Salom\n"
        "Rahmat\n"
        "你好\n"
        "谢谢"
    )


# =========================================================
# BOTNI ISHGA TUSHIRISH
# =========================================================

async def main():

    print("")
    print("===================================")
    print("🤖 TARJIMON SUPER BOT")
    print("===================================")
    print("✅ Bot ishga tushmoqda...")
    print("📱 Telegram polling boshlandi")
    print("🛑 To'xtatish: CTRL + C")
    print("===================================")
    print("")

    await dp.start_polling(
        bot
    )


# =========================================================
# START
# =========================================================

if __name__ == "__main__":

    try:

        asyncio.run(
            main()
        )

    except KeyboardInterrupt:

        print("")
        print("🛑 Bot to'xtatildi.")

