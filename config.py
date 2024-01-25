# (©)Codexbotz
# Recife By sanyagesya
# Kalo clone Gak usah hapus
# gue tandain akun tele nya ngentod


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6980611537:AAF0ZPhgsnqAE0CzpbM9lc_9vF1Px7D4SMg")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "10064016"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "b9ca5d9a6c625a890af28db4adf50cf4")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002027693771"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1948147616"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "@Arabnihnge")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://euymdfzi:miFOv9EsEqCJmn7aRQ1pWW1IG5Eu2mH7@tiny.db.elephantsql.com/euymdfzi")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "Arabc0de")
GROUP = os.environ.get("GROUP", "SiArab_Support")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002035236535"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001526366621"))

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1001898026780"))
FORCE_SUB_GROUP1 = int(os.environ.get("FORCE_SUB_GROUP1", "-1001916251589"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.\n</b>JIKA BOT BERMASALAH H>
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "6824711323 1948147616").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dah>
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(1971239428)
ADMINS.append(1250450587)
ADMINS.append(2010825200)
ADMINS.append(1750080384)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

