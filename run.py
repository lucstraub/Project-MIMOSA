from datetime import datetime
from mimosa import MIMOSA, load_params

params = load_params()

# Make changes to the params if needed
params["emissions"]["carbonbudget"] = False

model1 = MIMOSA(params)
model1.solve()
model1.save(f"testrun_price_calibrated_MACC_{datetime.today().strftime('%Y-%m-%d')}")
