from typing import Final  # Used for declaring constants
import os  # Used for accessing environment variables
from dotenv import load_dotenv  # Used for loading environment variables from a .env file
from discord import Intents, Client  # Importing necessary classes from discord.py library
from message_handling import handle_goat_message  # Importing a custom function for specific command handling

load_dotenv()  # Load environment variables from a .env file
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')  # Securely retrieves the bot's token from the environment variables

# Setting up the bot's intents, which specify what events the bot needs to receive
intents: Intents = Intents.default()
intents.message_content = True  # Enable the bot to receive message content

client: Client = Client(intents=intents)  # Initialize the Client with the specified intents

@client.event 
async def on_ready() -> None:
    # This event handler will run once the bot is connected and ready
    print(f'{client.user} is now running!')

@client.event 
async def on_message(message) -> None:
    # This event handler will run every time a message is received
    if message.author == client.user:
        return  # Ignore messages sent by the bot itself
    
    username: str = str(message.author)  # Extract the username of the message author
    user_message: str = message.content.lower()  # Convert the message to lowercase for case insensitivity
    channel: str = str(message.channel)  # Extract the channel name where the message was sent

    print(f'[{channel}] {username}: "{user_message}"')  # Log the message for debugging or monitoring
    
    if user_message.startswith('!goat '):
        query = user_message[6:]  # Extract the query part of the command
        await handle_goat_message(message, query)  # Handle the specific command with a custom function

def main() -> None:
    client.run(TOKEN)  # Start the bot using the token from the environment variable

if __name__ == "__main__":
    main()  # Entry point of the script
