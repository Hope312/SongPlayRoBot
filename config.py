import os
API_ID = int(os.getenv("29788473"))
API_HASH = os.getenv("7efa3ec44701eb2c5b7148c7c860fe2e")
BOT_TOKEN = os.getenv("6198995126:AAE3AqAlVXf0Nhaiw892NdWIZmq8gzBZI4A")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("5875628111", "").split()})
