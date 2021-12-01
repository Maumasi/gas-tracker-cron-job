from src.app.models.GasTrackerAPIModel import GasTrackerAPI

if (__name__ == '__main__'):
    gas_fee_tracker = GasTrackerAPI()
    gas_fee_tracker.getLatestGasEstimates()

    