# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:27:44 2022
Spyder IDE - Python 3.9.12 64-bit | Qt 5.9.7 | PyQt5 5.9.2 | Windows 10 
@author: JulianCastillo
"""


import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/ObservatorioTerritorialMetropolitano/AnalisisAreasLote/main/Data.csv'

df = pd.read_csv(url, sep=';')
df.head()

# Barbosa
#--------------------- Barbosa ------------------------------------------------
Municipio = 'Barbosa'
Separador = ' - '
Suelo= 'Rural'

Municipio_ = df[(df['Municipio'] == Municipio)]
MunicipioUrbano = Municipio_[(Municipio_['Suelo'] == 'Urbano')]
MunicipioRural = Municipio_[(Municipio_['Suelo'] == 'Rural')]

MunicipioAreaRural = MunicipioRural[['Shape_Area']].to_numpy()
MunicipioAreaUrbana = MunicipioUrbano[['Shape_Area']].to_numpy()

print('Figura Barbosa Rural')
fig1, ax1 = plt.subplots()
ax1.set_title('Área de lote sin atípicos')
ax1.set_xlabel(Municipio + Separador + Suelo)
ax1.set_ylabel('Área de Lote')
ax1.boxplot(MunicipioAreaRural, showfliers=False)

Suelo = 'Urbano'

print('Figura Barbosa Urbano')
fig2, ax2 = plt.subplots()
ax2.set_title('Área de lote sin atípicos')
ax2.set_xlabel(Municipio + Separador + Suelo)
ax2.set_ylabel('Área de Lote')
ax2.boxplot(MunicipioAreaUrbana, showfliers=False)
#--------------------- /Barbosa -----------------------------------------------
# Bello
#--------------------- Bello --------------------------------------------------
Municipio = 'Bello'
Separador = ' - '
Suelo= 'Rural'

Municipio_ = df[(df['Municipio'] == Municipio)]
MunicipioUrbano = Municipio_[(Municipio_['Suelo'] == 'Urbano')]
MunicipioRural = Municipio_[(Municipio_['Suelo'] == 'Rural')]

MunicipioAreaRural = MunicipioRural[['Shape_Area']].to_numpy()
MunicipioAreaUrbana = MunicipioUrbano[['Shape_Area']].to_numpy()

print('Figura ' + Municipio + ' ' + Suelo)
fig1, ax1 = plt.subplots()
ax1.set_title('Área de lote sin atípicos')
ax1.set_xlabel(Municipio + Separador + Suelo)
ax1.set_ylabel('Área de Lote')
ax1.boxplot(MunicipioAreaRural, showfliers=False)

Suelo = 'Urbano'

print('Figura ' + Municipio + ' ' + Suelo)
fig2, ax2 = plt.subplots()
ax2.set_title('Área de lote sin atípicos')
ax2.set_xlabel(Municipio + Separador + Suelo)
ax2.set_ylabel('Área de Lote')
ax2.boxplot(MunicipioAreaUrbana, showfliers=False)
#--------------------- /Bello -------------------------------------------------
# Caldas
#--------------------- Caldas -------------------------------------------------
Municipio = 'Caldas'
Separador = ' - '
Suelo= 'Rural'

Municipio_ = df[(df['Municipio'] == Municipio)]
MunicipioUrbano = Municipio_[(Municipio_['Suelo'] == 'Urbano')]
MunicipioRural = Municipio_[(Municipio_['Suelo'] == 'Rural')]

MunicipioAreaRural = MunicipioRural[['Shape_Area']].to_numpy()
MunicipioAreaUrbana = MunicipioUrbano[['Shape_Area']].to_numpy()

print('Figura ' + Municipio + ' ' + Suelo)
fig1, ax1 = plt.subplots()
ax1.set_title('Área de lote sin atípicos')
ax1.set_xlabel(Municipio + Separador + Suelo)
ax1.set_ylabel('Área de Lote')
ax1.boxplot(MunicipioAreaRural, showfliers=False)

Suelo = 'Urbano'

print('Figura ' + Municipio + ' ' + Suelo)
fig2, ax2 = plt.subplots()
ax2.set_title('Área de lote sin atípicos')
ax2.set_xlabel(Municipio + Separador + Suelo)
ax2.set_ylabel('Área de Lote')
ax2.boxplot(MunicipioAreaUrbana, showfliers=False)
#--------------------- /Caldas ------------------------------------------------
# Copacabana
#--------------------- Copacabana ---------------------------------------------
Municipio = 'Copacabana'
Separador = ' - '
Suelo= 'Rural'

Municipio_ = df[(df['Municipio'] == Municipio)]
MunicipioUrbano = Municipio_[(Municipio_['Suelo'] == 'Urbano')]
MunicipioRural = Municipio_[(Municipio_['Suelo'] == 'Rural')]

MunicipioAreaRural = MunicipioRural[['Shape_Area']].to_numpy()
MunicipioAreaUrbana = MunicipioUrbano[['Shape_Area']].to_numpy()

print('Figura ' + Municipio + ' ' + Suelo)
fig1, ax1 = plt.subplots()
ax1.set_title('Área de lote sin atípicos')
ax1.set_xlabel(Municipio + Separador + Suelo)
ax1.set_ylabel('Área de Lote')
ax1.boxplot(MunicipioAreaRural, showfliers=False)

Suelo = 'Urbano'

print('Figura ' + Municipio + ' ' + Suelo)
fig2, ax2 = plt.subplots()
ax2.set_title('Área de lote sin atípicos')
ax2.set_xlabel(Municipio + Separador + Suelo)
ax2.set_ylabel('Área de Lote')
ax2.boxplot(MunicipioAreaUrbana, showfliers=False)
#--------------------- /Copacabana --------------------------------------------
# Envigado
#--------------------- Envigado -----------------------------------------------
Municipio = 'Envigado'
Separador = ' - '
Suelo= 'Rural'

Municipio_ = df[(df['Municipio'] == Municipio)]
MunicipioUrbano = Municipio_[(Municipio_['Suelo'] == 'Urbano')]
MunicipioRural = Municipio_[(Municipio_['Suelo'] == 'Rural')]

MunicipioAreaRural = MunicipioRural[['Shape_Area']].to_numpy()
MunicipioAreaUrbana = MunicipioUrbano[['Shape_Area']].to_numpy()

print('Figura ' + Municipio + ' ' + Suelo)
fig1, ax1 = plt.subplots()
ax1.set_title('Área de lote sin atípicos')
ax1.set_xlabel(Municipio + Separador + Suelo)
ax1.set_ylabel('Área de Lote')
ax1.boxplot(MunicipioAreaRural, showfliers=False)

Suelo = 'Urbano'

print('Figura ' + Municipio + ' ' + Suelo)
fig2, ax2 = plt.subplots()
ax2.set_title('Área de lote sin atípicos')
ax2.set_xlabel(Municipio + Separador + Suelo)
ax2.set_ylabel('Área de Lote')
ax2.boxplot(MunicipioAreaUrbana, showfliers=False)
#--------------------- /Envigado ----------------------------------------------
# Girardota
#--------------------- Girardota ----------------------------------------------
Municipio = 'Girardota'
Separador = ' - '
Suelo= 'Rural'

Municipio_ = df[(df['Municipio'] == Municipio)]
MunicipioUrbano = Municipio_[(Municipio_['Suelo'] == 'Urbano')]
MunicipioRural = Municipio_[(Municipio_['Suelo'] == 'Rural')]

MunicipioAreaRural = MunicipioRural[['Shape_Area']].to_numpy()
MunicipioAreaUrbana = MunicipioUrbano[['Shape_Area']].to_numpy()

print('Figura ' + Municipio + ' ' + Suelo)
fig1, ax1 = plt.subplots()
ax1.set_title('Área de lote sin atípicos')
ax1.set_xlabel(Municipio + Separador + Suelo)
ax1.set_ylabel('Área de Lote')
ax1.boxplot(MunicipioAreaRural, showfliers=False)

Suelo = 'Urbano'

print('Figura ' + Municipio + ' ' + Suelo)
fig2, ax2 = plt.subplots()
ax2.set_title('Área de lote sin atípicos')
ax2.set_xlabel(Municipio + Separador + Suelo)
ax2.set_ylabel('Área de Lote')
ax2.boxplot(MunicipioAreaUrbana, showfliers=False)
#--------------------- /Girardota ---------------------------------------------
# Itagui
#--------------------- Itagui -------------------------------------------------
Municipio = 'Itagui'
Separador = ' - '
Suelo= 'Rural'

Municipio_ = df[(df['Municipio'] == Municipio)]
MunicipioUrbano = Municipio_[(Municipio_['Suelo'] == 'Urbano')]
MunicipioRural = Municipio_[(Municipio_['Suelo'] == 'Rural')]

MunicipioAreaRural = MunicipioRural[['Shape_Area']].to_numpy()
MunicipioAreaUrbana = MunicipioUrbano[['Shape_Area']].to_numpy()

print('Figura ' + Municipio + ' ' + Suelo)
fig1, ax1 = plt.subplots()
ax1.set_title('Área de lote sin atípicos')
ax1.set_xlabel(Municipio + Separador + Suelo)
ax1.set_ylabel('Área de Lote')
ax1.boxplot(MunicipioAreaRural, showfliers=False)

Suelo = 'Urbano'

print('Figura ' + Municipio + ' ' + Suelo)
fig2, ax2 = plt.subplots()
ax2.set_title('Área de lote sin atípicos')
ax2.set_xlabel(Municipio + Separador + Suelo)
ax2.set_ylabel('Área de Lote')
ax2.boxplot(MunicipioAreaUrbana, showfliers=False)
#--------------------- /Itagui ------------------------------------------------
# La Estrella
#--------------------- La Estrella --------------------------------------------
Municipio = 'La Estrella'
Separador = ' - '
Suelo= 'Rural'

Municipio_ = df[(df['Municipio'] == Municipio)]
MunicipioUrbano = Municipio_[(Municipio_['Suelo'] == 'Urbano')]
MunicipioRural = Municipio_[(Municipio_['Suelo'] == 'Rural')]

MunicipioAreaRural = MunicipioRural[['Shape_Area']].to_numpy()
MunicipioAreaUrbana = MunicipioUrbano[['Shape_Area']].to_numpy()

print('Figura ' + Municipio + ' ' + Suelo)
fig1, ax1 = plt.subplots()
ax1.set_title('Área de lote sin atípicos')
ax1.set_xlabel(Municipio + Separador + Suelo)
ax1.set_ylabel('Área de Lote')
ax1.boxplot(MunicipioAreaRural, showfliers=False)

Suelo = 'Urbano'

print('Figura ' + Municipio + ' ' + Suelo)
fig2, ax2 = plt.subplots()
ax2.set_title('Área de lote sin atípicos')
ax2.set_xlabel(Municipio + Separador + Suelo)
ax2.set_ylabel('Área de Lote')
ax2.boxplot(MunicipioAreaUrbana, showfliers=False)
#--------------------- /La Estrella -------------------------------------------
# Medellín
#--------------------- Medellín -----------------------------------------------
Municipio = 'Medellin'
Separador = ' - '
Suelo= 'Rural'

Municipio_ = df[(df['Municipio'] == Municipio)]
MunicipioUrbano = Municipio_[(Municipio_['Suelo'] == 'Urbano')]
MunicipioRural = Municipio_[(Municipio_['Suelo'] == 'Rural')]

MunicipioAreaRural = MunicipioRural[['Shape_Area']].to_numpy()
MunicipioAreaUrbana = MunicipioUrbano[['Shape_Area']].to_numpy()

print('Figura ' + Municipio + ' ' + Suelo)
fig1, ax1 = plt.subplots()
ax1.set_title('Área de lote sin atípicos')
ax1.set_xlabel(Municipio + Separador + Suelo)
ax1.set_ylabel('Área de Lote')
ax1.boxplot(MunicipioAreaRural, showfliers=False)

Suelo = 'Urbano'

print('Figura ' + Municipio + ' ' + Suelo)
fig2, ax2 = plt.subplots()
ax2.set_title('Área de lote sin atípicos')
ax2.set_xlabel(Municipio + Separador + Suelo)
ax2.set_ylabel('Área de Lote')
ax2.boxplot(MunicipioAreaUrbana, showfliers=False)
#--------------------- /Medellín ----------------------------------------------
# Sabaneta
#--------------------- Sabaneta -----------------------------------------------
Municipio = 'Sabaneta'
Separador = ' - '
Suelo= 'Rural'

Municipio_ = df[(df['Municipio'] == Municipio)]
MunicipioUrbano = Municipio_[(Municipio_['Suelo'] == 'Urbano')]
MunicipioRural = Municipio_[(Municipio_['Suelo'] == 'Rural')]

MunicipioAreaRural = MunicipioRural[['Shape_Area']].to_numpy()
MunicipioAreaUrbana = MunicipioUrbano[['Shape_Area']].to_numpy()

print('Figura ' + Municipio + ' ' + Suelo)
fig1, ax1 = plt.subplots()
ax1.set_title('Área de lote sin atípicos')
ax1.set_xlabel(Municipio + Separador + Suelo)
ax1.set_ylabel('Área de Lote')
ax1.boxplot(MunicipioAreaRural, showfliers=False)

Suelo = 'Urbano'

print('Figura ' + Municipio + ' ' + Suelo)
fig2, ax2 = plt.subplots()
ax2.set_title('Área de lote sin atípicos')
ax2.set_xlabel(Municipio + Separador + Suelo)
ax2.set_ylabel('Área de Lote')
ax2.boxplot(MunicipioAreaUrbana, showfliers=False)
#--------------------- /Sabaneta ----------------------------------------------