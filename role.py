import inspect

import globals
import permissions
from activities import Activity
from night_comunicates import operation_send, new_night_com
from postacie import give_faction
from utility import *


class Role(Activity):
    def __init__(self, name, player):
        self.roled_members = [None]
        self.name = name
        self.player = player
        self.revealed = False
        self.die_reason = None
        self.faction = None
        self.worked = True
        self.member = None
        try:
            self.ability_start = permissions.role_activities[name][0]
            self.count = permissions.role_activities[name][1]
            self.my_activities = permissions.role_activities[name][2].copy()
        except KeyError:
            self.ability_start = None
            self.count = None
            self.my_activities = {}

    async def new_night_start(self):
        output = ""
        if "start" in self.my_activities:
            for f in permissions.get_activity(self.my_activities["start"],
                                              self):
                if inspect.iscoroutinefunction(f):
                    await f()
                else:
                    f()
        if self.player.member in get_dead_role().members and not self.revealed:
            self.refusal()
            raise InvalidRequest(
                "{} nie żyje i nie jest ujawniony".format(self.name))
        if self.player.member in get_dead_role().members:
            raise InvalidRequest()
        if globals.current_game.day < self.ability_start:
            raise InvalidRequest()
        if globals.current_game.day != 0 and self.ability_start == -1:
            raise InvalidRequest()
        if self.player.sleeped:
            self.roled_members.append(None)
            self.refusal()
            raise InvalidRequest(
                "{} nie budzi się tej nocy, bo jest zamknięty(-a) lub upity(-a)".format(
                    self.name))
        if self.count == 0:
            self.refusal()
            raise InvalidRequest(
                "{} wykorzystał(-a) już swoje zdolności".format(
                    self.name.replace('_', ' ')))
        globals.current_game.nights[-1].active_role = self
        # self.player.active = True
        com = new_night_com[self.name]
        for c, f in com:
            output += c.format(self.my_activities[f])
        return output

    async def new_activity(self, ctx, operation,
                           member=None):  # working in progress
        if operation not in self.my_activities:
            raise InvalidRequest("Nie możesz użyć tego polecenia")
        if self.my_activities[operation] == 0:
            raise InvalidRequest("Nie możesz więcej użyć tej zdolności")
        self.member = member
        if not member is None:
            member = await converter(ctx, member)
            if member not in get_guild().members:
                raise InvalidRequest("Nie ma takiej osoby")
            if member not in get_player_role().members or member in get_dead_role().members:
                raise InvalidRequest("Ta osoba nie gra lub nie żyje")
            self.member = globals.current_game.player_map[member]
        output = ""
        try:
            for f in permissions.get_activity(operation, self):
                if inspect.iscoroutinefunction(f):
                    ret = await f()
                else:
                    ret = f()
                if not ret is None:
                    output += ret
        except InvalidRequest as err:
            raise InvalidRequest(err.reason)
        self.my_activities[operation] -= 1
        if output:
            await ctx.send(output)
        await operation_send(operation, self.player.member, self.name, member)
        self.roled_members.append(self.member)
        await ctx.message.add_reaction('✅')

    # efekty przy śmierci np. ochroniarz w operacjach pod die lista operacji
    async def die(self, reason=None):
        gracz = self.player.member
        try:
            globals.current_game.days[-1].remove_member(gracz)
            if self in globals.current_game.days[-1].duelers:
                await globals.current_game.days[-1].interrupt()
                await get_town_channel().send(
                    "Pojedynek został anulowany z powodu śmierci jednego z pojedynkujących")
            globals.current_game.days[-1].remove_member(self.player.member)
        except InvalidRequest:
            pass
        except AttributeError:
            pass
        await gracz.remove_roles(get_player_role())
        await gracz.add_roles(get_dead_role())
        nickname = gracz.display_name
        await get_town_channel().send("Ginie **{}**".format(nickname))
        await get_glosowania_channel().send("Ginie **{}**".format(nickname))
        self.die_reason = reason
        try:
            actions = self.my_activities["die"]
            for f in permissions.get_activity(actions, self):
                if inspect.iscoroutinefunction(f):
                    await f()
                else:
                    f()
        except KeyError:
            pass
        except InvalidRequest:
            pass
        try:
            globals.current_game.stats[give_faction(self.name)] -= 1
            if self.faction.leader == self.player and \
                    globals.current_game.nights[
                        -1].active_faction == self.faction:
                for role in self.faction.roles.values():
                    if role.player.member not in get_dead_role() and not role.player.sleeped:
                        self.faction.leader = role.player
                        await self.faction.channel.send(
                            "Ginie {}\nNowym liderem zostaje {}".format(
                                self.player.member.display_name,
                                self.faction.leader.role))
                        break
        except (KeyError, AttributeError):
            pass
        if nickname[0] != '+':
            try:
                await gracz.edit(nick="+" + nickname)
            except discord.errors.Forbidden:
                await gracz.send("Dodaj sobie '+' przed nickiem")
        if not globals.current_game.night and not self.revealed:
            await self.reveal()
        if self.die_reason == "herbs":
            globals.current_game.statue.day_search(self.player.member)
        self.indian_win()
        if not globals.current_game.night:
            self.inqui_win()
            if self.die_reason != "herbs":
                globals.current_game.statue.day_search(self.player.member)
        else:
            self.inqui_alone_win()
        self.unfollow()
        try:
            await globals.current_game.days[-1].if_next()
        except AttributeError:
            pass

    def alive(self):
        return self.player.member not in get_dead_role().members

    def work(self):
        if globals.current_game.day < self.ability_start:
            return False
        if globals.current_game.day != 0 and self.ability_start == -1:
            return False
        if self.player.member in get_dead_role().members and self.revealed:
            return False
        return True
