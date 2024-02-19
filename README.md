# GOAT-Discord-Bot

This Discord bot fetches and organizes data from GOAT, an online store for sneakers, apparel, and accessories, using web scraping. It also has reliable error handling to quickly address issues with unavailable or non-existent items.

## Setup Instructions

#### 1. Install Python and Required Libraries:
   - Ensure Python is installed on your system ([Download Python](https://www.python.org/))
   - Install the required libraries using pip:
     
     ```
     pip install discord.py python-dotenv requests
     ```

#### 2. Create a Discord Bot:
   - Navigate to the Discord Developer Portal ([Discord Developer Portal](https://discord.com/developers/applications))
   - Create a new application
   - Navigate to the "Bot" tab and click "Add Bot"
   - Copy the generated token and paste it into your `.env` file as `DISCORD_TOKEN`

#### 3. Enable Message Intents:
   - In the Discord Developer Portal, go to the "Bot" tab of your application
   - Enable the "PRESENCE INTENT" and "SERVER MEMBERS INTENT" under the "Privileged Gateway Intents" section

#### 4. File Overview:
   - The file `bot_setup.py` contains the core functionality of the Discord bot. It interacts with Discord servers, handles messages, and processes commands related to querying GOAT's database.
   - The `message_handling.py` file manages incoming messages for the bot, incorporating web scraping for efficient product searches on the GOAT website.

#### 5. Run the Bot:
   - Run your bot script by executing `bot_setup.py`.
   - Your bot should now be online and responding to commands prefixed with `!goat`.

#### Note:
   - Make sure to handle environment variables securely.
   - You may need to adjust permissions and roles within your Discord server for the bot to function correctly.
   - Make sure to set up your `.env` file with your Discord token before running the bot script.
  
## Demonstration 
https://github.com/SahajKAT/GOAT-Discord-Bot/assets/113306405/47f3fcc7-1124-4a07-99e7-e680077963c3

