from utils.db_api.mongo import plans_price_db

text = {
    'plan': '<b>DSS Insider</b>\n\n'
            'Por favor selecione o plano de subscrição:',

    'choose_plan': "<b>{}</b>\n\n"
                   "Tem acesso a:\n"
                   "✅<b>{}</b>(acesso ao grupo)\n\n"
                   "Preço:<b>{}</b>\n"
                   "Ciclo de Pagamento:<b>{}</b>\n"
                   "Tipo de Pagamento:<b>{}</b>",

    'pay_text': 'Por favor carregue no botão abaixo:',

    'start_text': "Olá, <b>{}!</b>",

    'status_text': "<b>⚡️O seu status:</b>\n\n"
                   "<b>🤖Telegram:</b> <code>{}</code>\n"
                   "<b>💰Preço: </b>{}\n"
                   "<b>💠Ciclo de pagamento: Anual: </b>{}\n"
                   "<b>📝Dias: </b>{}\n"
                   "<b>🆔Id_Pagamento: </b><code>{}</code>\n\n",

    'kick_notification_admin': "There are those who have to leave the group."
                               "Use the group /kick or <code>!code</code> command to remove them.",

    'kick_notification_user': "You have to pay or you will be kicked out of the group.",

    "change_plan_price": "To change plan prices, place them in ascending order in the following sequence. "
                         "e.x\n100\n1100\n2000\n3000",

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
    "user_status": "Your Status:\n\n"
                   "<b>💁 Days: </b>{}\n"
                   "<b>⚠️ Status: </b>{}",

    "help_button": "/start - Inicializa o bot\n"
                   "/help - Mostra este menu de ajuda\n"
                   "/info - Disponibiliza todas as informações sobre o grupo DSS Insider e os seus benefícios\n"
                   "/planos - Esta opção lista todos os planos que pode escolher\n"
                   "/status - Esta opção dá informação do estado da sua subscrição\n"
                   "/subscrever - Esta opção lista todos os planos que pode escolher\n" 
                   "/cancelar - Esta opção cancela a sua subscrição (não será mais cobrado no final do termo da mesma\n"
,

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

async def price():
    return plans_price_db.find_one()['plans_price']

days = plans_price_db.find_one()['plans_days']


async def plans_price():
    return {
        'plan1': 'Mensal (€): {} €/1 mês'.format(plans_price_db.find_one()['plans_price'][0]),
        'plan2': 'Mensal (R$): R$ {}/1 mês'.format(plans_price_db.find_one()['plans_price'][1]),
        'plan3': 'Anual (€): {} €/1 ano'.format(plans_price_db.find_one()['plans_price'][2]),
        'plan4': 'Anual (R$): R$ {}/1 ano'.format(plans_price_db.find_one()['plans_price'][3])
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
