###############################################################################
# Config Module
###############################################################################

################################# IMPORT SECTION ##############################
import fs
import json
import queue

#==================================================LOOPING
# Threads frequencies
MAIN_FREQ = 250
L_WATCHDOG = 60000

#====================== TSLOG CONFIG
# LOG path
LOG_PATH = "/zerynth/log"

# TSLOG Record Size
RECORD_SIZE = 512

# TSLOG COMMIT
DELTA_COMMIT = 1

#==================== PUB LOOP
PUB_DICT = {}

#==================================================FS MGMT
# Resources name and path on File System
FS_PARAM_PATH = "/zerynth/params.json"

#==================================================PARAMETERS
TAG_CONFIG = "config"

# WIFI config
WIFI_NAME = 'SMARTAPP_SNIFFER'
WIFI_PASSWORD = 'SmartAppSniffer'
# SNIFF config
SCAN_TIME = 5 * 1000
MAX_PACKETS = 1000
RELEVANT_FIELDS = (4, 5, 6, 8, 11, 12, 13)

################################### PARAMS UTILS ################################
#==================== FS MGMT
# Resources name and path on File System
FS_PARAM_PATH = "/zerynth/params.json"

#==================== PARAMS UTILS
def get_config(path):
    '''Function to read configured params from FS'''
    json_file = fs.open(path,"r")
    json_string = json_file.read()
    params = json.loads(json_string)
    json_file.close()
    return params

def init_recovery(path, dft_dict):
    '''Function to recover default params from default_config.py'''
    # Sensors default configuring
    print(dft_dict)
    json_params = json.dumps(dft_dict)
    json_file = fs.open(path,"w+")
    json_file.write(str(json_params))
    json_file.close()
    return dft_dict