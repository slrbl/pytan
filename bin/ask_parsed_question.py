#!/usr/bin/env python
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# ex: set tabstop=4
# Please do not change the two lines above. See PEP 8, PEP 263.
'''Ask a parsed question and save the results as a report format'''
__author__ = 'Jim Olsen (jim.olsen@tanium.com)'
__version__ = '0.1'

import os
import sys

sys.dont_write_bytecode = True
my_file = os.path.abspath(__file__)
my_dir = os.path.dirname(my_file)
parent_dir = os.path.dirname(my_dir)
lib_dir = os.path.join(parent_dir, 'lib')
path_adds = [lib_dir]

for aa in path_adds:
    if aa not in sys.path:
        sys.path.append(aa)

import customparser
import SoapWrap
import SoapUtil

SoapUtil.version_check(__version__)
parent_parser = customparser.setup_parser(__doc__)
parser = customparser.CustomParser(
    description=__doc__,
    parents=[parent_parser],
)
parser = customparser.setup_report_parser(parser)
parser = customparser.setup_question_report_parser(parser)
parser = customparser.setup_report_sort_parser(parser)
ask_question_group = parser.add_argument_group('Ask Parsed Question Options')
ask_question_group.add_argument(
    '--query',
    required=True,
    action='store',
    dest='query',
    help='Question to ask',
)
ask_question_group.add_argument(
    '--picker',
    required=False,
    action='store',
    default=None,
    dest='picker',
    help='Which parsed query to pick, only needed if parsed queries do not '
    'match lower cased input query - supply -1 to force a list of query '
    'matches',
)
args = parser.parse_args()
swargs = args.__dict__

# put our query args into their own dict and remove them from swargs
qgrp_names = ['Ask Parsed Question Options']
qgrp_opts = customparser.get_grp_opts(parser, qgrp_names)
qgrp_args = {k: swargs.pop(k) for k in qgrp_opts}

# put our transform args into their own dict and remove them from swargs
tgrp_names = [
    'Report Options',
    'Question Report Options',
    'Report Sort Options',
]
tgrp_opts = customparser.get_grp_opts(parser, tgrp_names)
tgrp_args = {k: swargs.pop(k) for k in tgrp_opts if k in swargs}

sw = SoapWrap.SoapWrap(**swargs)
print str(sw)

print "++ Asking parsed question: ", SoapUtil.json.dumps(qgrp_args)
response = sw.ask_parsed_question(**qgrp_args)
print "++ Received Response: ", str(response)

SoapUtil.write_object(sw, response, tgrp_args)
