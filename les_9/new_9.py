"""герой наносит урон скилету """

class Skeleton:
    hp = 20

    def was_attacked(self, damage: int):
        print(f"Skeleton was attacked. Hp = {self.hp}, damage = {damage}")
        self.hp = self.hp - damage
        if self.hp <= 0:
            self.died()

    def died(self):
        print("Skelet died!")


class Hero:
    hp = 100
    force = 50

    def attack(self, enemy: Skeleton):
        enemy.was_attacked(damage=self.force)


def main():
    hero = Hero()
    skeleton = Skeleton()
    print("=========================Hero vs Skeleton====================")
    hero.attack(skeleton)
    skeleton_list = []
    for _ in range(10):
        tmp_skelet = Skeleton()
        skeleton_list.append(tmp_skelet)

    for enemy in skeleton_list:
        hero.attack(enemy)




if __name__ == '__main__':
    main()