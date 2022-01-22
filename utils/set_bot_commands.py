from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Inicializa o bot"),
            types.BotCommand("planos",  "Esta opção lista todos os planos que pode escolher"),
            types.BotCommand("status", "Esta opção dá informação do estado da sua subscrição"),
            # types.BotCommand("subscrever", "Esta opção lista todos os planos que pode escolher"),
            types.BotCommand("cancelar", "Esta opção cancela a sua subscrição (não será mais cobrado no final do termo da mesma)"),
            types.BotCommand("help", "Mostra este menu de ajuda"),
            types.BotCommand("info", "Disponibiliza todas as informações sobre o grupo DSS Insider e os seus benefícios"),
        ]
    )
