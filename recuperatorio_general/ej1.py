import requests, os, json

n = int(input('Porfavor, ingrese la cantidad de usuarios deseada(Minimo 1 maximo 10) '))

ruta = 'Almacenamiento de usuarios'
if not os.path.exists(ruta):
    os.makedirs(ruta)

url_page = f'https://jsonplaceholder.typicode.com/users?_limit={n}'
nombres = ''


if n > 0 and n <= 10:
    response = requests.get(url_page)
    if response.status_code == 200:
        # json.loads()
        # json.dumps()
        
       
        usuarios = response.text
        
        dictsuarios = json.loads(usuarios)
        print(dictsuarios)
        print('se pudo acceder')
        
            
    else:
        print(f'No se pudo acceder. Codigo de error:{response.status_code}')    
        
else:
    print('Por favor ingrese una cantidad de usuarios valida')

    
def filtrar_voc(usuarios):
            vocales = ['a','e','i','o','u','A','E','I','O','U']
            vusers = []
            cusers = []        
            for user  in usuarios:
                if [['name'][0]] in vocales:
                    vusers.append(user['name'])
                        
                else:
                    cusers.append(user['name'])
                        
            print(vusers)
            
            
            
filtrar_voc(usuarios)
      
            
            
def filtrar_ubic(usuarios):
    ciudad = input('Ingrese una ciudad para filtrar')
    coincidencias = 0
    usuarios_por_ubic = []
    for usuario in usuarios:
        for i in usuarios[usuario]:
            if ['address'][i] == ciudad:
                usuarios_por_ubic.append(usuario)
            
            
            
# def busqueda_avanzada(usuarios):
    
                    
  
        