#from DnD.monsters import get_monster_data
#from DnD.spells import get_spell_data
from make_requests import get_request_json
from DnD.Message_Builder.message_builder import dnd_message_builder
import logger, random

API_URL = "https://www.dnd5eapi.co/api/"
API_URL_BASE = "https://www.dnd5eapi.co"

def get_dnd_data(command_array):
    try:
        if(len(command_array) > 1):
            arg = command_array[1]
            if(arg in options_dict):
                option = options_dict[arg]
                if(option != "options"):
                    data = {}
                    if(len(command_array) > 2):
                        data = get_defined_object(options_dict[arg], command_array)
                    else:
                        data = get_random_object(options_dict[arg])
                    if not ("error" in data):
                        message_builder = dnd_message_builder()
                        return {"message": message_builder.build_message_array(data)}
                    else:
                        return data
                else:
                    return {"error": get_dnd_options()}
            else:
                message = f"I don't recognise !dnd {arg} sorry! Try one of the following: !dnd\n\n"
                for option in options_list:
                    message += "- " + option + "\n"
                return {"error": message}
        else:
            return {"error": get_dnd_options()}
    except Exception as error:
        logger.log(error)
        return {"error": "I'm sorry, I'm having some issues figuring that out right now. Ask me again later!"}    

def get_dnd_options():
    message = "I can get you information on different elements of D&D! Use commands such as '!dnd monsters' to get more information on different areas! Options include !dnd \n\n"
    for option in options_list:
        message += f"- {option}\n"
    return message

def get_defined_object(obj_type, command_array):
    obj_name = ""
    for x in range(2, len(command_array)):
        obj_name += command_array[x] + "-"
    obj_name = obj_name[:-1]
    list_data = get_request_json(f"{API_URL}{obj_type}/")
    found = False
    obj_url = ""
    for obj in list_data['results']:
        if(obj_name == obj['index']):
            found = True
            obj_url = f"{API_URL_BASE}{obj['url']}"
            break
    if(found is False):
        return {"error": f"Sorry, I'm not sure what a {obj_name.replace('-', ' ')} is!"}
    return get_request_json(obj_url)

def get_random_object(obj_type):
    list_data = get_request_json(f"{API_URL}{obj_type}")
    obj_item = random.choice(list_data['results'])
    return get_request_json(f"{API_URL_BASE}{obj_item['url']}")

options_dict = {
    "options": "options",
    "option": "options",
    "-o": "options",
    "abilityscores": "ability-scores",
    "ability-scores": "ability-scores",
    "-ab": "ability-scores",
    "alignments": "alignments",
    "alignment": "alignments",
    "-a": "alignments",
    "conditions": "conditions",
    "condition": "conditions",
    "-co": "conditions",
    "monsters": "monsters",
    "monster": "monsters",
    "-m": "monsters",
    "spells": "spells",
    "spell": "spells",
    "-s": "spells"
}

options_list = [
    "options (-o)",
    "ability-scores (-ab)",
    "alignments (-a)",
    "conditions (-co)",
    "monsters (-m)",
    "spells (-s)"
]