from discord import Message, Embed # Importing necessary classes from discord.py
import requests # Used for making HTTP requests
import json # Used for parsing JSON data

def search(query):
    url = f'https://ac.cnstrc.com/autocomplete/{query.replace(" ", "%20")}?c=ciojs-client-2.35.2&key=key_XT7bjdbvjgECO5d8&i=7870065f-0570-401f-a5c0-8f46e51c8742&s=1&num_results_Products=25&num_results_Collections=20&_dt=1707708906394'

    html = requests.get(url=url) # Makes a GET request to the URL
    output = json.loads(html.text) # Parses the JSON response

    try:
        products = output['sections']['Products'] # Attempts to extract product data
        if products:
            return products[0] # Returns the first product found
    except (KeyError, IndexError):
        return None # Returns None if no product is found or if an error occurs
    
async def send_message(message: Message, embed: Embed) -> None:
    try:
        await message.channel.send(embed=embed) # Sends the embed to the channel
    except Exception as e:
        print(e) # Logs any exceptions
    
async def handle_goat_message(message: Message, query: str):
    result = search(query) # Searches for the product using the provided query
     
    if result:
        try:
            # Attempts to extract and convert the product's retail price from cents to dollars (CAD)
            price_in_cents_cad = result['data']['retail_price_cents_cad']
            price_in_dollars_cad = price_in_cents_cad / 100
        except KeyError:
            # Sends an error message if the retail price in CAD is not available
            await message.channel.send("Error: Retail price in CAD not available for this product. Please try again.")
            return

        # Prepares an embed with product details
        embed = Embed(
            title=result['value'],
            url='https://www.goat.com/en-ca/sneakers/' + result['data']['slug']
        )
        embed.set_thumbnail(
            url=result['data']['image_url']
        )
        embed.add_field(
            name='Color',
            value=result['data']['color'].capitalize()
        )
        embed.add_field(
            name='Category',
            value=result['data']['category'].capitalize()
        )        
        embed.add_field(
            name='Style ID',
            value=result['data']['sku']
        )    
        embed.add_field(
            name='Retail Price (USD)',
            value=f'${result["data"]["retail_price_cents"] / 100:,.2f}'
        )
        embed.add_field(
            name='Retail Price (CAD)',
            value=f'${price_in_dollars_cad:,.2f}'
        )
        embed.add_field(
            name='Lowest Price (USD)',
            value=f'${result["data"]["lowest_price_cents"] / 100:,.2f}'
        )
        embed.add_field(
            name='Lowest Price (CAD)',
            value=f'${result["data"]["lowest_price_cents_cad"] / 100:,.2f}'
        )
        embed.set_footer(
            text=" ©️ Made by SahajKAT and MAQ030",
            icon_url="https://avatars.githubusercontent.com/u/113306405?s=400&u=72fd60d4965008710d00c9f810c73b0811438a34&v=4"  # You can replace this with the URL of your GitHub profile picture
        )
        await send_message(message, embed) # Sends the prepared embed
    else:
        # Sends an error message if no matching product is found
        await message.channel.send("Error: No matching product found. Please try again.")

