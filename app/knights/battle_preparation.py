from __future__ import annotations


class Knight:
    instances = []

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
        Knight.instances.append(self)

    def apply_weapon(self) -> None:
        self.power += self.weapon.get("power")

    def apply_potion(self) -> None:
        # apply potion if exist
        if self.potion is not None:
            if "power" in self.potion.get("effect").keys():
                self.power += (self.potion.get("effect")
                               .get("power"))
            if "protection" in self.potion.get("effect").keys():
                self.protection += (self.potion.get("effect")
                                    .get("protection"))
            if "hp" in self.potion.get("effect").keys():
                self.hp = (self.hp + self.potion.get("effect")
                           .get("hp"))
