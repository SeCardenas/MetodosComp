#Centros de los rectangulos
x1 = 1.5
y1 = 1
x2 = 4
y2 = 2

#Lados de los rectangulos, a1 y a2 paralelos al eje x, y c1 y c2 paralelos al eje y.
a1 = 3
c1 = 2
a2 = 2
c2 = 2

#Variables de apoyo
dif_centros_x = x2-x1
dif_centros_y = y2-y1
prom_lados_x = 0.5*(a1+a2)
prom_lados_y = 0.5*(c1+c2)
cruce_x = prom_lados_x - abs(dif_centros_x)
cruce_y = prom_lados_y - abs(dif_centros_y)

#Casos
if cruce_x < 0 or cruce_y < 0:
    print "los rectangulos no se intersectan"
elif cruce_x == 0 and cruce_y == 0:
    x0 = x1 + (dif_centros_x/abs(dif_centros_x))*0.5*a1
    y0 = y1 + (dif_centros_y/abs(dif_centros_y))*0.5*c1
    print "los rectangulos se tocan en un solo punto de coordenadas", x0, ",", y0
else:
    #Variables para saber si un rectangulo esta completamente contenido dentro del otro
    a1_a2 = a1>a2+2*abs(dif_centros_x)
    a2_a1 = a2>a1+2*abs(dif_centros_x)
    c1_c2 = c1>c2+2*abs(dif_centros_y)
    c2_c1 = c2>c1+2*abs(dif_centros_y)
    if((a1_a2 and c1_c2) or (a2_a1 and c2_c1)):
        print "los rectangulos no se intersectan"
    else:
        #Casos en los que un lado de un rectangulo esta completamente dentro del otro
        if a1_a2:
            cruce_x = a2
        elif a2_a1:
            cruce_x = a1
        if c1_c2:
            cruce_y = c2
        elif c2_c1:
            cruce_y = c1
        #Variables para saber si los rectangulos se cruzan en una linea (en el caso en que un rectangulo este contenido dentro del otro)
        a1_a2 = a1 == a2+2*abs(dif_centros_x)
        a2_a1 = a2 == a1+2*abs(dif_centros_x)
        c1_c2 = c1 == c2+2*abs(dif_centros_y)
        c2_c1 = c2 == c1+2*abs(dif_centros_y)
        if ((a1_a2 or a2_a1) and not c1_c2 and not c2_c1) or cruce_x == 0:
            x0 = x1 + (dif_centros_x/abs(dif_centros_x))*0.5*a1
            print "los rectangulos se tocan en un segmento de recta vertival x =", x0
        elif ((c1_c2 or c2_c1) and not a1_a2 and not a2_a1) or cruce_y == 0:
            y0 = y1 + (dif_centros_y/abs(dif_centros_y))*0.5*c1
            print "los rectangulos se tocan en un segmento de recta horizontal y =", y0
        else:
            #Lados x , y
            print "los rectangulos se intersectan formando un rectangulo de lados ", cruce_x, ", ", cruce_y
