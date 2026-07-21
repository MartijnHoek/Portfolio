#include <iostream>
#include <string>

class Item {

private:
    std::string name;
    int damage;
    int level;
    double durability;

public:
    // Constructor
    Item(std::string itemName, int damage, int level, double durability = 100.0):
          name(itemName), damage(damage), level(level), durability(durability) {}

    void pickUpItem() {
        std::cout << "User picked up item: " << name << " Level(" << level << ")" << " Durability: " << durability << "%" << std::endl;
    }

    void lowerDurability(double itemDamage) {
        if (itemDamage < 0.0) {
            std::cout << "[!] Invalid item damage! Enter a positive number!" << std::endl;
            return;
        }

        std::cout << name << " took " << damage << "\% damage!" << std::endl; 
        durability -= itemDamage;

        if (durability < 0.0) {
            std::cout << name << "(" << level << ")" << " has been to serverly damaged and cannot be used until repaired!" << std::endl;
            durability = 0.0;
        }
    }

    void repairItem() {
        durability = 100;
        std::cout << name << "(" << level << ")" << " has been repaired!" << std::endl;
    }

    void displayInfo() {
        std::cout << "Name: " << name << "\nDamage: " << damage << "\nLevel: " << level << "\nDurability: " << durability << std::endl;
    }

};

int main () {
    Item item1("Sword", 54, 2);
    Item item2("Shovel", 10, 4, 15);

    item1.pickUpItem();
    item2.pickUpItem();

    item1.lowerDurability(45.0);
    item2.lowerDurability(30.0);

    item2.repairItem();

    item1.displayInfo();
    item2.displayInfo();

    return 0;

}