import httpx
from urllib.parse import quote
from itertools import combinations

set_dict = {
    #'10e': 'Tenth Edition',
    #'2ed': 'Unlimited Edition',
    '2xm': 'Double Masters',
    '2x2': 'Double Masters 2022',
    #'30a': '30th Anniversary Edition',
    #'3ed': 'Revised Edition',
    # '40k': 'Warhammer 40,000 Commander',
    #'4ed': 'Fourth Edition',
    #'5dn': 'Fifth Dawn',
    #'5ed': 'Fifth Edition',
    #'6ed': 'Classic Sixth Edition',
    #'7ed': 'Seventh Edition',
    #'8ed': 'Eighth Edition',
    #'9ed': 'Ninth Edition',
    #'a25': 'Masters 25',
    #'acr': "Assassin's Creed",
    'aer': 'Aether Revolt',
    # 'afc': 'Forgotten Realms Commander',
    'afr': 'Adventures in the Forgotten Realms',
    'akh': 'Amonkhet',
    #'akr': 'Amonkhet Remastered',
    'ala': 'Shards of Alara',
    'all': 'Alliances',
    'apc': 'Apocalypse',
    'arb': 'Alara Reborn',
    #'arc': 'Archenemy',
    #'arn': 'Arabian Nights',
    #'ath': 'Anthologies',
    #'atq': 'Antiquities',
    'avr': 'Avacyn Restored',
    'bbd': 'Battlebond',
    'bfz': 'Battle for Zendikar',
    'big': 'The Big Score',
    #blb': 'Bloomburrow',
    #'bng': 'Born of the Gods',
    'bok': 'Betrayers of Kamigawa',
    #'bot': 'Transformers',
    #'brb': 'Battle Royale Box Set',
    # 'brc': "The Brothers' War Commander",
    'bro': "The Brothers' War",
    #'brr': "The Brothers' War Retro Artifacts",
    # 'btd': 'Beatdown Box Set',
    # 'c13': 'Commander 2013',
    # 'c14': 'Commander 2014',
    # 'c15': 'Commander 2015',
    # 'c16': 'Commander 2016',
    # 'c17': 'Commander 2017',
    # 'c18': 'Commander 2018',
    # 'c19': 'Commander 2019',
    # 'c20': 'Commander 2020',
    # 'c21': 'Commander 2021',
    # 'clb': "Commander Legends: Battle for Baldur's Gate",
    # 'cc1': 'Commander Collection: Green',
    # 'cc2': 'Commander Collection: Black',
    # 'chk': 'Champions of Kamigawa',
    # 'chr': 'Chronicles',
    # 'clu': 'Ravnica: Clue Edition',
    # 'cm1': "Commander's Arsenal",
    # 'cm2': 'Commander Anthology Volume II',
    # 'cma': 'Commander Anthology',
    # 'cmd': 'Commander 2011',
    # 'cmm': 'Commander Masters',
    'cmr': 'Commander Legends',
    # 'cns': 'Conspiracy',
    # 'cn2': 'Conspiracy: Take the Crown',
    # 'con': 'Conflux',
    # 'csp': 'Coldsnap',
    # 'dgm': "Dragon's Maze",
    # 'dis': 'Dissension',
    # 'dka': 'Dark Ascension',
    # 'dkm': 'Deckmasters',
    # 'dmr': 'Dominaria Remastered',
    'dmu': 'Dominaria United',
    # 'dmc': 'Dominaria United Commander',
    'dom': 'Dominaria',
    # 'dpa': 'Duels of the Planeswalkers',
    # 'drb': 'From the Vault: Dragons',
    # 'drk': 'The Dark',
    'dst': 'Darksteel',
    'dtk': 'Dragons of Tarkir',
    # 'e01': 'Archenemy: Nicol Bolas',
    'e02': 'Explorers of Ixalan',
    # 'ea1': 'Explorer Anthology 1',
    'eld': 'Throne of Eldraine',
    # 'ema': 'Eternal Masters',
    'emn': 'Eldritch Moon',
    'eve': 'Eventide',
    # 'evg': 'Duel Decks Anthology: Elves vs. Goblins',
    # 'exo': 'Exodus',
    # 'exp': 'Zendikar Expeditions',
    # 'fem': 'Fallen Empires',
    # 'frf': 'Fate Reforged',
    'fut': 'Future Sight',
    # 'gpt': 'Guildpact',
    'grn': 'Guilds of Ravnica',
    # 'gtc': 'Gatecrash',
    # 'ha1': 'Historic Anthology 1',
    # 'hml': 'Homelands',
    # 'hop': 'Planechase',
    'hou': 'Hour of Devastation',
    # 'ice': 'Ice Age',
    'iko': 'Ikoria: Lair of Behemoths',
    # 'ima': 'Iconic Masters',
    #'inv': 'Invasion',
    'isd': 'Innistrad',
    # 'j20': 'Judge Gift Cards 2020',
    # 'j21': 'Jumpstart: Historic Horizons',
    # 'j22': 'Jumpstart 2022',
    # 'jmp': 'Jumpstart',
    'jou': 'Journey into Nyx',
    #'jud': 'Judgment',
    # 'khc': 'Kaldheim Commander',
    'khm': 'Kaldheim',
    'kld': 'Kaladesh',
    #'klr': 'Kaladesh Remastered',
    'ktk': 'Khans of Tarkir',
    # 'lcc': 'The Lost Caverns of Ixalan Commander',
    'lci': 'The Lost Caverns of Ixalan',
    #'lea': 'Limited Edition Alpha',
    #'leb': 'Limited Edition Beta',
    # 'leg': 'Legends',
    # 'lgn': 'Legions',
    'lrw': 'Lorwyn',
    # 'ltc': 'Tales of Middle-earth Commander',
    'ltr': 'The Lord of the Rings: Tales of Middle-earth',
    # 'm10': 'Magic 2010',
    # 'm11': 'Magic 2011',
    # 'm12': 'Magic 2012',
    # 'm13': 'Magic 2013',
    # 'm14': 'Magic 2014',
    # 'm15': 'Magic 2015',
    # 'm19': 'Core Set 2019',
    # 'm20': 'Core Set 2020',
    # 'm21': 'Core Set 2021',
    # 'm3c': 'Modern Horizons 3 Commander',
    # 'mat': 'March of the Machine: The Aftermath',
    # 'mb1': 'The List',
    'mbs': 'Mirrodin Besieged',
    # 'md1': 'Modern Event Deck 2014',
    # 'me1': 'Masters Edition',
    # 'me2': 'Masters Edition II',
    # 'me3': 'Masters Edition III',
    # 'me4': 'Masters Edition IV',
    # 'med': 'Mythic Edition',
    'mh1': 'Modern Horizons',
    'mh2': 'Modern Horizons 2',
    # 'mh3': 'Modern Horizons 3',
    # 'mic': 'Midnight Hunt Commander',
    'mid': 'Innistrad: Midnight Hunt',
    'mir': 'Mirage',
    # 'mkc': 'Murders at Karlov Manor Commander',
    'mkm': 'Murders at Karlov Manor',
    # 'mm2': 'Modern Masters 2015',
    # 'mm3': 'Modern Masters 2017',
    # 'mma': 'Modern Masters',
    # 'mmq': 'Mercadian Masques',
    # 'moc': 'March of the Machine Commander',
    'mom': 'March of the Machine',
    # 'mor': 'Morningtide',
    # 'mp2': 'Amonkhet Invocations',
    # 'mps': 'Kaladesh Inventions',
    'mrd': 'Mirrodin',
    # 'mul': 'Multiverse Legends',
    # 'nem': 'Nemesis',
    # 'nec': 'Neon Dynasty Commander',
    'neo': 'Kamigawa: Neon Dynasty',
    # 'nms': 'Nemesis',
    # 'ncc': 'New Capenna Commander',
    'nph': 'New Phyrexia',
    # 'ody': 'Odyssey',
    'ogw': 'Oath of the Gatewatch',
    # 'onc': 'Phyrexia: All Will Be One Commander',
    'one': 'Phyrexia: All Will Be One',
    # 'ons': 'Onslaught',
    # 'ori': 'Magic Origins',
    # 'otc': 'Outlaws of Thunder Junction Commander',
    'otj': 'Outlaws of Thunder Junction',
    # 'otp': 'Breaking News',
    # 'p02': 'Portal Second Age',
    # 'pc2': 'Planechase 2012',
    # 'pca': 'Planechase Anthology',
    # 'pcy': 'Prophecy',
    # 'pd2': 'Premium Deck Series: Fire and Lightning',
    # 'pd3': 'Premium Deck Series: Graveborn',
    'pip': 'Fallout',
    # 'plc': 'Planar Chaos',
    # 'pls': 'Planeshift',
    # 'po2': 'Portal Second Age',
    # 'por': 'Portal',
    # 'ptg': 'Ponies: The Galloping',
    # 'ptk': 'Portal Three Kingdoms',
    'rav': 'Ravnica: City of Guilds',
    # 'rex': 'Jurassic World Collection',
    'rix': 'Rivals of Ixalan',
    'rna': 'Ravnica Allegiance',
    'roe': 'Rise of the Eldrazi',
    'rtr': 'Return to Ravnica',
    # 'rvr': 'Ravnica Remastered',
    # 's00': 'Starter 2000',
    # 's99': 'Starter 1999',
    # 'scd': 'Starter Commander Decks',
    # 'scg': 'Scourge',
    'shm': 'Shadowmoor',
    # 'sir': 'Shadows over Innistrad Remastered',
    # 'sis': 'Shadows of the Past',
    # 'sld': 'Secret Lair Drop',
    # 'slu': 'Secret Lair: Ultimate Edition',
    'snc': 'Streets of New Capenna',
    'soi': 'Shadows over Innistrad',
    'sok': 'Saviors of Kamigawa',
    'som': 'Scars of Mirrodin',
    # 'spg': 'Special Guests',
    # 'ss1': 'Signature Spellbook: Jace',
    # 'ss2': 'Signature Spellbook: Gideon',
    # 'ss3': 'Signature Spellbook: Chandra',
    # 'sta': 'Strixhaven Mystical Archive',
    # 'sth': 'Stronghold',
    'stx': 'Strixhaven: School of Mages',
    # 'td2': 'Duel Decks: Mirrodin Pure vs. New Phyrexia',
    'thb': 'Theros Beyond Death',
    'ths': 'Theros',
    # 'tmp': 'Tempest',
    # 'tor': 'Torment',
    # 'tpr': 'Tempest Remastered',
    'tsp': 'Time Spiral',
    # 'tsr': 'Time Spiral Remastered',
    # 'uds': "Urza's Destiny",
    # 'ugl': 'Unglued',
    # 'ulg': "Urza's Legacy",
    # 'uma': 'Ultimate Masters',
    # 'und': 'Unsanctioned',
    # 'unf': 'Unfinity',
    # 'unh': 'Unhinged',
    # 'ust': 'Unstable',
    # 'usg': "Urza's Saga",
    # 'v09': 'From the Vault: Exiled',
    # 'v10': 'From the Vault: Relics',
    # 'v11': 'From the Vault: Legends',
    # 'v12': 'From the Vault: Realms',
    # 'v13': 'From the Vault: Twenty',
    # 'v14': 'From the Vault: Annihilation',
    # 'v15': 'From the Vault: Angels',
    # 'v16': 'From the Vault: Lore',
    # 'v17': 'From the Vault: Transform',
    # 'vis': 'Visions',
    # 'voc': 'Crimson Vow Commander',
    'vow': 'Innistrad: Crimson Vow',
    # 'vma': 'Vintage Masters',
    # 'w16': 'Welcome Deck 2016',
    # 'w17': 'Welcome Deck 2017',
    'war': 'War of the Spark',
    'who': 'Doctor Who',
    # 'woc': 'Wilds of Eldraine Commander',
    'woe': 'Wilds of Eldraine',
    # 'wot': 'Wilds of Eldraine: Enchanting Tales',
    'wth': 'Weatherlight',
    # 'wwk': 'Worldwake',
    'xln': 'Ixalan',
    'zen': 'Zendikar',
    # 'znc': 'Zendikar Rising Commander',
    'znr': 'Zendikar Rising'}

class BaseballData:
    def __init__(self, catagories: list) -> None:
        self.catagories = catagories

    """ def validate_category(self): # returns invalid category(s) if any
        invalid = []

        for x in len(self.catagories):
            for y in len(self.catagories[x]):
                 """

    def parse_api_url(query):
        # In case player name is not URL safe
        safe_query = quote(query)
        #return 'https://api.scryfall.com/cards/search?q="' + safe_query + '"+in:paper' # in:paper to remove arena/digital cards, put query in "" to disable ability to use scryfall terms to search
        return 'https://api.scryfall.com/cards/search?q=' + safe_query + '+in:paper' # use "" makes the query much longer??

    """ def determine_possible_players(self):
        url = self.parse_api_url("a")
        data = requests.get(url)
        data = data.json()["people"][0]["stats"][-1]["splits"]
        for season in data:
            try:
                print(f"Year: {season['season']}, Team: {season['team']['name']}")
            except KeyError:
                continue """

    @staticmethod
    async def search_players(player):
        #if "'" in player:
        #    player = player.split("'")[0]
        url = BaseballData.parse_api_url(player)
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            #data = response.json()["people"]
            data = response.json()["data"]
            return data
    
    # If card is a reprint, look up the previous printings to find the original print date
    @staticmethod
    async def search_reprints(player):
        reprint_sets = []
        url = player["prints_search_uri"]
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            #data = response.json()["data"][-1] # just get the first printing
            data = response.json()["data"]
            for card in data:
                if card['set'] not in reprint_sets:
                    reprint_sets.append(card['set'])
            #return data    
            return reprint_sets
        
    @staticmethod    
    def __get_old_team_names(team):
        match(team):
            case []:
                return "Colorless"
            case "W":
                return "White"
            case "U":
                return "Blue"
            case "B":
                return "Black"
            case "R":
                return "Red"
            case "G":
                return "Green"
            case "WU":
                return "Azorius"
            case "WB":
                return "Orzhov"
            case "WR":
                return "Boros"
            case "WG":
                return "Selesnya"
            case "UB":
                return "Dimir"
            case "UR":
                return "Izzet"
            case "UG":
                return "Simic"
            case "BR":
                return "Rakdos"
            case "BG":
                return "Golgari"
            case "RG":
                return "Gruul"
            case "UW":
                return "Azorius"
            case "BW":
                return "Orzhov"
            case "RW":
                return "Boros"
            case "GW":
                return "Selesnya"
            case "BU":
                return "Dimir"
            case "RU":
                return "Izzet"
            case "GU":
                return "Simic"
            case "RB":
                return "Rakdos"
            case "GB":
                return "Golgari"
            case "GR":
                return "Gruul"
            case _:
                return team
    @staticmethod    
    def __get_old_set_names(team):
        #set_dict[team]
        return set_dict.get(team)

    @staticmethod    
    def __get_hardmode_category(player):
        hardmode_categories = []
        if player['cmc'] > 2:
            hardmode_categories.append("Mana Value 3 or Greater")
        if player['cmc'] < 4:
            hardmode_categories.append("Mana Value 3 or Less")
        if "Legendary" in player['type_line']:
            hardmode_categories.append("Legendary Permanent")
        if "Instant" in player['type_line'] or "Sorcery" in player['type_line']:
            hardmode_categories.append("Instant or Sorcery")
        return hardmode_categories
            
    @staticmethod
    def get_player_teams(player):
        teams = []
        # Get the color identities 
        # if player["color_identity"] == []:
        #     teams.append(BaseballData.__get_old_team_names("C"))
        # else:
        color_combinations = []
        if 'color' in player: # some cards don't have a colors field
            for r in range(1, len(player["colors"]) + 1):
                color_combinations.extend([''.join(comb) for comb in combinations(player["colors"], r)])    
            if len(color_combinations)>0:
                for color in color_combinations:
                    teams.append(BaseballData.__get_old_team_names(color))
            else:
                teams.append(BaseballData.__get_old_team_names(color_combinations))
        else:
            for r in range(1, len(player["color_identity"]) + 1):
                color_combinations.extend([''.join(comb) for comb in combinations(player["color_identity"], r)]) 
            if len(color_combinations)>0:
                for color in color_combinations:
                    teams.append(BaseballData.__get_old_team_names(color))
            else:
                teams.append(BaseballData.__get_old_team_names(color_combinations))


        # Get the set name
        #teams.append(BaseballData.__get_old_set_names(player["set"])) # match set label to full set name
        teams.append(BaseballData.__get_old_set_names(player['set'])) # get the set name

        if "The " in player['name']:
            player_name = player['name'].split("The ")[1]
        else:
            player_name = player['name']

        teams.append(f"Starts with '{player_name[0]}'") # get the first letter of the card name
        teams.extend(BaseballData.__get_hardmode_category(player)) # get the hardmode category
        return teams
    
    @staticmethod
    def get_player_picture(player=None, id=None):
        try:
            if not player and not id:
                raise ValueError("Must provide either player or id")
            if player:
                id = player['id']
            #if id:
                #player = await BaseballData.lookup_by_id(id)
            #return f"https://img.mlbstatic.com/mlb-photos/image/upload/w_300,q_auto:best/v1/people/{id}/headshot/67/current"
            #return player['image_uris']['border_crop']
            return f"https://api.scryfall.com/cards/{id}/?format=image"
        except KeyError:
            return ""
    
    @staticmethod
    async def lookup_by_id(id):
        async with httpx.AsyncClient() as client:
            url = f"https://api.scryfall.com/cards/{id}"
            response = await client.get(url)
            data = response.json()
            return data
