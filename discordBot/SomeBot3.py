# Import libraries
# Interacts with discord
import discord
# Interacts with operating system
import os
# Generates random integers
import random
# Import request for package
from ec2_metadata import ec2_metadata

# Creates client object for accessing Bot from discord library.
client = discord.Bot()

'''Returns value of environmental variable accessed from the operating system. 
This value is stored as a string in the token object. Environmental variable should 
have already been created in ec2 instance with a value of the token you got from discord.'''
token = os.getenv("TOKEN")

'''Registers function as event listener. The client handles the event and connects to discord. 
    After connection, on_ready function is called. Prints formatted string to terminal.'''
@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

# Defines an event for discord bot.  
@client.event 
# Defines an asynchronous function that takes a message object as a parameter.
async def on_message(message): 

    '''The username of the user who sent the message is taken as a string. Split is used to take 
        the information before the "#" and store it as "username" variable. 
        For example the SomeBot in SomeBot#2759 is extracted.'''
    username = str(message.author).split("#")[0] 

    # Obtains the name of the channel where the message was sent.
    channel = str(message.channel.name) 

    # Obtains the what was written in the message in string format.
    user_message = str(message.content) 

    # All 3 variables are embedded into this string and printed on terminal.
    print(f'Message {user_message} by {username} on {channel}') 

    '''return is only executed if the author of the message is the bot. 
        Function continues running if the author is not the bot.'''
    if message.author == client.user: 
        return

    # Checking if channel name is "random"
    if channel == "random": 

        '''Converts the user message into lower case and checks if the message is equal to "hello" or "hi".
            Following code is run if either is true.'''
        if user_message.lower() == "hello" or user_message.lower() == 'hello world' or user_message.lower() == "hi": 

            '''await suspends execution till data is completed. In the channel the message was sent, the bot sends 
                back a message in a formatted string with the value of the username variable and the region the EC2 
                instance is running in.'''
            await message.channel.send(f'Hello {username}') 
            # Exits function to prevent looking for other identical conditions and sending multiple responses.
            return

        # Converts the user message into lower case and checks if the message is equal to string.
        elif user_message.lower() == "bye": 
            # Does same thing as previous await except sending the message "bye" with users username embedded.
            await message.channel.send(f'Bye {username}') 
            return

        # Does the same thing as previous options.    
        elif user_message.lower() == "ec2 data" or  user_message.lower() == "tell me about my server!": 

            # ec2 data is sent.
            await message.channel.send(f'Your EC2 Instance Data: Public IPv4 Address: {ec2_metadata.public_ipv4}, Instance Region: {ec2_metadata.region}, Instance Availability Zone: {ec2_metadata.availability_zone}, Instance ID: {ec2_metadata.instance_id}') 
            return
        
# Pass token object to run code
client.run(token)

