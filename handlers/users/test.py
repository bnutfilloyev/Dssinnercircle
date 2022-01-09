from utils.db_api.mongo import user_db, transaction_db

json_data = {
    'telegram_id': 1001,
    'days': 30,
    'plans': 'month',
    'status': True,
}

# days = user_db.find_one({'telegram_id': 433751560})
# if days == None:
#     days = 0
# else:
#     days = days['days']

# user_data = user_db.update_one({'telegram_id': 433751560}, {
#     "$set": {
#         "days": days + 10,
#         'status': True,
#         "plan": 'month'
#     }
# }, upsert=True)


for i in transaction_db.find({'telegram_id': 433751560}):
    print(i)
# print(user_db.find_one({'telegram_id'})['day'])
# "FSMContextProxy state = <default>, data = {'plans_price': 200, 'plan': 'month', 'pay-id': 'PAYID-MHNKKQY7UT80632R1915603H', 'intenet_id': 'pi_3KFxL6ERl483ddfA0yMyq98Y'}"