#include <iostream>
#include <vector>
using namespace std;

// Bug 1 (lógico): la suma ignora el último elemento.
// Bug 2 (ejecución): posible acceso fuera de rango al imprimir.

int suma(const vector<int>& v) {
    int total = 0;
    // Error: condición incorrecta (usa < v.size() - 1)
    for (size_t i = 0; i < v.size(); ++i) {
        total += v[i];
    }
    return total;
}

int main() {
    vector<int> datos = {1, 2, 3, 4}; // suma esperada = 10
    int s = suma(datos);
    cout << "Suma calculada: " << s << endl;

    // Error: acceso fuera de rango
    cout << "Elemento en indice 4: " << datos.at(3) << endl;
    return 0;
}