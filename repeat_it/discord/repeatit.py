import os, random, discord, sys, time
from discord.ext import tasks


token = os.getenv("DISCORD_TOKEN")
my_guild = os.getenv("DISCORD_GUILD")
intents = discord.Intents.default()
client = discord.Client(intents=intents)


#async def stats(ctx):
#    channel = client.get_channel(905445834592747600)
#    name = "/home/miner/dev/Crypto/closes.log"
#    with open(name, 'r') as f:
#        f = f.readlines()[-1]
#        await channel.send(f)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == my_guild:
            break

    print(
        f"{client.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
    )

    stats.start()
    closes.start()
    rsi.start()


@tasks.loop(minutes=1)
async def stats():
    channel = client.get_channel(905445834592747600)
    name = "/home/miner/dev/Crypto/sig.log"
    with open(name, 'r') as f:
        f = f.readlines()
        #await channel.send("Monitoring running. BTC/USDT - Binance - kline: 1 minute")
        await channel.send(f)

@tasks.loop(minutes=20)
async def closes():
    channel = client.get_channel(905445834592747600)
    name = "/home/miner/dev/Crypto/closes.log"
    with open(name, 'r') as f:
        f = f.readlines()[-1]
        await channel.send(f)

@tasks.loop(minutes=30)
async def rsi():
    channel = client.get_channel(905445834592747600)
    name = "/home/miner/dev/Crypto/rsi.log"
    with open(name, 'r') as f:
        f = f.readlines()[-1]
        await channel.send("Below is the latest RSI values")
        await channel.send(f)


#name = "/home/miner/dev/Crypto/closes.log"

#starttime = time.time()
#while True:
#    with open(name, 'r') as f:
#        f = f.readlines()[-1]
#        print(f)
#        time.sleep(60.0 -((time.time() - starttime) % 60.0))

client.run(token)
