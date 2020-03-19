# -*- coding: utf-8 -*-
import sys
import json

def parse_field( name, value, depth, last_item ):
  depth_print = '│   ' * ( depth - 1 )
  bar_print = ''
  
  if depth:
    bar_print = '└── ' if last_item else '├── '
  name_end_print = '/' if value else ''
  
  print "{}{}{}{}".format( depth_print, bar_print, name, name_end_print )

  for index, value_name in enumerate( value ):
    value_value = value[value_name]
    value_last = index == len( value ) - 1

    parse_field( name=value_name, value=value_value, depth=depth + 1, last_item=value_last )


if len( sys.argv ) is not 2:
  print "\
    Invalid use of script. Expected execution format to be the following:\n\
      python tree.py <file>\n\
    where <file> is a JSON file in the form specified in the README\
    "
  sys.exit()

tree = json.load( open( sys.argv[1] ) )

for index, field in enumerate( tree ):
  field_value = tree[field]
  last_item = index == len( tree ) - 1

  parse_field( name=field, value=field_value, depth=0, last_item=last_item )
