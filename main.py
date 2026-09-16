# 🇺🇿🇨🇳 UZ CN Tarjimon
# main.py

from config import run_bot


# ==============================
# BOT SOZLAMALARI
# ==============================

BOT_TOKEN = "8605594453:AAECMTUJ-j9FcBuXIvVaB4Aq25SlyUICEXw"

ADMIN_ID = 8197690967


# ==============================
# BOTNI ISHGA TUSHIRISH
# ==============================

if __name__ == "__main__":
    run_bot(
        token=BOT_TOKEN,
        admin_id=ADMIN_ID
    )