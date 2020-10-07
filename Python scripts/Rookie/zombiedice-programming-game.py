import zombiedice, random

#zombiedice.demo()

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class RandomBrainZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None and random.randint(0, 1) == 0:
            brains += diceRollResults['brains']
            diceRollResults = zombiedice.roll() # roll again

class CautiousZombie:
    def __init__(self, name, shotguns):
        self.name = name
        self.minShotgun=shotguns
    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            if shotguns < self.minShotgun:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class DicesCautiousZombie:
  def __init__(self, name,shotguns):
        self.name = name
        self.minShotgun=shotguns
        
  def turn(self, gameState): 

    diceRollResults = zombiedice.roll() # first roll
    # roll() returns a dictionary with keys 'brains', 'shotgun', and
    # 'footsteps' with how many rolls of each type there were.
    # The 'rolls' key is a list of (color, icon) tuples with the
    # exact roll result information.
    # Example of a roll() return value:
    # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
    #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
    #            ('green', 'shotgun')]}

    # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
    shotguns = 0
    diceCount=0
    maxRolls=random.randint(1,4)
    while diceRollResults is not None and diceCount <= maxRolls:
        shotguns += diceRollResults['shotgun']

        if shotguns < self.minShotgun:
            diceCount+=1
            diceRollResults = zombiedice.roll() # roll again
        else:
            break

class OverlyCautiousZombie:
    def __init__(self, name):
        self.name = name
        
    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        while diceRollResults is not None:
            if  diceRollResults['shotgun'] < diceRollResults['brains'] :
                diceRollResults = zombiedice.roll() # roll again
            else:
                break




zombies = (
    #zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    # Add any other zombie players here.
    MyZombie(name='2 brains hunter'),
    RandomBrainZombie(name="Randy Dice the Zombie"),
    CautiousZombie(name="2 shotguns then back off",shotguns=2),
    DicesCautiousZombie(name="Count rolls then Bites",shotguns=2),
    OverlyCautiousZombie(name="Love brains, hate shotguns")
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=100)
# zombiedice.runWebGui(zombies=zombies, numGames=1000)
