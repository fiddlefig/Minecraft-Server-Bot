import socket
import discord
# client = discord.Client(intents=discord.Intents.default())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('IP address', port))


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'logged in as {self.user} (ID: {self.user.id})')
        print('--------')
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('!ServerOn?'):
            # await message.reply('Hello')
            if result == 0:
                await message.reply('Server is up')
            else:
                await message.reply('Server is down')

intents = discord.Intents.default()
intents.message_content = True

sock.close()
client = MyClient(intents=intents)
client.run('token')

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# result = sock.connect_ex(('192.168.1.9', 9001))

# if result == 0:
#     print('Server is open!')
# else:
#     print('Server is closed :(')
# sock.close()