cmake_minimum_required(VERSION 3.16)

project(CapstoneProject)

set(CMAKE_CXX_STANDARD 20)

include(FetchContent)

FetchContent_Declare(
    json
    URL https://github.com/nlohmann/json/releases/download/v3.11.3/json.tar.xz
)

FetchContent_MakeAvailable(json)

add_executable(CapstoneProject main.cpp)

target_link_libraries(CapstoneProject PRIVATE nlohmann_json::nlohmann_json)