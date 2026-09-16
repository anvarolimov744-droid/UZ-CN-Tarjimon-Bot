
# -*- coding: utf-8 -*-

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import asyncio
import re


# =========================================================
# 🇺🇿 → 🇨🇳 OFFLINE LUG'AT
# =========================================================

UZ_CN = {

    # ---------- SALOMLASHUV ----------
    "salom": "你好",
    "assalomu alaykum": "您好",
    "xayr": "再见",
    "rahmat": "谢谢",
    "katta rahmat": "非常感谢",
    "iltimos": "请",
    "kechirasiz": "对不起",
    "uzr": "抱歉",
    "ha": "是",
    "yo'q": "不是",
    "yaxshi": "好",
    "juda yaxshi": "非常好",
    "yomon": "不好",
    "mayli": "好的",
    "albatta": "当然",
    "tushunarli": "明白",
    "tushunmadim": "我不明白",
    "bilaman": "我知道",
    "bilmayman": "我不知道",
    "xayrli tong": "早上好",
    "xayrli kun": "你好",
    "xayrli kech": "晚上好",
    "xayrli tun": "晚安",

    # ---------- ODAMLAR ----------
    "men": "我",
    "sen": "你",
    "siz": "您",
    "u": "他",
    "biz": "我们",
    "ular": "他们",
    "odam": "人",
    "bola": "孩子",
    "erkak": "男人",
    "ayol": "女人",
    "o'g'il": "儿子",
    "qiz": "女儿",
    "do'st": "朋友",
    "do'stim": "我的朋友",
    "qo'shni": "邻居",
    "mehmon": "客人",
    "o'qituvchi": "老师",
    "o'quvchi": "学生",
    "talaba": "大学生",
    "shifokor": "医生",
    "hamshira": "护士",
    "haydovchi": "司机",
    "sotuvchi": "销售员",
    "mijoz": "顾客",

    # ---------- OILA ----------
    "oila": "家庭",
    "ota": "父亲",
    "ona": "母亲",
    "dada": "爸爸",
    "oyi": "妈妈",
    "aka": "哥哥",
    "uka": "弟弟",
    "opa": "姐姐",
    "singil": "妹妹",
    "bobo": "爷爷",
    "buvi": "奶奶",
    "er": "丈夫",
    "xotin": "妻子",
    "ota-ona": "父母",
    "farzand": "孩子",
    "aka-uka": "兄弟",
    "opa-singil": "姐妹",

    # ---------- UY ----------
    "uy": "家",
    "xona": "房间",
    "eshik": "门",
    "deraza": "窗户",
    "devor": "墙",
    "pol": "地板",
    "shift": "天花板",
    "tom": "屋顶",
    "oshxona": "厨房",
    "yotoqxona": "卧室",
    "hammom": "浴室",
    "hojatxona": "厕所",
    "mehmonxona": "客厅",
    "stol": "桌子",
    "stul": "椅子",
    "karavot": "床",
    "divan": "沙发",
    "shkaf": "柜子",
    "oyna": "镜子",
    "chiroq": "灯",
    "televizor": "电视",
    "muzlatgich": "冰箱",
    "kir yuvish mashinasi": "洗衣机",
    "supurgi": "扫帚",

    # ---------- OVQAT ----------
    "ovqat": "食物",
    "non": "面包",
    "suv": "水",
    "choy": "茶",
    "qahva": "咖啡",
    "sut": "牛奶",
    "shakar": "糖",
    "tuz": "盐",
    "guruch": "米饭",
    "go'sht": "肉",
    "mol go'shti": "牛肉",
    "qo'y go'shti": "羊肉",
    "tovuq": "鸡肉",
    "baliq": "鱼",
    "tuxum": "鸡蛋",
    "olma": "苹果",
    "banan": "香蕉",
    "uzum": "葡萄",
    "apelsin": "橙子",
    "limon": "柠檬",
    "pomidor": "西红柿",
    "kartoshka": "土豆",
    "piyoz": "洋葱",
    "sabzi": "胡萝卜",
    "bodring": "黄瓜",
    "sho'rva": "汤",
    "salat": "沙拉",
    "nonushta": "早餐",
    "tushlik": "午餐",
    "kechki ovqat": "晚餐",

    # ---------- SAVDO ----------
    "do'kon": "商店",
    "bozor": "市场",
    "narx": "价格",
    "pul": "钱",
    "so'm": "苏姆",
    "dollar": "美元",
    "yevro": "欧元",
    "yuan": "元",
    "qimmat": "贵",
    "arzon": "便宜",
    "sotib olmoq": "购买",
    "sotmoq": "卖",
    "buyurtma": "订单",
    "chegirma": "折扣",
    "karta": "卡",
    "naqd pul": "现金",
    "to'lov": "付款",
    "chek": "收据",

    # ---------- TA'LIM ----------
    "maktab": "学校",
    "universitet": "大学",
    "sinf": "班级",
    "dars": "课",
    "kitob": "书",
    "daftar": "笔记本",
    "qalam": "笔",
    "ruchka": "钢笔",
    "o'qish": "学习",
    "yozish": "写",
    "savol": "问题",
    "javob": "答案",
    "imtihon": "考试",
    "vazifa": "作业",
    "fan": "科目",
    "matematika": "数学",
    "tarix": "历史",
    "ingliz tili": "英语",
    "xitoy tili": "中文",
    "o'zbek tili": "乌兹别克语",

    # ---------- IT ----------
    "kompyuter": "电脑",
    "telefon": "手机",
    "internet": "互联网",
    "sayt": "网站",
    "dastur": "程序",
    "kod": "代码",
    "dasturchi": "程序员",
    "fayl": "文件",
    "papka": "文件夹",
    "rasm": "图片",
    "video": "视频",
    "audio": "音频",
    "parol": "密码",
    "hisob": "账户",
    "server": "服务器",
    "ma'lumot": "信息",
    "baza": "数据库",
    "sun'iy intellekt": "人工智能",
    "robot": "机器人",

    # ---------- TRANSPORT ----------
    "mashina": "汽车",
    "avtomobil": "汽车",
    "avtobus": "公共汽车",
    "poyezd": "火车",
    "samolyot": "飞机",
    "velosiped": "自行车",
    "mototsikl": "摩托车",
    "taksi": "出租车",
    "yo'l": "道路",
    "ko'cha": "街道",
    "bekat": "车站",
    "aeroport": "机场",
    "chipta": "票",
    "haydamoq": "驾驶",
    "kelmoq": "来",
    "bormoq": "去",

    # ---------- JOYLAR ----------
    "shahar": "城市",
    "qishloq": "村庄",
    "mamlakat": "国家",
    "viloyat": "地区",
    "markaz": "中心",
    "mehmonxona": "酒店",
    "restoran": "餐厅",
    "kasalxona": "医院",
    "dorixona": "药店",
    "bank": "银行",
    "pochta": "邮局",
    "park": "公园",
    "masjid": "清真寺",

    # ---------- VAQT ----------
    "bugun": "今天",
    "kecha": "昨天",
    "ertaga": "明天",
    "hozir": "现在",
    "keyin": "以后",
    "oldin": "以前",
    "ertalab": "早上",
    "tush": "中午",
    "kechqurun": "晚上",
    "tun": "夜晚",
    "hafta": "星期",
    "oy": "月",
    "yil": "年",
    "kun": "天",
    "soat": "小时",
    "daqiqa": "分钟",
    "soniya": "秒",

    # ---------- SAVOLLAR ----------
    "nima": "什么",
    "kim": "谁",
    "qayer": "哪里",
    "qachon": "什么时候",
    "nega": "为什么",
    "qanday": "怎么样",
    "qancha": "多少",
    "qaysi": "哪个",
    "qayerda": "在哪里",
    "qayerga": "去哪里",

    # ---------- FE'LLAR ----------
    "bo'lmoq": "是",
    "qilmoq": "做",
    "olmoq": "拿",
    "bermoq": "给",
    "ko'rmoq": "看",
    "eshitmoq": "听",
    "gapirmoq": "说",
    "aytmoq": "说",
    "bilmoq": "知道",
    "tushunmoq": "理解",
    "xohlamoq": "想要",
    "yoqtirmoq": "喜欢",
    "sevmoq": "爱",
    "kutmoq": "等待",
    "ishlamoq": "工作",
    "yashamoq": "生活",
    "uxlamoq": "睡觉",
    "turmoq": "站",
    "o'tirmoq": "坐",
    "yemoq": "吃",
    "ichmoq": "喝",
    "yurmoq": "走",
    "yugurmoq": "跑",
    "o'ynamoq": "玩",
    "yozmoq": "写",
    "o'qimoq": "读",
    "o'rganmoq": "学习",
    "boshlamoq": "开始",
    "tugatmoq": "结束",
    "ochmoq": "打开",
    "yopmoq": "关闭",

    # ---------- SIFATLAR ----------
    "katta": "大",
    "kichik": "小",
    "uzun": "长",
    "qisqa": "短",
    "baland": "高",
    "past": "低",
    "tez": "快",
    "sekin": "慢",
    "yangi": "新",
    "eski": "旧",
    "issiq": "热",
    "sovuq": "冷",
    "toza": "干净",
    "iflos": "脏",
    "oson": "容易",
    "qiyin": "困难",
    "chiroyli": "漂亮",
    "xunuk": "丑",
    "muhim": "重要",
    "kerak": "需要",
    "tayyor": "准备好",
    "band": "忙",
    "bo'sh": "空",

    # ---------- SONLAR ----------
    "bir": "一",
    "ikki": "二",
    "uch": "三",
    "to'rt": "四",
    "besh": "五",
    "olti": "六",
    "yetti": "七",
    "sakkiz": "八",
    "to'qqiz": "九",
    "o'n": "十",
    "yuz": "一百",
    "ming": "一千",
    "million": "一百万",

    # ---------- KUNDALIK IBORALAR ----------
    "qalaysan": "你好吗",
    "ishlaring qalay": "你的工作怎么样",
    "hammasi yaxshi": "一切都很好",
    "men yaxshiman": "我很好",
    "isming nima": "你叫什么名字",
    "mening ismim": "我的名字是",
    "qayerdansan": "你来自哪里",
    "yordam bering": "请帮帮我",
    "menga yordam kerak": "我需要帮助",
    "bu nima": "这是什么",
    "bu qancha": "这个多少钱",
    "men tushunmadim": "我不明白",
    "yana ayting": "请再说一遍",
    "sekinroq gapiring": "请说慢一点",
    "xitoy tilini bilasizmi": "你会说中文吗",
    "ingliz tilini bilasizmi": "你会说英语吗",
    "muammo yo'q": "没问题",
    "ko'rishguncha": "再见",
}


# =========================================================
# 🇨🇳 → 🇺🇿 TESKARI LUG'AT
# =========================================================

CN_UZ = {}

for uzbek, xitoy in UZ_CN.items():
    if xitoy not in CN_UZ:
        CN_UZ[xitoy] = uzbek


# =========================================================
# MATN NORMALIZATSIYASI
# =========================================================

def normalize_text(text):
    if not text:
        return ""

    return text.strip().lower()


# =========================================================
# BIR SO'Z / IBORA TARJIMASI
# =========================================================

def translate_word(text, direction="uz_cn"):
    text = normalize_text(text)

    if direction == "uz_cn":
        return UZ_CN.get(text, text)

    if direction == "cn_uz":
        return CN_UZ.get(text, text)

    return text


# =========================================================
# GAP TARJIMASI
# =========================================================

def translate_text(text, direction="uz_cn"):
    text = text.strip()

    if not text:
        return ""

    # Avval to'liq iborani tekshiramiz
    result = translate_word(text, direction)

    if result != text.lower():
        return result

    dictionary = UZ_CN if direction == "uz_cn" else CN_UZ

    # Uzun iboralarni avval tekshirish
    sorted_words = sorted(
        dictionary.keys(),
        key=len,
        reverse=True
    )

    result = text

    for word in sorted_words:
        pattern = re.compile(
            r"(?<!\w)" + re.escape(word) + r"(?!\w)",
            re.IGNORECASE
        )

        result = pattern.sub(dictionary[word], result)

    return result


# =========================================================
# LUG'AT SONI
# =========================================================

def dictionary_count():
    return len(UZ_CN)


def get_dictionary():
    return UZ_CN


# =========================================================
# BOT
# =========================================================

dp = Dispatcher()


# Foydalanuvchining tarjima rejimi
user_modes = {}


# =========================================================
# KLAVIATURA
# =========================================================

def main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🇺🇿 → 🇨🇳 Tarjima"),
                KeyboardButton(text="🇨🇳 → 🇺🇿 Tarjima")
            ],
            [
                KeyboardButton(text="📊 Lug'at"),
                KeyboardButton(text="🆔 Mening ID")
            ],
            [
                KeyboardButton(text="ℹ️ Yordam")
            ]
        ],
        resize_keyboard=True
    )


# =========================================================
# START
# =========================================================

@dp.message(Command("start"))
async def start_handler(message: Message):

    user_modes[message.from_user.id] = "uz_cn"

    await message.answer(
        "🇺🇿🇨🇳 <b>UZ CN TARJIMON</b>\n\n"
        "API kerak emas.\n"
        "Offline lug'at orqali tarjima qiladi.\n\n"
        "🇺🇿 → 🇨🇳 O'zbekchadan xitoychaga\n"
        "🇨🇳 → 🇺🇿 Xitoychadan o'zbekchaga\n\n"
        "Pastdagi tugmalardan foydalaning.",
        reply_markup=main_keyboard(),
        parse_mode="HTML"
    )


# =========================================================
# UZ → CN
# =========================================================

@dp.message(F.text == "🇺🇿 → 🇨🇳 Tarjima")
async def uz_cn_mode(message: Message):

    user_modes[message.from_user.id] = "uz_cn"

    await message.answer(
        "🇺🇿 → 🇨🇳 rejim yoqildi.\n\n"
        "O'zbekcha so'z yoki gap yuboring."
    )


# =========================================================
# CN → UZ
# =========================================================

@dp.message(F.text == "🇨🇳 → 🇺🇿 Tarjima")
async def cn_uz_mode(message: Message):

    user_modes[message.from_user.id] = "cn_uz"

    await message.answer(
        "🇨🇳 → 🇺🇿 rejim yoqildi.\n\n"
        "Xitoycha so'z yoki gap yuboring."
    )


# =========================================================
# LUG'AT
# =========================================================

@dp.message(F.text == "📊 Lug'at")
async def dictionary_handler(message: Message):

    await message.answer(
        f"📚 Offline lug'at\n\n"
        f"🇺🇿 → 🇨🇳: {dictionary_count()} ta yozuv\n"
        f"🇨🇳 → 🇺🇿: {len(CN_UZ)} ta yozuv\n\n"
        f"API kerak emas."
    )


# =========================================================
# ID
# =========================================================

@dp.message(F.text == "🆔 Mening ID")
async def id_handler(message: Message):

    await message.answer(
        f"🆔 Sizning Telegram ID'ingiz:\n\n"
        f"<code>{message.from_user.id}</code>",
        parse_mode="HTML"
    )


# =========================================================
# YORDAM
# =========================================================

@dp.message(F.text == "ℹ️ Yordam")
async def help_handler(message: Message):

    await message.answer(
        "ℹ️ <b>UZ CN TARJIMON</b>\n\n"
        "1️⃣ 🇺🇿 → 🇨🇳 tugmasini bosing.\n"
        "2️⃣ O'zbekcha so'z yoki gap yuboring.\n"
        "3️⃣ Bot xitoycha tarjimasini chiqaradi.\n\n"
        "Yoki 🇨🇳 → 🇺🇿 rejimidan foydalaning.\n\n"
        "📚 Tarjima offline lug'at asosida ishlaydi.",
        parse_mode="HTML"
    )


# =========================================================
# MATN TARJIMASI
# =========================================================

@dp.message(F.text)
async def translate_handler(message: Message):

    text = message.text.strip()

    # Tugmalarni o'tkazib yuboramiz
    if text in [
        "🇺🇿 → 🇨🇳 Tarjima",
        "🇨🇳 → 🇺🇿 Tarjima",
        "📊 Lug'at",
        "🆔 Mening ID",
        "ℹ️ Yordam"
    ]:
        return

    user_id = message.from_user.id

    direction = user_modes.get(
        user_id,
        "uz_cn"
    )

    translated = translate_text(
        text,
        direction
    )

    if direction == "uz_cn":
        title = "🇺🇿 → 🇨🇳"
    else:
        title = "🇨🇳 → 🇺🇿"

    await message.answer(
        f"{title}\n\n"
        f"📥 {text}\n"
        f"📤 {translated}"
    )


# =========================================================
# BOTNI ISHGA TUSHIRISH
# =========================================================

async def start_bot(token):

    bot = Bot(token=token)

    print("===================================")
    print("🇺🇿🇨🇳 UZ CN TARJIMON")
    print("===================================")
    print(f"📚 Lug'at: {dictionary_count()} ta")
    print("🌐 API: KERAK EMAS")
    print("🤖 Bot ishga tushmoqda...")
    print("===================================")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


# =========================================================
# MAIN.PY UCHUN run_bot()
# =========================================================

def run_bot(token, admin_id=None):

    # admin_id keyinchalik admin funksiyalari uchun ishlatiladi
    if admin_id is not None:
        print(f"👤 Admin ID: {admin_id}")

    asyncio.run(
        start_bot(token)
    )

