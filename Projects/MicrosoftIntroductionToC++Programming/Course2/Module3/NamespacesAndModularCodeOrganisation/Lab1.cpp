#include <iostream>
#include <string>
#include <vector>
// Same namespace definitions as Task 2...
namespace Graphics {
    void render() {
        std::cout << "Rendering 2D sprites" << std::endl;
    }

    void render(bool use3D) {
        if (use3D) {
            std::cout << "Rendering 3D models" << std::endl;
        } else {
            std::cout << "Rendering 2D sprites" << std::endl;
        }
    }

    void initialize() {
        std::cout << "Initializing graphics system" << std::endl;
    }

    namespace Advanced {
        void renderShadows() {
            std::cout << "Rendering advanced shadows" << std::endl;
        }
    }
}

namespace Audio {
    void play() {
        std::cout << "Playing background music" << std::endl;
    }

    void play(const std::string& soundEffect) {
        std::cout << "Playing sound effect: " << soundEffect << std::endl;
    }

    void setVolume(float volume) {
        std::cout << "Setting audio volume to: " << volume << std::endl;
    }

    // Nested namespace for different audio types
    namespace Music {
        void playTrack(const std::string& filename) {
            std::cout << "Playing music track: " << filename << std::endl;
        }

        void fadeOut(float duration) {
            std::cout << "Fading out music over " << duration << " seconds" << std::endl;
        }
    }

    namespace Effects {
        void playExplosion() {
            std::cout << "Playing explosion sound effect" << std::endl;
        }

        void playFootstep(const std::string& surface) {
            std::cout << "Playing footstep on " << surface << std::endl;
        }
    }
}

namespace Physics {
    void update() {
        std::cout << "Updating physics calculations" << std::endl;
    }

    void update(double deltaTime) {
        std::cout << "Updating physics with delta time: " << deltaTime << "ms" << std::endl;
    }
}

// Example of GOOD using practices
void gameInitialization() {
    std::cout << "=== Game Initialization Function ===" << std::endl;

    // Limited scope using declarations - good practice
    using Graphics::initialize;
    using Physics::update;

    initialize();  // Clear which initialize() this is within this function
    update();      // Clear which update() this is within this function

    // Still need full qualification for other namespaces
    Audio::play();
}

void graphicsTestFunction() {
    std::cout << "\n=== Graphics Test Function ===" << std::endl;

    // Using entire namespace in limited scope - acceptable for focused functions
    using namespace Graphics;

    render();           // Graphics::render()
    render(true);       // Graphics::render(bool)
    initialize();       // Graphics::initialize()

    // Still need qualification for other namespaces
    Audio::play("test.wav");
}

// Example of BAD practice (commented out to avoid issues)
/*
// DON'T DO THIS - global using namespace can cause conflicts
using namespace Graphics;
using namespace Audio;
using namespace Physics;

void badExample() {
    // Now we have the same problems as before!
    // Which initialize()? Which update()? Which play()?
    initialize();  // Ambiguous!
    update();      // Ambiguous!
    play();        // Ambiguous!
}
*/

// Demonstration of namespace aliases for long names
namespace GFX = Graphics;
namespace SFX = Audio;

void gameLoop() {
    std::cout << "\n=== Game Loop (with aliases) ===" << std::endl;

    // Namespace aliases make long names shorter while keeping clarity
    GFX::render();
    GFX::Advanced::renderShadows();
    SFX::play("ambient.wav");

    // You can also use using declarations with aliases
    using GFX::render;
    render();  // Now refers to Graphics::render()
}

// Demonstration of using declarations with specific functions
void audioTest() {
    std::cout << "\n=== Audio Test (selective using) ===" << std::endl;

    // Only bring in specific functions we need
    using Audio::play;
    using Audio::setVolume;  // This would need to be defined in Audio namespace

    play();                    // Audio::play()
    play("button_click.wav");  // Audio::play(const std::string&)

    // Other Audio functions still need full qualification
    // Audio::Music::playTrack("song.mp3");  // Still need full path for nested
}

int main() {
    gameInitialization();
    graphicsTestFunction();
    gameLoop();
    audioTest();

    std::cout << "\n=== Manual Qualification (always safe) ===" << std::endl;

    // The safest approach - always be explicit
    Graphics::render();
    Graphics::render(true);
    Audio::play();
    Audio::play("game_over.wav");
    Physics::update();
    Physics::update(16.67);

    return 0;
}


// #include <iostream>
// #include <string>
// #include <vector>

// // Organized code using namespaces
// namespace Graphics {
//     void render() {
//         std::cout << "Rendering 2D sprites" << std::endl;
//     }
//     void render(bool use3D) {
//         if (use3D) {
//             std::cout << "Rendering 3D models" << std::endl;
//         } else {
//             std::cout << "Rendering 2D sprites" << std::endl;
//         }
//     }
//     void initialize() {
//         std::cout << "Initializing graphics system" << std::endl;
//     }
//     void setResolution(int width, int height) {
//         std::cout << "Setting resultion at: " << width << " x " << height << std::endl;
//     }
//     // Nested namespace for advanced rendering features
//     namespace Advanced {
//         void renderShadows() {
//             std::cout << "Rendering advanced shadows" << std::endl;
//         }
//         void renderParticles(int particleCount) {
//             std::cout << "Rendering " << particleCount << " particles" << std::endl;
//         }
//     }
// }

// namespace Audio {
//     void play() {
//         std::cout << "Playing background music" << std::endl;
//     }
//     void play(const std::string& soundEffect) {
//         std::cout << "Playing sound effect: " << soundEffect << std::endl;
//     }
//     void setVolume(float volume) {
//         std::cout << "Setting audio volume to: " << volume << std::endl;
//     }
//     // Nested namespace for different audio types
//     namespace Music {
//         void playTrack(const std::string& filename) {
//             std::cout << "Playing music track: " << filename << std::endl;
//         }
//         void fadeOut(float duration) {
//             std::cout << "Fading out music over " << duration << " seconds" << std::endl;
//         }
//     }
//     namespace Effects {
//         void playExplosion() {
//             std::cout << "Playing explosion sound effect" << std::endl;
//         }
//         void playFootstep(const std::string& surface) {
//             std::cout << "Playing footstep on " << surface << std::endl;
//         }
//         void playJump() {
//             std::cout << "Playing jump sound effect" << std::endl;
//         }
//     }
// }

// namespace Physics {
//     void update() {
//         std::cout << "Updating physics calculations" << std::endl;
//     }
//     void update(double deltaTime) {
//         std::cout << "Updating physics with delta time: " << deltaTime << "ms" << std::endl;
//     }
//     void initialize(int maxEntities) {
//         std::cout << "Initializing physics system with " << maxEntities << " entities" << std::endl;
//     }
//     void applyGravity(float force) {
//         std::cout << "Applying gravity force: " << force << std::endl;
//     }
//     void setGravity(float gravity) {
//         std::cout << "Applying gravity: " << gravity << std::endl;
//     }
//     // Nested namespace for collision detection
//     namespace Collision {
//         bool checkCollision(int entityA, int entityB) {
//             std::cout << "Checking collision between entity " << entityA << " and entity " << entityB << std::endl;
//             return true;
//         }
//         void resolveCollision(int entityA, int entityB) {
//             std::cout << "Resolving collision between entity " << entityA << " and entity " << entityB << std::endl;
//         }
//     }
// }

// int main() {
//     std::cout << "=== Game Engine Inititialization ===" << std::endl;
//     // Now it is clear what each function does!
//     Graphics::initialize();
//     Physics::initialize(1000);
//     std::cout << "\n=== Game Loop ===" << std::endl;
//     Graphics::render();
//     Graphics::render(true);
//     Graphics::setResolution(720, 1080);
//     Physics::update();
//     Physics::update(16.67);
//     Physics::applyGravity(9.8f);
//     Physics::setGravity(96);
//     Audio::play();
//     Audio::play("explosion.wav");
//     Audio::setVolume(0.8f);
//     std::cout << "\n=== Advanced Features ===" << std::endl;
//     Graphics::Advanced::renderShadows();
//     Graphics::Advanced::renderParticles(500);
//     Audio::Music::playTrack("background.mp3");
//     Audio::Effects::playExplosion();
//     Audio::Effects::playFootstep("grass");
//     Audio::Effects::playJump();
//     Physics::Collision::checkCollision(1, 2);
//     Physics::Collision::resolveCollision(1, 2);
//     return 0;
// }

// #include <iostream>
// #include <string>
// #include <vector>

// // Global functions from different developers - naming conflicts ahead!
// void render() {
//     std::cout << "Rendering 2D sprites" << std::endl;
// }

// void render(bool use3D) {
//     if (use3D) {
//         std::cout << "Rendering 3D models" << std::endl;
//     } else {
//         std::cout << "Rendering 2D sprites" << std::endl;
//     }
// }

// void play() {
//     std::cout << "Playing background music" << std::endl;
// }

// void play(std::string soundEffect) {
//     std::cout << "Playing sound effect: " << soundEffect << std::endl;
// }

// void update() {
//     std::cout << "Updating physics calculations" << std::endl;
// }

// void update(double deltaTime) {
//     std::cout << "Updating physics with delta time: " << deltaTime << std::endl;
// }

// void initialize() {
//     std::cout << "Initializing graphics system" << std::endl;
// }

// void initialize(int maxEntities) {
//     std::cout << "Initializing physics system with " << maxEntities << " entities" << std::endl;
// }

// int main() {
//     // This code is confusing - which functions do what?
//     render();
//     render(true);
//     play();
//     play("explosion.wav");
//     update();
//     update(16.67);
//     initialize();
//     initialize(1000);

//     return 0;
// }