"""Compute real Sun and Earth elevations at lunar sites with Skyfield (JPL DE421).
UNTESTED STARTER: written without being able to install Skyfield. Check it against
the Skyfield docs page on the Moon / planetary constants and fix anything that differs.
Setup:  pip install skyfield numpy      (first run downloads about 17 MB of data files)
"""
import json
from skyfield.api import load, PlanetaryConstants

SITES = {  # name: (lat, lon) in degrees, east positive
    "Shackleton rim": (-89.9, 0.0),
    "Malapert massif": (-86.0, 0.0),
    "Tranquility Base": (0.67, 23.47),
    "Taurus-Littrow": (20.19, 30.77),
    "Marius Hills": (14.1, -56.8),
    "Schrodinger basin": (-75.0, 132.4),
    "Change-4 site": (-45.46, 177.59),
}

ts = load.timescale()
eph = load("de421.bsp")
pc = PlanetaryConstants()
pc.read_text(load("moon_080317.tpc"))
pc.read_text(load("pck00008.tpc"))
pc.read_binary(load("moon_pa_de421_1900-2050.bpc"))
frame = pc.build_frame_named("MOON_ME_DE421")

# 30 days, every 2 hours, from 2026-11-02 (change as you like)
t = ts.utc(2026, 11, 2, range(0, 24 * 30, 2))
out = {}
for name, (lat, lon) in SITES.items():
    site = eph["moon"] + pc.build_latlon_degrees(frame, lat, lon)
    sun_alt = site.at(t).observe(eph["sun"]).apparent().altaz()[0].degrees
    earth_alt = site.at(t).observe(eph["earth"]).apparent().altaz()[0].degrees
    out[name] = {"sun": [round(float(v), 2) for v in sun_alt],
                 "earth": [round(float(v), 2) for v in earth_alt]}
    print(name, "sunlit:", round(float((sun_alt > 0).mean()), 2),
          "earth in view:", round(float((earth_alt > 0).mean()), 2))

json.dump(out, open("ephemeris.json", "w"))
# Next step: load ephemeris.json in index.html and compare it with the approximate model.
