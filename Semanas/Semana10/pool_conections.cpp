#include <iostream>
#include <thread>
#include <vector>
#include <semaphore>
#include <barrier>
#include <chrono>

const int NUM_HILOS = 6;
const int NUM_CONEXIONES = 3;
const int NUM_RONDAS = 3;

std::counting_semaphore<NUM_CONEXIONES> sem(NUM_CONEXIONES);
std::barrier barrera(NUM_HILOS, []() noexcept {
    std::cout << "\n--- Todos los hilos completaron la ronda ---\n" << std::endl;
});

void tarea(int id) {
    for (int ronda = 1; ronda <= NUM_RONDAS; ++ronda) {
        sem.acquire(); // solicita acceso al recurso limitado
        std::cout << "Hilo " << id << " accediendo al recurso (ronda " << ronda << ")" << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(300)); // simula uso del recurso
        std::cout << "Hilo " << id << " liberando el recurso (ronda " << ronda << ")" << std::endl;
        sem.release(); // libera el recurso

        barrera.arrive_and_wait(); // sincroniza con los demás hilos
    }
}

int main() {
    std::vector<std::thread> hilos;
    for (int i = 0; i < NUM_HILOS; ++i)
        hilos.emplace_back(tarea, i);

    for (auto &h : hilos)
        h.join();

    std::cout << "\nProcesamiento finalizado correctamente." << std::endl;
    return 0;
}
