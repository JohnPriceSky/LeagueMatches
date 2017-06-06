from django.db import models
import datetime


class Serie(models.Model):
    begin = models.DateField()
    end = models.DateField()

    def __str__(self):
        return str(self.begin) + ' - ' + str(self.end)


class Team(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Game(models.Model):
    date = models.DateField()
    length = models.IntegerField(default=20)
    teamA = models.ForeignKey(Team, related_name='teamA')
    teamB = models.ForeignKey(Team, related_name='teamB')
    winner = models.ForeignKey(Team, related_name='winner')
    serie = models.ForeignKey(Serie)

    def __str__(self):
        return self.teamA.name + ' vs ' + self.teamB.name + ' ' + str(self.date)

    def get_absolute_url(self):
        return "/games/%i/" % self.id


class Player(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    nickname = models.CharField(max_length=20)
    team = models.ForeignKey(Team)

    def __str__(self):
        return self.nickname


class Stat(models.Model):
    game = models.ForeignKey(Game)
    player = models.ForeignKey(Player)
    kills = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)

    def __str__(self):
        return str(self.game) + ' - ' + self.player.nickname


class Event(models.Model):
    type = models.CharField(max_length=20)
    value = models.FloatField()

    def __str__(self):
        return self.type


class MapObjective(models.Model):
    event = models.ForeignKey(Event, null=True)
    stat = models.ForeignKey(Stat, null=True)

    def __str__(self):
        return str(self.stat) + ' - ' + str(self.event)