import random
import BaseballData

class GameCategories:
    choices_colors = [
        ("ms ms-c ms-5x ms-cost ms-shadow", "Colorless"),
	    ("ms ms-b ms-5x ms-cost ms-shadow", "Black"),
        ("ms ms-w ms-5x ms-cost ms-shadow", "White"),
        ("ms ms-u ms-5x ms-cost ms-shadow", "Blue"),
        ("ms ms-r ms-5x ms-cost ms-shadow", "Red"),
        ("ms ms-g ms-5x ms-cost ms-shadow", "Green"),
        ("ms ms-wu ms-5x ms-cost ms-shadow", "Azorius"),
        ("ms ms-wb ms-5x ms-cost ms-shadow", "Orzhov"),
        ("ms ms-rw ms-5x ms-cost ms-shadow", "Boros"),
        ("ms ms-gw ms-5x ms-cost ms-shadow", "Selesnya"),   
        ("ms ms-ub ms-5x ms-cost ms-shadow", "Dimir"),
        ("ms ms-ur ms-5x ms-cost ms-shadow", "Izzet"),
        ("ms ms-gu ms-5x ms-cost ms-shadow", "Simic"),
        ("ms ms-br ms-5x ms-cost ms-shadow", "Rakdos"),
        ("ms ms-bg ms-5x ms-cost ms-shadow", "Golgari"),
        ("ms ms-rg ms-5x ms-cost ms-shadow", "Gruul"),
    ]

    choices_sets = [
        ("ss ss-isd ss-rare ss-grad ss-5x", "Innistrad"),
        ("ss ss-war ss-rare ss-grad ss-5x", "War of the Spark"),
        ("ss ss-one ss-rare ss-grad ss-5x", "Phyrexia: All Will Be One"),
        ("ss ss-woe ss-rare ss-grad ss-5x", "Wilds of Eldraine"),
        ("ss ss-rav ss-rare ss-grad ss-5x", "Ravnica: City of Guilds"),
        ("ss ss-rix ss-rare ss-grad ss-5x", "Rivals of Ixalan"),
        ("ss ss-dmu ss-rare ss-grad ss-5x", "Dominaria United"),
        ("ss ss-lrw ss-rare ss-grad ss-5x", "Lorwyn"),
    ]

    choices_name = [
        ("ms ms-ability-adventure ms-mechanic ms-5x", "Starts with 'S'"),
        ("ms ms-ability-adventure ms-mechanic ms-5x", "Starts with 'T'"),
        ("ms ms-ability-adventure ms-mechanic ms-5x", "Starts with 'R'"),
        ("ms ms-ability-adventure ms-mechanic ms-5x", "Starts with 'L'"),
        ("ms ms-ability-adventure ms-mechanic ms-5x", "Starts with 'M'"),
        ("ms ms-ability-adventure ms-mechanic ms-5x", "Starts with 'N'"),
        ("ms ms-ability-adventure ms-mechanic ms-5x", "Starts with 'A'")
    ]

    choices_easy = [
        ("ms ms-3 ms-5x ms-cost ms-shadow", "Mana Value 3 or Greater"),
        ("ms ms-3 ms-5x ms-cost ms-shadow", "Mana Value 3 or Less"),
        ("ss ss-v11 ss-mythic ss-grad ss-5x", "Legendary Permanent"),
    ]

    choices_hardmode = [
        ("ms ms-3 ms-5x ms-cost ms-shadow", "Mana Value 3 or Greater"),
        ("ms ms-3 ms-5x ms-cost ms-shadow", "Mana Value 3 or Less"),
        ("ss ss-v11 ss-mythic ss-grad ss-5x", "Legendary Permanent"),
        ("ms ms-sorcery ms-5x ms-cost ms-shadow", "Legendary Permanent")
    ]
    
    # create and then validate a 3D list of categories representing the grid
    def __init__(self) -> None:
        categories = []
        top = []
        bottom = []

        for _ in range(0, 3):
            # First choice (columns)
            choice = random.choice(self.choices_colors)
            while choice in top or choice in bottom:
                choice = random.choice(self.choices_colors)

            top.append(choice)
            # Second choice (rows)
            #choice = random.choice(self.choices_sets)
            random_set_code = random.choice(list(BaseballData.set_dict.keys()))
            random_set_name = BaseballData.set_dict[random_set_code]
            choice = (f"ss ss-{random_set_code} ss-rare ss-grad ss-5x", random_set_name)
            while choice in top or choice in bottom:
                #choice = random.choice(self.choices_sets)
                random_set_code = random.choice(list(BaseballData.set_dict.keys()))
                random_set_name = BaseballData.set_dict[random_set_code]
                choice = (f"ss ss-{random_set_code} ss-rare ss-grad ss-5x", random_set_name)

            bottom.append(choice)

        random_index = random.randint(0, len(bottom) - 1)
        random_choice_from_names = random.choice(self.choices_name)
        bottom[random_index] = random_choice_from_names

        random_index = random.randint(0, len(bottom) - 1)
        random_choice_from_easy = random.choice(self.choices_easy)
        bottom[random_index] = random_choice_from_easy

        hardmode = random.choice(self.choices_hardmode)
        while hardmode in top or hardmode in bottom:
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