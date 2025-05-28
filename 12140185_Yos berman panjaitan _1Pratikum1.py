import random

class Robot:
    def __init__(self, name, hp, attack, accuracy):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.accuracy = accuracy
        self.defending = False

    def is_alive(self):
        return self.hp > 0

    def attack_enemy(self, enemy):
        if random.random() < self.accuracy:
            damage = self.attack // 2 if enemy.defending else self.attack
            enemy.hp = max(0, enemy.hp - damage)
            print(f"{self.name} menyerang {enemy.name} dan memberikan {damage} damage!")
        else:
            print(f"{self.name} gagal menyerang {enemy.name}.")

    def regen_health(self):
        heal = random.randint(5, 15)
        self.hp += heal
        print(f"{self.name} bertahan dan memulihkan {heal} HP!")

    def giveup(self):
        self.hp = 0
        print(f"{self.name} menyerah!")


class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1

    def display_status(self):
        print(f"\nRound-{self.round} " + "=" * 60)
        print(f"{self.robot1.name} [{self.robot1.hp}|{self.robot1.attack}]")
        print(f"{self.robot2.name} [{self.robot2.hp}|{self.robot2.attack}]\n")

    def choose_action(self, robot):
        print("1. Attack     2. Defense     3. Giveup")
        while True:
            try:
                choice = int(input(f"{robot.name}, pilih aksi: "))
                if choice in [1, 2, 3]:
                    return choice
            except ValueError:
                pass
            print("Pilihan tidak valid, coba lagi.")

    def play(self):
        while self.robot1.is_alive() and self.robot2.is_alive():
            self.display_status()
            r1_action = self.choose_action(self.robot1)
            r2_action = self.choose_action(self.robot2)

            # Reset defending state
            self.robot1.defending = False
            self.robot2.defending = False

            # Apply actions
            if r1_action == 3:
                self.robot1.giveup()
            elif r1_action == 2:
                self.robot1.defending = True
                self.robot1.regen_health()
            elif r1_action == 1:
                pass  # will attack later

            if r2_action == 3:
                self.robot2.giveup()
            elif r2_action == 2:
                self.robot2.defending = True
                self.robot2.regen_health()
            elif r2_action == 1:
                pass

            # Attack after both decisions
            if r1_action == 1 and self.robot1.is_alive():
                self.robot1.attack_enemy(self.robot2)

            if r2_action == 1 and self.robot2.is_alive():
                self.robot2.attack_enemy(self.robot1)

            self.round += 1

        winner = self.robot1.name if self.robot1.is_alive() else self.robot2.name
        print(f"\n{winner} menang!")

# Contoh permainan
robot_a = Robot("Atreus", 500, 10, 0.9)
robot_b = Robot("Daedalus", 750, 8, 0.8)

game = Game(robot_a, robot_b)
game.play()
