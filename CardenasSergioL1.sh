#Numero de personas que obtuvieron entre 4 y 5 puntos en el parcial
awk '{if($3>=4 && $3<=5) print $6;}' notas.txt | wc -l
#Numero de personas que obtuvieron entre 4 y 5 puntos en el parcial y màs de 15 puntos en el final
(awk '{if($3>=4 && $3<=5) print $6;}' notas.txt | awk '{if($1>15) print $6;}') | wc -l  > RES1.txt

#punto 2
grep -w "0" notas.txt | awk '{if($7<6) print $1, $2}'

#punto 3
awk '{if($7>8) print $1, $7;}' notas.txt > RES2.txt
cat RES2.txt | wc -l

#punto 4
mkdir RESULTADO
mv RES1.txt ./RESULTADO
mv RES2.txt ./RESULTADO
