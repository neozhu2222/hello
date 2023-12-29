import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send_message(response) if is_private else message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE4ODk0OTA4MDA1MTgxNDQ3MA.Gw0qrk.YLtw0xp93PRXbGUGg7KzShYE7huUsLJR_nRWUw'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running")
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == "?":
            user_message = user_message[1:]
            await message.channel.send(responses.handle_response(user_message))
        else:
            await message.channel.send(responses.handle_response(user_message))
        

    client.run(TOKEN)