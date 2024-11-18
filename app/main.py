from app.config.config import KNIGHTS
from app.knights.battle_preparation import ApplyWeapon, ApplyPotion
from app.knights.knights import lancelot, mordred, arthur, red_knight
# from app.knights.battle import Battle


def battle(knights_config: dict) -> dict:
    # apply weapon
    ApplyWeapon.apply_weapon()

    # apply potion if exist
    ApplyPotion.apply_potion()

    # 1 Lancelot vs Mordred:
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    # check if someone fell in battle
    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    # Return battle results:
    return {
        lancelot.name.title(): lancelot.hp,
        arthur.name.title(): arthur.hp,
        mordred.name.title(): mordred.hp,
        red_knight.name.title(): red_knight.hp,
    }


print(battle(KNIGHTS))
