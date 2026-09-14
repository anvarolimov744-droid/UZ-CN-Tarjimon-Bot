const inputText = document.getElementById("inputText");
const resultText = document.getElementById("resultText");

const sourceLanguage = document.getElementById("sourceLanguage");
const targetLanguage = document.getElementById("targetLanguage");

const translateBtn = document.getElementById("translateBtn");
const clearBtn = document.getElementById("clearBtn");
const swapBtn = document.getElementById("swapBtn");

const copyBtn = document.getElementById("copyBtn");
const speakBtn = document.getElementById("speakBtn");
const voiceBtn = document.getElementById("voiceBtn");
const favoriteBtn = document.getElementById("favoriteBtn");

const themeBtn = document.getElementById("themeBtn");
const themeBtn2 = document.getElementById("themeBtn2");

const charCount = document.getElementById("charCount");

const toast = document.getElementById("toast");
const loading = document.getElementById("loading");

let lastTranslation = "";
let lastSource = "";
let lastTarget = "";


/* =========================
   TOAST
========================= */

function showToast(message) {

    toast.textContent = message;

    toast.classList.add("show");

    setTimeout(() => {
        toast.classList.remove("show");
    }, 2200);
}


/* =========================
   LOADING
========================= */

function showLoading(show) {

    if (show) {
        loading.classList.remove("hidden");
    } else {
        loading.classList.add("hidden");
    }
}


/* =========================
   CHAR COUNT
========================= */

function updateCharCount() {

    charCount.textContent =
        inputText.value.length;
}

inputText.addEventListener(
    "input",
    updateCharCount
);


/* =========================
   TARJIMA
========================= */

translateBtn.addEventListener(
    "click",
    async () => {

        const text =
            inputText.value.trim();

        if (!text) {
            showToast(
                "⚠️ Avval matn kiriting."
            );
            return;
        }

        showLoading(true);

        try {

            const response =
                await fetch(
                    "/translate",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({
                            text: text,
                            source:
                                sourceLanguage.value,
                            target:
                                targetLanguage.value
                        })
                    }
                );

            const data =
                await response.json();

            if (!data.success) {

                showToast(
                    data.message ||
                    "Tarjima xatosi."
                );

                return;
            }

            lastTranslation =
                data.translation;

            lastSource =
                data.source;

            lastTarget =
                data.target;

            resultText.textContent =
                data.translation;

            showToast(
                "✅ Tarjima tayyor!"
            );

            loadStats();

        } catch (error) {

            console.error(error);

            showToast(
                "❌ Server bilan aloqa yo‘q."
            );

        } finally {

            showLoading(false);
        }
    }
);


/* =========================
   CLEAR
========================= */

clearBtn.addEventListener(
    "click",
    () => {

        inputText.value = "";

        resultText.textContent =
            "Tarjima natijasi shu yerda chiqadi...";

        lastTranslation = "";

        updateCharCount();

        inputText.focus();
    }
);


/* =========================
   SWAP
========================= */

swapBtn.addEventListener(
    "click",
    () => {

        let source =
            sourceLanguage.value;

        let target =
            targetLanguage.value;

        if (source === "auto") {
            source = "uz";
        }

        sourceLanguage.value =
            target;

        targetLanguage.value =
            source;

        const oldInput =
            inputText.value;

        const oldResult =
            resultText.textContent;

        if (
            oldResult &&
            oldResult !==
            "Tarjima natijasi shu yerda chiqadi..."
        ) {

            inputText.value =
                oldResult;

            resultText.textContent =
                oldInput;
        }

        updateCharCount();
    }
);


/* =========================
   COPY
========================= */

copyBtn.addEventListener(
    "click",
    async () => {

        if (!lastTranslation) {

            showToast(
                "⚠️ Nusxalash uchun natija yo‘q."
            );

            return;
        }

        try {

            await navigator.clipboard.writeText(
                lastTranslation
            );

            showToast(
                "📋 Nusxalandi!"
            );

        } catch {

            showToast(
                "❌ Nusxalash ishlamadi."
            );
        }
    }
);


/* =========================
   SPEAK
========================= */

speakBtn.addEventListener(
    "click",
    () => {

        if (!lastTranslation) {

            showToast(
                "⚠️ Ovoz chiqarish uchun natija yo‘q."
            );

            return;
        }

        if (!("speechSynthesis" in window)) {

            showToast(
                "❌ Brauzer ovoz funksiyasini qo‘llamaydi."
            );

            return;
        }

        window.speechSynthesis.cancel();

        const utterance =
            new SpeechSynthesisUtterance(
                lastTranslation
            );

        utterance.lang =
            lastTarget === "zh"
                ? "zh-CN"
                : "uz-UZ";

        utterance.rate = 0.9;

        window.speechSynthesis.speak(
            utterance
        );
    }
);


/* =========================
   VOICE INPUT
========================= */

voiceBtn.addEventListener(
    "click",
    () => {

        const Recognition =
            window.SpeechRecognition ||
            window.webkitSpeechRecognition;

        if (!Recognition) {

            showToast(
                "❌ Ovozli kiritish Chrome'da mavjud emas."
            );

            return;
        }

        const recognition =
            new Recognition();

        recognition.continuous = false;
        recognition.interimResults = false;

        let language =
            sourceLanguage.value;

        if (language === "auto") {
            language = "uz";
        }

        recognition.lang =
            language === "zh"
                ? "zh-CN"
                : "uz-UZ";

        showToast(
            "🎤 Gapiring..."
        );

        recognition.start();

        recognition.onresult =
            function(event) {

                const text =
                    event.results[0][0].transcript;

                inputText.value =
                    text;

                updateCharCount();
            };

        recognition.onerror =
            function() {

                showToast(
                    "❌ Mikrofon ishlamadi."
                );
            };
    }
);


/* =========================
   FAVORITE
========================= */

favoriteBtn.addEventListener(
    "click",
    async () => {

        const original =
            inputText.value.trim();

        if (
            !original ||
            !lastTranslation
        ) {

            showToast(
                "⚠️ Avval tarjima qiling."
            );

            return;
        }

        try {

            const response =
                await fetch(
                    "/favorite",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            original:
                                original,

                            translation:
                                lastTranslation,

                            source:
                                lastSource,

                            target:
                                lastTarget
                        })
                    }
                );

            const data =
                await response.json();

            if (data.success) {

                showToast(
                    "⭐ Sevimlilarga qo‘shildi!"
                );

                loadFavorites();
                loadStats();

            } else {

                showToast(
                    data.message ||
                    "Xatolik."
                );
            }

        } catch (error) {

            console.error(error);

            showToast(
                "❌ Server xatosi."
            );
        }
    }
);


/* =========================
   NAVIGATION
========================= */

const navButtons =
    document.querySelectorAll(
        ".nav-btn"
    );

const pages = {
    translator:
        document.getElementById(
            "translatorPage"
        ),

    history:
        document.getElementById(
            "historyPage"
        ),

    favorites:
        document.getElementById(
            "favoritesPage"
        ),

    profile:
        document.getElementById(
            "profilePage"
        )
};


navButtons.forEach(button => {

    button.addEventListener(
        "click",
        () => {

            navButtons.forEach(btn => {
                btn.classList.remove(
                    "active"
                );
            });

            button.classList.add(
                "active"
            );

            Object.values(pages)
                .forEach(page => {
                    page.classList.remove(
                        "active"
                    );
                });

            const pageName =
                button.dataset.page;

            pages[pageName]
                .classList.add(
                    "active"
                );

            if (
                pageName === "history"
            ) {
                loadHistory();
            }

            if (
                pageName === "favorites"
            ) {
                loadFavorites();
            }

            if (
                pageName === "profile"
            ) {
                loadStats();
            }
        }
    );
});


/* =========================
   HISTORY
========================= */

async function loadHistory() {

    const container =
        document.getElementById(
            "historyList"
        );

    container.innerHTML =
        "Yuklanmoqda...";

    try {

        const response =
            await fetch("/history");

        const data =
            await response.json();

        if (
            !data.history ||
            data.history.length === 0
        ) {

            container.innerHTML =
                "<p>🕘 Tarix hali bo‘sh.</p>";

            return;
        }

        container.innerHTML =
            data.history
                .map(item => `

                    <div class="list-item">

                        <div class="original">
                            ${escapeHTML(
                                item.original
                            )}
                        </div>

                        <div class="translation">
                            ${escapeHTML(
                                item.translation
                            )}
                        </div>

                        <div class="date">
                            ${escapeHTML(
                                item.date
                            )}
                        </div>

                    </div>

                `)
                .join("");

    } catch (error) {

        console.error(error);

        container.innerHTML =
            "❌ Tarixni yuklab bo‘lmadi.";
    }
}


/* =========================
   CLEAR HISTORY
========================= */

document
    .getElementById(
        "clearHistoryBtn"
    )
    .addEventListener(
        "click",
        async () => {

            if (
                !confirm(
                    "Tarixni tozalaysizmi?"
                )
            ) {
                return;
            }

            try {

                await fetch(
                    "/history/clear",
                    {
                        method: "POST"
                    }
                );

                showToast(
                    "🗑️ Tarix tozalandi."
                );

                loadHistory();

            } catch {

                showToast(
                    "❌ Xatolik."
                );
            }
        }
    );


/* =========================
   FAVORITES
========================= */

async function loadFavorites() {

    const container =
        document.getElementById(
            "favoritesList"
        );

    container.innerHTML =
        "Yuklanmoqda...";

    try {

        const response =
            await fetch("/favorites");

        const data =
            await response.json();

        if (
            !data.favorites ||
            data.favorites.length === 0
        ) {

            container.innerHTML =
                "<p>⭐ Sevimlilar hali bo‘sh.</p>";

            return;
        }

        container.innerHTML =
            data.favorites
                .map(item => `

                    <div class="list-item">

                        <div class="original">
                            ${escapeHTML(
                                item.original
                            )}
                        </div>

                        <div class="translation">
                            ${escapeHTML(
                                item.translation
                            )}
                        </div>

                        <div class="date">
                            ${escapeHTML(
                                item.date
                            )}
                        </div>

                    </div>

                `)
                .join("");

    } catch (error) {

        console.error(error);

        container.innerHTML =
            "❌ Sevimlilarni yuklab bo‘lmadi.";
    }
}


/* =========================
   STATS
========================= */

async function loadStats() {

    try {

        const response =
            await fetch("/stats");

        const data =
            await response.json();

        if (!data.success) {
            return;
        }

        const stats =
            data.stats;

        document.getElementById(
            "statTranslations"
        ).textContent =
            stats.translations || 0;

        document.getElementById(
            "statFavorites"
        ).textContent =
            getFavoriteCount();

        document.getElementById(
            "statUsers"
        ).textContent =
            stats.users || 0;

    } catch (error) {

        console.error(error);
    }
}


async function getFavoriteCount() {

    try {

        const response =
            await fetch("/favorites");

        const data =
            await response.json();

        return data.favorites
            ? data.favorites.length
            : 0;

    } catch {

        return 0;
    }
}


/* =========================
   THEME
========================= */

function toggleTheme() {

    document.body.classList.toggle(
        "dark"
    );

    const dark =
        document.body.classList.contains(
            "dark"
        );

    localStorage.setItem(
        "theme",
        dark ? "dark" : "light"
    );

    themeBtn.textContent =
        dark ? "☀️" : "🌙";
}


themeBtn.addEventListener(
    "click",
    toggleTheme
);

themeBtn2.addEventListener(
    "click",
    toggleTheme
);


/* =========================
   LOAD THEME
========================= */

function loadTheme() {

    const theme =
        localStorage.getItem(
            "theme"
        );

    if (theme === "dark") {

        document.body.classList.add(
            "dark"
        );

        themeBtn.textContent =
            "☀️";

    } else {

        themeBtn.textContent =
            "🌙";
    }
}

loadTheme();


/* =========================
   QUICK BUTTONS
========================= */

document
    .querySelectorAll(
        ".quick-btn"
    )
    .forEach(button => {

        button.addEventListener(
            "click",
            () => {

                inputText.value =
                    button.dataset.text;

                updateCharCount();

                inputText.focus();
            }
        );
    });


/* =========================
   PREMIUM
========================= */

document
    .getElementById(
        "premiumBtn"
    )
    .addEventListener(
        "click",
        () => {

            showToast(
                "💎 Premium funksiyasi keyingi bosqichda."
            );
        }
    );


/* =========================
   HTML XAVFSIZLIK
========================= */

function escapeHTML(value) {

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}


/* =========================
   START
========================= */

updateCharCount();

loadStats();

console.log(
    "🌐 Tarjimon Super Bot ishga tushdi!"
);