# -*- coding: utf-8-sig -*-
import sys
import os
import pandas as pd

BASE_DIR='/home/cnovoa/Documents/ETL'
INPUT_DIR='{}/{}'.format(BASE_DIR, 'procesos_de_tecnicos')
cols=['Nombre','Apellidos','Rut (IDENTIFICADOR)','Etapa','E-mail', u'Teléfono',u'Móvil',u'Género','Edad','Nacionalidad',u'Región','Comuna','Grado Escolar',u'Años de Experiencia','Estado',u'Observación General','Oferta de empleo']
for col in cols:
    print 'COL: %s' % col

#
#for f in os.listdir(INPUT_DIR):
#    if f.endswith(".xlsx"):
#        print('Planilla: %s' % f)
#        df = pd.read_excel('{}/{}'.format(INPUT_DIR, f), usecols=cols, encoding='utf-8-sig')
#        append_df_to_excel('{}/{}'.format(BASE_DIR, 'consolidado.xlsx'), df, index=False)

df = pd.DataFrame()
for f in os.listdir(INPUT_DIR):
    if f.endswith(".xlsx"):
        print('Planilla: %s' % f)
        df2 = pd.read_excel('{}/{}'.format(INPUT_DIR, f), usecols=cols, encoding='utf-8-sig')
        df = df.append(df2)

writer = pd.ExcelWriter('{}/{}'.format(BASE_DIR, 'consolidado.xlsx'))
df.to_excel(writer, 'Sheet1', index=False)
writer.save()
