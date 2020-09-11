# Sāc ar Discord un OS funkciju importēšanu
import discord
import os
# ^ darīts tavā vietā lai nav jātērē taustiņu klikšķi (ja nu lieto mehānisko :^)
from discord.ext import commands # Papildus komandas, "discord.ext = discord extended", noderēs!

bot = commands.Bot(command_prefix=!!!) # aizvieto trīs izsaukuma zīmes ar savu prefiksu, lielākā daļa botu lieto "!"; "?"; "." tādēļ iesaku izvēlēties kādu citu ja tavā serverī ir vairāki boti
# Šis būs kā paziņojums tavam botam, ka jebkura ziņa, kas sākas ar noteikto prefiksu ir jāizlasa un jāpārbauda vai ir iespējama attiecīga funkcija.

@bot.event
async def on_ready(): # Kad bots iedarbināts...
    # Šeit iespējams mainīt bota 'presence', piemēram "streaming" , "listening to..." un pat "playing".
    # Sekojošais komentārs būs piemērs bota statusam
    # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="memes"))
    # ja esi slinks un izmantosi to pašu line, atceries vienas pakāpes "indentation" lai tas atrodas ZEM "async" funkcijas.
    # Rezultātā botam vajadzētu rādīt "watching memes" zem tā nika.
    extensions = os.listdir("cogs") # tieši tā - zobratiņi :D
    for extension in extensions:
        if extension.endswith(".py"):
            bot.load_extension(f"cogs.{extension[:-3]}")
            # šīs rindiņas ir ļoti svarīgas, šim failam nav "TL;DR" opciju - izlasi visu!
            # funkcija sagatavos jebkuru failu iekš ATSEVIŠĶAS mapes vārdā "cogs" un pievienos to bota funkcionalitātei.
            # folderu struktūrai būtu jābūt " šī mape>bot.py>cogs>*pārējie faili, kas radīsies nākotnē* "
            # kādēļ? Jo to būs DAUDZ vieglāk organizēt nākotnē, kā arī pārbaudīt ~50 līniju failu ir daudz vieglāk nekā 500 līniju.
            # jā, tici man- būs daudz problēmu ja visas komandas tiks ievietotas šinī pašā failā
            # tomēr ja pa visu varu vēlies tā darīt, atceries "bot.run" funkciju vienmēr atstāt pēdējo.
# nu vari doties uz "cogs" folderi un sekot līdzi pirmajam "example" failam.
bot.run(" TAVA BOTA TOKENS, NERĀDI TO NEVIENAM ")