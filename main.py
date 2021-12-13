from time import sleep, time
from datetime import datetime
from src.app.models.GasTrackerAPIModel import GasTrackerAPI
from editable_options import OPTIONS
from src.constants import ONE_MINUTE

if ((__name__ == '__main__') and (OPTIONS['ENABLE']) and (OPTIONS['CHECKS_PER_MINUTE'] > 0)):
    interval = ONE_MINUTE / OPTIONS['CHECKS_PER_MINUTE']


    
    if(OPTIONS['CHECKS_PER_MINUTE'] > 1):
        now = datetime.now()
        start_minute = now.minute
        
        for run_check in range(OPTIONS['CHECKS_PER_MINUTE']):
            interval_start = time()
            gas_fee_tracker = GasTrackerAPI()
            gas_fee_tracker.getLatestGasEstimates()  
            elapsed_time = time() - interval_start
            current_dt = datetime.now()
            current_minute = current_dt.minute
            if((start_minute == current_minute) and (interval > elapsed_time)):
                sleep(interval - elapsed_time)
    else: 
        gas_fee_tracker = GasTrackerAPI()
        gas_fee_tracker.getLatestGasEstimates()

        