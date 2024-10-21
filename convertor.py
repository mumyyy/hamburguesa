# convertidor.py

from temperatura import *
from masa import *
from tiempo import *

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == 'Celsius':
        if unidad_destino == 'Fahrenheit':
            return celsius_a_fahrenheit(valor)
        elif unidad_destino == 'Kelvin':
            return celsius_a_kelvin(valor)
    elif unidad_origen == 'Fahrenheit':
        if unidad_destino == 'Celsius':
            return fahrenheit_a_celsius(valor)
        elif unidad_destino == 'Kelvin':
            return fahrenheit_a_kelvin(valor)
    elif unidad_origen == 'Kelvin':
        if unidad_destino == 'Celsius':
            return kelvin_a_celsius(valor)
        elif unidad_destino == 'Fahrenheit':
            return kelvin_a_fahrenheit(valor)

def convertir_masa(valor, unidad_origen, unidad_destino):
    if unidad_origen == 'Kilogramos':
        if unidad_destino == 'Libras':
            return kilogramos_a_libras(valor)
        elif unidad_destino == 'Onzas':
            return kilogramos_a_onzas(valor)
    elif unidad_origen == 'Libras':
        if unidad_destino == 'Kilogramos':
            return libras_a_kilogramos(valor)
    elif unidad_origen == 'Onzas':
        if unidad_destino == 'Kilogramos':
            return onzas_a_kilogramos(valor)

def convertir_tiempo(valor, unidad_origen, unidad_destino):
    if unidad_origen == 'Segundos':
        if unidad_destino == 'Minutos':
            return segundos_a_minutos(valor)
        elif unidad_destino == 'Horas':
            return segundos_a_horas(valor)
    elif unidad_origen == 'Minutos':
        if unidad_destino == 'Segundos':
            return minutos_a_segundos(valor)
    elif unidad_origen == 'Horas':
        if unidad_destino == 'Segundos':
            return horas_a_segundos(valor)

def main():
    print("Seleccione la categoría de conversión:")
    print("1. Temperatura")
    print("2. Masa")
    print("3. Tiempo")
    
    categoria = input("Ingrese el número de la categoría: ")

    valor = float(input("Ingrese el valor a convertir: "))
    unidad_origen = input("Ingrese la unidad de origen: ")
    unidad_destino = input("Ingrese la unidad de destino: ")

    if categoria == '1':
        resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
    elif categoria == '2':
        resultado = convertir_masa(valor, unidad_origen, unidad_destino)
    elif categoria == '3':
        resultado = convertir_tiempo(valor, unidad_origen, unidad_destino)

    print(f"Resultado: {resultado}")

if _name_ == "_main_":
    main()