#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <queue>
#include <chrono>

const int BUFFER_SIZE = 5;
std::queue<int> buffer;
std::mutex mtx;
std::condition_variable cv_productor, cv_consumidor;
bool done = false;

void productor(int id, int n_tareas) {
    for (int i = 0; i < n_tareas; ++i) {
        std::unique_lock<std::mutex> lock(mtx);
        cv_productor.wait(lock, [] { return buffer.size() < BUFFER_SIZE; });

        int tarea = i + id * 100;
        buffer.push(tarea);
        std::cout << "[Productor " << id << "] generó tarea " << tarea << std::endl;

        lock.unlock();
        cv_consumidor.notify_all();
        std::this_thread::sleep_for(std::chrono::milliseconds(150));
    }
}

void consumidor(int id) {
    while (true) {
        std::unique_lock<std::mutex> lock(mtx);
        cv_consumidor.wait(lock, [] { return !buffer.empty() || done; });

        if (buffer.empty() && done) break;

        int tarea = buffer.front();
        buffer.pop();
        std::cout << "[Consumidor " << id << "] procesó tarea " << tarea << std::endl;

        lock.unlock();
        cv_productor.notify_all();
        std::this_thread::sleep_for(std::chrono::milliseconds(200));
    }
}

int main() {
    std::vector<std::thread> productores, consumidores;

    for (int i = 0; i < 3; ++i)
        productores.emplace_back(productor, i, 5);

    for (int i = 0; i < 2; ++i)
        consumidores.emplace_back(consumidor, i);

    for (auto &p : productores) p.join();

    {
        std::lock_guard<std::mutex> lock(mtx);
        done = true;
    }

    cv_consumidor.notify_all();

    for (auto &c : consumidores) c.join();

    std::cout << "Procesamiento finalizado correctamente." << std::endl;
}
