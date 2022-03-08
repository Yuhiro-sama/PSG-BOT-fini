import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(
            title="Page d'aide",
            description="Vous trouverez ici toutes les commandes du bot !",
            color=0x0AAB1D
        )
        
        embed.add_field(
            name="Commandes Argent ",
            value="-Faites `-addcoin ou +removecoin <membre> <montant>` pour ajouter/retirer des coins à un membre \n\n -Faites `+say <message>` pour faire répéter un message au bot \n\n -Faites `-buy <role>` pour acheter un role qui est dans le shop \n\n -Faites `-shop` pour voir les roles à vendre \n\n -Faites  `-addshop` pour ajouter un role au shop (sans permissions administrateur) "
        )
        embed.add_field(
            name="Commandes Ticket \n",
            value="-Faites `-ticket` pour afficher l'embed du ticket "
        )
        embed.add_field(
            name="Commandes Divers",
            value="-Faites `-top` pour voir les membres qui sont dans le top level \n\n -Faites `-rank <membre(optionel)>` pour voir vos statistiques \n\n -Faites `-pub` pour voir les règles de publicité"
        )
        await ctx.send(embed=embed)
    
        

def setup(bot):
    bot.add_cog(Help(bot))