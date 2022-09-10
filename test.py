import sys
import os

print('[*] running from ' + os.getcwd())
sys.path.append("/home/j0hn/ProgramingWorkshop/python/geo-node-tuff")

import geo_parse

geo_parse.parse_exp('(w*(x+y))')