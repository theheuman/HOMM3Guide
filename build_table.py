# Until i get my library into pip we'll have to do some stupid python imports, to get to my sibling package
# Directory structure looks like this:
# development
#     - HOMM3Guide
#     - jinja_datatables
import os
import sys
import importlib
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


import sys
from pathlib import Path # if you haven't already done so
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Additionally remove the current file's directory from sys.path
try:
    sys.path.remove(str(parent))
except ValueError: # Already removed
    pass

from jinja_datatables.jinja_datatables.datatable_classes import DatatableColumn, JSArrayDatatable
from jinja_datatables.jinja_datatables.jinja_extensions.datatableext import DatatableExt

if __name__ == '__main__' and __package__ is None:
    # include this column later
    # className: "details-control", orderable: false, data: null, defaultContent: "", target: 0
    columns = [
        DatatableColumn("townName", "Town", "select", {"className": "dt-center"}),
        DatatableColumn("imageSrc", "Image", "select",
                        {
                            "render": "function ( data, type, row, meta) {return '<img src=\"' + data +'\"/>';}",
                            "className": "dt-center"
                         }
                        ),
        DatatableColumn("name", "Name", "text", {"className": "dt-center"}),
        DatatableColumn("level", "Level", "select", {"className": "dt-center"}),
        DatatableColumn("type", "Type", "select", {"className": "dt-center"}),
        DatatableColumn("damage", "Damage", "text", {"className": "dt-center"}),
        DatatableColumn("health", "Health", "text", {"className": "dt-center"}),
        DatatableColumn("speed", "Speed", "text", {"className": "dt-center"}),
        DatatableColumn("specials", "Specials", "text", {"className": "dt-center"}),
    ]
    js_array = "troopInformation"
    html_arguments = {"id": "example", "class": "display", "style": "width:100%"}
    datatable_arguments = {
        "fixedHeader": "true",
        "order": '[[ 1, "asc" ]]',
        "columnDefs": '[{ "targets": [0], "searchable": false, "orderable": false, "visible": true }]'
    }
    table_view = JSArrayDatatable(
        columns,
        html_arguments,
        datatable_arguments,
        js_array,
    )

    current_dir = os.path.dirname(os.path.realpath(__file__))
    template_dir = os.path.join(current_dir, "./")
    env = Environment(loader=FileSystemLoader(template_dir), extensions=[DatatableExt])

    template = env.get_template("jinja_index.html")
    html = template.render(table_view=table_view)
    print(html)
    with open("index2.html", 'w') as fp:
        fp.write(html)



