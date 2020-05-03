import json
from bs4 import BeautifulSoup
import inflect


def configure_beautiful_soup(file_name):
    # open up the file, and get all the table rows
    file = open(file_name, "r", encoding="utf8")
    html = file.read()
    soup = BeautifulSoup(html, 'html.parser')
    table_body = soup.tbody
    table_rows = table_body.find_all('tr')
    index_to_key_map = [
        "name",
        "townName",
        "level",
        "attack",
        "defense",
        "damage_low",
        "damage_high",
        "health",
        "speed",
        "growth",
        "aiValue",
        "cost",
        "random_shit",
        "specials",
    ]
    return table_rows, index_to_key_map


def configure_inflect():
    p = inflect.engine()

    # Nix
    # Harpies
    # Serpent Flies
    # Dragon Flies
    # Monarchs
    # Cerberi
    # Efreet
    # Dead
    # Magi
    # Cyclopes
    # Pegasi
    # pegasi instead of pegasuses

    # define specials
    p.defnoun("Nix", "Nix")
    p.defnoun("Harpy", "Harpies")
    p.defnoun("Fly", "Flies")
    p.defnoun("Monarch", "Monarchs")
    p.defnoun("Cerberus", "Cerberi")
    p.defnoun("Efreet", "Efreet")
    p.defnoun("Dead", "Dead")
    p.defnoun("Mage", "Magi")
    p.defnoun("Cyclops", "Cyclopes")
    p.defnoun("Pegasus", "Pegasi")
    p.defnoun("Genie", "Genies")
    p.defnoun("Mummy", "Mummies")
    return p


def write_to_output(file_name, variable_name, array_of_dicts):
    # write to js file the new variable
    with open('js/' + file_name, 'w') as fp:
        fp.write("let " + variable_name + " = ")
        json.dump(array_of_dicts, fp, indent=2)


def pluralize(text: str, pluralizer):
    print(text)
    name_split = text.split(' ')
    name_split[-1] = pluralizer.plural(name_split[-1])
    text = ' '.join(name_split)
    print(text + "\n")
    return text


def town_information(table_rows, index_to_key_map, inflect_engine):
    towns = []
    town = {
        "name": "",
        "troops": []
    }
    troops = []

    for i, row in enumerate(table_rows):
        cells = row.find_all('td')
        troop = {}
        for j, cell in enumerate(cells):
            key = index_to_key_map[j]
            # key = "apple"
            troop[key] = ' '.join(cell.text.strip().split())

            # pluralize the troop names to match in game
            if key == "name":
                troop[key] = inflect_engine.plural(troop[key])

            # get the town name from the span title attribute
            elif key == "townName":
                troop[key] = cell.span['title'].strip()

            # cast int values to ints
            elif key not in ["random_shit", "specials", "level"]:
                troop[key] = int(troop[key])

        # create new town if the town name does not match
        if troop["townName"] != town["name"]:
            town["troops"].extend(troops)
            troops = []
            if i != 0:
                towns.append(town)
            town = {
                "name": troop["townName"],
                "troops": []
            }

        # delete unnecessary keys
        del troop["random_shit"]
        del troop["townName"]

        troops.append(troop)

    # sort by town name
    towns = sorted(towns, key=lambda k: k['name'])
    return towns


def troop_information(table_rows, index_to_key_map, inflect_engine):
    troops = []
    for i, row in enumerate(table_rows):
        cells = row.find_all('td')
        troop = {}
        for j, cell in enumerate(cells):
            key = index_to_key_map[j]
            # key = "apple"
            troop[key] = ' '.join(cell.text.strip().split())

            # pluralize the troop names to match in game
            if key == "name":
                troop[key] = pluralize(troop[key], inflect_engine)
                # troop[key] = inflect_engine.plural(troop[key])

            # get the town name from the span title attribute
            elif key == "townName":
                troop[key] = cell.span['title'].strip()

            # cast int values to ints
            elif key not in ["random_shit", "specials", "level"]:
                troop[key] = int(troop[key])

        # delete unnecessary keys
        del troop["random_shit"]

        # add image key
        troop["imageSrc"] = "./img/" + troop["townName"] + "/" + troop["name"] + ".PNG"

        # combine damage keys
        troop["damage"] = str(troop["damage_low"]) + "-" + str(troop["damage_high"])

        # type (archer/fast/tank/weak)
        # first get archer damage
        archer = "Ranged" in troop["specials"]
        if archer:
            troop["archerDamage"] = int(troop["specials"][8:10])
        else:
            troop["archerDamage"] = 0

        troop["type"] = ""
        if troop["archerDamage"] > 0:
            troop["type"] += "Archer (" + str(troop["archerDamage"]) + "dmg) "
        if troop["speed"] > 6:
            troop["type"] += "Fast "
        if troop["health"] > 50:
            troop["type"] += "Tank"
        if troop["type"] == "" and troop["health"] < 10:
            troop["type"] = "Weak"
        troop["type"] = troop["type"].strip()

        # done
        troops.append(troop)

    # sort by town name
    troops = sorted(troops, key=lambda k: k['townName'])
    return troops


if __name__ == '__main__':
    input_file_name = "troopTable.html"
    rows, key_map = configure_beautiful_soup(input_file_name)
    engine = configure_inflect()

    # town information
    # information_objects = town_information()
    # write_to_output("townInformation.js", "townInformation", information_objects)

    # troop information
    information_objects = troop_information(rows, key_map, engine)
    write_to_output("troopInformation.js", "troopInformation", information_objects)
