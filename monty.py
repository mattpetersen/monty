import asyncio

# pip install git+https://github.com/abenassi/Google-Search-API
import discord
from google import google

from config import TOKEN

from sub_math_expr import sub_math_expr


client = discord.Client()


@client.event
async def on_ready():
    print('Username:', client.user.name)
    print('User ID:', client.user.id)
    print('Ready.')


@client.event
async def on_message(message):
    if message.content.startswith('!count'):
        count = 0
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                count += 1
        await client.send_message(message.channel,
            f'{message.author} has sent {count} messages')

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'done sleeping')

    elif message.content.startswith('!google'):
        query = message.content[len('!google'):]
        results = google.search(query, 1)
        results = '\n'.join(r.description for r in results[:3])
        await client.send_message(message.channel, results)

    elif message.content.startswith('!calc'):
        await client.send_message(
            message.channel,
            sub_math_expr(
                message.content[len('!calc'):]
            )
        )


client.run(TOKEN)

