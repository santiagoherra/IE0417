CXX      = clang++
FLAGS    = -std=c++17 -g -O0 -fno-omit-frame-pointer
ASAN     = -fsanitize=address
TSAN     = -fsanitize=thread
LDFLAGS  = -lpthread

# Targets
all: suma_vector buffers race

suma_vector: suma_vector.cpp
	$(CXX) $(FLAGS) -o $@ $<

buffers: buffers.cpp
	$(CXX) $(FLAGS) -o $@ $<

race: race.cpp
	$(CXX) $(FLAGS) -o $@ $< $(LDFLAGS)

asan: buffers
	$(CXX) $(FLAGS) $(ASAN) -o buffers buffers.cpp
	./buffers

tsan: race
	$(CXX) $(FLAGS) $(TSAN) -o race race.cpp $(LDFLAGS)
	./race

valgrind: buffers
	valgrind --leak-check=yes --track-origins=yes --show-leak-kinds=all ./buffers

helgrind: race
	valgrind --tool=helgrind ./race

clean:
	rm -f suma_vector buffers race
