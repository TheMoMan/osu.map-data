# osu.map-data

This project reads .osu files and formats all mapsets, maps, and objects into an sqlite database. There are also several sql files that analyse the database for curiosity satisfaction purposes.

The code is a bit of a bodge job so some things like the query scripts might not be ready to run out of the box.

Thanks to [Mr HeliX](https://osu.ppy.sh/users/2330619) for providing a list of loved beatmap IDs.

### Videos
[This is the most common circle in osu!](https://youtu.be/bOLI0pVpfy)

## Setting up

You should probably have Python installed for this, I used 3.9. Sqlite3 is probably a good idea too.

- Clone this repository and navigate to it using your favourite command line interface with `cd osu.map-data`
- Create a new database file with `sqlite3 mapdata.db` and then set up the tables with `.read schema.sql`. Press `Ctrl+D` to close the database when you're done.
- Create a new directory named `maps` and add your .ose files in here. If you need a dump of all ranked and loved .osu files you can get them from https://data.ppy.sh/.
- Run `python3 run.py` to start reading and adding maps to the database. This will probably take some time (took me around an hour for the entire data dump), and will create a database file around 2GB in size.

When you're done you should have a database with four tables you're free to play around with.

## Database schema

Hopefully most of these tables and columns should be self-explanatory.

### beatmap_sets

| Column | Data type | Settings | Notes |
| ------ | --------- | -------- | ----- |
| beatmap_set_id | text | primary key | Very old beatmaps didn't store the beatmap set id in the .osu, so for these cases we use a hash of a string combining the metadata of the map. |
| title | text | not null | Uses the first instance found of the set. |
| title_unicode | text | not null | Uses the first instance found of the set. |
| artist | text | not null | Uses the first instance found of the set. |
| artist_unicode | text | not null | Uses the first instance found of the set.|
| creator | text | not null | Mapset host. Uses the first instance found of the set. |
| source | text | | Uses the first instance found of the set. |
| tags | text | | Uses the first instance found of the set. |

### beatmaps
| Column | Data type | Settings | Notes |
| ------ | --------- | -------- | ----- |
| beatmap_id | integer | primary key | Very old beatmaps didn't store the beatmap id in the .osu, so for these cases we use the file name the map was read from. |
| beatmap_set_id | text | not null, foreign key | |
| mode | integer | not null | Can only be `0`. We're only processing standard mode maps for now |
| difficulty_name | text | not null | |
| hp_drain | real | not null | |
| circle_size | real | not null | |
| overall_difficulty | real | not null | |
| approach_rate | real | not null | |
| slider_multiplier | real | not null | Base slider velocity. |
| slider_tick_rate | real | not null | |
| stack_leniency | real | not null | |

### objects
| Column | Data type | Settings | Notes |
| ------ | --------- | -------- | ----- |
| object_number | integer, primary key | not null | Goes up in the order that they appear in the .osu file. |
| beatmap_id | integer, primary key, foreign key | not null | |
| type | text | not null | `circle`, `slider`, or `spinner` |
| time | integer | not null | Time the object appears in milliseconds. |
| x | integer | not null | x co-ordinate of the object. |
| y | integer | not null | y co-ordinate of the object. |
| new_combo | integer | not null | `1` if the object is the start of a new combo, `0` otherwise. |
| anchors | text | | List of all slider anchors on this object. See [this](https://osu.ppy.sh/wiki/en/osu%21_File_Formats/Osu_%28file_format%29#sliders) for more info. |
| length | real | | Length of the slider in osu! pixels. See [this](https://osu.ppy.sh/wiki/en/osu%21_File_Formats/Osu_%28file_format%29#sliders) for more info. |
| curve_type | text | | Slider curve type. See [this](https://osu.ppy.sh/wiki/en/osu%21_File_Formats/Osu_%28file_format%29#sliders) for more info. |
| slides | integer | | Number of slides in the slider. See [this](https://osu.ppy.sh/wiki/en/osu%21_File_Formats/Osu_%28file_format%29#sliders) for more info. |

### beatmaps_web
This table only contains two columns for now, as it's just a bodge job to store loved beatmap IDs. Will probably re-use this to store all beatmap website data later.

| Column | Data type | Settings | Notes |
| ------ | --------- | -------- | ----- |
| beatmap_id | integer, primary key, foreign key | not null | Only realised I named this column incorrectly whilst writing this documentation, but I'm too lazy to fix it now. |
| status | text | not null | `loved` is the only value this can be for now. |

## Analysing

Feel free to write whatever queries to get interesting info from the database. I've provided a handful I used in the video in the `scripts` directory, which you can run by opening the database with `sqlite3 mapdata.db` and entering `.read scripts/objectCoordsByFreq.sql`.

There are also two python scripts in `app/queries` that I used for counting which co-ordinates were the least used. These can be simply run with `python3 app/queries/coordsWithFewObjects.py`.

There is one more script called `app/heatmap.py` that uses matplotlib to create the heatmaps of object frequency. This code reads .csv outputs made from the queries `objectCoords` and  `firstObjectCoords` and formats them to make a heatmap.
