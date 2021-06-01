import instance as instance
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import models

from loto.loto_app.common import myfunc
from loto.loto_app.models import Mybet, Player, Team, Bet


class AbetForm(forms.ModelForm):
    class Meta:
        model = Mybet
        fields = ('type_a_bet_1', 'type_a_bet_2')
        widgets = {
            'type_a_bet_1': forms.NumberInput(attrs={'class': 'bet-bets-1', 'min': '0', 'max': '20', 'size': '2'}),
            'type_a_bet_2': forms.NumberInput(attrs={'class': 'bet-bets-2', 'min': '0', 'max': '20', 'size': '2'}),
        }
        labels = {
            'type_a_bet_1': '',
            'type_a_bet_2': '',
        }

class BbetForm(forms.ModelForm):
    class Meta:
        model = Mybet
        fields = ('type_b_bet_1', 'type_b_bet_2', 'type_b_bet_3', 'type_b_bet_4')
        widgets = {
            'type_b_bet_1': forms.NumberInput(attrs={'class': 'bet-bets-1', 'min': '1', 'max': '4', 'size': '1'}),
            'type_b_bet_2': forms.NumberInput(attrs={'class': 'bet-bets-1', 'min': '1', 'max': '4', 'size': '1'}),
            'type_b_bet_3': forms.NumberInput(attrs={'class': 'bet-bets-1', 'min': '1', 'max': '4', 'size': '1'}),
            'type_b_bet_4': forms.NumberInput(attrs={'class': 'bet-bets-1', 'min': '1', 'max': '4', 'size': '1'}),
        }
        labels = {
            'type_b_bet_1': '',
            'type_b_bet_2': '',
            'type_b_bet_3': '',
            'type_b_bet_4': '',
        }

        class BbetForm(forms.ModelForm):
            class Meta:
                model = Mybet
                fields = ('type_b_bet_1', 'type_b_bet_2', 'type_b_bet_3', 'type_b_bet_4')
                widgets = {
                    'type_b_bet_1': forms.NumberInput(
                        attrs={'class': 'bet-bets-1', 'min': '1', 'max': '4', 'size': '1'}),
                    'type_b_bet_2': forms.NumberInput(
                        attrs={'class': 'bet-bets-1', 'min': '1', 'max': '4', 'size': '1'}),
                    'type_b_bet_3': forms.NumberInput(
                        attrs={'class': 'bet-bets-1', 'min': '1', 'max': '4', 'size': '1'}),
                    'type_b_bet_4': forms.NumberInput(
                        attrs={'class': 'bet-bets-1', 'min': '1', 'max': '4', 'size': '1'}),
                }
                labels = {
                    'type_b_bet_1': '',
                    'type_b_bet_2': '',
                    'type_b_bet_3': '',
                    'type_b_bet_4': '',
                }


    def clean(self):
        cleaned_data = super().clean()
        t1 = cleaned_data.get("type_b_bet_1")
        t2 = cleaned_data.get("type_b_bet_2")
        t3 = cleaned_data.get("type_b_bet_3")
        t4 = cleaned_data.get("type_b_bet_4")
        if t1 and t2 and t3 and t4:
            if t1 == t2 or t1 == t3 or t1 == t4 or t2 == t3 or t2 == t4 or t3 == t4:
                raise ValidationError(
                    "Два или повече отбора имат еднакво класиране"
                )

class CbetForm(forms.ModelForm):
    class Meta:
        model = Mybet
        fields = ('type_c_bet_1',)
        widgets = {
            'type_c_bet_1': forms.Select(attrs={'class': 'bet-bets-2',}),
        }
        labels = {
            'type_c_bet_1': '',
        }


class DbetForm(forms.ModelForm):
    class Meta:
        model = Mybet
        fields = ('type_d_bet_1',)
        widgets = {
            'type_d_bet_1': forms.Select(attrs={'class': 'bet-bets-2', }),
        }
        labels = {
            'type_d_bet_1': '',
        }

class EbetForm(forms.ModelForm):
    class Meta:
        model = Mybet
        fields = ('type_e_bet_1',)
        widgets = {
            'type_e_bet_1': forms.Select(attrs={'class': 'bet-bets-2', }),
        }
        labels = {
            'type_e_bet_1': '',
        }

class FbetForm(forms.ModelForm):
    class Meta:
        model = Mybet
        fields = ('type_f_bet_1', 'type_f_bet_2')
        widgets= {
            'type_f_bet_1': forms.NumberInput(attrs={'class': 'bet-bets-1', 'min': '0', 'max': '20', 'size': '2'}),
            'type_f_bet_2': forms.NumberInput(attrs={'class': 'bet-bets-2', 'min': '0', 'max': '20', 'size': '2'}),
        }
        labels = {
            'type_f_bet_1': '',
            'type_f_bet_2': '',
        }


class GbetForm(forms.ModelForm):
    class Meta:
        model = Mybet
        fields = ('type_g_bet_1',)
        widgets = {
            'type_g_bet_1': forms.NumberInput(attrs={'class': 'bet-bets-1', 'min': '0', 'max': '20', 'size': '2'}),
        }
        labels = {
            'type_g_bet_1': '',
        }


class PlayerForm(forms.Form):
    player = forms.ModelChoiceField(queryset=User.objects.all())


class EventForm(forms.Form):
    event = forms.ModelChoiceField(queryset=Bet.objects.all().order_by('id'))
