from os import path as p

# Bot Configuration
TOKEN = ""

# Webhook Configuration
WEBHOOK_HOST = ""
WEBHOOK_PORT = 0
WEBHOOK_LOCAL_HOST = "0.0.0.0"

WEBHOOK_URL_BASE = "https://{0}:{1}".format(WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{0}/".format(TOKEN)

WEBHOOK_SSL_CERT = "./certificates/webhook_cert.pem"
WEBHOOK_SSL_PRIV = "./certificates/webhook_pkey.pem"

# Message Generation
DESIRABLE_LENGTH = 50

# File Paths
WORK_DIRECTORY = p.join(p.dirname(p.abspath(__file__)), "..")
NEWS_DATA_DIRECTORY = p.join(WORK_DIRECTORY, "news_data")
IT_DATA = p.join(NEWS_DATA_DIRECTORY, "it")
IMPROVED_IT_DATA = p.join(NEWS_DATA_DIRECTORY, "improved_it")
POLITICAL_DATA = p.join(NEWS_DATA_DIRECTORY, "political")
