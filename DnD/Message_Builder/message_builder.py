from DnD.Message_Builder.message_builder_basic_details import dnd_basic_details
from DnD.Message_Builder.message_builder_order import dnd_order_message
from DnD.look_ups import ability_modifiers, message_part_order
import string

class dnd_message_builder:
    basic_details = {}
    basic_details_added = False
    ability_details_added = False

    def __init__(self) -> None:
        self.basic_details = dnd_basic_details()

    def build_message_array(self, data):
        message_dict = {}
        for key in data:
            if(key in self.key_dict):
                detail = self.key_dict[key](self, data)
                detail_key = next(iter(detail))
                if(detail_key != -1):
                    message_dict.update({detail_key: detail[detail_key]})
        message_list = dnd_order_message(message_dict)
        return message_list

    def add_ability_details(self, data):
        if(self.ability_details_added == False):
            self.ability_details_added = True
            return {message_part_order["add_ability_details"]: (f"**Abilities -** "
                f"Strength: {data['strength']}({ability_modifiers[data['strength']]})    "
                f"Dexterity: {data['dexterity']}({ability_modifiers[data['dexterity']]})    "
                f"Constiution: {data['constitution']}({ability_modifiers[data['constitution']]})    "
                f"Intelligence: {data['intelligence']}({ability_modifiers[data['intelligence']]})    "
                f"Wisdom: {data['wisdom']}({ability_modifiers[data['wisdom']]})    "
                f"Charisma: {data['charisma']}({ability_modifiers[data['charisma']]})\n\n")}
        else:
            return {-1: ""}

    def add_action_details(self, data):
        actions = data['actions']
        if(len(actions) > 0):
            message = "\n**Actions:**\n"
            for action in actions:
                message += f"- {action['name']} - {action['desc']}\n"
            return {message_part_order["add_action_details"]: message}
        else:
            return {-1: ""}    

    def add_basic_details(self, data):
        if(self.basic_details_added == False):
            self.basic_details_added = True
            url = data['url']
            if("ability-scores" in url):
                return {message_part_order['add_basic_details']: self.basic_details.add_basic_ability_details(data)}
            elif("alignments" in url):
                return {message_part_order['add_basic_details']: self.basic_details.add_basic_alignment_details(data)}
            elif("monsters" in url):
                return {message_part_order['add_basic_details']: self.basic_details.add_basic_monster_details(data)}
            elif("spells" in url):
                return {message_part_order['add_basic_details']: self.basic_details.add_basic_spell_details(data)}
            else:
                return {-1: ""}
        else:
            return {-1: ""}

    def add_classes_details(self, data):
        classes = data['classes']
        message = f"**Classes:** "
        for clas in classes:
            message += f"{clas['name']}, "
        message = message[:-2] + "\n\n"
        return {message_part_order['add_classes_details']: message}

    def add_condition_immunity_details(self, data):
        immunities = data['condition_immunities']
        if(len(immunities) > 0):
            message = "\n**Condition Immunities -** "
            for immunity in immunities:
                if(isinstance(immunity, str)):
                    immunity_string = string.capwords(immunity.replace("_", " "))
                    message += f"{immunity_string}, "
                elif(isinstance(immunity, object)):
                    immunity_string = immunity['name']
                    message += f"{immunity_string}, "
            message = message[:-2] + "\n"
            return {message_part_order['add_condition_immunity_details']: message}
        else:
            return {-1: ""}             

    def add_damage_immunity_details(self, data):
        immunities = data['damage_immunities']
        if(len(immunities) > 0):
            message = "\n**Damage Immunities -** "
            for immunity in immunities:
                immunity = string.capwords(immunity.replace("_", " "))
                message += f"{immunity}, "
            message = message[:-2] + "\n"
            return {message_part_order["add_damage_immunity_details"]: message}
        else:
            return {-1: ""}       

    def add_damage_resistance_details(self, data):
        resistances = data['damage_resistances']
        if(len(resistances) > 0):
            message = "\n**Damage Resistances -** "
            for resistance in resistances:
                resistance = string.capwords(resistance.replace("_", " "))
                message += f"{resistance}, "
            message = message[:-2]
            return {message_part_order["add_damage_resistance_details"]: message} 
        else:
            return{-1: ""}       

    def add_damage_vulnerability_details(self, data):
        vulnerabilities = data['damage_vulnerabilities']
        if(len(vulnerabilities) > 0):
            message = "\n**Damage Vulnerabilities -** "
            for vulnerability in vulnerabilities:
                vulnerability = string.capwords(vulnerability.replace("_", " "))
                message += f"{vulnerability}, "
            message = message[:-2]
            return {message_part_order["add_damage_vulnerability_details"]: message} 
        else:
            return{-1: ""}         

    def add_description_details(self, data):
        if("desc" in data):
            message = ""
            if(isinstance(data['desc'], str)):
                desc = data['desc'].replace("\n\n", "\n")
                message = f"\n**Description:**\n{desc}"
            elif(isinstance(data['desc'], list)):
                message = f"\n**Description:**\n"
                for line in data['desc']:
                    message += line.replace("\n\n", "\n")
            return {message_part_order["add_description_details"]: message}
        else:
            return {-1: ""}

    def add_higher_level_details(self, data):
        higher_level = data['higher_level']
        if(len(higher_level) > 0):
            message = "\n**At Higher Levels:** "
            for line in higher_level:
                message += f"{line}\n"
            return {message_part_order['add_higher_level_details']: message}
        else:
            return {-1: ""}        

    def add_language_details(self, data):
        if(data['languages'] != ""):
            return {message_part_order["add_language_details"]: f"**Languages -** {data['languages']}\n"}
        else:
            return {message_part_order["add_language_details"]: "**Languages -** N/A\n"}

    def add_legendary_action_details(self, data):
        legendary_actions = data['legendary_actions']
        if(len(legendary_actions) > 0):
            message = "\n**Legendary Actions:**\n"
            for action in legendary_actions:
                message += f"- {action['name']} - {action['desc']}\n"
            return {message_part_order["add_legendary_action_details"]: message} 
        else:
            return{-1: ""}         

    def add_proficiency_details(self, data):
        proficiencies = data['proficiencies']
        if(len(proficiencies) > 0):
            message = "**Proficiencies:**\n"
            for proficiency in proficiencies:
                message += f"- {proficiency['proficiency']['name']}: {proficiency['value']}\n"
            return {message_part_order["add_proficiency_details"]: message} 
        else:
            return{-1: ""}

    def add_reaction_details(self, data):
        if("reactions" in data):
            reactions = data['reactions']
            if(len(reactions) > 0):
                message = "\n**Reactions:**\n"
                for reaction in reactions:
                    message += f"- {reaction['name']} - {reaction['desc']}"
            return {message_part_order["add_reaction_details"]: message} 
        else:
            return{-1: ""}       

    def add_sense_details(self, data):
        senses = data['senses']
        if(len(senses) > 0):
            message = "**Senses -** "
            for key in senses:
                key_word = string.capwords(key.replace("_", " "))
                value = str(senses[key]).replace(".", "")
                message += f"{key_word}: {value}, "
            message = message[:-2] + "\n\n"
            return {message_part_order["add_sense_details"]: message} 
        else:
            return{-1: ""}  

    def add_skill_details(self, data):
        skills = data['skills']
        if(len(skills) > 0):
            message = "**Skills: **\n"
            for skill in skills:
                message += f"- {skill['name']}\n"
            return {message_part_order['add_skill_details']: message}
        else:
            return {-1: ""}

    def add_special_ability_details(self, data):
        special_abilities = data['special_abilities']
        if(len(special_abilities) > 0):
            message = "\n**Special Abilities:**\n"
            for ability in special_abilities:
                message += f"- {ability['name']} - {ability['desc']}\n"
            return {message_part_order["add_special_ability_details"]: message} 
        else:
            return{-1: ""}         

    def add_speed_details(self, data):
        speeds = data["speed"]
        message = "**Speeds -** "
        for key in speeds:
            key_word = string.capwords(key.replace("_", " "))
            message += f"{key_word}: {str(speeds[key])[:-1]}, "
        message = message[:-2] + "\n"
        return {message_part_order["add_speed_details"]: message}        

    key_dict = {
        "strength": add_ability_details,
        "dexterity": add_ability_details,
        "constitution": add_ability_details,
        "intelligence": add_ability_details,
        "wisdom": add_ability_details,
        "charisma": add_ability_details,
        "actions": add_action_details,
        "alignment": add_basic_details,
        "armor_class": add_basic_details,
        "challenge_rating": add_basic_details,
        "hit_dice": add_basic_details,
        "hit_points": add_basic_details,
        "hit_points_roll": add_basic_details,
        "index": add_basic_details,
        "name": add_basic_details,
        "proficiency_bonus": add_basic_details,
        "size": add_basic_details,
        "type": add_basic_details,
        "xp": add_basic_details,
        "classes": add_classes_details,
        "condition_immunities": add_condition_immunity_details,
        "damage_immunities": add_damage_immunity_details,
        "damage_resistances": add_damage_resistance_details,
        "damage_vulnerabilities": add_damage_vulnerability_details,
        "desc": add_description_details,
        "higher_level": add_higher_level_details,
        "proficiencies": add_proficiency_details,
        "languages": add_language_details,
        "legendary_actions": add_legendary_action_details,
        "reactions": add_reaction_details,
        "senses": add_sense_details,
        "skills": add_skill_details,
        "special_abilities": add_special_ability_details,
        "speed": add_speed_details
    }