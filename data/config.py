from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
MODE = env.str("MODE")
CLIEND_ID = env.str("CLIEND_ID")
CLIENT_SECRET = env.str("CLIENT_SECRET")
CHANEL = env.str("CHANEL")
STRIPE = env.str("STRIPE")

GROUP_NAME = 'Dssinnercircle PAID GROUP'
BILLING_MODE = 'recurring'

GROUP_ID = env.str('GROUP_ID')