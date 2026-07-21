#include <fstream>
#include <string>
#include <stdexcept>
#include <iostream>
#include <filesystem>
#include <sstream>
#include <iomanip>
#include <limits>
#include <cerrno>

#include <nlohmann/json.hpp>
using json = nlohmann::json;

namespace FileHandler {
    inline const std::filesystem::path inputFilePath =
    "C:\\Users\\Martijn\\PycharmProjects\\Portfolio\\Projects\\MicrosoftIntroductionToC++Programming\\Course2\\Module5";

    namespace Input {
        json readInputFile(const std::string &path = (inputFilePath / "input.json").string()) {
            // Function to read a JSON input file and return the parsed data
            std::ifstream inputFile(path);
            if (!inputFile.is_open()) {
                throw std::runtime_error(
                    "Error opening input file '" + path + "': " + std::strerror(errno)
                );
            }
            json inputData;
            inputFile >> inputData;
            std::cout << "Input File successfully read!" << std::endl;
            return inputData;
        }
    }

    namespace Output {
        void writeOutputFile(const std::string &data, const std::string &path = (inputFilePath / "output.txt").string()) {
            // Function to write JSON data to an output file
            std::ofstream outputFile(path);
            if (!outputFile.is_open()) {
                throw std::runtime_error(
                    "Error opening output file '" + path + "': " + std::strerror(errno)
                );
            }
            outputFile << data;
            std::cout << "Output File successfully written!" << std::endl;
        }
    }
}

namespace Processing {
    double processAveragePrice(const json &inputData) {
        double averagePrice = 0.0;
        int amountOfItems = 0;

        for (const auto &[key, value] : inputData.items()) {
            if (value.contains("price")) {
                double price = value["price"];
                averagePrice += price;
                amountOfItems++;
            }
        }
        if (amountOfItems > 0) {
            averagePrice /= amountOfItems;
        } else {
            throw std::runtime_error("No items with price field found");
        }        
        return averagePrice;
    }

    double findMinimumPrice(const json &inputData) {
        double minPrice = std::numeric_limits<double>::max();

        for (const auto &[key, value] : inputData.items()) {
            if (value.contains("price")) {
                double price = value["price"];
                if (price < minPrice) {
                    minPrice = price;
                }
            }
        }
        return minPrice;
    }

    double findMaximumPrice(const json &inputData) {
        double maxPrice = std::numeric_limits<double>::lowest();

        for (const auto &[key, value] : inputData.items()) {
            if (value.contains("price")) {
                double price = value["price"];
                if (price > maxPrice) {
                    maxPrice = price;
                }
            }
        }
        return maxPrice;
    }

    std::string processData(const json &inputData) {

        double averagePrice = Processing::processAveragePrice(inputData);
        double minimumPrice = Processing::findMinimumPrice(inputData);
        double maximumPrice = Processing::findMaximumPrice(inputData);

        std::ostringstream oss;
        oss << std::fixed << std::setprecision(2);
        oss << "Average Price: $" << averagePrice << "\n"
            << "Minimum Price: $" << minimumPrice << "\n"
            << "Maximum Price: $" << maximumPrice << "\n";

        return oss.str();
    }

}


int main() {

    try {
        json inputData = FileHandler::Input::readInputFile();
        std::string processedData = Processing::processData(inputData);
        FileHandler::Output::writeOutputFile(processedData);


} catch (const std::exception& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
    }

    return 0;
}