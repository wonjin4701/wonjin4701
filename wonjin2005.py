

import discord
 

token = "NzE2OTEzOTI5Nzk5OTkxMzQ5.XtSsJA.dfEfZxvKt-_MjeFQ3CqK8KV7Y2k"
client = discord.Client()


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game("테스트중"))
  print("원진#7917") 
  print(client.user.name) 
  print(client.user.id) 
   
@client.event
async def on_message(message):
 
  if message.content.startswith('/인증'): 
    author = message.guild.get_member(int(message.author.id))
    role = discord.utils.get(message.guild.roles, name="TEST") 
    await author.add_roles(role)
    await message.channel.send('인증완료') 













  

client.run(token)

