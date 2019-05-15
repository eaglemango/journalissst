TOKEN = ""

WEBHOOK_HOST = ""
WEBHOOK_PORT = 0
WEBHOOK_LOCAL_HOST = "0.0.0.0"

WEBHOOK_URL_BASE = "https://{0}:{1}".format(WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{0}/".format(TOKEN)

WEBHOOK_SSL_CERT = "./certificates/webhook_cert.pem"
WEBHOOK_SSL_PRIV = "./certificates/webhook_pkey.pem"


DESIRABLE_LENGTH = 50
