cmake_minimum_required(VERSION 3.10)
project(engine_project C)

add_library(engine SHARED engine.c)

# Output DLL as engine.dll
set_target_properties(engine PROPERTIES OUTPUT_NAME "engine")



# To build the project, run:
# cmake --build build --config Release

