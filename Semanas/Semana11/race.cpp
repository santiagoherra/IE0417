#include <mutex>
#include <thread>
#include <iostream>

int contador = 0;
std::mutex m;

void trabajo(int n) {
for (int i = 0; i < n; ++i) {
std::lock_guard<std::mutex> lk(m);
++contador;
}
}

int main() {
int iter = 1'000'000;
std::thread t1(trabajo, iter), t2(trabajo, iter);
t1.join(); t2.join();
std::cout << "Valor final: " << contador << '\n';
}
 