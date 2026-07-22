#include <iostream>
#include <string>

// VULNERABLE CLASS - Poor encapsulation in game system
class Character {

private:
    std::string name;
    int hitPoints;
    int attackStrength;

public:
    Character(std::string n, int hp, int attack) {
        setName(n); setHitPoints(hp); setAttackStrength(attack);
    }

    void setName(std::string newName) {
        if (newName.empty()) {
            std::cout << "[!] Entered name was empty!, could not set the name!" << std::endl;
            return;
        }
        name = newName;
    }

    void setHitPoints(int newHitPoints) {
        if (newHitPoints < 0){
            std::cout << "[!] Error when setting new hitpoints, can not be lower than 0!" << std::endl;
            return;
        } 
        hitPoints = newHitPoints;
    }

    void setAttackStrength(int newAttackStrength) {
        if (newAttackStrength < 0){
            std::cout << "[!] Error when setting new attack strength, can not be lower than 0!" << std::endl;
            return;
        } 
        attackStrength = newAttackStrength;
    }

    int getHitPoints() {return hitPoints;}

    int getAttackStrength() {return attackStrength;}


    void displayInfo() {
        std::cout << "Name: " << name << ", HP: " << hitPoints << ", Attack: " << attackStrength << std::endl;
    }

    friend void setAdminHealth(Character& character);
};

void setAdminHealth(Character& character) {
    character.hitPoints = 999;
}


int main() {
    // Demonstrating vulnerabilities with Character class
    Character hero("Warrior", 100, 25);

    hero.displayInfo();

    // Problems: Game logic can be broken by direct manipulation
    hero.setHitPoints(50);
    hero.setAttackStrength(999);

    std::cout << "After modifications:" << std::endl;
    hero.displayInfo();

    std::cout << "Admin takes control!" << std::endl;
    setAdminHealth(hero);
    hero.displayInfo();

    return 0;
}