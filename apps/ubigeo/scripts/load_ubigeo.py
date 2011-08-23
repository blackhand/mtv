# -*- coding: utf-8 -*-
"""
Load Ubigeo data from INEI dbf file to Ubigeo Model
"""

from django.db import transaction

from os.path import join, dirname
from ubigeo.models import Ubigeo
import dbf

def _is_dept(record):
    return int(record.codprov) == 0 and int(record.coddist) == 0

def _is_prov(record):
    return int(record.coddist) == 0

def _code(record):
    code = int(record.coddpto)
    if int(record.codprov) != 0:
        code = code*100 + int(record.codprov)
    if int(record.coddist) != 0:
        code = code*100 + int(record.coddist)
    return code

def _parent_code(record):
    code = None
    if int(record.codprov) != 0:
        code = int(record.coddpto)
    if int(record.coddist) != 0:
        code = code*100 + int(record.codprov)
    return code
    

def run():
    BASE_DIR = join(dirname(__file__))
    table = dbf.Table(join(BASE_DIR, 'ubigeo.dbf'))
    # we assume that the DBF (from 2008) data is ordered ... blame INEI and ONGEI if the script fails :P
    print 'BEGIN!'
    transaction.enter_transaction_management()
    transaction.managed(True)
    for record in table:
        ubigeo = Ubigeo.objects.create(
                id=_code(record), 
                parent_id=_parent_code(record),
                name=record.nombre.title())
    transaction.commit()
    print 'END!'
