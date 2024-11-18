from app.config.config import KNIGHTS
from app.knights.knights import lancelot, mordred, arthur, red_knight


class ApplyWeapon:
    @staticmethod
    def apply_weapon() -> None:
        lancelot.power += KNIGHTS.get("lancelot").get("weapon").get("power")
        arthur.power += KNIGHTS.get("arthur").get("weapon").get("power")
        mordred.power += KNIGHTS.get("mordred").get("weapon").get("power")
        red_knight.power += (KNIGHTS.get("red_knight")
                             .get("weapon").get("power"))


class ApplyPotion:
    @staticmethod
    def apply_potion() -> None:
        # apply potion if exist
        for knight in [lancelot, arthur, mordred, red_knight]:
            if knight.potion is not None:
                if knight.power in knight.potion.get("effect"):
                    knight.power += (knight.potion.get("effect")
                                     .get("power"))
                if knight.protection in knight.potion.get("effect"):
                    knight.protection += (knight.potion.
                                          get("effect").get("protection"))
                if knight.hp in knight.potion.get("effect"):
                    knight.hp += knight.potion.get("effect").get("hp")
