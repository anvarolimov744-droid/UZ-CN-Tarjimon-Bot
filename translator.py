
# ============================================================
# 🌐 TARJIMON SUPER BOT
# 🇺🇿 O'ZBEKCHA ↔ 🇨🇳 XITOYCHA
# Offline lug'at asosidagi tarjimon
# ============================================================

import re


# ============================================================
# 🇺🇿 → 🇨🇳 SO'ZLAR
# ============================================================

UZ_ZH = {
    # -------------------------
    # Salomlashish
    # -------------------------
    "salom": "你好",
    "assalomu alaykum": "您好",
    "alaykum assalom": "您好",
    "xayr": "再见",
    "rahmat": "谢谢",
    "katta rahmat": "非常感谢",
    "iltimos": "请",
    "kechirasiz": "对不起",
    "uzr": "抱歉",
    "marhamat": "不客气",
    "xo'p": "好的",
    "mayli": "可以",
    "ha": "是",
    "yo'q": "不是",
    "albatta": "当然",
    "balki": "也许",
    "yaxshi": "很好",
    "zo'r": "很好",
    "ajoyib": "太棒了",
    "yomon": "不好",

    # -------------------------
    # Kishilar
    # -------------------------
    "men": "我",
    "sen": "你",
    "siz": "您",
    "u": "他",
    "u ayol": "她",
    "biz": "我们",
    "sizlar": "你们",
    "ular": "他们",
    "odam": "人",
    "odamlar": "人们",
    "bola": "孩子",
    "bolalar": "孩子们",
    "erkak": "男人",
    "ayol": "女人",
    "o'g'il": "儿子",
    "qiz": "女儿",
    "do'st": "朋友",
    "do'stlar": "朋友们",
    "qo'shni": "邻居",
    "mehmon": "客人",
    "o'qituvchi": "老师",
    "o'quvchi": "学生",
    "talaba": "大学生",
    "shifokor": "医生",
    "hamshira": "护士",
    "politsiyachi": "警察",
    "haydovchi": "司机",
    "muhandis": "工程师",
    "dasturchi": "程序员",
    "ishchi": "工人",
    "rahbar": "领导",

    # -------------------------
    # Oila
    # -------------------------
    "oila": "家庭",
    "ota": "父亲",
    "ona": "母亲",
    "dada": "爸爸",
    "ona": "妈妈",
    "aka": "哥哥",
    "uka": "弟弟",
    "opa": "姐姐",
    "singil": "妹妹",
    "er": "丈夫",
    "xotin": "妻子",
    "bobo": "爷爷",
    "buvi": "奶奶",
    "amaki": "叔叔",
    "tog'a": "舅舅",
    "amma": "姑姑",
    "xola": "阿姨",
    "ota-ona": "父母",

    # -------------------------
    # Uy
    # -------------------------
    "uy": "家",
    "xona": "房间",
    "yotoqxona": "卧室",
    "oshxona": "厨房",
    "hammom": "浴室",
    "hojatxona": "厕所",
    "eshik": "门",
    "deraza": "窗户",
    "stol": "桌子",
    "stul": "椅子",
    "karavot": "床",
    "divan": "沙发",
    "televizor": "电视",
    "muzlatgich": "冰箱",
    "pech": "炉子",
    "chiroq": "灯",
    "kalit": "钥匙",
    "devor": "墙",
    "pol": "地板",
    "shift": "天花板",
    "bog'": "花园",

    # -------------------------
    # Maktab / ta'lim
    # -------------------------
    "maktab": "学校",
    "universitet": "大学",
    "kollej": "学院",
    "dars": "课",
    "darslik": "教材",
    "kitob": "书",
    "daftar": "笔记本",
    "qalam": "铅笔",
    "ruchka": "钢笔",
    "o'chirg'ich": "橡皮",
    "sumka": "书包",
    "doska": "黑板",
    "sinf": "班级",
    "imtihon": "考试",
    "savol": "问题",
    "javob": "答案",
    "uy vazifasi": "家庭作业",
    "bilim": "知识",
    "fan": "学科",
    "matematika": "数学",
    "fizika": "物理",
    "kimyo": "化学",
    "biologiya": "生物",
    "tarix": "历史",
    "geografiya": "地理",
    "ingliz tili": "英语",
    "xitoy tili": "中文",
    "o'rganish": "学习",
    "o'qish": "阅读",
    "yozish": "写作",

    # -------------------------
    # Ovqat
    # -------------------------
    "ovqat": "食物",
    "non": "面包",
    "guruch": "米饭",
    "osh": "抓饭",
    "sho'rva": "汤",
    "go'sht": "肉",
    "mol go'shti": "牛肉",
    "qo'y go'shti": "羊肉",
    "tovuq": "鸡肉",
    "baliq": "鱼",
    "tuxum": "鸡蛋",
    "sut": "牛奶",
    "pishloq": "奶酪",
    "yog'": "油",
    "tuz": "盐",
    "shakar": "糖",
    "meva": "水果",
    "sabzavot": "蔬菜",
    "olma": "苹果",
    "banan": "香蕉",
    "uzum": "葡萄",
    "apelsin": "橙子",
    "limon": "柠檬",
    "kartoshka": "土豆",
    "pomidor": "西红柿",
    "bodring": "黄瓜",
    "sabzi": "胡萝卜",
    "choy": "茶",
    "qahva": "咖啡",
    "suv": "水",
    "sharbat": "果汁",
    "nonushta": "早餐",
    "tushlik": "午餐",
    "kechki ovqat": "晚餐",
    "mazali": "好吃",
    "och": "饿",
    "chanqagan": "渴",

    # -------------------------
    # Shahar / joylar
    # -------------------------
    "shahar": "城市",
    "qishloq": "村庄",
    "ko'cha": "街道",
    "yo'l": "道路",
    "bozor": "市场",
    "do'kon": "商店",
    "supermarket": "超市",
    "restoran": "餐厅",
    "mehmonxona": "酒店",
    "kasalxona": "医院",
    "dorixona": "药店",
    "bank": "银行",
    "pochta": "邮局",
    "aeroport": "机场",
    "vokzal": "车站",
    "masjid": "清真寺",
    "park": "公园",
    "stadion": "体育场",
    "kutubxona": "图书馆",
    "muzey": "博物馆",

    # -------------------------
    # Transport
    # -------------------------
    "mashina": "汽车",
    "avtomobil": "汽车",
    "avtobus": "公共汽车",
    "poyezd": "火车",
    "samolyot": "飞机",
    "velosiped": "自行车",
    "mototsikl": "摩托车",
    "taksi": "出租车",
    "metro": "地铁",
    "kema": "船",
    "haydash": "驾驶",
    "bekat": "车站",
    "yoqilg'i": "燃料",
    "benzin": "汽油",
    "g'ildirak": "车轮",

    # -------------------------
    # Texnologiya
    # -------------------------
    "telefon": "手机",
    "kompyuter": "电脑",
    "noutbuk": "笔记本电脑",
    "internet": "互联网",
    "sayt": "网站",
    "dastur": "程序",
    "ilova": "应用程序",
    "kod": "代码",
    "dasturlash": "编程",
    "python": "Python",
    "javascript": "JavaScript",
    "html": "HTML",
    "css": "CSS",
    "server": "服务器",
    "ma'lumot": "数据",
    "fayl": "文件",
    "papka": "文件夹",
    "rasm": "图片",
    "video": "视频",
    "kamera": "相机",
    "internet tarmog'i": "互联网网络",
    "parol": "密码",
    "akkaunt": "账户",
    "profil": "个人资料",
    "telegram": "Telegram",
    "bot": "机器人",
    "sun'iy intellekt": "人工智能",
    "ai": "人工智能",

    # -------------------------
    # Ish
    # -------------------------
    "ish": "工作",
    "kasb": "职业",
    "lavozim": "职位",
    "ofis": "办公室",
    "firma": "公司",
    "kompaniya": "公司",
    "pul": "钱",
    "maosh": "工资",
    "rahbar": "经理",
    "mijoz": "客户",
    "uchrashuv": "会议",
    "reja": "计划",
    "loyiha": "项目",
    "vazifa": "任务",
    "natija": "结果",
    "muvaffaqiyat": "成功",
    "muammo": "问题",
    "yechim": "解决方案",

    # -------------------------
    # Tana / sog'liq
    # -------------------------
    "bosh": "头",
    "ko'z": "眼睛",
    "quloq": "耳朵",
    "burun": "鼻子",
    "og'iz": "嘴",
    "tish": "牙齿",
    "qo'l": "手",
    "oyoq": "脚",
    "yurak": "心脏",
    "qorin": "肚子",
    "orqa": "背",
    "soch": "头发",
    "yuz": "脸",
    "sog'liq": "健康",
    "kasal": "生病",
    "shifokor": "医生",
    "dori": "药",
    "og'riq": "疼痛",
    "isitma": "发烧",

    # -------------------------
    # Tabiat
    # -------------------------
    "tabiat": "自然",
    "daraxt": "树",
    "gul": "花",
    "o'simlik": "植物",
    "hayvon": "动物",
    "it": "狗",
    "mushuk": "猫",
    "qush": "鸟",
    "ot": "马",
    "sigir": "牛",
    "qo'y": "羊",
    "tovuq": "鸡",
    "baliq": "鱼",
    "tog'": "山",
    "daryo": "河流",
    "ko'l": "湖",
    "dengiz": "海",
    "o'rmon": "森林",
    "osmon": "天空",
    "quyosh": "太阳",
    "oy": "月亮",
    "yulduz": "星星",
    "yomg'ir": "雨",
    "qor": "雪",
    "shamol": "风",
    "bulut": "云",

    # -------------------------
    # Vaqt
    # -------------------------
    "bugun": "今天",
    "ertaga": "明天",
    "kecha": "昨天",
    "hozir": "现在",
    "keyin": "以后",
    "oldin": "以前",
    "ertalab": "早上",
    "tush": "中午",
    "kechqurun": "晚上",
    "tun": "夜晚",
    "kun": "天",
    "hafta": "星期",
    "oy": "月",
    "yil": "年",
    "vaqt": "时间",
    "soat": "小时",
    "daqiqa": "分钟",
    "soniya": "秒",

    # -------------------------
    # Hafta kunlari
    # -------------------------
    "dushanba": "星期一",
    "seshanba": "星期二",
    "chorshanba": "星期三",
    "payshanba": "星期四",
    "juma": "星期五",
    "shanba": "星期六",
    "yakshanba": "星期日",

    # -------------------------
    # Oylar
    # -------------------------
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

    # -------------------------
    # Savol so'zlari
    # -------------------------
    "nima": "什么",
    "kim": "谁",
    "qayer": "哪里",
    "qayerda": "在哪里",
    "qayerga": "去哪里",
    "qachon": "什么时候",
    "nega": "为什么",
    "nima uchun": "为什么",
    "qanday": "怎么样",
    "qaysi": "哪个",
    "qancha": "多少",
    "nechta": "多少个",
    "necha": "多少",

    # -------------------------
    # Sifatlar
    # -------------------------
    "katta": "大",
    "kichik": "小",
    "uzun": "长",
    "qisqa": "短",
    "baland": "高",
    "past": "低",
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
    "boy": "富有",
    "kambag'al": "贫穷",
    "to'g'ri": "正确",
    "noto'g'ri": "错误",

    # -------------------------
    # Fe'llar
    # -------------------------
    "borish": "去",
    "kelish": "来",
    "ketish": "离开",
    "ko'rish": "看",
    "eshitish": "听",
    "gapirish": "说",
    "aytish": "说",
    "so'rash": "问",
    "berish": "给",
    "olish": "拿",
    "yeyish": "吃",
    "ichish": "喝",
    "uxlash": "睡觉",
    "turish": "起床",
    "o'tirish": "坐",
    "yurish": "走",
    "yugurish": "跑",
    "o'ynash": "玩",
    "ishlash": "工作",
    "o'qish": "学习",
    "yozish": "写",
    "o'qimoq": "读",
    "kutish": "等待",
    "sevish": "爱",
    "xohlash": "想要",
    "bilish": "知道",
    "tushunish": "理解",
    "yordam berish": "帮助",
    "boshlash": "开始",
    "tugatish": "结束",
    "ochish": "打开",
    "yopish": "关闭",
    "qidirish": "搜索",
    "topish": "找到",
    "yo'qotish": "丢失",
    "sotib olish": "购买",
    "sotish": "卖",
    "to'lash": "付款",

    # -------------------------
    # Raqamlar
    # -------------------------
    "nol": "零",
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
    "yigirma": "二十",
    "o'ttiz": "三十",
    "qirq": "四十",
    "ellik": "五十",
    "oltmish": "六十",
    "yetmish": "七十",
    "sakson": "八十",
    "to'qson": "九十",
    "yuz": "一百",
    "ming": "一千",
    "million": "一百万",

    # -------------------------
    # O'zbekiston / davlatlar
    # -------------------------
    "o'zbekiston": "乌兹别克斯坦",
    "xitoy": "中国",
    "rossiya": "俄罗斯",
    "amerika": "美国",
    "angliya": "英国",
    "germaniya": "德国",
    "fransiya": "法国",
    "italiya": "意大利",
    "ispaniya": "西班牙",
    "turkiya": "土耳其",
    "qozog'iston": "哈萨克斯坦",
    "qirg'iziston": "吉尔吉斯斯坦",
    "tojikiston": "塔吉克斯坦",
    "koreya": "韩国",
    "yaponiya": "日本",
    "hindiston": "印度",

    # -------------------------
    # Ranglar
    # -------------------------
    "oq": "白色",
    "qora": "黑色",
    "qizil": "红色",
    "yashil": "绿色",
    "ko'k": "蓝色",
    "sariq": "黄色",
    "jigarrang": "棕色",
    "kulrang": "灰色",
    "pushti": "粉色",
    "binafsha": "紫色",

    # -------------------------
    # Kundalik iboralar
    # -------------------------
    "qalaysiz": "你好吗",
    "qalaysan": "你好吗",
    "men yaxshiman": "我很好",
    "hammasi yaxshi": "一切都很好",
    "ismingiz nima": "你叫什么名字",
    "mening ismim": "我的名字是",
    "qayerdansiz": "你来自哪里",
    "men o'zbekistondanman": "我来自乌兹别克斯坦",
    "tushunmadim": "我不明白",
    "tushundim": "我明白了",
    "yordam kerak": "需要帮助",
    "menga yordam bering": "请帮助我",
    "bu nima": "这是什么",
    "bu qancha": "这个多少钱",
    "qayerda": "在哪里",
    "men bilmayman": "我不知道",
    "muammo yo'q": "没问题",
    "hammasi joyida": "一切都很好",
    "ko'rishguncha": "再见",
    "xayrli tong": "早上好",
    "xayrli kun": "你好",
    "xayrli kech": "晚上好",
    "xayrli tun": "晚安",
}


# ============================================================
# 🇨🇳 → 🇺🇿
# ============================================================

ZH_UZ = {
    value: key
    for key, value in UZ_ZH.items()
}


# ============================================================
# XITOYCHA BELGILARINI ANIQLASH
# ============================================================

def contains_chinese(text):
    for char in text:
        if "\u4e00" <= char <= "\u9fff":
            return True

    return False


# ============================================================
# TILNI ANIQLASH
# ============================================================

def detect_language(text, source="auto"):

    text = str(text).strip()

    if source and source != "auto":
        return source

    if not text:
        return "uz"

    if contains_chinese(text):
        return "zh"

    return "uz"


# ============================================================
# XITOYCHA → O'ZBEKCHA
# ============================================================

def translate_zh_to_uz(text):

    text = text.strip()

    if not text:
        return ""

    # Avval to'liq iborani tekshiramiz
    if text in ZH_UZ:
        return ZH_UZ[text]

    # So'zlarni tekshirish
    result = text

    # Eng uzun iboralarni birinchi almashtirish
    sorted_items = sorted(
        ZH_UZ.items(),
        key=lambda item: len(item[0]),
        reverse=True
    )

    for zh, uz in sorted_items:

        if zh in result:
            result = result.replace(
                zh,
                " " + uz + " "
            )

    result = re.sub(r"\s+", " ", result).strip()

    return result


# ============================================================
# O'ZBEKCHA → XITOYCHA
# ============================================================

def translate_uz_to_zh(text):

    text = text.strip()

    if not text:
        return ""

    lower_text = text.lower()

    # To'liq ibora
    if lower_text in UZ_ZH:
        return UZ_ZH[lower_text]

    result = lower_text

    # Uzun iboralarni birinchi almashtirish
    sorted_items = sorted(
        UZ_ZH.items(),
        key=lambda item: len(item[0]),
        reverse=True
    )

    for uz, zh in sorted_items:

        pattern = r"(?<!\w)" + re.escape(uz) + r"(?!\w)"

        result = re.sub(
            pattern,
            " " + zh + " ",
            result,
            flags=re.IGNORECASE
        )

    result = re.sub(r"\s+", " ", result).strip()

    return result


# ============================================================
# ASOSIY TARJIMA FUNKSIYASI
# ============================================================

def translate_text(
    text,
    source="auto",
    target="zh"
):

    text = str(text).strip()

    if not text:
        return ""

    detected = detect_language(
        text,
        source
    )

    # 🇺🇿 → 🇨🇳
    if detected == "uz" and target == "zh":

        return translate_uz_to_zh(text)

    # 🇨🇳 → 🇺🇿
    if detected == "zh" and target == "uz":

        return translate_zh_to_uz(text)

    # Bir xil til
    if detected == target:

        return text

    return text


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    test_words = [
        "salom",
        "rahmat",
        "o'zbekiston",
        "maktab",
        "kitob",
        "mening ismim",
        "qalaysiz",
        "你好",
        "谢谢",
        "中国",
        "学校",
        "书"
    ]

    print("🌐 TARJIMON TEST")
    print("=" * 40)

    for word in test_words:

        detected = detect_language(
            word,
            "auto"
        )

        if detected == "zh":

            result = translate_text(
                word,
                "zh",
                "uz"
            )

        else:

            result = translate_text(
                word,
                "uz",
                "zh"
            )

        print(
            f"{word} → {result}"
        )

