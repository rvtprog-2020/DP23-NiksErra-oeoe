# hei, hei! sveicināts zobratos, tagad esi iekļuvis bota "motorā" un tev ir dota iespēja pievienot bezgalīgi daudz cilindrus.
# (motora jauda šā vai tā būs pilnībā atkarīga no tavām Python zināšanām)

import discord
from discord.ext import commands
# tā, kā šis ir atsevišķs fails mums vajag importēt šos divus no jauna.
# OS import šoreiz nebūs vajadzīgs, taču ir iespēja, ka tavām idejām tas būs nepieciešams
# atceries visu vienmēr importēt sākumā un tikai pēc tam ķerties pie rakstīšanas

class Zobrati(commands.Cog): # "commands.Cog" case sensitive!!
    # Classname vari mainīt uz savu patvaļu, taču to būs jālieto starp VISIEM 'cogs'
    def __init__(self, bot):
        self.bot = bot
        @commands.command() #tagad sākas komandas daļa
        async def sveiks(self,ctx):
            await ctx.send("Sveiks! :^)")
# Kad ierakstīsi čatā " *prefikss*sveiks " bots tevi pasveicinās atpakaļ.
# Kad definē komandu, tā ir " async def sveiks(self,ctx): " daļa, vari iekavās pēc "ctx" ievietot vēl argumentus ja vēlies ievadīt citus datus, kurus bots spēs uzglabāt.
# vienmēr izmanto async funkciju, tas nozīmē, ka bots "neiekārsies" gaidot tavu ziņu un turpinās funkcionēt fonā, tajā pašā laikā gaidot vai nerodas kāds apstāklis, kas ir minēts kodā
# jebko zem "async" ievieto "await" funkcijā, es to vienīgais varu pielīdzināt tādam dinamiskam "if" variantam.

# sekojošās DIVAS rindas ir ļoti svarīgas, tās ir nepieciešamas KATRA "zobrata" faila beigās lai bots spētu to sagatavot darbībai. 
# Iztēlojies, ka botam ļoti patīk lasīt filmu titrus un tas sēdēs līdz ekrāns satumsīs. Iekļauj šīs divas līnijas vai arī bots paliks kinozālē gaidot titrus.
# Jā - pieminu ar nokavēšanos taču iekļauj arī sākuma līnijas "class" un "def __init__" katrā zobrata failā, tas savukārt ir kā filmas nosaukums.
# filma bez nosaukuma ir tikai video ar saturu, bots vēlas izlasīt nosaukumu, noskatīties sižetu un redzēt titrus.
def setup(bot):
    bot.add_cog(Zobrati(bot))

    # šo print komandu NAV jāiekļauj katrā "zobratā", taču ja tev patīk pētīt ļoti "spammy" termināli, droši vari kopēt to :D
    print("Bots ir gatavs funkcionēt")
# šis būtībā vien parāda to, ka bots atrada savu "cogs" folderi un spēja ielādēt vismaz pirmo (šo pašu) zobratu.
# PARASTI ja kāds zobrats ir kļūdaini uzrakstīts, bots izmetīs kļūdas kodu un paskaidrojumu.
# šo vari vienīgais izmantot lai padarītu savu darba termināli "aktīvāku", redzot kā bots iestartē katru zobratu pēc kārtas
# protams - tekstu var droši mainīt. Šeit tas tikpat labi varēja būt "pirmais zobrats ir sagatavots"...