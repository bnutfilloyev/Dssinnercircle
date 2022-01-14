from pymongo import MongoClient
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import IP

client = MongoClient(IP)
storage = MemoryStorage()

database = client['Dssinnercircle']
user_db = database['users']
transaction_db = database['transaction']
plans_price_db = database['plans']
