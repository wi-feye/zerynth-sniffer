#################################################################################
# Title: utils.py
#################################################################################

################################# IMPORT SECTION ################################
import gpio
import watchdog

################################ FOTA UTILITY  #################################
fota_ongoing = False
pub_stopped = False
acq_stopped = True

def fota_checks(agent, step, arg):
    '''Function that wait for loop stopping to start downloading new FW'''
    global fota_ongoing, pub_stopped, acq_stopped
    if step=="check_version":
        print("[FOTA] Check version...")
        fota_ongoing = True
        while (not acq_stopped) and (not pub_stopped):
            print("[FOTA] Waiting for permission to download...")
            sleep(5000)
        print("[FOTA] Received permission from Threads")
        watchdog.setup(300000)
        return False
    elif step=="accept":
        print("[FOTA] Start FOTA download")
        # do not accept any firmware
        return False
    elif step=="download":
        print("[FOTA] Start FOTA download")
        return False

################################### Edge UTILS ##################################

def get_publish_ts(now, publish_period, ts_last_publish, offset=0):
    '''Function to set periodic publish at hh:mm:00'''
    publish_ts = 0

    delta = now%publish_period
    if delta < offset:
        delta += publish_period
        
    if (ts_last_publish < now-delta + offset) :
        publish_ts = now - delta + offset
    return publish_ts

