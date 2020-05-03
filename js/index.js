$(document).ready(
  function() {
    //buildTable()
    var table = $('#example').DataTable( {
        fixedHeader: true,
        data: troopInformation,
        order: [[ 1, "asc" ]],
        columns: [
            { className: "details-control", orderable: false, data: null, defaultContent: "", target: 0 },
            { title: "Town", data: "townName", name: "townName", target: 1},
            { title: "Image", data: "imageSrc", name: "imageSrc", target: 2, render: function ( data, type, row, meta) {return '<img src="' + data +'"/>';}},
            { title: "Name", data: "name", name: "name", target: 3},
            { title: "Level", data: "level", name: "level", target: 4},
            { title: "Type", data: "type", name: "type", target: 5},
            { title: "Damage", data: "damage", name: "damage", target: 6},
            { title: "Health", data: "health", name: "health", target: 7},
            { title: "Speed", data: "speed", name: "speed", target: 8},
            { title: "Specials", data: "specials", name: "specials", target: 9},
        ],
        columnDefs: [
            {className: "dt-center", targets: "_all"},
            { "targets": [0], "searchable": false, "orderable": false, "visible": true }
        ],
    } );

    // Add event listener for opening and closing details
    $('#example tbody').on('click', 'td.details-control', function () {
        var tr = $(this).closest('tr');
        var row = table.row( tr );

        if ( row.child.isShown() ) {
            // This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
        }
        else {
            // Open this row
            row.child( format(row.data()) ).show();
            tr.addClass('shown');
        }
    } );

    extras = [
            { title: "Troops Per Week", data: "growth", name: "growth", target: 0},
            { title: "AI Value", data: "aiValue", name: "aiValue", target: 1},
            { title: "Cost", data: "cost", name: "cost", target: 2},
            { title: "Attack", data: "attack", name: "attack", target: 3},
            { title: "Defense", data: "defense", name: "defense", target: 4},

    ]
  }
);
function format ( d ) {
    // `d` is the original data object for the row
    return '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">'+
        '<tr>'+
            '<td>Troops Per Week</td>'+
            '<td>'+d.growth+'</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Cost</td>'+
            '<td>'+d.cost+'</td>'+
        '</tr>'+
        '<tr>'+
            '<td>AI Value</td>'+
            '<td>'+d.aiValue+'</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Attack</td>'+
            '<td>'+d.attack+'</td>'+
        '</tr>'+
        '<tr>'+
            '<td>Defense</td>'+
            '<td>'+d.defense+'</td>'+
        '</tr>'+
    '</table>';
}

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