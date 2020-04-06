# -*- coding: utf-8 -*-
import sys
import json
from collections import OrderedDict

def parse_objects( objects, padding, start=False ):
  objects = OrderedDict( sorted( objects.items() ) )
  for index, entry in enumerate( objects ):
    last_item = entry == list( objects.keys() )[-1]
    name_end_print = '/' if objects[entry] else ''

    bar_print = '' if start else '└── ' if last_item else '├── '

    print "{}{}{}{}".format( padding, bar_print, entry, name_end_print )

    if objects[entry]:
      append_padding = '' if start else '    ' if last_item else '│   '
      parse_objects( objects[entry], padding + append_padding )

if len( sys.argv ) is not 2:
  print "\
    Invalid use of script. Expected execution format to be the following:\n\
      python tree.py <file>\n\
    where <file> is a JSON file in the form specified in the README\
    "
  sys.exit()

tree = json.load( open( sys.argv[1] ) )
parse_objects( tree, padding='', start=True )
