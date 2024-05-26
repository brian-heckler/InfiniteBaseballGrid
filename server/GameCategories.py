import random
import BaseballData

class GameCategories:
    choices_colors = [
        ("ms ms-c ms-5x ms-cost ms-shadow", "Colorless", "Card is at least these colors (not including including color identity)"),
	    ("ms ms-b ms-5x ms-cost ms-shadow", "Black", "Card is at least these colors (not including color identity)"),
        ("ms ms-w ms-5x ms-cost ms-shadow", "White", "Card is at least these colors (not including color identity)"),
        ("ms ms-u ms-5x ms-cost ms-shadow", "Blue", "Card is at least these colors (not including color identity)"),
        ("ms ms-r ms-5x ms-cost ms-shadow", "Red", "Card is at least these colors (not including color identity)"),
        ("ms ms-g ms-5x ms-cost ms-shadow", "Green", "Card is at least these colors (not including color identity)"),
        ("ms ms-wu ms-5x ms-cost ms-shadow", "Azorius", "Card is at least these colors (not including color identity)"),
        ("ms ms-wb ms-5x ms-cost ms-shadow", "Orzhov", "Card is at least these colors (not including color identity)"),
        ("ms ms-rw ms-5x ms-cost ms-shadow", "Boros", "Card is at least these colors (not including color identity)"),
        ("ms ms-gw ms-5x ms-cost ms-shadow", "Selesnya", "Card is at least these colors (not including color identity)"),   
        ("ms ms-ub ms-5x ms-cost ms-shadow", "Dimir", "Card is at least these colors (not including color identity)"),
        ("ms ms-ur ms-5x ms-cost ms-shadow", "Izzet", "Card is at least these colors (not including color identity)"),
        ("ms ms-gu ms-5x ms-cost ms-shadow", "Simic", "Card is at least these colors (not including color identity)"),
        ("ms ms-br ms-5x ms-cost ms-shadow", "Rakdos", "Card is at least these colors (not including color identity)"),
        ("ms ms-bg ms-5x ms-cost ms-shadow", "Golgari", "Card is at least these colors (not including color identity)"),
        ("ms ms-rg ms-5x ms-cost ms-shadow", "Gruul", "Card is at least these colors (not including color identity)"),
    ]

    choices_sets = [
        ("ss ss-isd ss-rare ss-grad ss-5x", "Innistrad", "Card was printed in this set, reprints included"),
        ("ss ss-war ss-rare ss-grad ss-5x", "War of the Spark", "Card was printed in this set, reprints included"),
        ("ss ss-one ss-rare ss-grad ss-5x", "Phyrexia: All Will Be One", "Card was printed in this set, reprints included"),
        ("ss ss-woe ss-rare ss-grad ss-5x", "Wilds of Eldraine", "Card was printed in this set, reprints included"),
        ("ss ss-rav ss-rare ss-grad ss-5x", "Ravnica: City of Guilds", "Card was printed in this set, reprints included"),
        ("ss ss-rix ss-rare ss-grad ss-5x", "Rivals of Ixalan", "Card was printed in this set, reprints included"),
        ("ss ss-dmu ss-rare ss-grad ss-5x", "Dominaria United", "Card was printed in this set, reprints included"),
        ("ss ss-lrw ss-rare ss-grad ss-5x", "Lorwyn", "Card was printed in this set, reprints included"),
    ]

    choices_name = [
        ("ms ms-ability-adventure ms-mechanic ms-5x", "Starts with 'S'", "First letter excluding 'A' and 'The'"),
        ("ms ms-ability-adventure ms-mechanic ms-5x", "Starts with 'T'", "First letter excluding 'A' and 'The'"),
        ("ms ms-ability-adventure ms-mechanic ms-5x", "Starts with 'R'", "First letter excluding 'A' and 'The'"),
        ("ms ms-ability-adventure ms-mechanic ms-5x", "Starts with 'L'", "First letter excluding 'A' and 'The'"),
        ("ms ms-ability-adventure ms-mechanic ms-5x", "Starts with 'M'", "First letter excluding 'A' and 'The'"),
        ("ms ms-ability-adventure ms-mechanic ms-5x", "Starts with 'N'", "First letter excluding 'A' and 'The'"),
        ("ms ms-ability-adventure ms-mechanic ms-5x", "Starts with 'A'", "First letter excluding 'A' and 'The'"),
    ]

    choices_easy = [
        ("ms ms-3 ms-5x ms-cost ms-shadow", "Mana Value 3 or Greater"),
        ("ms ms-3 ms-5x ms-cost ms-shadow", "Mana Value 3 or Less"),
        ("ss ss-v11 ss-mythic ss-grad ss-5x", "Legendary Permanent"),
        ("ms ms-sorcery ms-5x ms-cost ms-shadow", "Instant or Sorcery")
    ]

    choices_hardmode = [
        ("ms ms-3 ms-5x ms-cost ms-shadow", "Mana Value 3 or Greater", "Hard Mode - All cards must also match this"),
        ("ms ms-3 ms-5x ms-cost ms-shadow", "Mana Value 3 or Less", "Hard Mode - All cards must also match this"),
        ("ss ss-v11 ss-mythic ss-grad ss-5x", "Legendary Permanent", "Hard Mode - All cards must also match this"),
        #("ms ms-sorcery ms-5x ms-cost ms-shadow", "Instant or Sorcery", "Hard Mode - All cards must also match this"),
    ]
    
    # create and then validate a 3D list of categories representing the grid
    def __init__(self) -> None:
        categories = []
        top = []
        bottom = []

        set_tooltip = "Card was printed in this set, reprints included"

        for _ in range(0, 3):
            # First choice (columns)
            choice = random.choice(self.choices_colors)
            while choice in top or choice in bottom:
                choice = random.choice(self.choices_colors)

            top.append(choice)
            # Second choice (rows)
            #choice = random.choice(self.choices_sets)
            # Add the easy category
            choice = (random.choice(self.choices_easy))
            while choice in top or choice in bottom:
                #choice = random.choice(self.choices_sets)
                random_set_code = random.choice(list(BaseballData.set_dict.keys()))
                random_set_name = BaseballData.set_dict[random_set_code]
                choice = (f"ss ss-{random_set_code} ss-rare ss-grad ss-5x", random_set_name, set_tooltip)

            bottom.append(choice)

        # Add a single Set game category
        random_index = random.randint(0, len(bottom) - 1)
        random_set_code = random.choice(list(BaseballData.set_dict.keys()))
        random_set_name = BaseballData.set_dict[random_set_code]
        choice = (f"ss ss-{random_set_code} ss-rare ss-grad ss-5x", random_set_name, set_tooltip)
        bottom[random_index] = choice

        # Add the name category
        random_index = random.randint(0, len(bottom) - 1)
        choice = random.choice(self.choices_name)
        bottom[random_index] = choice

        # Add the hardmode category
        hardmode = random.choice(self.choices_hardmode)
        while hardmode in top or hardmode in bottom:
        #while any(hardmode[1][0:4] == item[1][0:4] for item in top if isinstance(item, tuple)) or any(hardmode[1][0:4] == item[1] for item in bottom if isinstance(item, tuple)):
            hardmode = random.choice(self.choices_hardmode)
        
        categories.append(top)
        categories.append(bottom)

        categories.append(hardmode)

        self.categories = categories

    def get_grid(self):
        return self.categories
    
    @staticmethod
    def get_matchups(categories: list[list[tuple]]) -> list[tuple]:
        teams_top, teams_left = (categories[0], categories[1])
        matchups = [(top[1], left[1]) for top in teams_top for left in teams_left]
        return matchups

    def __str__(self) -> str:
        return str(self.categories)