from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
categorizacion_meses = {}

#----EXTRAER MAS DE UNA COLUMNA----
id_y_refund = [ [sale[0], sale[2]] for sale in lifestore_sales]
for par in id_y_refund:
  print(par)
  

#---IMPRIMIR SOLO LOS MEJORES RESEÑAS
id_y_refund = [ [sale[0], sale[2]] for sale in lifestore_sales if sale [2] == 5]
for par in id_y_refund:
  print(par)

#----DIVIDIR POR MESES LAS VENTAS---
id_fecha = [ [sale [0], sale [3]]for sale in lifestore_sales if sale [4] == 0]  

id_fecha = [ [sale [0], sale [3]]for sale in lifestore_sales if sale [4] == 0]  


for par in id_fecha:
  id = par[0]
  _, mes, _ = par[1].split('/')
  if mes not in categorizacion_meses.keys():
      categorizacion_meses[mes] = []
  categorizacion_meses[mes].append(id)

for key in categorizacion_meses.keys():
  print(key)
  print(categorizacion_meses[key])

#SUMAR EL TOTAL DE LAS VENTAS POR MES EN EL 2020

for key in categorizacion_meses.keys():
  lista_mes = categorizacion_meses[key]
  suma_venta = 0
  for id_venta in lista_mes:
    indice = id_venta - 1
    info_venta = lifestore_sales[indice] 
    id_product = info_venta[1]
    precio = lifestore_products[id_product -1] [2]
    suma_venta += precio
  print(key, suma_venta)

 
#---- REVIEW POR CATEGORIA, VENTAS Y PROMEDIO---
prod_reseña = {}
for sale in lifestore_sales:
  prod_id = sale[1]
  reseña = sale[2]
  if prod_id not in prod_reseña.keys():
    prod_reseña[prod_id] = []
  prod_reseña[prod_id].append(reseña)

#CATEGORIA CON ID

for key in prod_reseña.keys():
  print(key)
  print(prod_reseña[key])

category_ids = {}
for prod in lifestore_products:
  prod_id = prod [0]
  category = prod [3]
  if category not in category_ids.keys():
    category_ids[category] = []
  category_ids[category].append(prod_id)

for key, values in category_ids.items():
  print(key)
  print(values)


resultados_por_categoria = {}
for category, prod_id_list in category_ids.items():
  reviews = 0
  ganancias = 0
  ventas = 0
  for prod_id in prod_id_list:
    if prod_id not in prod_reseña.keys():
      continue 
    reviews_ventas = prod_reseña[prod_id]
    precio = lifestore_products[prod_id][2]
    total_ventas = len(reviews_ventas)
    g = precio * total_ventas
    reviews = reviews_ventas 
    ganancias += g
    ventas += total_ventas

  prom_reviews = sum(reviews) / len(reviews)

  resultados_por_categoria[category] = {
      'review promedio': prom_reviews,
      'ganancias': ganancias,
      'ventas totales': ventas  
  }

for cat, dic in resultados_por_categoria.items():
  print(cat)
  for key, val in dic.items():
      print('\t', key, val)

id_y_refund = [ [sale[0], sale[2]] for sale in lifestore_sales]
for par in id_y_refund:
  print(par)
 

#---IMPRIMIR SOLO LOS MEJORES RESEÑAS
id_y_refund = [ [sale[0], sale[2]] for sale in lifestore_sales if sale [2] == 3]
for par in id_y_refund:
  print(par)

#----LOGIN----

Nombre_usuario = "Lori11"
contraseña = "3mtechp1"
tries = 0; Access = False

while not Access:
  tries += 1
  if tries == 3:
    exit()
  
  if input('Nombre de usuario: ') == Nombre_usuario and input ('Contraseña: ') == contraseña:
    Access = True
    print('Acceso permitido') 
  else:
    print(f'tienes {3 - tries} intentos')

#---PRODUCTOS MAS VENDIDOS---
ventas_totales = 0
lista_ventas_ind = []

for producto in lifestore_products:
  ventas_individuales = 0
for venta in lifestore_sales:
  if producto [0] == venta [1]:
    ventas_individuales += 1
    ventas_totales += 1
  registro_individual = [producto[0], producto[1], ventas_individuales]
  lista_ventas_ind.append(registro_individual)

lista_ventas_max = list(lista_ventas_ind)
ventas_ordenadas_max = []

while lista_ventas_max:
  maximo = lista_ventas_max[0][2]
  registro_actual = lista_ventas_max [0]
  for registro in lista_ventas_max:
    if registro [2] > maximo:
      maximo = registro [2]
      registro_actual = registro
  ventas_ordenadas_max.append(registro_actual)
  lista_ventas_max.remove(registro_actual)

for i in range(5):
print (f'id:{veces buscado[i][0]}\t nombre: {veces buscado[i][1]}\t busquedas: {veces buscado[i][2]}')
break
