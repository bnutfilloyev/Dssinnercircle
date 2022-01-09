from utils.db_api.mongo import user_db, transaction_db


async def database(data, telegram_id):
    days = user_db.find_one({'telegram_id': telegram_id})

    if days == None:
        days = 0
    else:
        days = days['days']

    user_db.update_one({'telegram_id': telegram_id}, {
        "$set": {
            "days": days + data['days'],
            'status': True,
            "plan": data['plan']
        }
    }, upsert=True)

    data['telegram_id'] = telegram_id
    transaction_db.insert_one(dict(data.as_dict()))


if __name__ == "__main__":
    database({'telegram_id': 433751560, 'days': 30, 'plan': 'month'}, 433751560)
