mkdir Temperaturas
wget https://climate.nasa.gov/system/internal_resources/details/original/647_Global_Temperature_Data_File.txt 
cd Temperaturas
cp ~/tempdata_masfacil.txt ./tempdata_masfacil.txt
awk 'BEGIN {FS=","} {for(i = 2; i <= 13; i++) {if($i < -30.0 && $i != "" && $1 != "    ") {print $1; break;}}}' tempdata_masfacil.txt? > menorque30.txt
awk 'BEGIN {FS=","} {a = 1; for(i = 2; i <= 13; i++) {if($i > -6.0 || $i == "") {a = 0; break;}} if(a && $1 != "    ") {print $1}}' tempdata_masfacil.txt? > menorque6.txt
awk 'BEGIN {FS=","} {if($7 != "  J  " && $7 != "") print $7;}' tempdata_masfacil.txt? > junio.txt
awk 'BEGIN {FS=","; a = 0}{if($14 > -15.0) a++;} END {print a}' tempdata_masfacil.txt
rm tempdata_masfacil.txt
cd ~/ 
python CardenasSergio_temp.py 
