# XP management system
class XPManager:
    def __init__(self):
        self.xp = 0
        self.level = 1
        self.milestones = [10, 50, 100, 200]

    def add_xp(self, amount):
        self.xp += amount
        self.check_level_up()

    def check_level_up(self):
        if self.level < len(self.milestones) and self.xp >= self.milestones[self.level - 1]:
            self.level += 1
            print(f"Level up! New level: {self.level}")
