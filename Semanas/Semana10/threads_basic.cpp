#include <iostream>
#include <thread>
#include <chrono>

void tarea(int id) {
    for (int i = 0; i < 5; ++i) {
        std::cout << "Hilo " << id << " ejecutando iteración " << i << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(200));
    }
}

int main() {
    std::thread h1(tarea, 1);
    std::thread h2(tarea, 2);
    std::thread h3(tarea, 3);
    std::thread h4(tarea, 4);

    h1.join();
    h2.join();
    h3.join();
    h4.join();

    std::cout << "Ejecución finalizada." << std::endl;
}
