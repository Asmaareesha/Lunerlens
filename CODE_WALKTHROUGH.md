# LunarLens code walkthrough

Open `index.html` in a text editor. Everything is in the `<script>` at the bottom. Read it in this order.

## 1. The data: `SITES`
Each site has a name, latitude, longitude, an `ice` score (0 to 1), a `lift` (a small elevation offset for high ground), and a note. Latitude is negative in the south. Longitude is positive in the east.

## 2. Where are the Sun and Earth? `geo(jd)`
`jd` is the Julian date (days since 4713 BC), a simple way to count time.
- **Sun longitude (`sl`)**: the Moon's phase is how far through the 29.53-day cycle it is. At new moon the Sun is over the far side (180 degrees). At full moon it is over 0 degrees. So `180 - 360 * phase`.
- **Sun latitude (`sb`)**: the Moon's axis is tilted about 1.54 degrees, so the Sun wanders up to 1.54 degrees north and south over a year. I used a cosine with a 346.62-day period (the eclipse year).
- **Earth longitude and latitude (`el`, `eb`)**: libration. The Moon rocks slightly, so Earth is not always at 0, 0 in the Moon's sky. Longitude swings about 7.9 degrees and latitude about 6.7 degrees. I used sine waves with the matching periods.
These are approximations. Real values come from JPL ephemeris data (see `ephemeris_skyfield.py`).

## 3. The key formula: `elev(lat, lon, b, l)`
The elevation of a body above the horizon at a site, where the body is directly overhead at latitude `b` and longitude `l`:

    sin(elevation) = sin(lat) sin(b) + cos(lat) cos(b) cos(lon - l)

This is the spherical law of cosines. The angle between the site and the point where the body is overhead is the body's distance from the zenith, so elevation = 90 degrees minus that angle. The same formula works for the Sun and for Earth.

## 4. Statistics: `stats(site, jd0)`
Steps through 30 days in 2-hour samples. It counts samples where the Sun is above the horizon, samples where Earth is, and tracks the longest run with no sunlight.

## 5. Score: `scoreOf`
    score = 100 * (wPower * sunFraction + wComms * earthFraction + wIce * ice) / (sum of weights)

## 6. Drawing the Moon: `drawMoon`
For each pixel inside the disc it works backwards from screen position to latitude and longitude (an inverse orthographic projection), then uses `elev` to decide how bright that spot is. `project` does the opposite for the site markers.

## Break it on purpose
Change one thing, reload, and write down what happened and why.
1. In `geo`, change `7.9` to `30`. What happens to the far-side edge of Earth visibility?
2. Set `1.54` to `20`. Which sites change most, and why the polar ones?
3. In `stats`, change `a>0` to `a>5`. What does this model? (Hint: a real lander needs the Sun a few degrees up.)
4. Change a site's `lift` to `0` for Shackleton. What happens to its score?
5. Set all three weights to 0. Why does the code use `||1`?

## Rewrite one part yourself
Pick one and write your own version without looking, then compare:
- `elev`: derive it from a diagram of two points on a sphere.
- `scoreOf`: add a fourth criterion (for example the longest-night length) and decide how to normalise it.
- `stats`: also return the number of separate sunlit periods.

## Questions to be ready to answer
- Why do most Moon sites have about 14 days of night, but polar peaks can stay lit?
- Why does the far side never see Earth, and what does a relay satellite do?
- What does the model ignore, and how would that change the results?
- How would you test that the numbers are right? (Compare against Skyfield or NASA data.)
