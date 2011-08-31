# -*- coding: utf-8 -*-

from datetime import date
from django.shortcuts import render
from models import Draw,

MIN_DATE = date(2011,9,1)
MAX_DATE = date(2011,10,31)
NOW = date.today()


if self.NOW.weekday == 6:
    self.MAX_DATE = self.NOW
else:
    self.MAX_DATE.day = self.NOW - (self.NOW+1)


def show_winners(request):    
    winners = Draw.objects.filter(play_date__range=(MIN_DATE, MAX_DATE)).order_by('play_date')
    return render(request, 'template',{
        'winners':winners,
        })


def get_winners(request):
    day = 0
    participants = Options.objects.filter(register_date__renge=(MIN_DATE, MAX_DATE))
    while day <=6:
        number_win = random.randint(0,participants.count()-1)
        Draw.objects.create(winner=participants.get(number_win).participant,play_date=self.NOW).save()
        day = day+1
	return redirect('show_winners')
