from make_requests import get_request_json
from DnD.look_ups import spell_levels
import random

def get_spell_data(command_array):
    reply = ""
    if(len(command_array) <= 2):
        reply = get_random_spell()
    else:
        reply = get_defined_spell(command_array)
    return reply

def get_defined_spell(command_array):
    spell_name = ""
    for x in range(2, len(command_array)):
        spell_name += command_array[x] + "-"
    spell_name = spell_name[:-1]
    data = get_request_json("https://www.dnd5eapi.co/api/spells/")
    found = False
    spell_url = "https://www.dnd5eapi.co"
    for spell in data["results"]:
        if(spell_name == spell['index']):
            found = True
            spell_url += spell['url']
            break
    if(found is False):
        return f"Sorry, I'm not family with the {spell_name.replace('-', ' ')} spell!"
    spell_data = get_request_json(spell_url)
    spell_string = create_spell_string(spell_data)
    return spell_string

def get_random_spell():
    data = get_request_json("https://www.dnd5eapi.co/api/spells/")
    spell_item = random.choice(data['results'])
    spell_data = get_request_json(f"https://www.dnd5eapi.co{spell_item['url']}")
    spell_string = create_spell_string(spell_data)
    return spell_string

def create_spell_string(data):
    message = add_spell_base_details(data)
    message = add_spell_casting_time(message, data)
    message = add_spell_range(message, data)
    message = add_spell_components(message, data)
    message = add_spell_duration(message, data)
    message = add_spell_classes(message, data)
    message = add_spell_description(message, data)
    message = add_spell_higher_level(message, data)
    return message

def add_spell_base_details(data):
    message = f"**Name:** {data['name']}\n"
    if(data['level'] == 0):
        message += f"**Level:** {spell_levels[data['level']]} {data['school']['name']}"
    else:
        message += f"**Level:** {spell_levels[data['level']]} Level {data['school']['name']}"
    if(data['ritual'] == True):
        message += " (ritual)\n\n"
    else:
        message += "\n\n"
    return message

def add_spell_casting_time(message, data):
    message += f"**Casting Time:** {data['casting_time']}\n"
    return message

def add_spell_range(message, data):
    message += f"**Range:** {data['range']}\n"
    return message

def add_spell_components(message, data):
    components = data['components']
    message += f"**Components:** "
    for component in components:
        message += component + " "
    message += "\n"
    return message

def add_spell_duration(message, data):
    if(data['concentration'] == True):
        message += f"**Duration:** Concentration, {data['duration']}\n"
    else:
        message += f"**Duration:** {data['duration']}\n"
    return message

def add_spell_classes(message, data):
    classes = data['classes']
    message += f"**Classes:** "
    for clas in classes:
        message += f"{clas['name']}, "
    message = message[:-2] + "\n\n"
    return message

def add_spell_description(message, data):
    description_dict = data['desc']
    description = ""
    for line in description_dict:
        description += f"{line}\n"
    if(len(description) < 2000):
        message += description
    else:
        for line in description_dict:
            message += f"{line}\n\n"
    return message

def add_spell_higher_level(message, data):
    higher_level = data['higher_level']
    if(len(higher_level) > 0):
        message += "\n**At Higher Levels:** "
        for line in higher_level:
            message += f"{line}\n"
    return message