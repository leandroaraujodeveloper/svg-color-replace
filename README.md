# SVG color replace tool 
Tool for change color of many svg files
## Usage
Changing one or few svg files:

```bash
$ python  modify_color_fill.py --previous_color '#000000' --new_color '#FFFFFF' your_svg_file.svg

```
Changing many svg files:

```bash
$ python modify_color_fill.py --previous_color '#000000' --new_color '#FFFFFF' $(ls *.svg)
```
