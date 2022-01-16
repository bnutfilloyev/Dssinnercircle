from utils.db_api.mongo import plans_price_db

text = {
    'plan': '<b>DSS Insider</b>\n\n'
            'Please select your subscription plan:',

    'choose_plan': "<b>{}</b>\n\n"
                   "Tem acesso a:\n"
                   "✅<b>{}</b>(acesso ao grupo)\n\n"
                   "Preço:<b>{}.00</b>\n"
                   "Ciclo de Pagamento:<b>{}</b>\n"
                   "Tipo de Pagamento:<b>{}</b>",

    'pay_text': 'Por favor carregue no botão abaixo:',

    'start_text': "Olá, <b>{}!</b>",

    'status_text': "<b>⚡️Your Status:</b>\n\n"
                   "<b>🤖Telegram:</b> <code>{}</code>\n"
                   "<b>💰Price: </b>{}\n"
                   "<b>💠Billing period: </b>{}\n"
                   "<b>📝Days: </b>{}\n"
                   "<b>🆔Pay_ID: </b><code>{}</code>\n\n",

    'kick_notification_admin': "There are those who have to leave the group."
                               "Use the group /kick or <code>!code</code> command to remove them.",

    'kick_notification_user': "You have to pay or you will be kicked out of the group.",

    "change_plan_price": "To change plan prices, place them in ascending order in the following sequence. "
                         "e.x 100,1100,2000,3000",

    "info": "Bem vindo à porta de entrada do grupo PREMIUM “DSS Insider”, "
            "um grupo que lhe vai abrir novos horizontes para o seu negócios de Dropshipping.\n\n"
            "Esta é uma comunidade de pessoas com mentalidade igual e que se ajuda diariamente.\n\n"
            "Aqui terá acesso a:\n\n- Masterclasses sobre temas relevantes\n"
            "- Videos Chats semanais de perguntas e respostas\n"
            "- Divulgação de produtos vencedores\n"
            "- Anáise de lojas e campanhas de publicidade dos membros\n"
            "- Descontos exclusivos para membros em ferramentas e serviços\n"
            "- Acesso a agentes privados\n"
            "- Concursos com ofertas\n"
            "- E muito mais\n\n"
            "Escolha entre uma assinatura mensal ou anual.\n\n"
            "Preços:\n\n"
            "Mensal: 10 € ou R$ 64.50 (válido por um mêscancele a qualquer altura)\n"
            "Anual: 95 € ou R$ 610 (válido por um ano, cancele a qualquer altura) \n\n"
            "Vemo-nos lá dentro!\n\n"
            "Nuno Cabral",
}

confirm_payment_button_text = {
    'subscribe': "🅿Subscrever",
    'confirm': "Confirmar",
}

default_button = {
    'plan': 'Planos',
    'status': 'Status',
    'info': 'Informações',
}

price = plans_price_db.find_one()['plans_price']
days = plans_price_db.find_one()['plans_days']


plans_price = {
    'plan1': 'Mensal (€): {},00 €/1 mês'.format(plans_price_db.find_one()['plans_price'][0]),
    'plan2': 'Mensal (R$): R$ {}.00/1 mês'.format(plans_price_db.find_one()['plans_price'][1]),
    'plan3': 'Anual (€): {}.00 €/1 ano'.format(plans_price_db.find_one()['plans_price'][2]),
    'plan4': 'Anual (R$): R$ {}.00/1 ano'.format(plans_price_db.find_one()['plans_price'][3])
}

plans_name = [
    'Mensal (€)', 'Mensal (R$)', 'Anual (€)', 'Anual (R$)',
]

billing_period = [
    '1 month', '1 year', '1 month', '1 year',
]

payment_method = {
    'paypal': '🅿️PayPal',
    'stripe': 'Cartão de Crédito',
    'back': '⏪Back'
}
