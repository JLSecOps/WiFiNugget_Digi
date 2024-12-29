# Core AI behavior and evolution logic
## ai_logic.py
```python
class AILogic:
    def __init__(self):
        self.stage = "egg"
        self.xp = 0
        self.level = 1

    def evolve(self):
        stages = ["egg", "rookie", "champion", "ultimate"]
        if self.xp >= self.level * 10:
            self.level += 1
            self.stage = stages[min(self.level - 1, len(stages) - 1)]
            print(f"AI evolved to {self.stage} stage!")

    def gain_xp(self, amount):
        self.xp += amount
        self.evolve()
```
