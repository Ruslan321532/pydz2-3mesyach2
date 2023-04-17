from random import *
from enum import Enum

round_number = 0


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4
    ABSORB_DAMAGE = 5
    STUN = 6
    PROTECTION = 7
    REVIVE = 8
    INVIS = 9


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.health} damage: {self.damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        GameEntity.__init__(self, name, health, damage)
        self.__defence = None

    @property
    def defense(self):
        return self.__defence

    @defense.setter
    def defense(self, value):
        self.__defence = value

    def hit(self, heroes):
        is_golem_alive = False
        for hero in heroes:
            if hero.health > 0:
                if hero.super_ability == SuperAbility.ABSORB_DAMAGE:
                    is_golem_alive = True
                if hero.super_ability == SuperAbility.SAVE_DAMAGE_AND_REVERT:
                    hero.saved_damage = self.damage
                hero.health -= self.damage

    def choose_defence(self, heroes):
        chosen_hero = choice(heroes)
        self.__defence = chosen_hero.super_ability

    def __str__(self):
        return f'BOSS {self.name} health: {self.health} damage: {self.damage} defence: {self.defense}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        GameEntity.__init__(self, name, health, damage)
        if not isinstance(super_ability, SuperAbility):
            self.__super_ability = None
            raise AttributeError('Wrong data type for super_ability')
        else:
            self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def hit(self, boss):
        if boss.health > 0 and self.health > 0:
            boss.health -= self.damage

    def apply_super_ability(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_ability(self, boss, heroes):
        coefficient = randint(2, 6)
        boss.health -= self.damage * coefficient
        print(f'{self.name} Critted boss by {coefficient * self.damage}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        Hero.__init__(self, name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points
        print(f'{self.name} healed all by {self.__heal_points}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.BOOST)

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.damage = hero.damage + 2
        print(f'{self.name} applied damage buff')


class Berserk(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage,
                      SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    @property
    def saved_damage(self):
        return self.__saved_damage

    @saved_damage.setter
    def saved_damage(self, value):
        self.__saved_damage = value

    def apply_super_ability(self, boss, heroes):
        if boss.health > 0:
            reverted_damage = self.saved_damage // randint(3, 5)
            boss.health = max(0, boss.health - reverted_damage)
            print(f'Berserk {self.name} hitted boss by {reverted_damage}')
            self.saved_damage = 0


class Thor(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.STUN)

    def apply_super_ability(self, boss, heroes):
        chance = randint(1, 8)
        if chance == 1:
            for hero in heroes:
                hero.health += boss.damage
            print(f'{self.name} stunned BOSS')


class Golem(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.PROTECTION)

    def apply_super_ability(self, boss, heroes):
        if self.health > 0:
            protection = boss.damage // 5
            sum_prot = 0
            for hero in heroes:
                if hero.health > 0 and self != hero:
                    hero.health += protection
                    sum_prot += protection
                    self.health -= protection
                if self.health < 0:
                    self.health = 0

            print(f'{self.name} protected {sum_prot} damage')


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.REVIVE)

    def apply_super_ability(self, boss, heroes):
        if self.health > 0:
            for hero in heroes:
                if hero.health <= 0:
                    hero.health = self.health
                    self.health = 0
                    print(f'{self.name} revived {hero.name}')


class Avrora(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.INVIS)
        self.rounds_remaining = 2
        self.absorbed_damage = 0

    def apply_super_ability(self, boss, heroes):
        if self.rounds_remaining > 0:
            self.absorbed_damage += boss.damage
            self.health += boss.damage
            self.rounds_remaining -= 1
            if self.rounds_remaining == 0:
                boss.health -= self.absorbed_damage
                self.absorbed_damage = 0


def print_statistics(boss, heroes):
    global round_number
    print(f'ROUND {round_number} (◕‿◕)')
    print(boss)
    for hero in heroes:
        print(hero)
    print("٩(｡•́‿•̀｡)۶")


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        hero.health = max(0, hero.health)
        if boss.defense != hero.super_ability and hero.health > 0:
            if type(Hero) == Witcher:
                hero.damage = 0
            hero.hit(boss)
            hero.apply_super_ability(boss, heroes)
    boss.health = max(0, boss.health)
    print_statistics(boss, heroes)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes Won!!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss Won!!!')
    return all_heroes_dead


def start():
    boss = Boss('Drogon', 1900, 50)
    golem = Golem('Rock', 450, 0)
    witcher = Witcher('Vanda', 340, 0)
    warrior = Warrior('Ahiles', 280, 10)
    magic = Magic('Strange', 260, 15)
    berserk = Berserk('Berserk', 270, 15)
    doc = Medic('Aibolit', 250, 5, 15)
    thor = Thor('Thor', 300, 15)
    avrora = Avrora('Avrora', 240, 10)
    heroes_list = [witcher, golem, warrior, doc, thor, avrora, magic, berserk]
    print_statistics(boss, heroes_list)
    while not is_game_finished(boss, heroes_list):
        play_round(boss, heroes_list)


start()
