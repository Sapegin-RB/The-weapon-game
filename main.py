# Импортируем библиотеки для создания абстрактных классов
from abc import ABC, abstractmethod


# Шаг 1: Создаем абстрактный класс для оружия
# Принцип открытости/закрытости начинается с того, что мы определяем интерфейс, который можно расширять,
# но не изменять. Все новое оружие будет расширять этот класс, добавляя свои уникальные атаки.

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        """Абстрактный метод, который должны реализовать все конкретные виды оружия"""
        pass


# Шаг 2: Реализуем конкретные типы оружия
# Каждое оружие должно реализовать метод attack() по-своему.

class Sword(Weapon):
    def attack(self):
        """Реализация атаки мечом"""
        return "Боец наносит удар мечом."


class Bow(Weapon):
    def attack(self):
        """Реализация атаки луком"""
        return "Боец стреляет из лука."


# Шаг 3: Модифицируем класс Fighter
# Теперь боец будет иметь возможность использовать разные виды оружия.

class Fighter:
    def __init__(self, name, weapon: Weapon):
        """Инициализация бойца с выбранным оружием"""
        self.name = name
        self.weapon = weapon

    def change_weapon(self, new_weapon: Weapon):
        """Метод для смены оружия бойца"""
        self.weapon = new_weapon

    def attack(self):
        """Боец атакует, используя текущее оружие"""
        return self.weapon.attack()


# Шаг 4: Реализуем бой
# Опишем монстра и логику битвы между бойцом и монстром.

class Monster:
    def __init__(self, health):
        """Инициализация монстра с определенным количеством здоровья"""
        self.health = health

    def take_damage(self, damage):
        """Метод получения урона монстром"""
        self.health -= damage
        if self.health <= 0:
            return "Монстр побежден!"
        else:
            return f"У монстра осталось {self.health} здоровья."


# Пример демонстрации
if __name__ == "__main__":
    # Создаем бойца с мечом
    fighter = Fighter(name="Воин", weapon=Sword())
    # Создаем монстра с 10 единицами здоровья
    monster = Monster(health=10)

    # Вывод атаки мечом
    print(fighter.attack())  # "Боец наносит удар мечом."
    print(monster.take_damage(10))  # "Монстр побежден!"

    # Меняем оружие на лук
    fighter.change_weapon(Bow())

    # Новый бой с другим монстром
    new_monster = Monster(health=5)
    print(fighter.attack())  # "Боец стреляет из лука."
    print(new_monster.take_damage(5))  # "Монстр побежден!"
