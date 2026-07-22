#include <iostream>
#include <string>
#include <memory>

class DatabaseConnection {
private:
    std::string connectionString;
    std::string databaseName;
    bool isConnected;
    int connectionId;
    static int nextId;

    // Simulate connection establishment
    bool establishConnection() {
        std::cout << "Establishing connection to " << databaseName << "..." << std::endl;
        // Simulate connection logic
        isConnected = true;
        return true;
    }

    // Simulate connection cleanup
    void closeConnection() {
        if (isConnected) {
            std::cout << "Closing database connection [ID: " << connectionId << "]" << std::endl;
            isConnected = false;
        }
    }

public:
    // Default constructor
    DatabaseConnection()
        : connectionString("localhost:5432"),
          databaseName("default_db"),
          isConnected(false),
          connectionId(++nextId) {
        std::cout << "Creating default database connection [ID: " << connectionId << "]" << std::endl;
        establishConnection();
    }

    // Parameterized constructor
    DatabaseConnection(const std::string& connStr, const std::string& dbName)
        : connectionString(connStr),
          databaseName(dbName),
          isConnected(false),
          connectionId(++nextId) {
        std::cout << "Creating database connection [ID: " << connectionId
                  << "] to " << databaseName << std::endl;
        establishConnection();
    }

    // Copy constructor (creates new connection)
    DatabaseConnection(const DatabaseConnection& other)
        : connectionString(other.connectionString),
          databaseName(other.databaseName + "_copy"),
          isConnected(false),
          connectionId(++nextId) {
        std::cout << "Creating copied database connection [ID: " << connectionId
                  << "] based on connection " << other.connectionId << std::endl;
        establishConnection();
    }

    // Destructor
    ~DatabaseConnection() {
        std::cout << "Destroying database connection [ID: " << connectionId << "]" << std::endl;
        closeConnection();
    }

    // Member functions
    void executeQuery(const std::string& query) {
        if (isConnected) {
            std::cout << "Executing on " << databaseName << ": " << query << std::endl;
        } else {
            std::cout << "Cannot execute - connection not established" << std::endl;
        }
    }

    bool getConnectionStatus() const {
        return isConnected;
    }

    int getId() const {
        return connectionId;
    }
};

// Initialize static member
int DatabaseConnection::nextId = 0;

// Complete the main function
int main() {
    std::cout << "=== Database Connection Manager ===" << std::endl;

    // Test default constructor
    std::cout << "\n1. Creating default connection:" << std::endl;
    DatabaseConnection defaultConn;
    defaultConn.executeQuery("SELECT * FROM users");

    // Test parameterized constructor
    std::cout << "\n2. Creating custom connections:" << std::endl;
    DatabaseConnection prodConn("prod-server:5432", "production_db");
    DatabaseConnection testConn("test-server:5432", "test_db");

    prodConn.executeQuery("SELECT COUNT(*) FROM orders");
    testConn.executeQuery("SELECT * FROM test_table");

    // Test copy constructor and scoping
    std::cout << "\n3. Testing connection copying:" << std::endl;
    {
        DatabaseConnection copiedConn = prodConn;  // Copy constructor
        copiedConn.executeQuery("SELECT * FROM copied_data");

        std::cout << "Original connection ID: " << prodConn.getId() << std::endl;
        std::cout << "Copied connection ID: " << copiedConn.getId() << std::endl;

        std::cout << "\n--- Copied connection going out of scope ---" << std::endl;
    } // copiedConn destructor called here

    std::cout << "\n4. Original connection still works:" << std::endl;
    prodConn.executeQuery("SELECT * FROM final_query");

    std::cout << "\n=== Program ending - cleanup phase ===" << std::endl;

    return 0;
}


// #include <iostream>
// #include <string>
// #include <chrono>
// #include <ctime>

// class DigitalAsset {
// private:
//     std::string fileName;
//     std::string fileType;
//     double fileSizeMB;
//     std::string creationDate;
//     bool isActive;
//     static int totalAssets;  // Track total number of assets created

// public:
//     // Default constructor
//     DigitalAsset()
//         : fileName("untitled"), fileType("unknown"), fileSizeMB(0.0), isActive(true) {

//         // Get current date for creation timestamp
//         auto now = std::chrono::system_clock::now();
//         auto time_t = std::chrono::system_clock::to_time_t(now);
//         creationDate = std::ctime(&time_t);
//         creationDate.pop_back(); // Remove newline

//         totalAssets++;
//         std::cout << "✓ Default asset created: " << fileName
//                   << " | Total assets: " << totalAssets << std::endl;
//     }

//     // Parameterized constructor
//     DigitalAsset(const std::string& name, const std::string& type, double size)
//         : fileName(name), fileType(type), fileSizeMB(size), isActive(true) {

//         auto now = std::chrono::system_clock::now();
//         auto time_t = std::chrono::system_clock::to_time_t(now);
//         creationDate = std::ctime(&time_t);
//         creationDate.pop_back(); // Remove newline

//         totalAssets++;
//         std::cout << "✓ Asset created: " << fileName << " (" << fileType
//                   << ") | Total assets: " << totalAssets << std::endl;
//     }

//     // Copy constructor
//     DigitalAsset(const DigitalAsset& other)
//         : fileName(other.fileName + "_copy"),
//           fileType(other.fileType),
//           fileSizeMB(other.fileSizeMB),
//           creationDate(other.creationDate),
//           isActive(other.isActive) {

//         totalAssets++;
//         std::cout << "✓ Asset copied: " << fileName
//                   << " from " << other.fileName
//                   << " | Total assets: " << totalAssets << std::endl;
//     }

//     // Destructor
//     ~DigitalAsset() {
//         totalAssets--;
//         std::cout << "✗ Asset destroyed: " << fileName
//                   << " | Remaining assets: " << totalAssets << std::endl;
//     }

//     // Member functions
//     void displayInfo() const {
//         std::cout << "Asset: " << fileName
//                   << " [" << fileType << "] - "
//                   << fileSizeMB << "MB - Created: " << creationDate
//                   << " - Status: " << (isActive ? "Active" : "Archived")
//                   << std::endl;
//     }

//     void archive() {
//         isActive = false;
//         std::cout << "Asset " << fileName << " has been archived." << std::endl;
//     }

//     static int getTotalAssets() {
//         return totalAssets;
//     }
// };

// // Initialize static member
// int DigitalAsset::totalAssets = 0;

// int main() {
//     std::cout << "=== Digital Asset Management System ===" << std::endl;
//     std::cout << "Initial total assets: "
//               << DigitalAsset::getTotalAssets() << std::endl << std::endl;

//     // Test default constructor
//     std::cout << "1. Creating default asset:" << std::endl;
//     DigitalAsset defaultAsset;
//     defaultAsset.displayInfo();
//     std::cout << std::endl;

//     // Test parameterized constructor
//     std::cout << "2. Creating specific assets:" << std::endl;
//     DigitalAsset logo("company_logo.png", "image", 2.5);
//     DigitalAsset video("promo_video.mp4", "video", 150.0);

//     logo.displayInfo();
//     video.displayInfo();
//     std::cout << std::endl;

//     // Test copy constructor and demonstrate lifecycle
//     std::cout << "3. Testing copy constructor:" << std::endl;
//     {
//         DigitalAsset logoCopy = logo;  // Copy constructor called
//         logoCopy.displayInfo();
//         logoCopy.archive();

//         std::cout << "--- logoCopy going out of scope ---" << std::endl;
//     } // logoCopy destructor called here

//     std::cout << "\n4. Final status:" << std::endl;
//     std::cout << "Total assets remaining: "
//               << DigitalAsset::getTotalAssets() << std::endl;

//     std::cout << "\n=== Program ending - remaining objects will be destroyed ===" << std::endl;

//     return 0;
// }