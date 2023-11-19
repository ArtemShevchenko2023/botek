import os
import sqlite3
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Вход выполнен как {bot.user}')
@bot.command()
async def тест(ctx):
    a = ctx.author
    await ctx.send(f'Привет {a}!')
@bot.command()
async def запись(ctx, username: str, age: int):
    conn = sqlite3.connect("user.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, age INTEGER)''')
    c.execute("INSERT INTO users (username, age) VALUES (?, ?)", (username, age))
    conn.commit()
    conn.close()
    await ctx.send(f'Пользователь {username} успешно записан в базу данных с возрастом {age}!')
@bot.command()
async def юзер(ctx, username: str):
    conn = sqlite3.connect("user.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    if result:
        fetched_age, fetched_username, _ = result
        await ctx.send(f'Имя пользователя: {fetched_username}, Возраст: {fetched_age}')
    else:
        await ctx.send(f'Пользователь {username} не найден.')
bot.run("MTE3NTQxMjA5MjI4MzY1NDI0NQ.GdhmFB.c869ev4_h8QwuITS2_JC0Mf9E5ShL2Echvu1j(ponon)A")
