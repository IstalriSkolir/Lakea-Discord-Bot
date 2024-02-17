from PIL import Image, ImageDraw, ImageFont
import logger, string

def create_scoreboard(characters, path_seperator):
    try:
        image_name = "monster_battles_scoreboard.png"
        image = load_base_image(path_seperator)
        canvas = ImageDraw.Draw(image)
        canvas = write_character_data(canvas, characters, path_seperator)
        image.save(image_name)
        return image_name
    except Exception as error:
        logger.log(error)

def load_base_image(path_seperator):
    try:
        image = Image.open(f"Resources{path_seperator}MonsterScoreboard.png")
        return image
    except Exception as error:
        logger.log(error)
        return Image.new(mode = "RGB", size = (1500, 1500), color = (0, 150, 0))
    
def write_character_data(canvas, characters, path_seperator):
    font = ImageFont.truetype(f"Resources{path_seperator}Cataneo_BT.ttf", 60)
    font_bold = ImageFont.truetype(f"Resources{path_seperator}Cataneo_BT_Bold.ttf", 60)
    for x in range(len(characters)):
        character_name = edit_character_name(characters[x].name)
        character_xp = edit_character_xp(str(characters[x].xp))
        if(x < 3):
            canvas = write_text(canvas, character_name, font_bold, (75, ((x * 114) + 350)))
            canvas = write_text(canvas, str(characters[x].level), font_bold, (775, ((x * 114) + 350)))
            canvas = write_text(canvas, character_xp, font_bold, (1145, ((x * 114) + 350)))
        else:
            canvas = write_text(canvas, character_name, font, (75, ((x * 114) + 350)))
            canvas = write_text(canvas, str(characters[x].level), font, (775, ((x * 114) + 350)))
            canvas = write_text(canvas, character_xp, font, (1145, ((x * 114) + 350)))

def write_text(canvas, text, font, location):
    canvas.text(location, text, font=font, fill=(255, 0, 0))
    return canvas

def edit_character_name(name):
    name = name.replace("_", " ")
    name = string.capwords(name)
    return name

def edit_character_xp(xp):
    new_xp = ""
    if(len(xp) > 3):
        char_list = list(xp)        
        char_list.reverse()
        for x in range(0, len(char_list)):
            new_xp += char_list[x]
            if(((x + 1) % 3) == 0 and x != 0):
                new_xp += "'"
        new_xp = new_xp[::-1]
    else:
        return xp   
    return new_xp