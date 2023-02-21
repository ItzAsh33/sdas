import requests, random 
from discord_webhook import DiscordWebhook, DiscordEmbed # pip install discord_webhook
print('''\x1b[34m
GROUP FINDER FREE SOURCE CODE! 
''')
print("\x1b[32mSTAR THE REPO ON GITHUB ! \x1b[39m")
while True:
        ID = random.randint(1000000, 16000000) # Start and stop IDs edit this if you want!
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1077431755218374768/SplG4vTb26SzERnGAeO3px9Jeny7YLbk4OaRvWrA0jOgm8vPtdSLdX5E96Wm7uhgTC20") # initates connection with discord_webhook module
        r = requests.get(f'https://groups.roblox.com/v1/groups/{ID}') #sends requests using id
        json = r.json() # json
        if 'owner' in r.text: #checks if the group is valid to prevent key errors
                if json['owner'] == None and json['publicEntryAllowed'] == True and 'isLocked' not in r.text: # check if the group isnt locked and is open with no owner
                        members = json['memberCount'] #members
                        desc = json['description'] #obvious what this one is
                        print(f"\x1b[42mhttps://www.roblox.com/groups/{ID}")
                        print(r.text)
                        embed = DiscordEmbed(title='New Group Found! Group', color=242424) # embed title
                        embed.add_embed_field(name='ID', value=f'{ID}') #Id to embed
                        embed.add_embed_field(name='Description', value=f'"{desc}"') #description to embed
                        embed.add_embed_field(name='Members', value=f'{members}') #adds members to embed
                        embed.add_embed_field(name='Link', value=f'https://www.roblox.com/groups/{ID}') # im getting bored commenting
                        embed.set_author(name='Boblox Hub', icon_url='https://cdn.discordapp.com/icons/993314189223415808/a_ff7d44a66f07a91be082e2168c5a5a00.gif?size=4096') #stuff
                        embed.set_footer(text='Boblox Hub', icon_url='https://cdn.discordapp.com/icons/993314189223415808/a_ff7d44a66f07a91be082e2168c5a5a00.gif?size=4096') # stuff
                        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/993314189223415808/a_ff7d44a66f07a91be082e2168c5a5a00.gif?size=4096')
                        webhook.add_embed(embed) #adds the embed to the response
                        response = webhook.execute() # sends to webhook
                else:
                        print(f"\x1b[31mNothing found... https://discord.gg/KaMcTSH88d {ID}")                     
        else:
                print(f"\x1b[31mNothing found... https://discord.gg/KaMcTSH88d {ID}") 