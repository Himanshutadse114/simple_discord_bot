
import nextcord
import discord
from neuralintents import GenericAssistant

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

client = discord.Client()


@client.event
async  def on_message(message):

    msg= message.author

    if msg == client.user:
          return
    if message.content.startswith("bot"):
        response = chatbot.request(message.content[2:])
        await message.channel.send(response)


client.run('your bot token')
