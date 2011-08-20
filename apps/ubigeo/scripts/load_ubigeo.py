# -*- coding: utf-8 -*-
"""
Load Ubigeo data from INEI dbf file to Ubigeo Model
"""


from os.path import join, dirname
from ubigeo.models import Ubigeo
import dbf

def is_dept(record):
    return record.codprov == 0 and record.coddist == 0

def is_dist(record):
    return record.coddist != 0


def run():
    BASE_DIR = join(dirname(__file__))
    table = dbf.Table(join(BASE_DIR, 'ubigeo.dbf'))
    # we assume that the DBF data is ordered ... blame INEI and ONGEI if the script fails :P
    for record in table:
        ubigeo = Ubigeo.objects.create(name=record.nombre)
        if not is_dept():
            parent = ubigeo.id
            if is_dist():
                parent = parent.parent
            ubigeo.parent = parent
            ubigeo.save()
