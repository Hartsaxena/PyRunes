from pathlib import Path
import json
import os
import time


os.chdir(Path(__file__).parent.absolute())

runebranch = {
    "Precision": {
        "Keystones": {"Press The Attack": 8005, "Lethal Tempo": 8008, "Fleet Footwork": 8021, "Conquerer": 8010},
        "Layer_A": {"Overheal": 9101, "Triumph": 9111, "Presence Of Mind": 8009},
        "Layer_B": {"Legend: Alacrity": 9104, "Legend: Tenacity": 9105, "Legend: Bloodline": 9103},
        "Layer_C": {"Coup De Grace": 8014, "Cut Down": 8017, "Last Stand": 8299}
    },
    "Domination": {
        "Keystones": {"Electrocute": 8112, "Predator": 8124, "Dark Harvest": 8128, "Hail of Blades": 9923},
        "Layer_A": {"Cheap Shot": 8126, "Taste Of Blood": 8139, "Sudden Impact": 8143},
        "Layer_B": {"Zombie Ward": 8136, "Ghost Poro": 8120, "Eyeball Collection": 8138},
        "Layer_C": {"Ravenous Hunter": 8135, "Ingenious Hunter": 8134, "Relentless Hunter": 8105, "Ultimate Hunter": 8106}
    },
    "Sorcery": {
        "Keystones": {"Summon Aery": 8214, "Arcane Comet": 8229, "Phase Rush": 8230},
        "Layer_A": {"Nullifying Orb": 8224, "Manaflow Band": 8226, "Nimbus Cloak": 8275},
        "Layer_B": {"Transcendence": 8210, "Celerity": 8234, "Absolute Focus": 8233},
        "Layer_C": {"Scorch": 8237, "Waterwalking": 8446, "Gathering Storm": 8236}
    },
    "Resolve": {
        "Keystones": {"Grasp Of The Undying": 8437, "Aftershock": 8439, "Bone Plating": 8465},
        "Layer_A": {"Demolish": 8446, "Font Of Life": 8463, "Shield Bash": 8401},
        "Layer_B": {"Conditioning": 8429, "Second Wind": 8444, "Bone Plating": 8473},
        "Layer_C": {"Overgrowth": 8451, "Revitalize": 8453, "Unflinching": 8242}
    },
    "Inspiration": {
        "Keystones": {"Glacial Augment": 8351, "Unsealed Spellbook": 8360, "Prototype: Omnistone": 8358},
        "Layer_A": {"Hextech Flashtraption": 8306, "Magical Footwear": 8304, "Perfect Timing": 8313},
        "Layer_B": {"Future's Market": 8321, "Minion Dematerializer": 8316, "Biscuit Delivery": 8345},
        "Layer_C": {"Cosmic Insight": 8347, "Approach Velocity": 8410, "Time Warp Tonic": 8352}
    },
}

mastery_rune_id = {
    "Precision": 8000,
    "Domination": 8100,
    "Sorcery": 8200,
    "Resolve": 8300,
    "Inspiration": 8400
}

stat_runes = {
    "Layer_A": {"Adaptive Force": 5008, "Attack Speed": 5005, "Ability Haste": 5007},
    "Layer_B": {"Adaptive Force": 5008, "Armor": 5002, "Magic Resist": 5003},
    "Layer_C": {"Health": 5001, "Armor": 5002, "Magic Resist": 5003},
}

example_runepage1 = {
    "Precision": {
        "Keystones": "Fleet Footwork",
        "Layer_A": "Triumph",
        "Layer_B": "Legend: Alacrity",
        "Layer_C": "Coup De Grace",
    },
    "Domination": {
        "Secondary_A": "Sudden Impact",
        "Secondary_B": "Ravenous Hunter",
    },
    "Stat_Runes": ["Attack Speed", "Armor", "Armor"]
}

example_runepage2 = {
    "Resolve": {
        "Keystones": "Aftershock",
        "Layer_A": "Font Of Life",
        "Layer_B": "Second Wind",
        "Layer_C": "Overgrowth"
    },
    "Inspiration": {
        "Secondary_A": "Hextech Flashtraption",
        "Secondary_B": "Biscuit Delivery"
    },
    "Stat_Runes": ["Adaptive Force", "Armor", "Magic Resist"],
}


# Code to check if a runepage is valid

def valid(page):
    try:
        Runemains = ["Precision", "Domination", "Sorcery", "Resolve", "Inspiration"]
        mains = []
        # Checks if the basic mastery runes exist (Precision, Domination, etc.)
        for runemain in page:
            mains.append(runemain)
            if runemain not in Runemains and runemain != "Stat_Runes":
                return False
        primary = mains[0]
        secondary = mains[1]
        # Checks the individual runes of the primary rune
        for rune in page[primary]:
            if page[primary][rune] not in runebranch[primary][rune]:
                return False

        # Checks the individual runes of the secondary rune
        all_secondary_layers = [runebranch[secondary]["Layer_A"], runebranch[secondary]["Layer_B"], runebranch[secondary]["Layer_C"]]
        falseswitch1, falseswitch2 = True, True
        for layer in all_secondary_layers:
            if page[secondary]["Secondary_A"] in layer:
                falseswitch1 = False
            if page[secondary]["Secondary_B"] in layer:
                falseswitch2 = False
            if page[secondary]["Secondary_B"] in layer and page[secondary]["Secondary_A"] in layer:
                return False
        if falseswitch1 or falseswitch2:
            return False

        statrunes = page["Stat_Runes"]
        if not (statrunes[0] in stat_runes["Layer_A"] and statrunes[1] in stat_runes["Layer_B"] and statrunes[2] in stat_runes["Layer_C"]):
            return False

        return True
    except KeyError:
        return False


# Finish Everything else first before actually importing to the game
# def forward_to_game(page):
#     os.chdir(Path.home())
#     # path_to_runefile = "Applications/League of Legends.app/Contents/LoL/Config/PerksPreferences.yaml"
#     path_to_runefile = "/Users/hartsaxena/code/Python/PyRunes/test_files/PerksPreferences.yaml"
#     runefile = open("/Users/hartsaxena/code/Python/PyRunes/test_files/PerksPreferences.yaml", 'r')
#     runefile.seek(0)
#     runefile_lines = runefile.readlines()
#

# with open("runesaves.json", 'w+') as json_file:
#     json.dump({"Thresh (change)": example_runepage2}, json_file, indent=4)

def find_rune_name(rune_path, reverse=False):
    # Just a little function that translates the path of a savefile into an actual name of the the rune
    # reverse can be enabled to change a runename into a filename
    if reverse == False:
        try:
            return rune_path[rune_path.find("saves/") + len("saves/"):rune_path.find(".json")].replace("_", " ")
        except:
            return "ERROR: Rune_Path couldn't be translated into rune name."
    else:
        bug_variable = "_"
        # For some reason, putting a raw "_" in the .replace function pulls up a syntax error, but replacing it with a variable works just fine.
        # return f"saves/{rune_path.replace(" ", bug_variable)}.json"
        return ("saves/" + rune_path.replace(" ", bug_variable) + ".json")


def present(runepage):
    # A Function that presents the json of a runepage in an easily readable format.
    indexes = {"Primary": ["Keystones", "Layer_A", "Layer_B", "Layer_C"], "Secondary": ["Secondary_A", "Secondary_B"]}
    try:
        print("This rune page consists of...\n")
        currentrunesection = "Primary"
        for thing in runepage:
            if thing != "Stat_Runes":
                print(f"{thing}, with...")
                for index in indexes[currentrunesection]:
                    punc = ", "
                    if index == "Layer_C" or index == "Secondary_B":
                        print("and ", end="")
                        punc = ".\n"
                    print(str(runepage[thing][index]) + punc)
                currentrunesection = "Secondary"
            else:
                print("With:")
                for num in range(0, 3):
                    punc = ", "
                    if num == 2:
                        print("and ", end="")
                        punc = ".\n"
                    print(str(runepage["Stat_Runes"][num]) + punc, end="")
                # print (f"With {str(runepage["Stat_Runes"][num] + "\n" for num in range(1, 4))}")
    except KeyError:
        print("Rune page is not formatted correctly.")


def file_to_page(savefilepath):
    runepagename = find_rune_name(savefilepath)
    with open(savefilepath, "r") as json_file:
        new_json = json.load(json_file)[runepagename]
    return new_json


def rune_save(runepage):
    # There must be the name of the rune page in the dictionary
    # This function saves a rune page into a .json file located in the saves folder
    for thing in runepage:
        name = thing
    with open(find_rune_name(name, reverse=True), 'w') as savefile:
        json.dump(runepage, savefile, indent=4)


if __name__ == "__main__":
    newthing = file_to_page("saves/Thresh_(change).json")
    rune_save({"Thresh (change)": newthing})
