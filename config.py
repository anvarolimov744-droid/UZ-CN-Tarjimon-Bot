# ============================================================
# 🇺🇿🇨🇳 UZ CN TARJIMON — config.py
# ============================================================

from aiogram import Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# ============================================================
# DICTIONARY
# ============================================================

UZ_CN = {
    "salom": "你好",
    "assalomu alaykum": "您好",
    "xayr": "再见",
    "rahmat": "谢谢",
    "iltimos": "请",
    "ha": "是",
    "yo‘q": "不",
    "yo'q": "不",
    "yaxshi": "好",
    "yomon": "坏",

    "men": "我",
    "sen": "你",
    "siz": "您",
    "u": "他",
    "biz": "我们",
    "ular": "他们",

    "nima": "什么",
    "kim": "谁",
    "qayer": "哪里",
    "qachon": "什么时候",
    "nega": "为什么",
    "qanday": "怎么样",

    "bugun": "今天",
    "ertaga": "明天",
    "kecha": "昨天",
    "hozir": "现在",
    "keyin": "以后",
    "ertalab": "早上",
    "tush": "中午",
    "kechqurun": "晚上",
    "tun": "夜晚",
    "kun": "天",
    "hafta": "星期",
    "oy": "月",
    "yil": "年",
    "vaqt": "时间",

    "ota": "父亲",
    "ona": "母亲",
    "aka": "哥哥",
    "uka": "弟弟",
    "opa": "姐姐",
    "singil": "妹妹",
    "oila": "家庭",
    "bola": "孩子",
    "o‘g‘il": "儿子",
    "qiz": "女儿",
    "do‘st": "朋友",
    "inson": "人",
    "odam": "人",

    "uy": "家",
    "xona": "房间",
    "eshik": "门",
    "deraza": "窗户",
    "stol": "桌子",
    "stul": "椅子",
    "karavot": "床",
    "oshxona": "厨房",
    "hammom": "浴室",
    "bog‘": "花园",

    "maktab": "学校",
    "universitet": "大学",
    "o‘qituvchi": "老师",
    "talaba": "学生",
    "o‘quvchi": "学生",
    "kitob": "书",
    "daftar": "笔记本",
    "qalam": "铅笔",
    "ruchka": "钢笔",
    "dars": "课",
    "savol": "问题",
    "javob": "答案",
    "imtihon": "考试",
    "bilim": "知识",

    "ish": "工作",
    "kasb": "职业",
    "shifokor": "医生",
    "muhandis": "工程师",
    "dasturchi": "程序员",
    "rahbar": "领导",
    "xodim": "员工",
    "firma": "公司",
    "kompaniya": "公司",

    "telefon": "手机",
    "kompyuter": "电脑",
    "internet": "互联网",
    "sayt": "网站",
    "dastur": "程序",
    "kod": "代码",
    "fayl": "文件",
    "rasm": "图片",
    "video": "视频",
    "audio": "音频",
    "xabar": "消息",
    "telegram": "电报",
    "google": "谷歌",

    "non": "面包",
    "suv": "水",
    "choy": "茶",
    "qahva": "咖啡",
    "sut": "牛奶",
    "go‘sht": "肉",
    "guruch": "米饭",
    "osh": "抓饭",
    "sho‘rva": "汤",
    "olma": "苹果",
    "banan": "香蕉",
    "uzum": "葡萄",
    "anor": "石榴",
    "meva": "水果",
    "sabzavot": "蔬菜",
    "tuz": "盐",
    "shakar": "糖",

    "katta": "大",
    "kichik": "小",
    "uzun": "长",
    "qisqa": "短",
    "yangi": "新",
    "eski": "旧",
    "tez": "快",
    "sekin": "慢",
    "issiq": "热",
    "sovuq": "冷",
    "chiroyli": "漂亮",
    "xunuk": "丑",
    "oson": "容易",
    "qiyin": "困难",
    "toza": "干净",
    "iflos": "脏",

    "bor": "有",
    "yo‘q": "没有",
    "kelmoq": "来",
    "ketmoq": "去",
    "bormoq": "去",
    "kelish": "来",
    "ko‘rmoq": "看",
    "eshitmoq": "听",
    "gapirmoq": "说",
    "yozmoq": "写",
    "o‘qimoq": "读",
    "yemoq": "吃",
    "ichmoq": "喝",
    "uxlamoq": "睡觉",
    "turmoq": "站",
    "o‘tirmoq": "坐",
    "yurmoq": "走",
    "yugurmoq": "跑",
    "olmoq": "拿",
    "bermoq": "给",
    "qilmoq": "做",
    "bilmoq": "知道",
    "xohlamoq": "想",
    "sevmoq": "爱",
    "kutmoq": "等",
    "topmoq": "找到",
    "yo‘qotmoq": "丢失",

    "bir": "一",
    "ikki": "二",
    "uch": "三",
    "to‘rt": "四",
    "besh": "五",
    "olti": "六",
    "yetti": "七",
    "sakkiz": "八",
    "to‘qqiz": "九",
    "o‘n": "十",
    "yuz": "一百",
    "ming": "一千",

    "pul": "钱",
    "narx": "价格",
    "bozor": "市场",
    "do‘kon": "商店",
    "sotuvchi": "卖家",
    "xaridor": "买家",
    "sotmoq": "卖",
    "sotib olmoq": "买",
    "buyurtma": "订单",
    "to‘lov": "付款",
    "bepul": "免费",
    "qimmat": "贵",
    "arzon": "便宜",

    "shahar": "城市",
    "qishloq": "村庄",
    "ko‘cha": "街道",
    "yo‘l": "道路",
    "mashina": "汽车",
    "avtomobil": "汽车",
    "avtobus": "公共汽车",
    "poyezd": "火车",
    "samolyot": "飞机",
    "aeroport": "机场",
    "mehmonxona": "酒店",
    "sayohat": "旅行",
    "mamlakat": "国家",

    "O‘zbekiston": "乌兹别克斯坦",
    "Xitoy": "中国",
    "Rossiya": "俄罗斯",
    "AQSh": "美国",
    "Turkiya": "土耳其",
    "Qozog‘iston": "哈萨克斯坦",
    "Qirg‘iziston": "吉尔吉斯斯坦",
    "Tojikiston": "塔吉克斯坦",

    "sog‘liq": "健康",
    "kasal": "生病",
    "kasallik": "疾病",
    "shifoxona": "医院",
    "dori": "药",

    "bosh": "头",
    "ko‘z": "眼睛",
    "quloq": "耳朵",
    "burun": "鼻子",
    "og‘iz": "嘴",
    "qo‘l": "手",
    "oyoq": "脚",
    "yurak": "心脏",
    "sog‘lom": "健康",

    "baxt": "幸福",
    "baxtli": "幸福的",
    "xursand": "高兴",
    "g‘amgin": "悲伤",
    "qo‘rqmoq": "害怕",
    "umid": "希望",
    "orzu": "梦想",
    "muammo": "问题",
    "yordam": "帮助",
    "kerak": "需要",
    "mumkin": "可以",
    "mumkin emas": "不可以",

    "rang": "颜色",
    "qizil": "红色",
    "ko‘k": "蓝色",
    "yashil": "绿色",
    "sariq": "黄色",
    "oq": "白色",
    "qora": "黑色",
    "jigarrang": "棕色",

    "ob-havo": "天气",
    "quyosh": "太阳",
    "oy": "月亮",
    "yulduz": "星星",
    "osmon": "天空",
    "yomg‘ir": "雨",
    "qor": "雪",
    "shamol": "风",
    "bulut": "云",

    "telefon raqami": "电话号码",
    "manzil": "地址",
    "ism": "名字",
    "familiya": "姓氏",
    "yosh": "年龄",
    "erkak": "男人",
    "ayol": "女人",
    "janob": "先生",
    "xonim": "女士",

    "birinchi": "第一",
    "ikkinchi": "第二",
    "uchinchi": "第三",
    "oxirgi": "最后",
    "oldin": "以前",
    "keyin": "以后",
    "ichida": "里面",
    "tashqarida": "外面",
    "yuqori": "上面",
    "past": "下面",
    "chap": "左",
    "o‘ng": "右",

    "kunduz": "白天",
    "kechasi": "晚上",
    "hafta kuni": "工作日",

    "dushanba": "星期一",
    "seshanba": "星期二",
    "chorshanba": "星期三",
    "payshanba": "星期四",
    "juma": "星期五",
    "shanba": "星期六",
    "yakshanba": "星期日",

    "yanvar": "一月",
    "fevral": "二月",
    "mart": "三月",
    "aprel": "四月",
    "may": "五月",
    "iyun": "六月",
    "iyul": "七月",
    "avgust": "八月",
    "sentabr": "九月",
    "oktabr": "十月",
    "noyabr": "十一月",
    "dekabr": "十二月",

    "til": "语言",
    "o‘zbek": "乌兹别克语",
    "xitoy": "中文",
    "rus": "俄语",
    "ingliz": "英语",
    "tarjima": "翻译",
    "tarjimon": "翻译员",
    "lug‘at": "词典",
    "so‘z": "单词",
    "gap": "句子",
    "ma’no": "意思",

    "ochmoq": "打开",
    "yopmoq": "关闭",
    "yoqmoq": "打开",
    "o‘chirmoq": "关闭",
    "bosmoq": "按",
    "qidirish": "搜索",
    "saqlamoq": "保存",
    "yubormoq": "发送",
    "qabul qilmoq": "接收",
    "ulanish": "连接",
    "yuklash": "下载",
    "yuklamoq": "上传",

    "rasmga olish": "拍照",
    "kamera": "相机",
    "mikrofon": "麦克风",
    "ovoz": "声音",
    "tinglamoq": "听",
    "matn": "文本",
    "belgi": "符号",
    "raqam": "数字",

    "xavfsiz": "安全",
    "xavf": "危险",
    "ehtiyot": "小心",
    "muhim": "重要",
    "to‘g‘ri": "正确",
    "noto‘g‘ri": "错误",
    "tayyor": "准备好了",
    "boshla": "开始",
    "tugatmoq": "结束",
}


# ============================================================
# REVERSE DICTIONARY
# ============================================================

CN_UZ = {}

for uz, cn in UZ_CN.items():
    if cn not in CN_UZ:
        CN_UZ[cn] = uz


# ============================================================
# NORMALIZE
# ============================================================

def normalize_text(text: str) -> str:
    return (
        text.lower()
        .strip()
        .replace("’", "'")
        .replace("‘", "'")
        .replace("ʻ", "'")
    )


# ============================================================
# ONE WORD TRANSLATION
# ============================================================

def translate_word(
    text: str,
    direction: str = "uz_cn"
) -> str:

    original = text.strip()
    key = normalize_text(original)

    dictionary = (
        UZ_CN
        if direction == "uz_cn"
        else CN_UZ
    )

    if key in dictionary:
        return dictionary[key]

    cleaned = key.strip(
        ".,!?;:()[]{}\""
    )

    if cleaned in dictionary:
        return dictionary[cleaned]

    return ""


# ============================================================
# TEXT TRANSLATION
# ============================================================

def translate_text(
    text: str,
    direction: str = "uz_cn"
) -> str:

    text = text.strip()

    if not text:
        return ""

    direct = translate_word(
        text,
        direction
    )

    if direct:
        return direct

    dictionary = (
        UZ_CN
        if direction == "uz_cn"
        else CN_UZ
    )

    words = text.split()
    result = []

    for word in words:

        clean = word.strip(
            ".,!?;:()[]{}\""
        )

        translated = dictionary.get(
            normalize_text(clean)
        )

        if translated:
            result.append(translated)
        else:
            result.append(word)

    return " ".join(result)


# ============================================================
# DICTIONARY INFO
# ============================================================

def dictionary_count() -> int:
    return len(UZ_CN)


def get_dictionary():
    return UZ_CN


# ============================================================
# BOT
# ============================================================

dp = Dispatcher()

user_modes = {}
user_stats = {}
dictionary_pages = {}

WORDS_PER_PAGE = 100


# ============================================================
# MAIN MENU
# ============================================================

def main_keyboard():

    keyboard = ReplyKeyboardBuilder()

    keyboard.button(
        text="🇺🇿 → 🇨🇳 Tarjima"
    )

    keyboard.button(
        text="🇨🇳 → 🇺🇿 Tarjima"
    )

    keyboard.button(
        text="🔄 Yo‘nalishni almashtirish"
    )

    keyboard.button(
        text="📚 Lug‘at"
    )

    keyboard.button(
        text="📊 Statistikam"
    )

    keyboard.button(
        text="ℹ️ Yordam"
    )

    keyboard.adjust(2, 2, 2)

    return keyboard.as_markup(
        resize_keyboard=True,
        is_persistent=True
    )


# ============================================================
# DICTIONARY MENU
# ============================================================

def dictionary_keyboard():

    keyboard = ReplyKeyboardBuilder()

    keyboard.button(
        text="🔎 So‘z qidirish"
    )

    keyboard.button(
        text="📖 Barcha so‘zlar"
    )

    keyboard.button(
        text="🇺🇿 → 🇨🇳 O‘zbekcha → Xitoycha"
    )

    keyboard.button(
        text="🇨🇳 → 🇺🇿 Xitoycha → O‘zbekcha"
    )

    keyboard.button(
        text="⬅️ Bosh menyu"
    )

    keyboard.adjust(1, 1, 1, 1, 1)

    return keyboard.as_markup(
        resize_keyboard=True,
        is_persistent=True
    )


# ============================================================
# PAGINATION
# ============================================================

def page_keyboard(
    current_page: int,
    total_pages: int
):

    builder = ReplyKeyboardBuilder()

    if current_page > 1:
        builder.button(
            text="⬅️ Oldingi"
        )

    if current_page < total_pages:
        builder.button(
            text="➡️ Keyingi"
        )

    builder.button(
        text="📚 Lug‘at menyusi"
    )

    builder.adjust(2, 1)

    return builder.as_markup(
        resize_keyboard=True,
        is_persistent=True
    )


# ============================================================
# START
# ============================================================

@dp.message(Command("start"))
async def start_handler(
    message: Message
):

    user_id = message.from_user.id

    user_modes[user_id] = "uz_cn"

    if user_id not in user_stats:
        user_stats[user_id] = {
            "translations": 0,
            "uz_cn": 0,
            "cn_uz": 0
        }

    await message.answer(
        "Assalomu alaykum! 👋\n\n"
        "/start\n\n"
        "🇺🇿 → 🇨🇳 Tarjima\n"
        "🇨🇳 → 🇺🇿 Tarjima\n"
        "🔄 Yo‘nalishni almashtirish\n"
        "📚 Lug‘at\n"
        "📊 Statistikam\n"
        "ℹ️ Yordam",
        reply_markup=main_keyboard()
    )


# ============================================================
# UZ → CN
# ============================================================

@dp.message(
    F.text == "🇺🇿 → 🇨🇳 Tarjima"
)
async def uz_cn_button(
    message: Message
):

    user_modes[
        message.from_user.id
    ] = "uz_cn"

    await message.answer(
        "🇺🇿 → 🇨🇳 tarjima rejimi yoqildi.\n\n"
        "O‘zbekcha so‘z yoki gap yuboring."
    )


# ============================================================
# CN → UZ
# ============================================================

@dp.message(
    F.text == "🇨🇳 → 🇺🇿 Tarjima"
)
async def cn_uz_button(
    message: Message
):

    user_modes[
        message.from_user.id
    ] = "cn_uz"

    await message.answer(
        "🇨🇳 → 🇺🇿 tarjima rejimi yoqildi.\n\n"
        "Xitoycha so‘z yoki gap yuboring."
    )


# ============================================================
# CHANGE DIRECTION
# ============================================================

@dp.message(
    F.text == "🔄 Yo‘nalishni almashtirish"
)
async def change_direction(
    message: Message
):

    user_id = message.from_user.id

    current = user_modes.get(
        user_id,
        "uz_cn"
    )

    if current == "uz_cn":

        user_modes[user_id] = "cn_uz"

        await message.answer(
            "🔄 Yo‘nalish almashtirildi.\n\n"
            "🇨🇳 → 🇺🇿\n"
            "Xitoycha matn yuboring."
        )

    else:

        user_modes[user_id] = "uz_cn"

        await message.answer(
            "🔄 Yo‘nalish almashtirildi.\n\n"
            "🇺🇿 → 🇨🇳\n"
            "O‘zbekcha matn yuboring."
        )


# ============================================================
# DICTIONARY MENU
# ============================================================

@dp.message(F.text == "📚 Lug‘at")
async def dictionary_menu(
    message: Message
):

    await message.answer(
        "📚 LUG‘AT\n\n"
        f"Jami: {dictionary_count()} ta so‘z\n\n"
        "🔎 So‘z qidirish\n"
        "📖 Barcha so‘zlar\n"
        "🇺🇿 → 🇨🇳 O‘zbekcha → Xitoycha\n"
        "🇨🇳 → 🇺🇿 Xitoycha → O‘zbekcha\n"
        "⬅️ Bosh menyu",
        reply_markup=dictionary_keyboard()
    )


# ============================================================
# SEARCH MODE
# ============================================================

@dp.message(
    F.text == "🔎 So‘z qidirish"
)
async def dictionary_search_start(
    message: Message
):

    user_modes[
        message.from_user.id
    ] = "search"

    await message.answer(
        "🔎 So‘z qidirish\n\n"
        "O‘zbekcha yoki xitoycha so‘zni yuboring."
    )


# ============================================================
# SHOW DICTIONARY PAGE
# ============================================================

async def show_dictionary_page(
    message: Message,
    page: int = 1,
    direction: str = "uz_cn"
):

    dictionary = (
        UZ_CN
        if direction == "uz_cn"
        else CN_UZ
    )

    items = list(
        dictionary.items()
    )

    total = len(items)

    total_pages = max(
        1,
        (
            total
            + WORDS_PER_PAGE
            - 1
        )
        // WORDS_PER_PAGE
    )

    page = max(
        1,
        min(page, total_pages)
    )

    start = (
        page - 1
    ) * WORDS_PER_PAGE

    end = (
        start
        + WORDS_PER_PAGE
    )

    selected = items[start:end]

    title = (
        "🇺🇿 → 🇨🇳"
        if direction == "uz_cn"
        else "🇨🇳 → 🇺🇿"
    )

    lines = [
        f"📖 LUG‘AT {title}",
        "",
        f"📄 Sahifa: {page}/{total_pages}",
        f"📚 Jami: {total} ta",
        ""
    ]

    for index, (
        word,
        translation
    ) in enumerate(
        selected,
        start=start + 1
    ):

        lines.append(
            f"{index}. {word} → {translation}"
        )

    await message.answer(
        "\n".join(lines),
        reply_markup=page_keyboard(
            page,
            total_pages
        )
    )

    dictionary_pages[
        message.from_user.id
    ] = {
        "page": page,
        "direction": direction
    }


# ============================================================
# ALL WORDS
# ============================================================

@dp.message(
    F.text == "📖 Barcha so‘zlar"
)
async def all_words(
    message: Message
):

    await show_dictionary_page(
        message,
        page=1,
        direction="uz_cn"
    )


# ============================================================
# UZ → CN DICTIONARY
# ============================================================

@dp.message(
    F.text == "🇺🇿 → 🇨🇳 O‘zbekcha → Xitoycha"
)
async def dictionary_uz_cn(
    message: Message
):

    await show_dictionary_page(
        message,
        page=1,
        direction="uz_cn"
    )


# ============================================================
# CN → UZ DICTIONARY
# ============================================================

@dp.message(
    F.text == "🇨🇳 → 🇺🇿 Xitoycha → O‘zbekcha"
)
async def dictionary_cn_uz(
    message: Message
):

    await show_dictionary_page(
        message,
        page=1,
        direction="cn_uz"
    )


# ============================================================
# NEXT PAGE
# ============================================================

@dp.message(
    F.text == "➡️ Keyingi"
)
async def next_page(
    message: Message
):

    user_id = message.from_user.id

    data = dictionary_pages.get(
        user_id,
        {
            "page": 1,
            "direction": "uz_cn"
        }
    )

    dictionary = (
        UZ_CN
        if data["direction"] == "uz_cn"
        else CN_UZ
    )

    total_pages = max(
        1,
        (
            len(dictionary)
            + WORDS_PER_PAGE
            - 1
        )
        // WORDS_PER_PAGE
    )

    next_page_number = (
        data["page"] + 1
    )

    if next_page_number > total_pages:
        next_page_number = total_pages

    await show_dictionary_page(
        message,
        next_page_number,
        data["direction"]
    )


# ============================================================
# PREVIOUS PAGE
# ============================================================

@dp.message(
    F.text == "⬅️ Oldingi"
)
async def previous_page(
    message: Message
):

    user_id = message.from_user.id

    data = dictionary_pages.get(
        user_id,
        {
            "page": 1,
            "direction": "uz_cn"
        }
    )

    previous_page_number = max(
        1,
        data["page"] - 1
    )

    await show_dictionary_page(
        message,
        previous_page_number,
        data["direction"]
    )


# ============================================================
# BACK TO DICTIONARY
# ============================================================

@dp.message(
    F.text == "📚 Lug‘at menyusi"
)
async def dictionary_back(
    message: Message
):

    await message.answer(
        "📚 LUG‘AT\n\n"
        f"Jami: {dictionary_count()} ta so‘z",
        reply_markup=dictionary_keyboard()
    )


# ============================================================
# BACK TO MAIN
# ============================================================

@dp.message(
    F.text == "⬅️ Bosh menyu"
)
async def back_main(
    message: Message
):

    user_modes[
        message.from_user.id
    ] = "uz_cn"

    await message.answer(
        "🏠 Bosh menyu",
        reply_markup=main_keyboard()
    )


# ============================================================
# STATISTICS
# ============================================================

@dp.message(
    F.text == "📊 Statistikam"
)
async def statistics(
    message: Message
):

    user_id = message.from_user.id

    stats = user_stats.get(
        user_id,
        {
            "translations": 0,
            "uz_cn": 0,
            "cn_uz": 0
        }
    )

    await message.answer(
        "📊 STATISTIKAM\n\n"
        f"👤 ID: {user_id}\n"
        f"🔤 Tarjimalar: {stats['translations']}\n"
        f"🇺🇿 → 🇨🇳: {stats['uz_cn']}\n"
        f"🇨🇳 → 🇺🇿: {stats['cn_uz']}\n"
        f"📚 Lug‘at: {dictionary_count()} ta so‘z"
    )


# ============================================================
# HELP
# ============================================================

@dp.message(
    F.text == "ℹ️ Yordam"
)
async def help_handler(
    message: Message
):

    await message.answer(
        "ℹ️ YORDAM\n\n"
        "🇺🇿 → 🇨🇳 — O‘zbekchadan xitoychaga\n"
        "🇨🇳 → 🇺🇿 — Xitoychadan o‘zbekchaga\n"
        "🔄 — Tarjima yo‘nalishini almashtirish\n"
        "📚 — Lug‘at\n"
        "🔎 — So‘z qidirish\n"
        "📊 — Statistikangiz\n\n"
        "Misol:\n"
        "salom\n"
        "rahmat\n"
        "kitob\n"
        "maktab"
    )


# ============================================================
# TRANSLATION MESSAGE
# ============================================================

@dp.message()
async def translate_handler(
    message: Message
):

    text = message.text

    if not text:
        return

    menu_buttons = {
        "🇺🇿 → 🇨🇳 Tarjima",
        "🇨🇳 → 🇺🇿 Tarjima",
        "🔄 Yo‘nalishni almashtirish",
        "📚 Lug‘at",
        "📊 Statistikam",
        "ℹ️ Yordam",
        "🔎 So‘z qidirish",
        "📖 Barcha so‘zlar",
        "🇺🇿 → 🇨🇳 O‘zbekcha → Xitoycha",
        "🇨🇳 → 🇺🇿 Xitoycha → O‘zbekcha",
        "⬅️ Bosh menyu",
        "➡️ Keyingi",
        "⬅️ Oldingi",
        "📚 Lug‘at menyusi"
    }

    if text in menu_buttons:
        return

    user_id = message.from_user.id

    mode = user_modes.get(
        user_id,
        "uz_cn"
    )

    # ========================================================
    # SEARCH
    # ========================================================

    if mode == "search":

        key = normalize_text(text)

        found = []

        for uz, cn in UZ_CN.items():

            if (
                key in normalize_text(uz)
                or key in normalize_text(cn)
            ):

                found.append(
                    f"• {uz} → {cn}"
                )

        for cn, uz in CN_UZ.items():

            if (
                key in normalize_text(cn)
                or key in normalize_text(uz)
            ):

                line = f"• {cn} → {uz}"

                if line not in found:
                    found.append(line)

        if found:

            await message.answer(
                "🔎 QIDIRUV NATIJASI\n\n"
                + "\n".join(
                    found[:50]
                )
            )

        else:

            await message.answer(
                "❌ Bu so‘z lug‘atdan topilmadi."
            )

        return

    # ========================================================
    # TRANSLATE
    # ========================================================

    result = translate_text(
        text,
        direction=mode
    )

    if user_id not in user_stats:

        user_stats[user_id] = {
            "translations": 0,
            "uz_cn": 0,
            "cn_uz": 0
        }

    user_stats[user_id][
        "translations"
    ] += 1

    if mode == "uz_cn":

        user_stats[user_id][
            "uz_cn"
        ] += 1

        await message.answer(
            "🇺🇿 → 🇨🇳\n\n"
            f"📝 {text}\n"
            f"➡️ {result}"
        )

    else:

        user_stats[user_id][
            "cn_uz"
        ] += 1

        await message.answer(
            "🇨🇳 → 🇺🇿\n\n"
            f"📝 {text}\n"
            f"➡️ {result}"
        )


# ============================================================
# START BOT
# ============================================================

async def start_bot(
    token: str
):

    from aiogram import Bot

    bot = Bot(
        token=token
    )

    print(
        "==================================="
    )
    print(
        "🇺🇿🇨🇳 UZ CN TARJIMON"
    )
    print(
        "==================================="
    )
    print(
        f"📚 Lug'at: {dictionary_count()} ta"
    )
    print(
        "🌐 API: KERAK EMAS"
    )
    print(
        "🤖 Bot ishga tushmoqda..."
    )
    print(
        "==================================="
    )

    try:

        await dp.start_polling(
            bot
        )

    finally:

        await bot.session.close()


# ============================================================
# RUN BOT — RENDER UCHUN TO‘G‘RI
# MUHIM: BU YERDA asyncio.run() YO‘Q
# ============================================================

async def run_bot(
    token: str,
    admin_id: int | None = None
):

    if admin_id is not None:

        print(
            f"👤 Admin ID: {admin_id}"
        )

    await start_bot(
        token
    )