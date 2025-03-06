"""
Utilities for main game generic functions such as displaying text
"""

if __name__ == '__main__':
    print("Error incorrect file run please run __main__.py")
    quit()

try:
    from constants import *
    from otherFunctions import addText
    from world import World
    from turrets import Machinelaser, Cannon
except ModuleNotFoundError as err:
    print(err)
    print("Error missing module please ensure all this games modules are present in their original directory")
    quit()

def displayGameTexts(world:World, selectedTurret:Machinelaser|Cannon|None) -> None:
    """
    function to display game information text on the main game screen
    """

    # Displaying Game Information Texts
    addText("Money: $" + str(world.money), FONT3, (255, 255, 255),SCREEN_WIDTH + 50, SCREEN_HEIGHT - 100)
    addText("HP: " + str(world.health), FONT3, (255, 255, 255),SCREEN_WIDTH + 50, SCREEN_HEIGHT - 80)
    addText("WAVE: " + str(world.wave), FONT3, (255, 255, 255),SCREEN_WIDTH + 50, SCREEN_HEIGHT - 60)
    if selectedTurret:
        addText("Damage: " + str(selectedTurret.damage), FONT3, (255, 255, 255),SCREEN_WIDTH + 15, SCREEN_HEIGHT - 450)
        addText("Range: " + str(selectedTurret.range), FONT3, (255, 255, 255),SCREEN_WIDTH + 15, SCREEN_HEIGHT - 410)
        addText("Cooldown: " + str(selectedTurret.data[selectedTurret.tier - 1].get("cooldown")) + "ms", FONT3, (255, 255, 255), SCREEN_WIDTH + 15, SCREEN_HEIGHT -370)
        addText("Tier: " + str(selectedTurret.tier) + "/4", FONT3, (255, 255, 255),SCREEN_WIDTH + 15, SCREEN_HEIGHT - 330)

        if selectedTurret.tier < 4:
            damageBonus = selectedTurret.data[selectedTurret.tier].get("damage") - selectedTurret.damage
            rangeBonus = selectedTurret.data[selectedTurret.tier].get("range") - selectedTurret.range
            cooldownBonus = selectedTurret.data[selectedTurret.tier - 1].get("cooldown") - selectedTurret.data[selectedTurret.tier].get("cooldown")
            if damageBonus > 0:
                addText("+" + str(damageBonus), FONT3, (144, 238, 144),SCREEN_WIDTH + 175, SCREEN_HEIGHT - 450)
            
            if rangeBonus > 0:
                addText("+" + str(rangeBonus), FONT3, (144, 238, 144),SCREEN_WIDTH + 175, SCREEN_HEIGHT - 410)
            
            if cooldownBonus > 0:
                addText("-" + str(cooldownBonus) + "ms", FONT3, (144, 238, 144), SCREEN_WIDTH + 215, SCREEN_HEIGHT -370)