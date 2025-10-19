# run_lab.ps1
Write-Output "Ejecutando productor_consumidor.cpp con varios parámetros" | Out-File -FilePath log_lab.txt -Encoding utf8

# Compilar el programa
g++ productor_consumidor.cpp -o lab -pthread

# Combinaciones de productores y consumidores
$prods = @(10)
$cons = @(1, 2, 3, 4,5,6,7)

# Recorre todas las combinaciones
foreach ($p in $prods) {
    foreach ($c in $cons) {

        $msg = "-------------------------------------------------------------`nEjecutando con $p productores y $c consumidores"
        Write-Output $msg | Tee-Object -FilePath log_lab.txt -Append

        # Medir tiempo de ejecución del programa
        $tiempo = Measure-Command {
            .\lab $p $c 1 | Tee-Object -FilePath log_lab.txt -Append
        }

        # Registrar tiempo en el log
        $resultado = "Duración: {0:N2} segundos" -f $tiempo.TotalSeconds
        Write-Output $resultado | Tee-Object -FilePath log_lab.txt -Append
        Write-Output "`n" | Out-File -Append -FilePath log_lab.txt
    }
}

Write-Output "Todas las ejecuciones completadas. Resultados guardados en log_lab.txt"
