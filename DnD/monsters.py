from make_requests import get_request_json
from DnD.look_ups import ability_modifiers
import random, string

def get_monster_data(command_array):
    reply = ""
    if(len(command_array) <= 2):
        reply = get_random_monster()
    else:
        reply = get_defined_monster(command_array)
    return reply

def get_defined_monster(command_array):
    monster_name = ""
    for x in range(2, len(command_array)):
        monster_name += command_array[x] + "-"
    monster_name = monster_name[:-1]
    data = get_request_json("https://www.dnd5eapi.co/api/monsters/")
    found = False
    monster_url = "https://www.dnd5eapi.co"
    for monster in data["results"]:
        if(monster_name == monster['index']):
            found = True
            monster_url += monster['url']
            break
    if(found is False):
        return f"Sorry, I'm not sure what a {monster_name.replace('-', ' ')} is!"    
    monster_data = get_request_json(monster_url)
    monster_string = create_monster_string(monster_data)
    return monster_string

def get_random_monster():
    data = get_request_json("https://www.dnd5eapi.co/api/monsters/")
    monster_item = random.choice(data["results"])
    monster_data = get_request_json(f"https://www.dnd5eapi.co{monster_item['url']}")
    monster_string = create_monster_string(monster_data)
    return monster_string

def create_monster_string(data):
    message = (f"**Name:** {data['name']}    **Size:** {data['size']}    **Type:** {data['type']}    **Alignment:** {data['alignment']}\n"
        f"**Challenge Rating:** {data['challenge_rating']}    **Proficiency Bonus:** {data['proficiency_bonus']}    **XP:** {data['xp']}\n\n"
        f"**Hit Points:** {data['hit_points']}    **Hit Dice:** {data['hit_dice']}    **Hit Points Roll:** {data['hit_points_roll']}"
        f"**Armour Type:** {data['armor_class'][0]['type']}    **Armour Class:** {data['armor_class'][0]['value']}\n")
    message = add_monster_abilities(message, data)
    message = add_monster_languages(message, data)
    message = add_monster_speeds(message, data)
    message = add_monster_senses(message, data)
    message = add_monster_proficiencies(message, data)
    message = add_monster_damage_vulnerabilities(message, data)
    message = add_monster_damage_resistances(message, data)
    message = add_monster_damage_immunities(message, data)
    message = add_monster_special_abilities(message, data)
    message = add_monster_actions(message, data)
    message = add_monster_reactions(message, data)
    message = add_monster_legendary_actions(message, data)
    return message

def add_monster_abilities(message, data):
    message += (f"**Abilities -** "
        f"Strength: {data['strength']}({ability_modifiers[data['strength']]})    "
        f"Dexterity: {data['dexterity']}({ability_modifiers[data['dexterity']]})    "
        f"Constiution: {data['constitution']}({ability_modifiers[data['constitution']]})    "
        f"Intelligence: {data['intelligence']}({ability_modifiers[data['intelligence']]})    "
        f"Wisdom: {data['wisdom']}({ability_modifiers[data['wisdom']]})    "
        f"Charisma: {data['charisma']}({ability_modifiers[data['charisma']]})\n\n")
    return message

def add_monster_languages(message, data):
    if(data['languages'] != ""):
        message += f"**Languages -** {data['languages']}\n"
    else:
        message += "**Languages -** N/A\n"
    return message

def add_monster_speeds(message, data):
    speeds = data["speed"]
    message += "**Speeds -** "
    for key in speeds:
        key_word = string.capwords(key.replace("_", " "))
        message += f"{key_word}: {str(speeds[key])[:-1]}, "
    message = message[:-2] + "\n"
    return message

def add_monster_senses(message, data):
    senses = data['senses']
    if(len(senses) > 0):
        message += "**Senses -** "
        for key in senses:
            key_word = string.capwords(key.replace("_", " "))
            value = str(senses[key]).replace(".", "")
            message += f"{key_word}: {value}, "
        message = message[:-2] + "\n\n"
    return message

def add_monster_proficiencies(message, data):
    proficiencies = data['proficiencies']
    if(len(proficiencies) > 0):
        message += "**Proficiencies:**\n"
        for proficiency in proficiencies:
            message += f"- {proficiency['proficiency']['name']}: {proficiency['value']}\n"
    return message

def add_monster_damage_vulnerabilities(message, data):
    vulnerabilities = data['damage_vulnerabilities']
    if(len(vulnerabilities) > 0):
        message += "\n**Damage Vulnerabilities -** "
        for vulnerability in vulnerabilities:
            vulnerability = string.capwords(vulnerability.replace("_", " "))
            message += f"{vulnerability}, "
        message = message[:-2]
    return message

def add_monster_damage_resistances(message, data):
    resistances = data['damage_resistances']
    if(len(resistances) > 0):
        message += "\n**Damage Resistances -** "
        for resistance in resistances:
            resistance = string.capwords(resistance.replace("_", " "))
            message += f"{resistance}, "
        message = message[:-2]
    return message

def add_monster_damage_immunities(message, data):
    immunities = data['damage_immunities']
    if(len(immunities) > 0):
        message += "\n**Damage Immunities -** "
        for immunity in immunities:
            immunity = string.capwords(immunity.replace("_", " "))
            message += f"{immunity}, "
        message = message[:-2] + "\n"
    return message

def add_monster_special_abilities(message, data):
    special_abilities = data['special_abilities']
    if(len(special_abilities) > 0):
        message += "\n**Special Abilities:**\n"
        for ability in special_abilities:
            message += f"- {ability['name']} - {ability['desc']}\n"
    return message

def add_monster_actions(message, data):
    actions = data['actions']
    if(len(actions) > 0):
        message += "\n**Actions:**\n"
        for action in actions:
            message += f"- {action['name']} - {action['desc']}\n"
    return message

def add_monster_reactions(message, data):
    if("reactions" in data):
        reactions = data['reactions']
        if(len(reactions) > 0):
            message += "\n**Reactions:**\n"
            for reaction in reactions:
                message += f"- {reaction['name'] - {reaction['desc']}}"
    return message

def add_monster_legendary_actions(message, data):
    legendary_actions = data['legendary_actions']
    if(len(legendary_actions) > 0):
        message += "\n**Legendary Actions:**\n"
        for action in legendary_actions:
            message += f"- {action['name']} - {action['desc']}\n"
    return message