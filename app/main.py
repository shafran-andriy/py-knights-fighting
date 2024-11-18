from app.config.config import KNIGHTS
from app.knights.battle_preparation import ApplyWeapon, ApplyPotion
from app.knights.battle import Battle


# apply weapon
ApplyWeapon.apply_weapon()

# apply potion if exist
ApplyPotion.apply_potion()

# # BATTLE:
battle = Battle.battle(KNIGHTS)

print(battle)
