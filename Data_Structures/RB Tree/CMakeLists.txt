cmake_minimum_required(VERSION 3.15)
project(ex3 C)

set(CMAKE_C_STANDARD 99)

#add_executable(ex3 RBTree.c Structs.c Structs.h)
add_executable(ex3 RBTree.c Structs.c RButilities.c RButilities.h Structs.h)