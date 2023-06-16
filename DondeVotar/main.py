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
    '0705': 'Nahuala',
    '0801': 'Totonicapán',
    '0802': 'San Cristóbal Totonicapan',
    '0803': 'San Francisco el Alto',
    '0804': 'San Andrés Xecul',
    '0805': 'Momostenango',
    '0901': 'Quetzaltenango',
    '0902': 'Salcajá',
    '0903': 'Olintepeque',
    '0904': 'San Carlos Sija',
    '0905': 'Sibilia',
    '1001': 'Mazatenango',
    '1002': 'Cuyotenango',
    '1003': 'San Francisco Zapotitlán',
    '1004': 'San Bernardino',
    '1005': 'San José El Idolo',
    '1101: ' 'Retalhuleu',
    '1102: ' 'San Sebastián',
    '1103: ' 'Santa Cruz Muluá',
    '1104: ' 'San Martín Zapotitlán',
    '1105: ' 'San Felipe',
    '1201: ' 'San Marcos',
    '1202: ' 'San Pedro Sacatepéquez',
    '1203: ' 'San Antonio Sacatepéquez',
    '1204: ' 'Comitancillo',
    '1205: ' 'San Miguel Ixtahuacán',
    '1301: ' 'Huehuetenango',
    '1302: ' 'Chiantla',
    '1303: ' 'Malacatancito',
    '1304: ' 'Cuilco',
    '1305: ' 'Nentón',
    '1401: ' 'Santa Cruz del Quiché',
    '1402: ' 'Chiché',
    '1403: ' 'Chinique',
    '1404: ' 'Zacualpa',
    '1405: ' 'Chajul',
    '1501: ' 'Salamá',
    '1502: ' 'San Miguel Chicaj',
    '1503: ' 'Rabinal',
    '1504: ' 'Cubulco',
    '1505: ' 'Granados',
    '1601: ' 'Cobán',
    '1602: ' 'Santa Cruz Verapaz',
    '1603: ' 'San Cristóbal Verapaz',
    '1604: ' 'Tactic',
    '1605: ' 'Tamahú',
    '1701: ' 'Flores',
    '1702: ' 'San José',
    '1703: ' 'San Benito',
    '1704: ' 'San Andrés',
    '1705: ' 'La Libertad',
    '1801: ' 'Puerto Barrios',
    '1802: ' 'Livingston',
    '1803: ' 'El Estor',
    '1804: ' 'Morales',
    '1805: ' 'Los Amates',
    '1901: ' 'Zacapa',
    '1902: ' 'Estanzuela',
    '1903: ' 'Río Hondo',
    '1904: ' 'Gualán',
    '1905: ' 'Teculután',
    '2001: ' 'Chiquimula',
    '2002: ' 'San José La Arada',
    '2003: ' 'San Juan Ermita',
    '2004: ' 'Jocotán',
    '2005: ' 'Camotán',
    '2101: ' 'Jalapa',
    '2102: ' 'San Pedro Pinula',
    '2103: ' 'San Luis Jilotepeque',
    '2104: ' 'San Manuel Chaparrón',
    '2105: ' 'San Carlos Alzatate',
    '2201: ' 'Jutiapa',
    '2202: ' 'El Progreso',
    '2203: ' 'Santa Catarina Mita',
    '2204: ' 'Agua Blanca',
    '2205: ' 'Asunción Mita'







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