from app.config.config import KNIGHTS
from app.knights.battle_preparation import Knight
from app.knights.battle import fight


def battle(knights_config: dict) -> dict:
    lancelot = Knight(
        name=knights_config.get("lancelot").get("name").lower(),
        power=knights_config.get("lancelot").get("power"),
        hp=knights_config.get("lancelot").get("hp"),
        armour=knights_config.get("lancelot").get("armour"),
        weapon=knights_config.get("lancelot").get("weapon"),
        potion=knights_config.get("lancelot").get("potion"),
        protection=sum(
            [protect.get("protection")
             for protect in knights_config.get("lancelot").get("armour")]
        )
    )

    arthur = Knight(
        name=knights_config.get("arthur").get("name").lower(),
        power=knights_config.get("arthur").get("power"),
        hp=knights_config.get("arthur").get("hp"),
        armour=knights_config.get("arthur").get("armour"),
        weapon=knights_config.get("arthur").get("weapon"),
        potion=knights_config.get("arthur").get("potion"),
        protection=sum(
            [protect.get("protection")
             for protect in knights_config.get("arthur").get("armour")]
        )
    )

    mordred = Knight(
        name=knights_config.get("mordred").get("name").lower(),
        power=knights_config.get("mordred").get("power"),
        hp=knights_config.get("mordred").get("hp"),
        armour=knights_config.get("mordred").get("armour"),
        weapon=knights_config.get("mordred").get("weapon"),
        potion=knights_config.get("mordred").get("potion"),
        protection=sum(
            [protect.get("protection")
             for protect in knights_config.get("mordred").get("armour")]
        )
    )

    red_knight = Knight(
        name=knights_config.get("red_knight").get("name").lower(),
        power=knights_config.get("red_knight").get("power"),
        hp=knights_config.get("red_knight").get("hp"),
        armour=knights_config.get("red_knight").get("armour"),
        weapon=knights_config.get("red_knight").get("weapon"),
        potion=knights_config.get("red_knight").get("potion"),
        protection=sum(
            [protect.get("protection")
             for protect in knights_config.get("red_knight").get("armour")]
        )
    )

    for knight in Knight.instances:
        # apply weapon
        knight.apply_weapon()
        # apply potion if exist
        knight.apply_potion()

    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)

    return {
        knights_config.get("lancelot").get("name"): lancelot.hp,
        knights_config.get("arthur").get("name"): arthur.hp,
        knights_config.get("mordred").get("name"): mordred.hp,
        knights_config.get("red_knight").get("name"): red_knight.hp,
    }


print(battle(KNIGHTS))

