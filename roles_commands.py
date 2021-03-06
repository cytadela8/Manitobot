import discord
from discord.ext import commands

import globals
import utility
from utility import get_member, InvalidRequest


class PoleceniaPostaci(commands.Cog, name="Polecenia postaci i frakcji"):

    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return not utility.lock

    def proper_channel():
        async def predicate(ctx):
            faction = globals.current_game.nights[-1].active_faction
            if not faction is None and ctx.channel != faction.channel:
                raise commands.NoPrivateMessage
            if faction is None and ctx.channel.type != discord.ChannelType.private:
                raise commands.PrivateMessageOnly
            return True

        return commands.check(predicate)

    async def command_template(self, ctx, member, operation):
        author = get_member(ctx.author.id)
        utility.lock = True
        try:
            faction = globals.current_game.nights[-1].active_faction
            if faction != None and faction == globals.current_game.nights[
                -1].active_role:
                await faction.new_activity(ctx, operation, member)
            else:
                await globals.current_game.player_map[
                    author].role_class.new_activity(ctx, operation, member)
        except InvalidRequest as err:
            await ctx.send(err.reason)
        except KeyError as err:
            await ctx.send("Nie grasz w tej grze")
            raise err
        utility.lock = False

    @commands.command(name='śledź')
    @commands.dm_only()
    async def follow(self, ctx, *, member):
        '''Służy do śledzenia'''
        await self.command_template(ctx, member, "follow")

    @commands.command(name='lustruj')
    @commands.dm_only()
    async def mirror(self, ctx, *, member):
        '''Służy do zlustrowania'''
        await self.command_template(ctx, member, "mirror")

    @commands.command(name='kopiuj')
    @commands.dm_only()
    async def copy_it(self, ctx):
        '''Służy do skopiowania zdolności'''
        await self.command_template(ctx, None, "copy")

    @commands.command(name='heretyk')
    @proper_channel()
    async def heretic(self, ctx, *, member):
        '''Służy do sprawdzenia czy osoba jest heretykiem'''
        await self.command_template(ctx, member, "heretic")

    @commands.command(name='przesz', aliases=['przeszukaj'])
    @proper_channel()
    async def research(self, ctx):
        '''/&przesz/Służy do przeszukania sprawdzanej osoby'''
        await self.command_template(ctx, None, "research")

    @commands.command(name='daj')
    @proper_channel()
    async def special_hold(self, ctx, *, member):
        '''Awaryjne oddawanie posążka w razie przerwania gry'''
        await self.command_template(ctx, member, "sphold")

    @commands.command(name='dobij')
    @proper_channel()
    async def finoff(self, ctx):
        '''Służy do zabicia sprawdzanej osoby'''
        await self.command_template(ctx, None, "finoff")

    @commands.command(name='posiadacze', aliases=['posiad'])
    @proper_channel()
    async def holders(self, ctx, *, member):
        '''/&posiad/Służy do sprawdzenia, czy osoba jest z frakcji posiadaczy posążka'''
        await self.command_template(ctx, member, "holders")

    @commands.command(name='spal')
    @commands.dm_only()
    async def burn(self, ctx, *, member):
        '''Służy biskupowi do zabicia i ujawnienia się'''
        globals.current_game.nights[-1].bishop_base = ctx
        author = get_member(ctx.author.id)
        utility.lock = True
        try:
            await globals.current_game.player_map[
                author].role_class.new_activity(ctx, "burn", member)
        except InvalidRequest as err:
            await ctx.send(err.reason)
        except KeyError as err:
            await ctx.send("Nie grasz w tej grze")
            raise err
        utility.lock = False

    @commands.command(name='podłóż', aliases=['podł'])
    @proper_channel()
    async def plant(self, ctx, *, member):
        '''/&podł/Służy do podłożenia posążka przez Cichą Stopę'''
        await self.command_template(ctx, member, "plant")

    @commands.command(name='ograj')
    @proper_channel()
    async def cheat(self, ctx, *, member):
        '''Służy do ogrania osoby przez Szulera'''
        await self.command_template(ctx, member, "cheat")

    @commands.command(name='ziółka', aliases=['zioł'])
    @proper_channel()
    async def herbs(self, ctx, *, member):
        '''/&zioł/Służy do podłożenia ziółek przez Szamankę'''
        await self.command_template(ctx, member, "herb")

    @commands.command(name='kto')
    @proper_channel()
    async def who(self, ctx):
        '''Służy do sprawdzenia kto ma posążek'''
        await self.command_template(ctx, None, "who")

    @commands.command(name='detektuj', aliases=['detekt'])
    @proper_channel()
    async def detect(self, ctx, *, member):
        '''/&detekt/Służy do użycia Detektora'''
        await self.command_template(ctx, member, "detect")

    @commands.command(name='karta')
    @proper_channel()
    async def card(self, ctx, *, member):
        '''Służy do prawdzenia karty'''
        await self.command_template(ctx, member, "check")

    @commands.command(name='rola')
    @proper_channel()
    async def role(self, ctx, *, member):
        '''Służy do sprawdzenia roli'''
        await self.command_template(ctx, member, "eat")

    @commands.command(name='szam')
    @proper_channel()
    async def szam(self, ctx, *, member):
        '''Służy do oszamanienia osoby'''
        await self.command_template(ctx, member, "szam")

    @commands.command(name='zabij')
    @proper_channel()
    async def zabij(self, ctx, *, member):
        '''Służy do zabicia osoby'''
        await self.command_template(ctx, member, "kill")

    @commands.command(name='posążek', aliases=['pos'])
    @proper_channel()
    async def posag(self, ctx, *, member):
        '''Służy do przeszukania osoby'''
        await self.command_template(ctx, member, "hold")

    @commands.command(name='szukaj')
    @proper_channel()
    async def szukaj(self, ctx, *, member):
        '''Służy do przeszukania osoby'''
        await self.command_template(ctx, member, "search")

    @commands.command(name='graj')
    @commands.dm_only()
    async def play(self, ctx, *, member):
        '''Służy do zabicia osoby przez Hazardzistę'''
        await self.command_template(ctx, member, "play")

    @commands.command(name='upij', aliases=['pij'])
    @commands.dm_only()
    async def drink(self, ctx, *, member):
        '''/&pij/Służy do upijania przez Opoja lub Pijanego Sędziego'''
        await self.command_template(ctx, member, "drink")

    @commands.command(name='dziw', aliases=['zadziw'])
    @commands.dm_only()
    async def hmmm(self, ctx, *, member):
        '''/&zadziw/Służy do sprawdzenia osoby przez Dziwkę'''
        await self.command_template(ctx, member, "dziw")

    @commands.command(name='zamknij', aliases=['zamk'])
    @commands.dm_only()
    async def arrest(self, ctx, *, member):
        '''/&zamk/Służy do zamknięcia osoby przez Szeryfa'''
        await self.command_template(ctx, member, "arrest")

    @commands.command(name='spowiedź', aliases=['spowiadaj', 'spow'])
    @commands.dm_only()
    async def pasteur(self, ctx, *, member):
        '''/&spow/Służy do wyspowiadania osoby przez pastora'''
        await self.command_template(ctx, member, "pasteur")

    @commands.command(name='wygrywa', aliases=['wygr'])
    @commands.dm_only()
    async def wins(self, ctx, *, member=None):
        '''/&wygr/Służy do ujawnienia się przez Sędziego, użyte z nazwą gracza powoduje, że wygrywa on pojedynek, użyte samo ujawnia Sędziego powodując utratę zdolności'''
        await self.command_template(ctx, member, "wins")

    @commands.command(name='veto', aliases=['łaska'])
    @commands.dm_only()
    async def veto(self, ctx):
        '''/&łaska/Służy do ujawnienia się przez Burmistrza, użyte w trakcie wieszania ułaskawia, użyte poza ujawnia Burmistrza powodując utratę zdolności'''
        await self.command_template(ctx, None, "peace")

    @commands.command(name='nie')
    async def nein(self, ctx):
        '''Służy do odmowy skorzystania ze zdolności'''
        await self.command_template(ctx, None, "refuse")

    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.PrivateMessageOnly):
            await ctx.send("Tej komendy teraz można używać tylko w DM")
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send(
                "Tej komendy teraz można używać tylko na kanale frakcji")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("Spróbuj ponownie za chwilę")

    """@commands.command(name='arrest')
    async def arrest(self, ctx, *, member):
      '''Służy do zamknięcia osoby w więzieniu'''
      player = get_member(ctx.author.id)
      try:
        if globals.current_game.active_player.player.member != player:
          raise AttributeError
        await globals.current_game.active_player.activity(ctx, member)
        await ctx.send("Pomyślnie zamknięto {}".format(member))
      except InvalidRequest as err:
        await ctx.send(err.reason)
      except AttributeError:
        await ctx.send("Nie możesz teraz zamykać (lub w ogóle).")
  
    @commands.command(name='drink')
    async def drink(self, ctx, *, member):
      '''Służy do upicia osoby'''
      player = get_member(ctx.author.id)
      try:
        if globals.current_game.active_player == None or  globals.current_game.active_player.player.member != player:
          raise AttributeError
        await globals.current_game.active_player.activity(ctx, member)
        await ctx.send("Pomyślnie upito {}".format(member))
      except InvalidRequest as err:
        await ctx.send(err.reason)
      except AttributeError:
        await ctx.send("Nie możesz teraz upijać (lub w ogóle).")
  
    @commands.command(name='pasteur')
    async def pasteurization(self, ctx, *, member):
      '''Służy do sprawdzenia osoby przez pastora'''
      player = get_member(ctx.author.id)
      try:
        if globals.current_game.active_player.player.member != player:
          await ctx.send("Nie możesz teraz sprawdzać (lub w ogóle).")
          return
        await globals.current_game.active_player.activity(ctx, member)
        await ctx.send("Pomyślnie sprawdzono {}".format(member))
      except InvalidRequest as err:
        await ctx.send(err.reason)
      except:
        await ctx.send("Nie możesz teraz sprawdzać (lub w ogóle).")
  
    @commands.command(name='dziw')
    async def hooking(self, ctx, *, member):
      '''Służy do zadziwienia osoby przez dziwkę'''
      player = get_member(ctx.author.id)
      try:
        if globals.current_game.active_player.player.member != player:
          raise AttributeError
        await globals.current_game.active_player.activity(ctx, member)
        await ctx.send("Pomyślnie zadziwiono {}".format(member))
      except InvalidRequest as err:
        await ctx.send(err.reason)
      except AttributeError:
        await ctx.send("Nie możesz teraz działać (lub w ogóle).")
  
  
    @commands.command(name='sędzia')
    @manitou_cmd
    async def sedzia(self,ctx):
      '''Służy do ujawnienia się sędziego przez sędziego lub Manitou'''
      member = get_member(ctx.author.id)
      if czy_manitou(ctx):
        try:
          me = globals.current_game.role_map["Pijany_Sędzia"]
        except:
          try:
            me = globals.current_game.role_map["Sędzia"]
          except:
            await ctx.send("W tej grze nie gra sędzia lub gra nie została rozpoczęta")
            return
        member = me.player.member
      if ctx.channel.type != discord.ChannelType.private and not czy_manitou(ctx):
        await ctx.send("Tą wiadomość można wysłać tylko na priv")
        return
      try:
        role = globals.current_game.player_map[member].role
      except:
        ctx.send("Gra nie została rozpoczęta")
      if role != "Sędzia" and role != "Pijany_Sędzia":
        await ctx.send("Tylko Sędzia lub Manitou może użyć tej komendy")
        return
      nickname = get_nickname(member.id)
      if nickname[-1] != ')':
        try:
          await member.edit(nick=nickname + "({})".format(globals.current_game.player_map[member].role))
        except discord.errors.Forbidden:
          await ctx.send("Nie mam uprawnień aby zmienić nick")
        await get_town_channel().send("Rola **{}** to **{}**".format(nickname.replace('+',' '),globals.current_game.player_map[member].role))
      else:
        await ctx.send("Sędzia jest już ujawniony")
      await ctx.send("Done!")
  
  
    @commands.command(name='burmistrz')
    async def burmistrz(self,ctx):
      '''Służy do ujawnienia się burmistrza przez burmistrza lub Manitou'''
      member = get_member(ctx.author.id)
      if czy_manitou(ctx):
        try:
          me = globals.current_game.role_map["Burmistrz"]
        except:
          await ctx.send("W tej grze nie gra burmistrz lub gra nie została rozpoczęta")
          return
        member = me.player.member
      if ctx.channel.type != discord.ChannelType.private and not czy_manitou(ctx):
        await ctx.send("Tą wiadomość można wysłać tylko na priv")
        return
      try:
        role = globals.current_game.player_map[member].role
      except:
        ctx.send("Gra nie została rozpoczęta")
      if role != "Burmistrz":
        await ctx.send("Tylko burmistrz lub Manitou może użyć tej komendy")
        return
      nickname = get_nickname(member.id)
      if nickname[-1] != ')':
        try:
          await member.edit(nick=nickname + "({})".format(globals.current_game.player_map[member].role))
        except discord.errors.Forbidden:
          await ctx.send("Nie mam uprawnień aby zmienić nick")
        await get_town_channel().send("Rola **{}** to **{}**".format(nickname.replace('+',' '),globals.current_game.player_map[member].role))
      else:
        await ctx.send("Burmistrz jest już ujawniony")
      await ctx.send("Done!")"""

    '''@commands.command(name='no')
    async def refuse(self, ctx):
      """Odmowa skorzystania postaci z nocnej możliwości"""
      member = get_member(ctx.author)
      try:
        player = globals.current_game.player_map[member]
        if not player.active:
          await ctx.send("Nie możesz teraz korzystać ze swojej zdolności, tym bardziej odmówić korzystania!")
          return
        if not player.can_refuse():
          await ctx.send("Nie możesz odmówić skorzystania ze swojej zdolności!")
          return
        player.active = False
        globals.current_game.active_player = None
        await send_to_manitou("{} nie skorzystał ze swojej zdolności".format(player.role))
        await ctx.send("Done!")
      except:
        await ctx.send("Nie grasz teraz")'''
