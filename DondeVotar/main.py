import datetime
'''
Municipios:
Alta Verapaz:
-Cobán
-Santa Cruz Verapaz
-San Cristobal Verapaz
-Tactíc
-Tamahú
Baja Verapaz:
-Salamá
-San Miguel Chicaj
-Rabinal
-Cubulco
-Granados
Chimaltenango:
-Chimaltenango
-San José Poaquil
-San Martín Jilotepeque
-San Juan Comalapa
-Santa Apolonia
Chiquimula:
-Chiquimula
-San José La Arada
-San Juan Hermita
-Jocotán
-Camotán
El Petén:

-Flores
-San José
-San Benito
-San Andrés
-La Libertad

El Progreso. Municipios:

Guastatoya
Morazán
San Agustín Acasaguastlan
San Cristóbal Acasaguastlan
El Jícaro
El Quiché. Municipios:

Santa Cruz del Quiche
Chiche
Chinique
Zacualpa
Chajul

Escuintla. Municipios:
Escuintla
Santa Lucía Cotzumalguapa
La Democracia
Siquinalá
Masagua

Guatemala. Municipios:
Guatemala
Santa Catarina Pinula
San José Pinula
San José del Golfo
Palencia

Huehuetenango. Municipios:
Huehuetenango
Chiantla
Malacatancito
Cuilco
Nentón

Izabal. Municipios:
Puerto Barrios
Livingston
El Estor
Morales
Los Amate

Jalapa. Municipios:
Jalapa
San Pedro Pinula
San Luis Jilotepeque
San Manuel Chaparrón
San Carlos Alzatate

Jalapa. Municipios:
Jalapa
San Pedro Pinula
San Luis Jilotepeque
San Manuel Chaparrón
San Carlos Alzatate

Quetzaltenango. Municipios:
Quetzaltenango
Salcajá
Olintepeque
San Carlos Sija
Sibilia

Retalhuleu. Municipios:
Retalhuelu
San Sebastián
Santa Cruz Mulúa
San Martín Zapotitlán
San Felipe Retalhuleu

Sacatepéquez. Municipios:
Antigua Guatemala
Jocotenango
Pastores
Sumpango
Santo Domingo Xenacoj

San Marcos. Municipios:
San Marcos
San Pedro Sacatepéquez
Comitancillo
San Antonio Sacatepéquez
San Miguel Ixtahuacan

Santa Rosa. Municipios:
Cuilapa
Berberena
San Rosa de Lima
Casillas
San Rafael Las Flores

Sololá. Municipios:
Sololá
San José Chacaya
Santa María Visitación
Santa Lucía Utatlán
Nahualá

Suchitepéquez. Municipios:
Mazatenango
Cuyotenango
San Francisco Zapotitlán
San Bernardino
San José El Ídolo

Suchitepéquez. Municipios:
Mazatenango
Cuyotenango
San Francisco Zapotitlán
San Bernardino
San José El Ídolo

Zacapa. Municipios:
Zacapa
Estanzuela
Río Hondo
gualán
Teculután
'''

departamentos = {
    '0101': 'Guatemala',
    '0102': 'Santa Catarina Pinula',
    '0103': 'San José Pinula',
    '0104': 'San José del Golfo',
    '0105': 'Palencia',
    '0201': 'Guastatoya',
    '0203': 'Morazán',
    '0204': 'San Cristobal Acasaguastlán',
    '0205': 'El Jícaro',
    '0301': 'Antigua Guatemala',
    '0302': 'Jocotenango',
    '0303': 'Pastores',
    '0304': 'Sumpango',
    '0305': 'Santo Domingo Xenacoj',
    '0401': 'Chimaltenango',
    '0402': 'San Jose Poaquil',
    '0403': 'San MartÍn Jilotepeque',
    '0404': 'Comalapa',
    '0405': 'Santa Apolonia',
    '0501': 'Escuintla',
    '0502': 'Santa Lucía Cotzumalguapa',
    '0503': 'La Democracia',
    '0504': 'Siquinala',
    '0505': 'Masagua',
    '0601': 'Culiapa',
    '0602': 'Barbarena',
    '0603': 'Santa Rosa de Lima',
    '0604': 'Casillas',
    '0605': 'San Rafael Las Flores',
    '0701': 'Sololá',
    '0702': 'San José Chacayá',
    '0703': 'Santa María Visitación',
    '0704': 'Santa Lucía Utatlan',
    '0705': 'Nahuala'


}
def deptos_municipios():


def dpi(codigo):
    num_mesa = ''
    centro_votacion = ''
    depto = ''
    municipio = ''
    if len(codigo) > 13:
        print('Su código de identificación no es válido.')
    else:
        for i in range(0, 4):
            num_mesa += codigo[i]
        for i in range(4, 9):
            centro_votacion += codigo[i]
        for i in range(9, 11):
            depto += codigo[i]
        for i in range(11, 13):
            municipio += codigo[i]
    return num_mesa, centro_votacion, depto, municipio
def mayoria_edad(fecha):
    anio = cadena_nacimiento(fecha)[2]
    mes = cadena_nacimiento(fecha)[1]
    dia = cadena_nacimiento(fecha)[0]
    anio_actual = ''
    mes_actual = ''
    dia_actual = ''
    actual = str(datetime.datetime.now())
    for i in range(0, 4):
        anio_actual += actual[i]
    for i in range(5, 7):
        mes_actual += actual[i]
    for i in range(8, 10):
        dia_actual += actual[i]
    if (int(anio_actual) - int(anio)) < 18:
        return False
    elif (int(anio_actual) - int(anio)) == 18:
        if (int(mes_actual)) < int(mes):
            return False
        elif (int(mes_actual)) == int(mes):
            if int(dia_actual) < int(dia):
                return False
            else:
                return True
        else:
            return True
    else:
        return True





def cadena_nacimiento(fecha):
    cadena_anio = ''
    cadena_mes = ''
    cadena_dia = ''
    if len(fecha) > 8:
        print('La cadena que ingresó no es válida.')
        exit()
    else:
        for i in range(4, len(fecha)):
            cadena_anio += fecha[i]
        for i in range(2, 4):
            cadena_mes += fecha[i]
        for i in range(0, 2):
            cadena_dia += fecha[i]
    return cadena_dia, cadena_mes, cadena_anio
def main():
    fecha_nac = input('Ingrese su fecha de nacimiento DDMMAAAA: ')
    if mayoria_edad(fecha_nac):
        cui = input('Ingrese su Codigo de Identificación Único: ')
    else:
        print('Aún no es mayor de edad.')
        exit()



main()