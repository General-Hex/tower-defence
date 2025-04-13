# TOWER DEFENSE MAYHEM ©
## By Ryan Beikrasouli
#### ID: 6137
#### Year of creation: 2025

## ALL LINKS
- [Project Overview](#project-overview)
- [Project Requirements and Implementation](#project-requirements--implementation)
- [Requrements](#requirements)
- [How To Play](#how-to-play)
- [Controls](#controls)
- [Turrets and Monster Guide](#turret-and-monster-guide)
- [Credits](#credits)
- [Challenges Faced](#log-of-challenges-faced)
- [Developer Retrospective](#developer-retrospective)
- [Final Notes](#final-notes)

## PROJECT OVERVIEW:
The purpose of my project was to create a fun and interactive tower defence game using the programming skills I have learned including Object Oriented Programming and modularisation along side the pygame library to allow me to effectively create the game. The key features of my tower defence game are having a main screen, having a level selection screen (which currently only has two levels) and having a main game which varies between levels and each level has multiple waves of increasing difficulty. For a more in depth explination of the differnt turrets and enemies currently implemented in the game please view [Turret and Monster Guide](#turret-and-monster-guide)

## PROJECT REQUIREMENTS & IMPLEMENTATION:
| Requirement | Implementation |
| :---: | :---: |
| Multiple maps with a path monsters can follow | Used the Tiled app to create maps and waypoints and export them as both png and JSON files so the data can be extracted |
| Create Method for monsters to follow waypoints | The __move() method as defined in the enemy parent class (in [enemies.py](/models/enemies.py)) alows the monsters to follow the waypoints using vectors |
| Monsters must spawn in waves of increasing difficulty until the last wave | Using a dictionary defined in the [constants.py](constants.py) file I outlined the type and amount of monsters for each wave allowing me to manually define the difficulty of each wave and create however many waves I desire easily |
| If a monster reaches the end of the path the player's base must take damage | Once again in the __move() method defined in the parent enemy class (in [enemies.py](/models/enemies.py)) there is a conditional statement which checks if there is no more waypoints left for the monster to go to, and if this is the case the monster is removed from the screen and the monster's damage is subtracted from the player's base | 
| There muust be multiple unique monsters with unique attributes | Using the parent enemy class and inheritance (in [enemies.py](/models/enemies.py)) I was able to effectively create both a [Zombie](#zombies) and [Skeleton](#skeletons) enemies. Both of these enemies have unique attributes as specified in [Monsters](#monsters) |
|The player must be able to buy and place down turrets only on grassy and empty tiles| Using a function called createTurret() (as defined in [turrets.py](models/turrets.py)) which allows me to append a new turret to a pygame's group I am able to simply check whether the player has purchaced a turret and if that turret is placed in a usable tile (Which I check against the GRASS_TILE_VALUES constant as defined in [constants.py](constants.py)).|
|The player must be able to upgrade turrets which would boost their stats|Using the upgrade() method defined in the parent turret class (in [turrets.py](/models/turrets.py)) through inheritance I was able to allow for the child classes to be able to upgrade their stats based on an upgrade list of dictionaries.|
|Killing monsters and finishing waves should give the player an income which can be used to buy or upgrade turrets|Using the money attribute of the world class (defined in [world.py](/models/world.py)) I was able to edit this value in other class' methods such as the enemy's __checkAlive() method (defined in [enemies.py](models/enemies.py)) which adds the killed enemy's worth to the world object's money attribute. This money is then subtracted if there is sufficent amounts for buying or upgrading a turret|
|There must be a variety of turrets with differnt upgrades and attributes| Similar to the differnt enemies I was able to use the parent turret class (as defined in [turrets.py](models/turrets.py)) to create two child classes: Cannon and Machine laser. These two turrets are very unique in their attributes each benifitial for differnt situations as specified in [Weapons](#weapons)|
|There must be multiple levels with different maps and increasing difficulty which also introduce new enemies and turrets.| Currently I have only implemented two levels however these levels are vastly differnt in difficulty and level 2 introduces a new turret and a new monster as specified in [Turret and Monster Guide](#turret-and-monster-guide)|
|The player must be given a score apon winning| I implemeted a simple score calculation in [gameStates.py](models/gameStates.py) which gives a player a score based on the speed of level compleation and how much health their base has left and only if they have sucessfully beat the level. This score is not saved yet however in future I do plan on expanding on and using this score for further uses|

## REQUIREMENTS
- pygame version ≥ 2.5.2 | install using _pip install pygame_
- python version ≥ 3.11
- ensure all files are in correct directory as shown in [Files](#files)

## Files
[README.md](README.md)

[\_\_main\_\_.py](__main__.py)

[constants.py](constants.py)

[gitupdate.sh](gitupdate.sh)

[otherFunctions.py](otherFunctions.py)

[unitTesting.](unitTesting.py)

### ./Deliverables:
- [Class Diagram.png](Deliverables/Class%20Diagram.png)

- [Deliverable 1- Project Proposal & Requirements Specification by Ryan Beikrasouli.docx](Deliverables/Deliverable%201-%20Project%20Proposal%20&%20Requirements%20Specification%20by%20Ryan%20Beikrasouli.docx)

- [Deliverable 1- Project Proposal & Requirements Specification by Ryan Beikrasouli.pdf](Deliverables/Deliverable%201-%20Project%20Proposal%20&%20Requirements%20Specification%20by%20Ryan%20Beikrasouli.pdf)

- [Deliverable 2- Detailed Project Design Document by Ryan Beikrasouli.docx](Deliverables/Deliverable%202-%20Detailed%20Project%20Design%20Document%20by%20Ryan%20Beikrasouli.docx)

- [Deliverable 2- Detailed Project Design Document by Ryan Beikrasouli.pdf](Deliverables/Deliverable%202-%20Detailed%20Project%20Design%20Document%20by%20Ryan%20Beikrasouli.pdf)

- [Deliverable 3 - Initial Prototype - Development Milestone by Ryan Beikrasouli.docx](Deliverables/Deliverable%203%20-%20Initial%20Prototype%20-%20Development%20Milestone%20by%20Ryan%20Beikrasouli.docx)

- [Flow Chart.docx](Deliverables/Flow%20Chart.docx)

- [~$liverable 1- Project Proposal & Requirements Specification by Ryan Beikrasouli.docx](Deliverables/~$liverable%201-%20Project%20Proposal%20&%20Requirements%20Specification%20by%20Ryan%20Beikrasouli.docx)

- [~$liverable 2- Detailed Project Design Document by Ryan Beikrasouli .docx](Deliverables/~$liverable%202-%20Detailed%20Project%20Design%20Document%20by%20Ryan%20Beikrasouli%20.docx)

### ./Sound Assets:
- [gun_shot.wav](Sound%20Assets/gun_shot.wav)

- [laser_shot.wav](Sound%20Assets/laser_shot.wav)

- [loss_theme.mp3](Sound%20Assets/loss_theme.mp3)

- [main_theme.mp3](Sound%20Assets/main_theme.mp3)

- [upgrade_sound.wav](Sound%20Assets/upgrade_sound.wav)

- [victory_theme.mp3](Sound%20Assets/victory_theme.mp3)

### ./models:
- [\_\_init\_\_.py](models/__init__.py)

- [buttons.py](models/buttons.py)

- [enemies.py](models/enemies.py)

- [gameStates.py](models/gameStates.py)

- [turrets.py](models/turrets.py)

- [world.py](models/world.py)

### ./sprite images:
- [Adobe Express - file (1) copy.png](sprite%20images/Adobe%20Express%20-%20file%20(1)%20copy.png)
- [Map 1.tiled-project](sprite%20images/Map%201.tiled-project)
- [Map 1.tiled-session](sprite%20images/Map%201.tiled-session)
- [hp_bar.png](sprite%20images/hp_bar.png)
- [levels_button_off.png](sprite%20images/levels_button_off.png)
- [levels_button_on.png](sprite%20images/levels_button_on.png)
- [login_button_off.png](sprite%20images/login_button_off.png)
- [login_button_on.png](sprite%20images/login_button_on.png)
- [main_logo.png](sprite%20images/main_logo.png)
- [main_logo2.png](sprite%20images/main_logo2.png)
- [map1.json](sprite%20images/map1.json)
- [map1.png](sprite%20images/map1.png)
- [map2.json](sprite%20images/map2.json)
- [map2.png](sprite%20images/map2.png)
- [map2.tmx](sprite%20images/map2.tmx)
- [pause_button.png](sprite%20images/pause_button.png)
- [quit_button_off.png](sprite%20images/quit_button_off.png)
- [quit_button_on.png](sprite%20images/quit_button_on.png)

#### ./sprite images/Default Assets:
- [default_sprite 1.png](sprite%20images/Default%20Assets/default_sprite%201.png)
- [default_sprite 2.png](sprite%20images/Default%20Assets/default_sprite%202.png)
- [default_sprite 3.png](sprite%20images/Default%20Assets/default_sprite%203.png)
- [default_sprite 4.png](sprite%20images/Default%20Assets/default_sprite%204.png)
- [default_sprite 5.png](sprite%20images/Default%20Assets/default_sprite%205.png)
- [default_sprite 6.png](sprite%20images/Default%20Assets/default_sprite%206.png)

#### ./sprite images/Skeleton Assets:
- [skeleton 1.png](sprite%20images/Skeleton%20Assets/skeleton%201.png)
- [skeleton 2.png](sprite%20images/Skeleton%20Assets/skeleton%202.png)
- [skeleton 3.png](sprite%20images/Skeleton%20Assets/skeleton%203.png)
- [skeleton 4.png](sprite%20images/Skeleton%20Assets/skeleton%204.png)

#### ./sprite images/Turret Assets:
- [cannon_tier_1.png](sprite%20images/Turret%20Assets/cannon_tier_1.png)
- [cannon_tier_2.png](sprite%20images/Turret%20Assets/cannon_tier_2.png)
- [cannon_tier_3.png](sprite%20images/Turret%20Assets/cannon_tier_3.png)
- [cannon_tier_4.png](sprite%20images/Turret%20Assets/cannon_tier_4.png)
- [machine_laser_tier_1.png](sprite%20images/Turret%20Assets/machine_laser_tier_1.png)
- [machine_laser_tier_2.png](sprite%20images/Turret%20Assets/machine_laser_tier_2.png)
- [machine_laser_tier_3.png](sprite%20images/Turret%20Assets/machine_laser_tier_3.png)
- [machine_laser_tier_4.png](sprite%20images/Turret%20Assets/machine_laser_tier_4.png)

#### ./sprite images/Zombie Assets:
- [zombie 1.png](sprite%20images/Zombie%20Assets/zombie%201.png)
- [zombie 2.png](sprite%20images/Zombie%20Assets/zombie%202.png)
- [zombie 3.png](sprite%20images/Zombie%20Assets/zombie%203.png)
- [zombie 4.png](sprite%20images/Zombie%20Assets/zombie%204.png)
- [zombie 5.png](sprite%20images/Zombie%20Assets/zombie%205.png)
- [zombie 6.png](sprite%20images/Zombie%20Assets/zombie%206.png)
- [zombie 7.png](sprite%20images/Zombie%20Assets/zombie%207.png)
- [zombie 8.png](sprite%20images/Zombie%20Assets/zombie%208.png)
- [zombie 9.png](sprite%20images/Zombie%20Assets/zombie%209.png)

### ./utilities:
- [\_\_init\_\_.py](utilities/__init__.py)
- [buttonUtilities.py](utilities/buttonUtilities.py)
- [gameStateManager.py](utilities/gameStateManager.py)
- [mainUtilities.py](utilities/mainUtilities.py)

## HOW TO PLAY:
- Ensure all [requirements](#requirements) are installed properly
### OPTION 1:
1. Go to your terminal
2. Change directory to directory with Missile Mayhem folder using: _cd [path to directory holding TowerDefence folder]_
3. Run: _python3 TowerDefence_

### OPTION2:
1. Go to your terminal
2. Change directory to directory with Missile Mayhem folder using: _cd [path to TowerDefence folder]_
3. Run: _python3 \_\_main\_\_.py_

## CONTROLS:
This game is entirely mouse controlled meaning you need to use your mouse and left click button to click on buttons which allows you to conduct actions such as buying turrets, placing turrets, upgrading turrets and selecting your level just to name a few.

## TURRET AND MONSTER GUIDE
Currently in the game there are two levels, two different turrets and two different monsters.

### Monsters
- #### Zombies
    The Zombie is the first monster you will encounter in level 1. This horrifying creature has high health, and deals vast amounts of damage to your base if they are allowed to reach the end of the path. However they do have very slow moment speed as they are decaying bodies after all. 

- #### Skeletons 
    The Second and last monster you will have to face in this game first appears in the second level. These walking piles of bones are small and fragile but have extreme speeds and will fly past weapons with longer cool downs such as the [cannon]()

### Weapons
- #### Cannons
    The first weapon you will have access to in the first level is the trust worthy cannon. The cannon packs a powerful but slow reloading shot which only becomes stronger and faster as it is upgraded which makes it the prime counter to those beefy slow moving [Zombies](#zombies). However the cannon is weak against the fast moving [Skeletons](#skeletons) who just zoom past before the cannon can reload a second shot.

- #### Machine Lasers
    The last weapon you will unlock in the second level of the game is the machine laser. As the name suggests this futuristic weapon is a laser machine gun with a high fire rate but far less damage than the [Cannon](#cannons) making it the perfecr counter to those pesky fast pace [Skeletons](#skeletons) but weak against those beefy slow moving carcases ([Zombies](#zombies))


## Credits

Tiles: https://www.kenney.nl/assets/tower-defense-top-down

Turrets: https://zintoki.itch.io/ground-shaker

Zombie: https://www.freepik.com/premium-vector/zombie-boy-game-sprites_3674450.htm

Skeleton: https://caz-creates-games.itch.io/skeleton

Cannon sfx: https://pixabay.com/sound-effects/search/gun/

Machinelaser sfx: https://pixabay.com/sound-effects/search/laser%20machinegun/

Upgrade sfx: https://pixabay.com/sound-effects/search/mechanical%20upgrade/

Main/victory/loss themesong: https://suno.com (AI)

Button frames: https://www.vectorstock.com/

## Log of Challenges Faced:
- Getting path data from tile:
    - Issue: Incorrect name used
    - Solution: changed the correct "name" value to "waypoints" in .json file

- Fixing enemy Rotation:
    - Issue: Rotating enemy Y and at wrong times
    - Solution: Rotating only Enemy X and at certain anges so enemy's feet stay pointing to bottom of screen

- Adding text crashing game:
    - Issue: Font not initilised
    - Solution: moved _pygame.init()_ and _pygame.mixer.init()_ to before importing GameStateManager in _\_\_main\_\_.py_

## Developer Retrospective
Overall this programming project was both very fun to develop but also taught me many lessons which I can use in my future developments of different projects. The main thing that worked well in this project was my implementation of proper Object Oriented Programming which through the use of abstraction, inheritance and polymorphism I was able to not only create a very clean and well structured program, but also an easily maintainable and scaleable program. This was very important and useful as I quickly learned when it came to implementing more turrets, weapons and a second level, the process of creating new classes or scaling the number of levels was very simple and easy thanks to the Object Oriented Programming which I was taught and was able to effectively implement. However this project did come with its fair share of challenges. Some of these I have specified in [Challenges Faced](#log-of-challenges-faced) however the key challenges came with me learning how to correctly use the Object Oriented Programming principles without causing any logic or runtime errors. Throughout the development of this project I have learned many lessons, from how to create a tiled map using the Tiled application, to using vectors for path following and even the really core practices of how to properly develop code which implements the Object Oriented Programming principles allowing for a beautiful, clean, maintainable and scalable program. Nevertheless I am very pleased with what my game has become and despite being small; with only two levels, two monsters and two differnt turrets, I am very proud of what I was able to develop and I do truely believe I have effectively implemented all of my project requirement outlines (as specified in [Project Requirements & Implementation](#project-requirements--implementation)) and even more. I ensured to abide by ethical and legal conciderations when creating my program by ensuring to credit any assets used (as shown in [Credits](#credits)) to ensure I am not violating any copyright laws. Also by not directly copying any other developers code or using AI for my actual programming I was able to ensure that I was not infringing on any intellectual property protected by copyright laws while also allowing for my own program to be protected by copyright laws as in Australia (the contry of creation) copyright laws will apply upon the moment of creation of the intellectual property.

## Final Notes:

Please note that the _LOGIN_ button does not work and is only there as a placeholder for the time being

I do not claim ownership of any of the images or audios attached to this game. Many of them are AI generated or taking from the internet as referanced in [Credits](#credits).

I would also like to give many thanks to my computer science teacher Mr Sullivan. Many of the skills and proper programming practices I have learned during the development of this program (such as Object Oriented Programming) can be attributed to his teachings so he certainly deservse credit for providing me with the tools I required to develop this game.

Tower Defence Mayhem is protected by copywrite laws and any infrindgement will face consequences.

