#include <iostream>
#include <string>
#include <vector>
#include <regex>

class UserProfile {
private:
    std::string username;
    std::string email;
    std::string passwordHash;
    std::string fullName;
    int age;
    std::vector<std::string> friends;
    bool isPrivateProfile;
    bool isVerified;
    std::string phoneNumber;

    // Private validation helpers
    bool isValidEmail(const std::string& email) const {
        std::regex emailPattern(R"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})");
        return std::regex_match(email, emailPattern);
    }

    bool isValidUsername(const std::string& username) const {
        return username.length() >= 3 && username.length() <= 20;
    }

public:
    // Constructor with comprehensive validation
    UserProfile(const std::string& user,
                const std::string& mail,
                const std::string& name)
        : isPrivateProfile(true),
          isVerified(false),
          age(0) {

        if (!setUsername(user)) {
            throw std::invalid_argument("Invalid username");
        }

        if (!setEmail(mail)) {
            throw std::invalid_argument("Invalid email address");
        }

        if (!setFullName(name)) {
            throw std::invalid_argument("Invalid full name");
        }
    }

    // Getters for public information
    std::string getUsername() const {
        return username;
    }

    std::string getEmail() const {
        return email;
    }

    std::string getDisplayName() const {
        return isPrivateProfile ? username : fullName;
    }

    bool isProfilePrivate() const {
        return isPrivateProfile;
    }

    bool isUserVerified() const {
        return isVerified;
    }

    int getFriendCount() const {
        return friends.size();
    }

    // Secured setters with validation
    bool setUsername(const std::string& newUsername) {
        if (isValidUsername(newUsername)) {
            username = newUsername;
            return true;
        }

        std::cout << "Error: Username must be 3-20 characters long" << std::endl;
        return false;
    }

    bool setEmail(const std::string& newEmail) {
        if (isValidEmail(newEmail)) {
            email = newEmail;
            return true;
        }

        std::cout << "Error: Invalid email format" << std::endl;
        return false;
    }

    bool setFullName(const std::string& name) {
        if (!name.empty() && name.length() <= 100) {
            fullName = name;
            return true;
        }

        std::cout << "Error: Full name cannot be empty or exceed 100 characters" << std::endl;
        return false;
    }

    bool setAge(int newAge) {
        if (newAge >= 13 && newAge <= 120) {
            age = newAge;
            return true;
        }

        std::cout << "Error: Age must be between 13 and 120" << std::endl;
        return false;
    }

    // Your implementation here: Add methods for privacy settings, friend management, etc.
    void setPrivacyStatus(bool status) {
        isPrivateProfile = status;
        std::cout << "Profile set to " << (status ? "private" : "public") << std::endl;
    }

    void addFriend(std::string friendUsername) {
        if (friendUsername == username) {
            std::cout << "[!] Cannot add yourself as friend!" << std::endl;
            return;
        }

        for (const auto& existingFriends : friends) {
            if (existingFriends == friendUsername) {
                std::cout << "[!] Friend already added to friendslist!" << std::endl;
                return;
            }
        }
        friends.push_back(friendUsername);
        std::cout << "Added " << friendUsername << " as a friend!" << std::endl;
    }

    void displayPublicProfile() const {
        std::cout << "=== Public Profile ===" << std::endl;
        std::cout << "Username: " << username << std::endl;
        std::cout << "Display Name: " << getDisplayName() << std::endl;
        std::cout << "Verified: " << (isVerified ? "Yes" : "No") << std::endl;
        std::cout << "Friends: " << getFriendCount() << std::endl;
    }

    // Friend declarations for platform administration
    friend class PlatformModerator;
    friend void technicalSupport(UserProfile& user, const std::string& issue);
};

class PlatformModerator {
public:
    static void performModeration(const UserProfile& user) {
        std::cout << "\n=== MODERATION REVIEW ===" << std::endl;
        std::cout << "Full access to: " << user.username << std::endl;
        std::cout << "Real name: " << user.fullName << std::endl;
        std::cout << "Email: " << user.email << std::endl;
        std::cout << "Age: " << user.age << std::endl;
        std::cout << "Friend count: " << user.friends.size() << std::endl;
    }    
};

void technicalSupport(UserProfile& user, const std::string& issue) {
    std::cout << "Technical Support accessing account: " << user.username << std::endl;
    std::cout << "Issue: " << issue << std::endl;
    std::cout << "Contact email: " << user.email << std::endl;
};

// Complete this implementation
int main() {
    std::cout << "=== User Profile Management System ===" << std::endl;

    try {
        UserProfile user1("alice123", "alice@email.com", "Alice Johnson");

        user1.setAge(25);
        user1.displayPublicProfile();

        // Test friend management
        user1.addFriend("bob456");
        user1.addFriend("charlie789");
        user1.addFriend("alice123"); // Should fail

        // Test privacy controls
        user1.setPrivacyStatus(false);
        user1.displayPublicProfile();

        // Test friend access
        PlatformModerator::performModeration(user1);
        technicalSupport(user1, "Password reset request");

    }
    catch (const std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }

    return 0;
}


// #include <iostream>
// #include <string>
// #include <vector>
// #include <iomanip>

// // VULNERABLE CLASS - Current implementation with security flaws
// class InsecureAccount {
// public:
//     std::string accountNumber;
//     std::string ownerName;
//     double balance;
//     std::string accountType;
//     bool isActive;

//     void displayAccount() {
//         std::cout << "Account: " << accountNumber
//                   << " | Owner: " << ownerName
//                   << " | Balance: $" << std::fixed << std::setprecision(2)
//                   << balance << std::endl;
//     }
// };

// // SECURE REFACTORED CLASS - Your implementation
// class SecureAccount {
// private:
//     std::string accountNumber;
//     std::string ownerName;
//     double balance;
//     std::string accountType;
//     bool isActive;
//     std::vector<std::string> transactionHistory;

//     // Private helper method for transaction logging
//     void logTransaction(const std::string& transaction) {
//         transactionHistory.push_back(transaction);

//         if (transactionHistory.size() > 50) {
//             transactionHistory.erase(transactionHistory.begin());
//         }
//     }

// public:
//     // Constructor with validation
//     SecureAccount(const std::string& accNum,
//                   const std::string& owner,
//                   const std::string& type,
//                   double initialBalance = 0.0)
//         : accountNumber(accNum),
//           ownerName(owner),
//           accountType(type),
//           balance(initialBalance),
//           isActive(true) {

//         if (accNum.empty() || owner.empty()) {
//             throw std::invalid_argument("Account number and owner name cannot be empty");
//         }

//         if (initialBalance < 0) {
//             balance = 0.0;
//             std::cout << "Warning: Negative initial balance set to $0.00" << std::endl;
//         }

//         logTransaction("Account created with initial balance: $" + std::to_string(initialBalance));
//     }

//     // Getters with appropriate access levels
//     std::string getAccountNumber() const { return accountNumber; }
//     std::string getOwnerName() const { return ownerName; }
//     double getBalance() const { return balance; }
//     std::string getAccountType() const { return accountType; }
//     bool getActiveStatus() const { return isActive; }

//     // Secured transaction methods with validation
//     bool deposit(double amount) {
//         if (!isActive) {
//             std::cout << "Error: Cannot deposit to inactive account" << std::endl;
//             return false;
//         }

//         if (amount <= 0) {
//             std::cout << "Error: Deposit amount must be positive" << std::endl;
//             return false;
//         }

//         if (amount > 50000) {
//             std::cout << "Error: Deposit exceeds daily limit of $50,000" << std::endl;
//             return false;
//         }

//         balance += amount;
//         logTransaction("Deposit: +$" + std::to_string(amount));

//         std::cout << "Successfully deposited $" << std::fixed
//                   << std::setprecision(2) << amount
//                   << ". New balance: $" << balance << std::endl;

//         return true;
//     }

//     bool withdraw(double amount) {
//         if (!isActive) {
//             std::cout << "Error: Cannot withdraw from inactive account" << std::endl;
//             return false;
//         }

//         if (amount <= 0) {
//             std::cout << "Error: Withdrawal amount must be positive" << std::endl;
//             return false;
//         }

//         if (amount > balance) {
//             std::cout << "Error: Insufficient funds. Current balance: $"
//                       << std::fixed << std::setprecision(2)
//                       << balance << std::endl;
//             return false;
//         }

//         if (amount > 10000) {
//             std::cout << "Error: Withdrawal exceeds daily limit of $10,000" << std::endl;
//             return false;
//         }

//         balance -= amount;
//         logTransaction("Withdrawal: -$" + std::to_string(amount));

//         std::cout << "Successfully withdrew $" << std::fixed
//                   << std::setprecision(2) << amount
//                   << ". New balance: $" << balance << std::endl;

//         return true;
//     }

//     // Account management methods
//     void setAccountStatus(bool status) {
//         isActive = status;
//         logTransaction(status ? "Account activated" : "Account deactivated");

//         std::cout << "Account "
//                   << (status ? "activated" : "deactivated")
//                   << std::endl;
//     }

//     void displayAccount() const {
//         std::cout << "=== Account Information ===" << std::endl;
//         std::cout << "Account Number: " << accountNumber << std::endl;
//         std::cout << "Owner: " << ownerName << std::endl;
//         std::cout << "Type: " << accountType << std::endl;
//         std::cout << "Balance: $" << std::fixed << std::setprecision(2)
//                   << balance << std::endl;
//         std::cout << "Status: " << (isActive ? "Active" : "Inactive") << std::endl;
//         std::cout << "Recent Transactions: " << transactionHistory.size() << std::endl;
//     }

//     // Friend function for regulatory compliance and auditing
//     friend class ComplianceAuditor;
//     friend void emergencyFreeze(SecureAccount& account, const std::string& reason);
// };

// // Friend function for emergency account freezing
// void emergencyFreeze(SecureAccount& account, const std::string& reason) {
//     account.isActive = false;
//     account.logTransaction("EMERGENCY FREEZE: " + reason);

//     std::cout << "EMERGENCY: Account "
//               << account.accountNumber
//               << " frozen due to: "
//               << reason << std::endl;
// }

// // Friend class for compliance auditing
// class ComplianceAuditor {
// public:
//     static void performAudit(const SecureAccount& account) {
//         std::cout << "\n=== COMPLIANCE AUDIT ===" << std::endl;
//         std::cout << "Account: " << account.accountNumber << std::endl;
//         std::cout << "Balance: $" << std::fixed
//                   << std::setprecision(2)
//                   << account.balance << std::endl;

//         std::cout << "Transaction History Count: "
//                   << account.transactionHistory.size() << std::endl;

//         std::cout << "Recent Transactions:" << std::endl;

//         int displayCount = std::min(5, static_cast<int>(account.transactionHistory.size()));

//         for (int i = account.transactionHistory.size() - displayCount;
//              i < static_cast<int>(account.transactionHistory.size());
//              ++i) {
//             std::cout << " - " << account.transactionHistory[i] << std::endl;
//         }

//         std::cout << "Audit completed successfully." << std::endl;
//     }
// };

// int main() {
//     std::cout << "=== Financial Account Security System Demo ===" << std::endl;

//     // Demonstrate vulnerabilities of the insecure version
//     std::cout << "\n1. INSECURE VERSION - Vulnerabilities:" << std::endl;

//     InsecureAccount insecure;
//     insecure.accountNumber = "ACC001";
//     insecure.ownerName = "John Doe";
//     insecure.balance = 1000.0;

//     // Anyone can directly manipulate the balance!
//     insecure.balance = 999999.99;
//     insecure.balance = -5000.0;

//     std::cout << "Insecure account manipulated - Balance now: $"
//               << std::fixed << std::setprecision(2)
//               << insecure.balance << std::endl;

//     // Demonstrate the secure version
//     std::cout << "\n2. SECURE VERSION - Protected Operations:" << std::endl;

//     try {
//         SecureAccount secure("ACC002", "Jane Smith", "Checking", 1500.0);

//         secure.displayAccount();

//         std::cout << "\nTesting deposit operations:" << std::endl;
//         secure.deposit(500.0);
//         secure.deposit(-100.0);
//         secure.deposit(60000.0);

//         std::cout << "\nTesting withdrawal operations:" << std::endl;
//         secure.withdraw(200.0);
//         secure.withdraw(5000.0);
//         secure.withdraw(50000.0);

//         std::cout << "\n3. Emergency compliance action:" << std::endl;
//         emergencyFreeze(secure, "Suspicious activity detected");

//         std::cout << "\nTrying operations on frozen account:" << std::endl;
//         secure.deposit(100.0);

//         std::cout << "\n4. Compliance audit:" << std::endl;
//         ComplianceAuditor::performAudit(secure);

//     } catch (const std::exception& e) {
//         std::cout << "Error creating account: "
//                   << e.what() << std::endl;
//     }

//     return 0;
// }