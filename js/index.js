$(document).ready(
  function() {
    //buildTable()
    $('#example').DataTable( {
        data: troopInformation,
        columns: [
            { title: "Town", data: "townName", name: "townName", target: 0},
            { title: "Image", data: "imageSrc", name: "imageSrc", target: 1, render: function ( data, type, row, meta) {return '<img src="' + data +'"/>';}},
            { title: "Name", data: "name", name: "name", target: 2},
            { title: "Level", data: "level", name: "level", target: 3},
            { title: "Damage Low", data: "damage_low", name: "damage_low", target: 4},
            { title: "Damage High", data: "damage_high", name: "damage_high", target: 5},
            { title: "Health", data: "health", name: "health", target: 6},
            { title: "Speed", data: "speed", name: "speed", target: 7},
            { title: "Troops Per Week", data: "growth", name: "growth", target: 8},
            { title: "AI Value", data: "aiValue", name: "aiValue", target: 9},
            { title: "Cost", data: "cost", name: "cost", target: 10},
            { title: "Specials", data: "specials", name: "specials", target: 11},
        ]
    } );
  }
);

  function buildTable() {
    for (town of townInformation) {
        let table = document.getElementById("tableBody")
        buildSection(table, town);
    }
  }

  function buildSection(table, town) {
    for (i = 0; i < town.troops.length; i++) {
        let row = buildRow(town.name,  i+1, town.troops[i])
	table.append(row)
    } 
  }

  function buildRow(name, index, troop) {
    let prepend = "/lv"
    let imageSrc = "./img/" + name + "/" + troop.name + ".PNG"

    let row = document.createElement("tr")
    let cell = document.createElement("td")
    cell.innerHTML = name;
    row.append(cell)
    
    cell = document.createElement("td")
    cell.innerHTML = troop.name;
    row.append(cell)

    cell = document.createElement("td")
    cell.innerHTML = "Level " + troop.level;
    row.append(cell)

    cell = document.createElement("td")
    cell.innerHTML = '<img src="' + imageSrc + '">';
    row.append(cell)

    cell = document.createElement("td")
    cell.innerHTML = troop.type;
    row.append(cell)

    cell = document.createElement("td")
    cell.innerHTML = troop.damage_low + "-" + troop.damage_high;
    row.append(cell)

    cell = document.createElement("td")
    cell.innerHTML = troop.health;
    row.append(cell)

    cell = document.createElement("td")
    cell.innerHTML = troop.speed;
    row.append(cell)
    
    return row
  }