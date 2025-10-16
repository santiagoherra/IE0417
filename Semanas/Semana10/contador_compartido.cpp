#include <iostream>
#include <thread>
#include <mutex>

int contador = 0;
std::mutex mtx;

void incrementar(int id) {
    for (int i = 0; i < 1000; ++i) {
        //std::lock_guard<std::mutex> lock(mtx);
        ++contador;
    }
}

int main() {
    std::thread t1(incrementar, 1);
    std::thread t2(incrementar, 2);
    std::thread t3(incrementar, 3);

    t1.join();
    t2.join();
    t3.join();

    std::cout << "Valor final del contador: " << contador << std::endl;
}
