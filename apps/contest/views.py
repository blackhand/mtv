# -*- coding: utf-8 -*-

from datetime import date
import random
from django.shortcuts import render, redirect
from models import Draw, Option

MIN_DATE = date(2011,9,1)
MAX_DATE = date(2011,10,31)
NOW = date.today()


if NOW.weekday == 6:
    MAX_DATE = NOW
else:
    MAX_DATE.day = NOW - (NOW+1)


def show_winners(request):    
    winners = Draw.objects.filter(play_date__range=(MIN_DATE, MAX_DATE)).order_by('play_date')
    return render(request, 'template',{
        'winners':winners,
        })


def get_winners(request):
    day = 0
    participants = Option.objects.filter(register_date__renge=(MIN_DATE, MAX_DATE))
    while day <=6:
        number_win = random.randint(0,participants.count()-1)
        Draw.objects.create(winner=participants.get(number_win).participant,play_date=NOW).save()
        day = day+1
	return redirect('show_winners')
