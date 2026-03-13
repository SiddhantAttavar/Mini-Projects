CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -Iraylib/src
LDFLAGS = raylib/src/libraylib.a -lGL -lm -lpthread -ldl -lX11
SOURCES = main.c game.c
HEADERS = game.h
EXECUTABLE = pacman

.PHONY: all clean run

all: $(EXECUTABLE)

$(EXECUTABLE): $(SOURCES) $(HEADERS)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDFLAGS)

test: test_raylib
	./test_raylib

clean:
	rm -f $(EXECUTABLE) test_raylib *.o

run: $(EXECUTABLE)
	./$(EXECUTABLE)
