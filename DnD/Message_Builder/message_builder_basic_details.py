from DnD.look_ups import spell_levels

class dnd_basic_details:

    def add_basic_monster_details(self, data):
        return (f"**Name:** {data['name']}    **Size:** {data['size']}    **Type:** {data['type']}    **Alignment:** {data['alignment']}\n"
        f"**Challenge Rating:** {data['challenge_rating']}    **Proficiency Bonus:** {data['proficiency_bonus']}    **XP:** {data['xp']}\n"
        f"**Hit Points:** {data['hit_points']}    **Hit Dice:** {data['hit_dice']}    **Hit Points Roll:** {data['hit_points_roll']}    "
        f"**Armour Type:** {data['armor_class'][0]['type']}    **Armour Class:** {data['armor_class'][0]['value']}\n")

    def add_basic_spell_details(self, data):
        message = f"**Name:** {data['name']}\n"
        if(data['level'] == 0):
            message += f"**Level:** {spell_levels[data['level']]} {data['school']['name']}"
        else:
            message += f"**Level:** {spell_levels[data['level']]} Level {data['school']['name']}"
        if(data['ritual'] == True):
            message += " (ritual)\n"
        message += f"**\nCasting Time:** {data['casting_time']}\n**Range:** {data['range']}\n**Components:** "
        for component in data['components']:
            message += f"{component} "
        if(data['concentration'] == True):
            message += f"\n**Duration:** Concentration, {data['duration']}"
        else:
            message += f"\n**Duration:** {data['duration']}"
        return message
    
    def add_basic_ability_details(self, data):
        return f"**Name:** {data['full_name']}\n"
    
    def add_basic_alignment_details(self, data):
        return f"**Name:** {data['name']} ({data['abbreviation']})"
    
    def add_basic_condition_details(self, data):
        return f"**Name:** {data['name']}"
    
    def add_basic_skill_details(self, data):
        return f"**Name:** {data['name']}"
    
    def add_basic_trait_details(self, data):
        return f"**Name:** {data['name']}"

    def add_basic_language_details(self, data):
        return f"**Name:** {data['name']}\n**Type:** {data['type']}\n**Script:** {data['script']}"
    
    def add_basic_magic_school_details(self, data):
        return f"**Name: ** {data['name']}"
    
    def add_basic_damage_type_details(self, data):
        return f"**Name: ** {data['name']}"