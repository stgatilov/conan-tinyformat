cmake_minimum_required(VERSION 3.0)
project(ConanTest CXX)

find_package(tinyformat CONFIG REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example tinyformat::tinyformat)
