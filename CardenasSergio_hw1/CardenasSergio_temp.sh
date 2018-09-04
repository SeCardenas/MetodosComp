mkdir Temperaturas
cd Temperaturas
#wget https://climate.nasa.gov/system/internal_resources/details/original/647_Global_Temperature_Data_File.txt
cp ../tempdata.txt tempdata.txt
awk '{for(i = 2; i <= 13; i++) {if($i < -30.0 && $i != "") {print $1; break;}}}' tempdata.txt > menorque30.txt
awk '{a = 1; for(i = 2; i <= 13; i++) {if($i > -6.0 || $i == "") {a = 0; break;}} if(a) {print $1}}' tempdata.txt > menorque6.txt
awk '{if($7 != "J" && $7 != "") print $7;}' tempdata.txt > junio.txt
#creo el archivo para poder imprimir el numero.
awk 'BEGIN {a = 0}{if($14 > -15.0) a++;} END {print a}' tempdata.txt > h.txt
cat h.txt
rm h.txt
#rm tempdata.txt
#python CardenasSergio_temp.py
