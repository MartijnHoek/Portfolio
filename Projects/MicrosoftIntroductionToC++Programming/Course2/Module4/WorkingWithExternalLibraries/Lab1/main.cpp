// Complete main.cpp for Task 1
#include <iostream>
#include <string>
#include <fstream>
#include <nlohmann/json.hpp>
using json = nlohmann::json;

json loadConfigFromFile(const std::string& filename) {
    // JSON file reading and parsing
    // Return parsed JSON object
    std::ifstream configFile(filename);
    if (!configFile.is_open()) {
        throw std::runtime_error("Could not open config file: " + filename);
    }

    json json_config;
    configFile >> json_config;
    return json_config;
}

void displayConfig(const json& json_config) {
    for (const auto& [key, value] : json_config.items())
    {
        std::cout << key << " : " << value << std::endl;
    }
}

int main () {
    std::cout << "Configuration Manager v2.0" << std::endl;
    try {
        // First, create a sample config file
        std::ofstream configFile("config.json");
        configFile << R"({
            "app_name":         "FileBasedApp",
            "version":          "2.0.0",
            "debug_mode":       false,
            "max_connections":  200,
            "features":         ["logging", "caching", "monitoring"] 
            })";
        configFile.close();

        // Load config file
        json json_config = loadConfigFromFile("config.json");
        displayConfig(json_config);

    } catch (const std::exception& e) { 
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}









// void displayConfiguration(const json& config) {
//     // Access and display each configuration value
//     // Handle potential parsing errors
//     std::cout << "\n=== Configuration Details ===" << std::endl;
//     std::cout << "Application Name: " << config["app_name"] << std::endl;
//     std::cout << "Version: " << config["version"] << std::endl;
//     std::cout << "Debug Mode: " << config["debug_mode"] << std::endl;
//     std::cout << "Max Connections: " << config["max_connections"] << std::endl; 
//     // Access nested objects
//     if (config.contains("database")) {
//         std::cout << "Database Host: " << config["database"]["host"] << std::endl;
//         std::cout << "Database Port: " << config["database"]["port"] << std::endl;
//     }
// }

// int main() {
//     std::cout << "Configuration Manager v1.0" << std::endl;
//     std::string configData = R"({
//         "app_name": "MyApplication",
//         "version": "1.2.3",
//         "debug_mode": true,
//         "max_connections": 100
//         "database": {
//             "host": "localhost",
//             "port": 5432
//         }
//     })";
//     try {
//         json config = json::parse(configData);
//         displayConfiguration(config);
//     } catch (const json::exception& e) {
//         std::cerr << "JSON parsing error: " << e.what() << std::endl;
//         return 1;
//     }   
//     return 0;
// }