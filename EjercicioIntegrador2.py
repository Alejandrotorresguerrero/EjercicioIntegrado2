import csv

pasajeros = []
vuelos = []
ciudad=[]
IATA=[]
escrito=[]
with open('EjercicioIntegrador2.csv','r') as archivo_csv:
   lector = csv.reader(archivo_csv)
   
   for linea in lector:
       if linea[4] != ('0' and 'Vuelos_Sinaloa'):
           ciudad.append(linea[1])
           IATA.append(linea[2])
           pasajeros.append(int(linea[3]))  
           vuelos.append(linea[4]) 
        
   x=dict(zip(IATA,ciudad))
   y=(list(zip(pasajeros,vuelos)))
   z=(list(zip(IATA,pasajeros)))
   a=(list(zip(IATA,vuelos)))
   z.sort(reverse=True, key=lambda x:x[1])
   print('AEROPUERTOS CON MAYOR CANTIDAD DE PASAJEROS')
   for list in range(5):
     #  print(z[list])
       index=(z[list][0])    
       print(index,'-->',x[index],end=': ')
       print(z[list][1],'pasajeros')

   print('\nPromedio de pasajeros por aeropuerto: '.upper(),int(sum(pasajeros)/len(pasajeros)))
   print('\nCIUDADES CON LOS MENORES VUELOS A SINALOA')
   a.sort(reverse=False, key=lambda x:x[1])
   for list in range(5):
       index=(a[list][0])    
       print(x[index],end=': ')
       print(a[list][1],'vuelos')


with open('Ejercicio.csv', 'w', newline='') as reporte_csv:
    writer = csv.writer(reporte_csv)
    writer.writerow(['AEROPUERTOS CON MAYOR CANTIDAD DE PASAJEROS'])
    writer.writerow(['AEROPUERTO' ,'PASAJEROS'])
    for list in range(5):
        index=(z[list][0])    
        r=index,z[list][1]
        writer.writerows([r])
    writer.writerow(' ')    
    writer.writerow(['CIUDADES CON LOS MENORES VUELOS A SINALOA'])
    writer.writerow(['CIUDAD' ,'VUELOS'])
    for list in range(5):
        index=(a[list][0])  
        h=x[index],a[list][1]
        writer.writerows([h])
      