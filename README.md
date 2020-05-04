# HOMM3Guide

Searchable and sortable table of creatures for Heroes of Might and Magic Horn of the Abyss

To view the site simply download the project and then open index.html in your preferred browser.

You can download either by downloading the zip file, or by cloning the project with your favorite git client

[Download Zip](https://github.com/theheuman/HOMM3Guide/archive/master.zip)


## Datatables
Utilizes datatables 

- [Fixed header](https://datatables.net/extensions/fixedheader/)
- [Load from js array](https://datatables.net/release-datatables/examples/data_sources/js_array.html)
- [Detailed child view](https://datatables.net/examples/api/row_details.html)

Datatables configuration is found in js/index.js

## Python html parser
Data is grabbed from the [heroes wiki](heroes.v.thelazy.net/index.php/List_of_creatures_(HotA))

Utilizes 
- beautiful soup
 
to generate js file that contains a json object which datatables reads

- inflect 

to pluralize creature names since in game names are almost always pluralized

## Images
Grabbed directly from screnshots of the game.