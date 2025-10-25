#include <iostream>
#include <cstring>
using namespace std;

// Bugs intencionales: overflow, use-after-free y fuga de memoria.

char* copiar(const char* src) {
//size_t n = strlen(src);
if (!src) return nullptr;
size_t n = strlen(src);
char* buf = (char*) malloc(n + 1);
memcpy(buf, src, n + 1);
return buf;
}

int main() {
const char* msg = "hola mundo";
char* a = copiar(msg); // Overflow al copiar
if (a) {
cout << a << '\n' << endl;
free(a);
a = nullptr;
}

char* leak = (char*) malloc(128);
strcpy(leak, "leak detectado"); // Fuga de memoria (no se libera 'leak')
free(leak);

return 0;
}
