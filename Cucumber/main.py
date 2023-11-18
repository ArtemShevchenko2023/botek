import sqlite3
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
pon = ".\pon.db"
@bot.event
async def on_ready():
    print(f'Вход выполнен как {bot.user}')
@bot.command()
async def тест(ctx):
    a = ctx.author
    await ctx.send(f'Привет {a}!')
@bot.command()
async def запись(ctx, name, age):
    # Подключение к базе данных
    conn = sqlite3.connect(pon)
    c = conn.cursor()

    # Создание таблицы, если она не существует
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)''')

    # Вставка данных пользователя в таблицу
    c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

    # Закрытие соединения с базой данных
    conn.close()

    await ctx.send(f'Пользователь {name} успешно записан в базу данных с возрастом {age}!')
@bot.command()
async def юзер(ctx, name: str):
    conn = sqlite3.connect(pon)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE name=?", (name,))
    result = c.fetchone()
    conn.close()
    if result:
        name, age = result
        await ctx.send(f'Имя пользователя: {name}, Возраст: {age}')
    else:
        await ctx.send(f'Пользователь {name} не найден.')
bot.run("MTE3NTQxMjA5MjI4MzY1NDI0NQ.GdhmFB.c869ev4_h8QwuITS2_JC0Mf9E5ShL2Echvu1j(ponon)A")