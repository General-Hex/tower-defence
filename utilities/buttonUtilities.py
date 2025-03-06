import pygame
from buttons import Button
from world import World
from turrets import Cannon, Machinelaser
from constants import *

if __name__ == '__main__':
    print("Error incorrect file run please run __main__.py")
    quit()

def buttonSetup(doubleSpeed:bool, levelStarted:bool, placingTurrets:bool, world:World, demoCannon:Cannon, demoMachinelaser:Machinelaser, turretType:str|None, selectedTurret:Cannon|Machinelaser|None) -> bool:
    if doubleSpeed:
        speedButton.MouseCheck(SCREEN, newText="1x Speed")
    else:
        speedButton.MouseCheck(SCREEN, newText="2x Speed")

    # Updating Buy Turret Buttons
    if world.money >= demoCannon.cost:
        buyCannonButton.MouseCheck(SCREEN)
    else:
        buyCannonButton.MouseCheck(SCREEN, True, (220, 220, 220))
        if turretType == "cannon":
            placingTurrets = False

    if world.money >= demoMachinelaser.cost:
        buyMachinelaserButton.MouseCheck(SCREEN)
    else:
        buyMachinelaserButton.MouseCheck(SCREEN, True, (220, 220, 220))
        if turretType == "machinelaser":
            placingTurrets = False

    # Updating Cancel Button
    if placingTurrets:
        cancelButton.MouseCheck(SCREEN)
    else:
        cancelButton.active = False
    
    # Updating Start Button
    if not levelStarted:
        startButton.MouseCheck(SCREEN)
    else:
        startButton.active = False

    # Updating Upgrade Button
    if selectedTurret and selectedTurret.tier < len(TURRET_DATA):
        upgradeButton.MouseCheck(SCREEN, not (world.money >= selectedTurret.upgradeCost), (200, 200, 200), "Upgrade: $" + str(selectedTurret.upgradeCost))
    else:
        upgradeButton.active = False

    return placingTurrets

def checkButtons(world:World, cursorTurret:Cannon|Machinelaser|None, selectedTurret:Cannon|Machinelaser|None, placingTurrets:bool, levelStarted:bool, doubleSpeed:bool, turretType:str|None) -> list:
    # Checking Buttons
    if cancelButton.MouseClick():
        placingTurrets = False
        
    if buyCannonButton.MouseClick():
        placingTurrets = True
        cursorTurret = Cannon(0, 0)
        turretType = "cannon"
    
    elif buyMachinelaserButton.MouseClick():
        placingTurrets = True
        cursorTurret = Machinelaser(0, 0)
        turretType = "machinelaser"
    
    if selectedTurret:
        if upgradeButton.MouseClick() and world.money >= selectedTurret.upgradeCost: 
            selectedTurret.upgrade()
            world.money -= selectedTurret.upgradeCost
    
    if startButton.MouseClick():
        levelStarted = True
    
    if speedButton.MouseClick():
        doubleSpeed = not doubleSpeed
    
    return [placingTurrets, cursorTurret, turretType, levelStarted, doubleSpeed]