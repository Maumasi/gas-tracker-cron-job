from src.constants import BASE_FEE, ESTIMATED_GAS_PRICE, MAX_GAS_PRICE

# ===========================================================  Crontab technical setup
# These options are assuming that the cron job is set up with
# an run interval of: * * * * * => every minute of every day

# this application uses the https://www.blocknative.com/gas-estimator API to collect gas prices

# =====================================================================================
OPTIONS = {
    # Enable or disable script: boolean
    # True | False
    'ENABLE': True,
    
    # How many times perminute to check the current gas price: int
    #  - Example: 4 => (60 / 4) | AKA every 15 seconds
    # Run once per min: 0 
    # Min value: 1
    # Max value: 30
    'CHECKS_PER_MINUTE': 4,
    
    # This script currently uses Slack to send notifications to alert a user by user ID: string
    'SLACK_USERNAME_TO_NOTIFY': '@U02T62L7Q4C',
    
    # Choose which threeshhold option to use for triggering notifications: BASE_FEE | ESTIMATED_GAS_PRICE | MAX_GAS_PRICE
    'THRESHHOLD_TO_USE': BASE_FEE,
        
    # threshhold options provide a few different rates that you can find on "blocknative.com/gas-estimator"
    # only one option will e used to define the threshhold, which is set the the `THRESHHOLD_TO_USE` property above.
    
    'THRESHHOLD_OPTIONS': {
        # The max threshhold of the base price (in USD) before sending sending a notifications: float
        #  - only used if `'THRESHHOLD_TO_USE': MAX_BASE_FEE`
        'BASE_FEE': 60.0,
        
        # The max threshhold gas price (in USD) before sending sending a notifications: float
        # This is the "estimated" gas price for 99% probability NOT the "max" gas price for 99% probability
        #  - The max threshhold is applied to the 99% probability of success gas rate
        #  - only used if `'THRESHHOLD_TO_USE': ESTIMATED_GAS_PRICE`
        'ESTIMATED_GAS_PRICE': 60.0,
        
        # The max threshhold of the MAX gas price (in USD) before sending sending a notifications: float
        # This is the "max" gas price for 99% probability NOT the "estimated" gas price for 99% probability
        #  - The max threshhold is applied to the 99% probability of success gas rate
        #  - only used if `'THRESHHOLD_TO_USE': MAX_GAS_PRICE`
        'MAX_GAS_PRICE': 180.0,
    },
    
    
    
}