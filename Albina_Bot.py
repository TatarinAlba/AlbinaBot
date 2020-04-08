import discord
from discord.ext import commands
from discord.ext.commands import Bot
from random import choice as cc
import os
Bot = commands.Bot(command_prefix='!')
def citata():
    cit = open('citata.txt', "r")
    sbornik = [i[:-1] for i in cit]
    q = cc(sbornik)
    return q
def rem(item):
    f = open("Our_Class.txt","r")
    lines = f.readlines()
    f.close()
    f = open("Our_Class.txt","w")
    for line in lines:
        if item not in line:
         f.write(line)
    f.close()
def randoma():
    form = open('Our_Class.txt', 'r+')
    Bag = open('Bag.txt', 'a')
    who_will_be = [i[:-1] for i in form if bool(i) != False]
    if len(who_will_be) <= 2:
        form.close()
        Bag.close()
        form = open("Our_Class.txt", "a")
        Bag = open('Bag.txt', 'r')
        ok = [i[:-1] for i in Bag if i != ""]
        for i in ok:
            form.write(i + '\n')
        Bag = open('Bag.txt', 'w')
        Bag.write('')
        form.close()
        Bag.close()
        Bag = open('Bag.txt', 'a')
        form = open('Our_Class.txt', 'r+')
    our_choice = cc(who_will_be)
    Bag.write(our_choice + '\n')
    rem(our_choice)
    return our_choice
@Bot.event
async def on_ready():
    print("Bot is online")

@Bot.command(text_commands = True)
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f"Ну привет, {author.mention} :*")
@Bot.command(text_commands = True)
async def random(ctx):
    await ctx.send(f"💎💎💎 Ну что же!!! Сегодня на охоту отправляется 😎😎😎||{randoma()}|| 😎😎😎. Удачи мой друг!!!. Цитатку тебе в дорогу 💎💎💎.\n```\n {citata()}```")
@Bot.command(text_commands = True)
async def GoodNight(ctx):
    author = ctx.message.author
    await ctx.send(f"😊😊😊Спокойной ночи, сладких снов, {author.mention}. Удачи завтра 😊😊😊")
token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))
