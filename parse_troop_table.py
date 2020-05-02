import json
from bs4 import BeautifulSoup
import inflect

file_name = "troopTable.html"
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

townInformation = []
town = {
    "name": "",
    "troops": []
}
troops = []

p = inflect.engine()
for i, row in enumerate(table_rows):
    cells = row.find_all('td')
    troop = {}
    for j, cell in enumerate(cells):
        key = index_to_key_map[j]
        # key = "apple"
        troop[key] = ' '.join(cell.text.strip().split())

        # pluralize the troop names to match in game
        if key == "name":
            troop[key] = p.plural(troop[key])

        # get the town name from the span title attribute
        if key == "townName":
            troop[key] = cell.span['title'].strip()

    # create new town if the town name does not match
    if troop["townName"] != town["name"]:
        town["troops"].extend(troops)
        troops = []
        if i != 0:
            townInformation.append(town)
        town = {
            "name": troop["townName"],
            "troops": []
        }

    # delete unnecessary keys
    del troop["random_shit"]
    del troop["townName"]

    troops.append(troop)

# sort by town name
townInformation = sorted(townInformation, key=lambda k: k['name'])
# write to js file the new variable
with open('js/townInformation.js', 'w') as fp:
    fp.write("let townInformation = ")
    json.dump(townInformation, fp, indent=2)
