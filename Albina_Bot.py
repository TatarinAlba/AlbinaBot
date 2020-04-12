import apiai
import json
import discord
import fileinput
from discord.ext import commands
from discord.ext.commands import Bot
from random import choice as cc
import os
quoters = [ 'Неграмотными людьми 21 века будут не те, кто не умеет читать и писать, а те, кто не умеет учиться и переучиваться. *Алвин Тоффлер*',
'Нельзя научиться у того, кто постоянно с тобой соглашается. Дадли Филд Малоун',
'Иди по жизни так, будто впереди всегда есть чему научиться и ты точно это сможешь сделать. *Вернон Говард*',
'Развивайте страсть к обучению. Если у вас получится, то вы всегда будете расти. *Энтони Жд. ДиАнжело*',
'Мы учимся, когда мы что-то делаем. *Джордж Херберт*',
'Заполнить свой разум миллионов разных фактов, но при этом ничему не научиться вполне возможно.*Алек Борн.*']
members = ['Абрамова',
'Авхадеев',
'Алтунин',
'Ахметова',
'Белов',
'Биксон',
'Акшаев',
'Галиаскаров',
'Григорьев',
'Журавлева',
'Обмолова',
'Морозова',
'Парфишина',
'Яшин',
'Ярцева',
'Савинова',
'Османова',
'Маслов',
'Биксон',
'Спирина',
'Идрисов',
'Каюмов',
'Хадиуллин',
'Молчанов',
]
Bot = commands.Bot(command_prefix='!')
@Bot.command(text_commands = True)
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f"Ну привет, {author.mention}. Ха-ха-ха-ха-ха")
@Bot.command(text_commands = True)
async def random(ctx):
    winner = cc(members)
    quoter = cc(quoters)
    await ctx.send(f"💎💎💎 Ну что же!!! Сегодня на охоту отправляется 😎😎😎||{winner}|| 😎😎😎. Удачи мой друг!!!. Цитатку тебе в дорогу 💎💎💎.\n```\n {quoter}```")
@Bot.command(text_commands = True)
async def gn(ctx):
    author = ctx.message.author
    await ctx.send(f"😊😊😊Спокойной ночи, сладких снов, {author.mention}. Удачи завтра 😊😊😊")
@Bot.command(text_commands = True)
async def quoter(text_commands = True):
    quoter = cc(quoters)
    await ctx.send(f"```\n {quoter}```")
Bot.run(str(os.environ.get('BOT_TOKEN')))
@Bot.event
    async def on_message(message):
    await ctx.send("Вы можете написать какое либо сообщение, чтобы начать общение с ботом")
    async def send_message(message):
    request = apiai.ApiAI("4a66b62af37a451f9b7c701be99e4d8e").text_request()
    request.lang = 'ru'
    request.session_id = 'session_1'
    request.query = message
    response = json.loads(request.getresponse().read().decode('utf-8'))
    await ctx.send(response['result']['fulfillment']['speech'])
