import asyncio
import discord
from config import TOKEN

# pip install git+https://github.com/abenassi/Google-Search-API
from google import google


client = discord.Client()


@client.event
async def on_ready():
    print(f'Username: {client.user.name} ID: {client.user.id}')


@client.event
async def on_message(message):
    if message.content.startswith('!count'):
        temp = await client.send_message(message.channel,
            f'counting messages by {message.author}....')
        count = 0
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                count += 1
        await client.edit_message(temp,
            f'@{message.author} has sent {count} messages')

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'done sleeping')

    elif message.content.startswith('!google'):
        query = message.content[len('!google'):]
        temp = await client.send_message(message.channel,
            f'googling {query}...')
        results = google.search(query, 1)
        results = '\n'.join(r.description for r in results[:3])
        await client.edit_message(temp, results)

    elif message.content.startswith('!calc'):
        query = message.content[len('!calc'):]
        temp = await client.send_message(message.channel,
            f'calculating {query!r}...')
        regex = r'(\d+) + (\d+)'

        await client.edit_message(temp, top_result)



client.run(TOKEN)

