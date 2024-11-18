from app.config.config import KNIGHTS


class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict = None,
                 protection: int = 0
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection


lancelot = Knight(
    name=KNIGHTS.get("lancelot").get("name").lower(),
    power=KNIGHTS.get("lancelot").get("power"),
    hp=KNIGHTS.get("lancelot").get("hp"),
    armour=KNIGHTS.get("lancelot").get("armour"),
    weapon=KNIGHTS.get("lancelot").get("weapon"),
    potion=KNIGHTS.get("lancelot").get("potion"),
    protection=sum(
        [protect.get("protection")
         for protect in KNIGHTS.get("lancelot").get("armour")]
    )
)

arthur = Knight(
    name=KNIGHTS.get("arthur").get("name").lower(),
    power=KNIGHTS.get("arthur").get("power"),
    hp=KNIGHTS.get("arthur").get("hp"),
    armour=KNIGHTS.get("arthur").get("armour"),
    weapon=KNIGHTS.get("arthur").get("weapon"),
    potion=KNIGHTS.get("arthur").get("potion"),
    protection=sum(
        [protect.get("protection")
         for protect in KNIGHTS.get("arthur").get("armour")]
    )
)

mordred = Knight(
    name=KNIGHTS.get("mordred").get("name").lower(),
    power=KNIGHTS.get("mordred").get("power"),
    hp=KNIGHTS.get("mordred").get("hp"),
    armour=KNIGHTS.get("mordred").get("armour"),
    weapon=KNIGHTS.get("mordred").get("weapon"),
    potion=KNIGHTS.get("mordred").get("potion"),
    protection=sum(
        [protect.get("protection")
         for protect in KNIGHTS.get("mordred").get("armour")]
    )
)

red_knight = Knight(
    name=KNIGHTS.get("red_knight").get("name").lower(),
    power=KNIGHTS.get("red_knight").get("power"),
    hp=KNIGHTS.get("red_knight").get("hp"),
    armour=KNIGHTS.get("red_knight").get("armour"),
    weapon=KNIGHTS.get("red_knight").get("weapon"),
    potion=KNIGHTS.get("red_knight").get("potion"),
    protection=sum(
        [protect.get("protection")
         for protect in KNIGHTS.get("red_knight").get("armour")]
    )
)
