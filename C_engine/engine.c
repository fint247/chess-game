// engine.c
#include "engine.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

__declspec(dllexport)
const char* process_input(const char* input) {
    static char buffer[256]; // Static buffer to hold the processed output
    snprintf(buffer, sizeof(buffer), "Received: %s", input);
    return buffer;
}
