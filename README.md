# TOWER DEFENSE MAYHEM ©
## By Ryan Beikrasouli
#### ID: 6137 | 31698082
#### Year of creation: 2025

## REQUIREMENTS
- pygame version ≥ 2.5.2
- python version ≥ 3.11

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

## Final Notes:

Please note that the _LOGIN_ button does not work and is only there as a placeholder for the time being

I do not claim ownership of any of the images or audios attached to this game. Many of them are AI generated or taking from the internet in [Credits](#credits).

Tower Defence Mayhem is protected by copywrite laws and any infrindgement will face consequences.

