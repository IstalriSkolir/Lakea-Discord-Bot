class character:
    name = ""
    id = -1
    level = -1
    xp = -1
    hp = -1
    st = -1
    de = -1
    co = -1
    st_mod = -1
    de_mod = -1
    co_mod = -1

    def __init__(self, path):
        character_dict = self.get_character_info(path)
        self.name = character_dict["NAME"]
        self.id = int(character_dict["ID"])
        self.level = int(character_dict["LEVEL"])
        self.xp = int(character_dict["XP"])
        self.hp = int(character_dict["HP"])
        self.st = int(character_dict["STR"])
        self.de = int(character_dict["DEX"])
        self.co = int(character_dict["CON"])
        self.st_mod = self.st // 3
        self.de_mod = self.de // 3
        self.co_mod = self.co // 3

    def get_character_info(self, path):
        character_dict = {}
        reader = open(path)
        lines = reader.read().splitlines()
        reader.close()
        for string in lines:
            parts = string.split(':', 1)
            character_dict.update({parts[0]: parts[1]})
        return character_dict