# fastf1improvedmonza
last time i did leclerc vs verstappen at monza(i belive i used 2023?) but this time i did an improved one w 2 plots including time delta with leclerc vs antonelli 

## what it does
pulls the race session via fastf1, grabs each driver's fastest lap and builds a two-panel thing speed vs. distance on top (3/4 of the height), and the cumulative time gap on the bottom (1/4). the two panels share an x-axis so everything lines up and looks decent

## requirements
```bash
pip install fastf1 matplotlib
```
python 3.8+ i think but python 3 should be the same ig? i'm not sure but im gonna go with python 3.8+

## setup
change the cache path cz mine is coded to `/users/annikababerwal/gcse_cs/f1_cache`, which nobody else can reach cuz you are not annika baberwal ie: me
therefore pls do:
```python
fastf1.cache.enable_cache('/path/to/your/f1_cache')
```
make the folder first, fastf1 won't create it:
```bash
mkdir -p /path/to/your/f1_cache
```
first run downloads session data, every run after pulls from cache

## usage

```bash
python ant_lec_delta.py
```

## how it reads
- **top panel** is speed (km/h) vs distance (m) apexes and stuff
- **bottom panel** the time gap in seconds. the dashed grey line at zero is the reference. line goes up = leclerc ahead line goes down = antonelli ahead per your axis label.

## notes / things to watch

- **drivers** antonelli's only in the data from 2025 onward bc he was a rookie lsat year, so if you roll the year back further, swap `'ant'` for someone who was actually on the grid (i uploaded a pia v lec also for this reason cuz piastri's been around longer than antonelli)
- **delta direction** `utils.delta_time(ant_lap, lec_lap)` treats the first arg (antonelli) as the reference, so the sign is relative to him. worth double-checking the up/down reads the way your label says before you trust it in a writeup
- `pick_driver` / `pick_fastest` are deprecated in newer fastf1 builds
- fastest laps can come from different laps entirely w different fuel, tyre age, traffic so it's indicative, not rly like quali data bc quali data is stint and tyre specific i would presume

## I AM NOT AFFLILIATED WITH FORMULA 1 THO I WOULD RLY LIKE TO BE 🤪
