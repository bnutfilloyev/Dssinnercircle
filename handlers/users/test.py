from utils.db_api.mongo import plans_price_db

plans = plans_price_db.find_one()
print(plans)

plans = plans_price_db.find_one_and_update({}, update={
    '$set': {'plans_price': ['10', '64', '90', '610'], 'plans_days': [30, 90, 30, 365]}
}, return_document=True)
print(plans)