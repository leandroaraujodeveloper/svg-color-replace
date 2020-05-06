import os
import argparse

parser = argparse.ArgumentParser(description='Change colors in svg files')

parser.add_argument('files', metavar='F', type=str, nargs='+', help='svg files that you want modify')
parser.add_argument('--previous_color', type=str, help="previous color that you want change")
parser.add_argument('--new_color', type=str, help="new color that you replace previous")

args = parser.parse_args()

writing_data = ''
read_data = ''

for file in args.files:    
    with open(file) as f:
        read_data = f.read()
    f.closed

    writing_data = read_data.replace(args.color_previous, args.color_new)

    with open(file, 'w') as f:
        f.write(writing_data)
    f.close()

