import datetime

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from fernet_fields import EncryptedIntegerField

from pytz import utc


class Team(models.Model):
    name = models.CharField(max_length=35, blank=False)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=35, blank=False)

    def __str__(self):
        return self.name


class Bet(models.Model):
    TYPE_A = 'type_a'
    TYPE_B = 'type_b'
    TYPE_C = 'type_c'
    TYPE_D = 'type_d'
    TYPE_E = 'type_e'
    TYPE_F = 'type_f'
    TYPE_G = 'type_g'


    BETS_TYPES = (
        (TYPE_A, 'Резултат от мач'),
        (TYPE_B, 'Класиране в група'),
        (TYPE_C, 'Голмайстор'),
        (TYPE_D, 'Втори голмайстор'),
        (TYPE_E, 'Шампион'),
        (TYPE_F, 'Резултат от мач / Отбор победител'),
        (TYPE_G, 'Голмайстор брой голове'),
    )
    name = models.CharField(max_length=35, default='Резултат от мач')
    type = models.CharField(max_length=35, choices=BETS_TYPES, default=TYPE_A)
    time_to_edit = models.DateTimeField()
    type_a_1_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_a_1', blank=True, null=True)
    type_a_2_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name= 'team_a_2', blank=True, null=True)
    is_result_a = models.BooleanField(default=False)
    type_a_1_result= models.IntegerField(blank=True, null=True)
    type_a_2_result = models.IntegerField(blank=True, null=True)
    type_b_1_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name= 'team_b_1', blank=True, null=True)
    type_b_2_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name= 'team_b_2', blank=True, null=True)
    type_b_3_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name= 'team_b_3', blank=True, null=True)
    type_b_4_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name= 'team_b_4', blank=True, null=True)
    is_result_b = models.BooleanField(default=False)
    type_b_1_result = models.IntegerField(blank=True, null=True)
    type_b_2_result = models.IntegerField(blank=True, null=True)
    type_b_3_result = models.IntegerField(blank=True, null=True)
    type_b_4_result = models.IntegerField(blank=True, null=True)
    is_result_c = models.BooleanField(default=False)
    type_c_result = models.ForeignKey(Player, on_delete=models.CASCADE, related_name= 'player_c_1', blank=True, null=True)
    is_result_d = models.BooleanField(default=False)
    type_d_result = models.ForeignKey(Player, on_delete=models.CASCADE, related_name= 'player_d_1', blank=True, null=True)
    is_result_e = models.BooleanField(default=False)
    type_e_result = models.ForeignKey(Team, on_delete=models.CASCADE, related_name= 'team_е_1', blank=True, null=True)
    type_f_1_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name= 'team_f_1', blank=True, null=True)
    type_f_2_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name= 'team_f_2', blank=True, null=True)
    is_result_f = models.BooleanField(default=False)
    type_f_1_result = models.IntegerField(blank=True, null=True)
    type_f_2_result = models.IntegerField(blank=True, null=True)
    type_f_3_result = models.ForeignKey(Team, on_delete=models.CASCADE, related_name= 'team_f_3', blank=True, null=True)
    is_result_g = models.BooleanField(default=False)
    type_g_result = models.IntegerField(blank=True, null=True)

    def __str__(self):
        if self.type == 'type_a':
            return str(self.id) + ' ' + self.name + ' ' + self.type_a_1_team.name + ' ' + self.type_a_2_team.name
        if self.type == 'type_b':
            return str(self.id) + ' ' + self.name
        if self.type == 'type_c':
            return str(self.id) + ' ' + self.name
        if self.type == 'type_d':
            return str(self.id) + ' ' + self.name
        if self.type == 'type_e':
            return str(self.id) + ' ' + self.name
        if self.type == 'type_f':
            return str(self.id) + ' ' + self.name + ' ' + self.type_f_1_team.name + ' ' + self.type_f_2_team.name
        if self.type == 'type_g':
            return str(self.id) + ' ' + self.name


    @property
    def is_possible_edit(self):
        expired_on = self.time_to_edit.replace(tzinfo=utc)
        checked_on = datetime.datetime.now().replace(tzinfo=utc)

        return expired_on > checked_on

    @property
    def fteams(self):
        teams = []
        teams.append(self.type_f_1_team.name)
        teams.append(self.type_f_2_team.name)
        return teams


class Mybet (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bet = models.ForeignKey(Bet, on_delete=models.CASCADE)
    type_a_bet_1 = EncryptedIntegerField(blank=False, default=0)
    type_a_bet_2 = EncryptedIntegerField(blank=False, default=0)
    type_b_bet_1 = EncryptedIntegerField(blank=False, default=1, validators=[MinValueValidator(1), MaxValueValidator(4)])
    type_b_bet_2 = EncryptedIntegerField(blank=False, default=2, validators=[MinValueValidator(1), MaxValueValidator(4)])
    type_b_bet_3 = EncryptedIntegerField(blank=False, default=3, validators=[MinValueValidator(1), MaxValueValidator(4)])
    type_b_bet_4 = EncryptedIntegerField(blank=False, default=4, validators=[MinValueValidator(1), MaxValueValidator(4)])
    type_c_bet_1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='goalscorer', blank=True, null=True, default='')
    type_d_bet_1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='second_goalscorer', blank=True, null=True, default='')
    type_e_bet_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='champion', blank=True, null=True, default='')
    type_f_bet_1 = EncryptedIntegerField(blank=False, default=0, validators=[MinValueValidator(0), MaxValueValidator(20)])
    type_f_bet_2 = EncryptedIntegerField(blank=False, default=0, validators=[MinValueValidator(0), MaxValueValidator(20)])
    type_f_bet_3 = models.CharField(max_length=35, default='')
    type_g_bet_1 = EncryptedIntegerField(blank=False, default=0, validators=[MinValueValidator(0), MaxValueValidator(20)])


    @property
    def points (self):
        points = 0
        if self.bet.type == 'type_a':
            if self.bet.is_result_a == True:
                if self.bet.type_a_1_result == self.type_a_bet_1 and self.bet.type_a_2_result == self.type_a_bet_2:
                    points += 2
                else:
                    if self.type_a_bet_1 > self.type_a_bet_2:
                        if self.bet.type_a_1_result > self.bet.type_a_2_result:
                            points += 1
                    elif self.type_a_bet_1 == self.type_a_bet_2:
                        if self.bet.type_a_1_result == self.bet.type_a_2_result:
                            points += 1
                    else:
                        if self.bet.type_a_1_result < self.bet.type_a_2_result:
                            points += 1
        if self.bet.type == 'type_b':
            if self.bet.is_result_b == True:
                results = {}
                bets = {}
                results[self.bet.type_b_1_result] = 1
                results[self.bet.type_b_2_result] = 2
                results[self.bet.type_b_3_result] = 3
                results[self.bet.type_b_4_result] = 4
                bets[self.type_b_bet_1] = 1
                bets[self.type_b_bet_2] = 2
                bets[self.type_b_bet_3] = 3
                bets[self.type_b_bet_4] = 4
                sorted_results = sorted(results.items())
                sorted_bets = sorted(bets.items())
                if sorted_bets[0][1] == sorted_results[0][1]:
                    points += 2
                elif sorted_bets [0][1] == sorted_results[1][1]:
                    points += 1
                if sorted_bets[1][1] == sorted_results[0][1]:
                    points +=1
                elif sorted_bets[1][1] == sorted_results[1][1]:
                    points +=1
                if sorted_bets[2][1] == sorted_results[2][1] and sorted_bets[3][1] == sorted_results[3][1]:
                    points += 0.5
        if self.bet.type == 'type_c':
            if self.bet.is_result_c == True:
                if self.bet.type_c_result == self.type_c_bet_1:
                    points += 4
        if self.bet.type == 'type_d':
            if self.bet.is_result_d == True:
                if self.bet.type_d_result == self.type_d_bet_1:
                    points += 1.5
        if self.bet.type == 'type_e':
            if self.bet.is_result_e == True:
                if self.bet.type_e_result == self.type_e_bet_1:
                    points += 5
        if self.bet.type == 'type_f':
            if self.bet.is_result_f == True:
                if self.bet.type_f_1_result == self.type_f_bet_1 and self.bet.type_f_2_result == self.type_f_bet_2:
                    points += 2
                else:
                    if self.type_f_bet_1 > self.type_f_bet_2:
                        if self.bet.type_f_1_result > self.bet.type_f_2_result:
                            points += 1
                    elif self.type_f_bet_1 == self.type_f_bet_2:
                        if self.bet.type_f_1_result == self.bet.type_f_2_result:
                            points += 1
                    else:
                        if self.bet.type_f_1_result < self.bet.type_f_2_result:
                            points += 1
                if self.bet.type_f_3_result.name == self.type_f_bet_3:
                    points += 0.5
        if self.bet.type == 'type_g':
            if self.bet.is_result_g == True:
                if self.bet.type_g_result == self.type_g_bet_1:
                    points += 1
        return points