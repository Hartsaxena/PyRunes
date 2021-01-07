from pathlib import Path
import back
import inflect
import json
import os

os.chdir(Path(__file__).parent.absolute())
inflectengine = inflect.engine()


def verbose_client():
    print("Hello!")
    print("Welcome to PyRunes!")
    justopened = False
    while True:
        if justopened:
            os.system("clear")
        justopened = True
        if os.listdir("saves") != []:
            empty_savefolder = False
            print("\nYour Currently saved runepages are:\n")
            for thing in os.listdir("saves"):
                print(back.find_rune_name(f"saves/{thing}"))
        else:
            empty_savefolder = True
            print("You don't have any saved rune pages yet.")
        userinput = input("\nWhat would you like to do?\n[\"create\" - Create a new rune page, \"View\" View a pre-existing rune page, \"delete\" - delete a pre-existing rune page.]\n").lower()
        if userinput == "create":
            process_make_new()
        elif userinput == "view":
            if empty_savefolder:
                print("Sorry, but you don't have any previously saved rune pages to view.")
            else:
                while True:
                    runepage_selection_pre = input("Which Rune page would you like to view?\n(Type \"Nevermind\" if you change your mind)\n")
                    runepage_selection = runepage_selection_pre.lower()
                    if runepage_selection == "nevermind":
                        break
                    correlatedrune = "N/A"
                    for page in [back.find_rune_name(f"saves/{thing}") for thing in os.listdir("saves")]:
                        if runepage_selection == page.lower():
                            correlatedrune = page
                    if correlatedrune == "N/A":
                        print("Sorry, your response isn't a listed Rune Page.")
                        print("Please try again.\n")
                    else:
                        try:
                            print() # prints blank line as a spacing line, since end="\n" is default on print()
                            selected_page = back.file_to_page(back.find_rune_name(correlatedrune, reverse=True))
                            back.present(selected_page)
                            continueswitch = input("\n\nPress Enter to exit back to the Main Menu. ")
                            break
                        except UnboundLocalError:
                            pass
        elif userinput == "delete":
            if empty_savefolder:
                print("Sorry, but there are no rune pages to delete.")
            else:
                print("Ok!")
                while True:
                    deleting_runepage_pre = input("Which rune page would you like to delete?\n")
                    deleting_runepage = deleting_runepage_pre.lower()
                    if deleting_runepage == "nevermind":
                        break
                    if back.find_rune_name(deleting_runepage, reverse=True)[len("saves/"):] in [filename.lower() for filename in os.listdir("saves")]:
                        os.remove(back.find_rune_name(deleting_runepage_pre, reverse=True))
                        break
                    else:
                        print("Sorry, but the runepage you entered does not exist.")
                        print("Please try again.\n")
        elif userinput == "quit" or userinput == "stop":
            break
        else:
            print("Sorry, but the option you entered does not exist.\nPlease type in \"View\", \"Create\", or \"Delete\".")


def process_make_new():
    runepagename = input("\nPlease input what you would like the new rune page to be named: ")
    if runepagename.lower() == "nevermind":
        return 0
    while True:
        options = [prime for prime in back.runebranch]
        primary_rune = input(f"Please input what you would like {runepagename}'s primary rune to be:\n(Your options are {options})\n").title()
        if primary_rune not in options:
            print("Sorry, but it seems that you didn't type one of the valid primary runes.")
            print("Please try again.\n")
        else:
            break
    while True:
        options = [keystone for keystone in back.runebranch[primary_rune]["Keystones"]]
        keystone = input(f"Please input what you would like the keystone of {runepagename} to be:\n(Your options are {options})\n").title()
        if keystone not in options:
            print("Sorry, but it seems that you didn't type one of the valid Keystones.")
            print("Please try again.\n")
        else:
            break
    layerindexes = ["Layer_A", "Layer_B", "Layer_C"]
    runeselections = []
    for i in range(0, 3):
        while True:
            options = [primerune for primerune in back.runebranch[primary_rune][layerindexes[i]]]
            runeselected = input(f"Please input what you would like the {inflectengine.ordinal(i+1)} rune of {runepagename} to be:\n(Your options are {options})\n").title()
            if runeselected not in options:
                print("Sorry, but it seems that you didn't type one of the valid Runes.")
                print("Please try again.\n")
            else:
                break
        runeselections.append(runeselected)
    while True:
        options = [prime for prime in back.runebranch if prime != primary_rune]
        secondary_rune = input(f"Please input what you would like {runepagename}'s secondary rune category to be:\n(Your options are {options})\n").title()
        if secondary_rune not in options:
            print("Sorry, but it seems that you didn't type on of the valid secondary runes.")
            print("Please try again.\n")
        else:
            break
    secondary_layerindexes = ["Layer_A", "Layer_B", "Layer_C"]
    secondary_runeselections = []
    for i in range(0, 2):
        if i == 1:
            previous_secondary_rune = secondary_runeselections[0]
            for x in range(0, 3):
                if previous_secondary_rune in back.runebranch[secondary_rune][secondary_layerindexes[x]]:
                    conditional = x
        else:
            conditional = 5  # Just some random number that can't be reached with range(0,3)
        while True:
            options = []
            for x in range(0, 3):
                if x != conditional:
                    for secondrune in back.runebranch[secondary_rune][secondary_layerindexes[x]]:
                        options.append(secondrune)
            runeselected = input(f"Please input what you would like the {inflectengine.ordinal(i+1)} secondary rune of {runepagename} to be:\n(Your options are {options})\n").title()
            if runeselected not in options:
                print("Sorry, but it seems that you didn't type one of the valid Secondary Runes.")
                print("Please try again.\n")
            else:
                break
        secondary_runeselections.append(runeselected)
    statrune_layerindexes = ["Layer_A", "Layer_B", "Layer_C"]
    statrune_selections = []
    for i in range(0, 3):
        while True:
            options = [statrune for statrune in back.stat_runes[statrune_layerindexes[i]]]
            runeselected = input(f"Please input what you would like the {inflectengine.ordinal(i+1)} minor rune of {runepagename} to be:\n(Your options are {options})\n").title()
            if runeselected not in options:
                print("Sorry, but it seems that you didn't type one of the valid Minor Runes.")
                print("Please try again.\n")
            else:
                break
        statrune_selections.append(runeselected)

    createdrunepage = {
        runepagename: {
            primary_rune: {
                "Keystones": keystone,
                "Layer_A": runeselections[0],
                "Layer_B": runeselections[1],
                "Layer_C": runeselections[2],
            },
            secondary_rune: {
                "Secondary_A": secondary_runeselections[0],
                "Secondary_B": secondary_runeselections[1],
            },
            "Stat_Runes": [
                statrune_selections[0],
                statrune_selections[1],
                statrune_selections[2],
            ]
        }
    }
    back.rune_save(createdrunepage)


if __name__ == "__main__":
    verbose_client()
