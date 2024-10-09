productos={}
cgo=int(input('Ingrese código, 0 para terminar '))
while cgo!=0:
    if cgo not in productos:
        desc=input('Descripción de %d '%cgo)
unidad=input('Unidad de Medida de %s '%desc)
precio=float(input('Precio unitario de %s '%desc))
productos[cgo]=(desc,unidad,precio)
cgo=int(input('Ingrese código, 0 para terminar '))
for cgo in productos:
    print(cgo,*productos[cgo])
total=0
cgo=int(input('Qué lleva? 0 para salir '))
while cgo not in productos and cgo!=0:
    cgo=int(input('Qué lleva? 0 para salir '))
while cgo!=0:
    cant=float(input('Cantidad de %s '%(productos[cgo][0])))
total+=cant*productos[cgo][2]
cgo=int(input('Qué lleva? 0 para salir '))
while cgo not in productos and cgo!=0:
    cgo=int(input('Qué lleva? 0 para salir '))
print('Debe abonar: $%.2f'%total,sep='')