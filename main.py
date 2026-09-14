from flask import Flask, render_template, request, jsonify
from pathlib import Path
import json
from datetime import datetime

from translator import translate_text, detect_language

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(exist_ok=True)

HISTORY_FILE = DATA_DIR / "history.json"
FAVORITES_FILE = DATA_DIR / "favorites.json"
USERS_FILE = DATA_DIR / "users.json"
STATS_FILE = DATA_DIR / "stats.json"


def load_json(path, default):
    try:
        if not path.exists():
            save_json(path, default)
            return default

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception:
        return default


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def init_files():
    if not HISTORY_FILE.exists():
        save_json(HISTORY_FILE, [])

    if not FAVORITES_FILE.exists():
        save_json(FAVORITES_FILE, [])

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


init_files()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/translate", methods=["POST"])
def translate():

    data = request.get_json() or {}

    text = str(data.get("text", "")).strip()
    source = data.get("source", "auto")
    target = data.get("target", "zh")

    if not text:
        return jsonify({
            "success": False,
            "message": "Matn kiriting."
        })

    detected = detect_language(text, source)

    result = translate_text(
        text,
        source,
        target
    )

    history = load_json(
        HISTORY_FILE,
        []
    )

    history.insert(
        0,
        {
            "id": int(datetime.now().timestamp() * 1000),
            "source": detected,
            "target": target,
            "original": text,
            "translation": result,
            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }
    )

    save_json(
        HISTORY_FILE,
        history[:500]
    )

    stats = load_json(
        STATS_FILE,
        {
            "translations": 0,
            "users": 0,
            "subscribers": 0
        }
    )

    stats["translations"] = (
        int(stats.get("translations", 0)) + 1
    )

    save_json(STATS_FILE, stats)

    return jsonify({
        "success": True,
        "translation": result,
        "source": detected,
        "target": target
    })


@app.route("/history")
def history():

    return jsonify({
        "success": True,
        "history": load_json(
            HISTORY_FILE,
            []
        )
    })


@app.route("/history/clear", methods=["POST"])
def clear_history():

    save_json(
        HISTORY_FILE,
        []
    )

    return jsonify({
        "success": True
    })


@app.route("/favorite", methods=["POST"])
def favorite():

    data = request.get_json() or {}

    original = str(
        data.get("original", "")
    ).strip()

    translation = str(
        data.get("translation", "")
    ).strip()

    if not original or not translation:
        return jsonify({
            "success": False,
            "message": "Ma'lumot yetarli emas."
        })

    favorites = load_json(
        FAVORITES_FILE,
        []
    )

    favorites.insert(
        0,
        {
            "id": int(datetime.now().timestamp() * 1000),
            "original": original,
            "translation": translation,
            "source": data.get("source", ""),
            "target": data.get("target", ""),
            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }
    )

    save_json(
        FAVORITES_FILE,
        favorites[:500]
    )

    return jsonify({
        "success": True,
        "message": "⭐ Sevimlilarga qo‘shildi."
    })


@app.route("/favorites")
def favorites():

    return jsonify({
        "success": True,
        "favorites": load_json(
            FAVORITES_FILE,
            []
        )
    })


@app.route("/stats")
def stats():

    data = load_json(
        STATS_FILE,
        {
            "translations": 0,
            "users": 0,
            "subscribers": 0
        }
    )

    return jsonify({
        "success": True,
        "stats": data
    })


if __name__ == "__main__":

    print("")
    print("===================================")
    print("🌐 TARJIMON SUPER BOT")
    print("===================================")
    print("Server: http://127.0.0.1:5000")
    print("To'xtatish: CTRL + C")
    print("===================================")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )