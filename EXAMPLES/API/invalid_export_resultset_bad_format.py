
"""
Export a ResultSet from asking a question using a bad export_format
"""
# Path to lib directory which contains pytan package
PYTAN_LIB_PATH = '../lib'

# connection info for Tanium Server
USERNAME = "Tanium User"
PASSWORD = "T@n!um"
HOST = "172.16.31.128"
PORT = "444"

# Logging conrols
LOGLEVEL = 2
DEBUGFORMAT = False

import sys, tempfile
sys.path.append(PYTAN_LIB_PATH)

import pytan
handler = pytan.Handler(
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    loglevel=LOGLEVEL,
    debugformat=DEBUGFORMAT,
)

print handler

# setup the export_obj kwargs for later
export_kwargs = {}
export_kwargs["export_format"] = u'bad'

# ask the question that will provide the resultset that we want to use
ask_kwargs = {
    'qtype': 'manual_human',
    'sensors': [
        "Computer Name"
    ],
}
response = handler.ask(**ask_kwargs)
export_kwargs['obj'] = response['question_results']

# export the object to a string
# this should throw an exception: pytan.utils.HandlerError
import traceback

try:
    handler.export_obj(**export_kwargs)
except Exception as e:
    traceback.print_exc(file=sys.stdout)



'''Output from running this:
Handler for Session to 172.16.31.128:444, Authenticated: True, Version: 6.2.314.3258
2015-02-11 12:19:17,704 INFO     question_progress: Results 0% (Get Computer Name from all machines)
2015-02-11 12:19:22,717 INFO     question_progress: Results 0% (Get Computer Name from all machines)
2015-02-11 12:19:27,731 INFO     question_progress: Results 100% (Get Computer Name from all machines)
Traceback (most recent call last):
  File "<string>", line 48, in <module>
  File "/Users/jolsen/gh/pytan/lib/pytan/handler.py", line 1413, in export_obj
    raise HandlerError(err)
HandlerError: u'bad' not a supported export format for ResultSet, must be one of: json, csv

'''