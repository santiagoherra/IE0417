echo "Ejecutando productor_consumidor.cpp con varios parametros" > log_lab.txt
g++ productor_consumidor.cpp -o lab -pthread

./lab 1 1 1 >> log_lab.txt
echo "" >> log_lab.txt

./lab 1 2 1 >> log_lab.txt
echo "" >> log_lab.txt

./lab 1 4 1 >> log_lab.txt
echo "" >> log_lab.txt

./lab 2 1 1 >> log_lab.txt
echo "" >> log_lab.txt

./lab 4 1 1 >> log_lab.txt
echo "" >> log_lab.txt
