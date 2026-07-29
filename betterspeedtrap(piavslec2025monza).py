import fastf1
from fastf1 import plotting, utils
import matplotlib.pyplot as plt
plotting.setup_mpl(mpl_timedelta_support=True)
fastf1.Cache.enable_cache('/Users/annikababerwal/GCSE_CS/f1_cache')  # pls change cuz ur defo not me so u cant really access my fastf1 folder but its literally a pip install away so ye
session = fastf1.get_session(2025, 'Monza', 'R') #change the race and the year but antonelli's only been around hor 2025 and 2026 so change the driver if u wanna go further back
session.load()
pia_lap = session.laps.pick_driver('PIA').pick_fastest()
lec_lap = session.laps.pick_driver('LEC').pick_fastest()
pia_tel = pia_lap.get_car_data().add_distance()
lec_tel = lec_lap.get_car_data().add_distance()
delta_time, ref_tel, compare_tel = utils.delta_time(pia_lap, lec_lap)
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(12, 8), sharex=True,
    gridspec_kw={'height_ratios': [3, 1]}
)
ax1.plot(pia_tel['Distance'], pia_tel['Speed'], color="#F3A72F", label='PIA')
ax1.plot(lec_tel['Distance'], lec_tel['Speed'], color='#E8002D', label='LEC')
ax1.set_ylabel('Speed (km/h)')
ax1.set_title('PIA vs LEC — Fastest Lap Speed Trace + Delta — 2025 Italian GP')
ax1.legend()
ax2.plot(ref_tel['Distance'], delta_time, color="#FF6600")
ax2.axhline(0, color='grey', linewidth=0.8, linestyle='--')
ax2.set_xlabel('Distance (m)')
ax2.set_ylabel('Gap (s)\nLEC ahead ^ / PIA ahead v')
#so this has 2 graphs the first is top speed the 2nd is delta 
plt.tight_layout()
plt.show()

