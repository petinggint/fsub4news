# (©)Codexbotz
# Recife By sanyagesya
# Kalo clone Gak usah hapus
# gue tandain akun tele nya ngentod


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8006646597:AAF9mQL66wsg4VTEAThLWn3n8cUk16t5lUc")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "13261150"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "64fe89043e67bc994eb5ae95f081e57a")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002275227387"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7461183106"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "@syaaaallweb")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://euymdfzi:miFOv9EsEqCJmn7aRQ1pWW1IG5Eu2mH7@tiny.db.elephantsql.com/euymdfzi")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "OFFICIALSYAAA")
GROUP = os.environ.get("GROUP", "OFFICIALSYAAA")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002677755125"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1002553492693"))

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1002821282234"))
FORCE_SUB_GROUP1 = int(os.environ.get("FORCE_SUB_GROUP1", "-1002553492693"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.\n</b>JIKA BOT BERMASALAH H>
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "7461183106").split())]
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

ADMINS.append(7461183106)
ADMINS.append(7461183106)
ADMINS.append(7461183106)
ADMINS.append(7461183106)

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

