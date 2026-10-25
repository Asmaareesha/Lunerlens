# LunarLens

**An interactive lunar landing-site explorer for understanding the engineering trade-offs behind future Moon missions.**

[**Explore the live website →**](https://asmaareesha.github.io/Lunerlens/) · [View the source code](https://github.com/Asmaareesha/Lunerlens)

LunarLens is an independent space-science project by **Asma Areesha Hanifi**. It compares seven lunar landing sites by looking at three important mission considerations: sunlight for power, Earth visibility for communication, and potential access to water ice.

No single site is best at everything. LunarLens lets users explore how the date and mission priorities affect the ranking, making the trade-offs easier to understand.

This project was inspired by the problem behind NASA's Space Apps challenge on comparing lunar landing sites, sunlight, and communication windows. It is an independent project and is **not affiliated with or endorsed by NASA**.

## Explore the project

- **Interactive Moon view:** Rotate the Moon and explore landing sites on the near side, far side, and south pole.
- **Time exploration:** Move through a 30-day window, play the timeline, or return to the current date setting.
- **Sunlight and communication:** Inspect how the Sun's elevation and Earth's visibility change over time at a selected site.
- **Site ranking:** Compare seven candidate sites using scores that respond to the selected date and mission priorities.
- **Adjustable mission priorities:** Change the relative importance of power, Earth communication, and water-ice access, then observe how the ranking changes.
- **Model explanation:** Review the assumptions and limitations behind the calculations.

## Why these factors matter

### 1. Sunlight for power

Surface equipment may rely on solar power. How much sunlight a location receives, and how long its night lasts, affects how a mission could plan energy generation and storage.

### 2. Earth visibility for communication

A lander needs a communication path to Earth, directly or through a relay. Earth visibility changes with location and lunar geometry. Locations on the far side cannot communicate directly with Earth through the Moon.

### 3. Potential water-ice access

Water ice is an important resource to investigate for future exploration. LunarLens includes a **rough qualitative ice-access score**, not a measurement or confirmation that ice is present at a specific site.

These factors can compete with one another. The tool is designed to help users explore those trade-offs rather than claim that one location is universally best.

## Built with

- **HTML** for the page structure
- **CSS** for layout, styling, responsive presentation, and visual controls
- **JavaScript** for lunar geometry approximations, site calculations, scoring, interaction, and visualization
- **HTML Canvas** for the interactive Moon and visual data displays
- **Python and Skyfield** in `ephemeris_skyfield.py` as an example of how the approximate geometry could be replaced with ephemeris-based calculations

The published website is a static site. The main interactive experience runs in the browser without requiring a backend or package installation. The Python script is a supplementary development/reference tool and is not required to open the live website.

## Try it yourself

1. Open [LunarLens](https://asmaareesha.github.io/Lunerlens/).
2. Select the **Near side**, **South pole**, or **Far side** view.
3. Drag the Moon to rotate it.
4. Select a landing site from the map or the site ranking.
5. Use the timeline controls to explore the next 30 days.
6. Adjust the **Power**, **Earth link**, and **Water ice** priorities.
7. Observe how the ranking and site conditions change.

### Questions to investigate

- Which sites benefit most when power becomes the highest priority?
- How does Earth visibility differ between near-side and far-side sites?
- Why can a site with favorable sunlight still present communication challenges?
- How does changing the date affect the site ranking?
- How would more accurate terrain and lighting data change the conclusions?

## How the model works

The current browser model uses simplified geometry to make the main relationships interactive.

- The Sun's direction follows an approximate **29.53-day lunar cycle**.
- The model includes the Moon's axial tilt of about **1.5°** and approximate lunar libration for Earth's apparent direction.
- Solar and Earth elevation at a site are calculated using spherical geometry.
- Over a 30-day window, the tool estimates the fraction of time sunlight is available, the fraction of time Earth is visible, and the longest continuous night.
- A weighted score combines power, Earth-link, and ice-access priorities. The ranking responds to the selected weights.

For more implementation detail, see [`CODE_WALKTHROUGH.md`](CODE_WALKTHROUGH.md).

## Scientific assumptions and limitations

LunarLens is an **educational exploration tool**, not a validated lunar mission-planning system.

- **Approximate positions:** The browser model does not use full, high-precision ephemeris data for the Sun, Moon, and Earth.
- **Terrain is not modeled:** Local hills, crater rims, and horizon obstructions can strongly affect sunlight and line of sight. Small offsets stand in for high ground at some sites.
- **Ice estimates are qualitative:** The ice-access score is not a measurement, detection, or guarantee of accessible water ice.
- **Simplified scoring:** The weighted score reflects the priorities selected by the user, not an official mission assessment or a universal scientific ranking.
- **Limited time window:** The displayed 30-day analysis is a simplified view of changing conditions, not a complete mission-duration simulation.

The project identifies Malapert and the Chang'e-4 landing region as examples checked against lunar research and mission sources. These checks do not validate every approximation or score in the application.

## Run locally

The main website is static and does not need a build step.

```bash
git clone https://github.com/Asmaareesha/Lunerlens.git
cd Lunerlens
```

Open `index.html` in a modern browser. An editor with a local static-server preview can also be used during development. Google Fonts requires an internet connection to load the preferred typefaces; fallback fonts are provided.

### Optional Python ephemeris helper

The repository includes `ephemeris_skyfield.py`, a supplementary script illustrating how ephemeris data could be used in a more precise model. It is **not needed** to run the browser-based website. Consult that file for its specific requirements before running it.

## Repository structure

```text
Lunerlens/
├── index.html              # Interactive web application
├── README.md               # Project overview and getting-started guide
├── CODE_WALKTHROUGH.md     # Detailed implementation walkthrough
├── ephemeris_skyfield.py   # Supplementary ephemeris example
└── screenshot.png          # Project screenshot
```

## Future improvements

Potential next steps include:

- Replace approximate Sun and Earth directions with verified ephemeris data.
- Incorporate lunar elevation models, terrain, and illumination maps.
- Improve the evidence behind water-ice accessibility estimates.
- Validate the scoring approach against published mission studies.
- Add more detailed citations and uncertainty ranges for individual sites.
- Add automated tests for geometry, visibility calculations, and ranking behavior.
- Improve text alternatives and keyboard accessibility for interactive visualizations.

## Sources and further reading

The project notes the following source checks for its example sites and mission context:

- [NASA](https://www.nasa.gov/) — lunar exploration and Artemis mission information
- [Lunar Reconnaissance Orbiter Camera (LROC), Arizona State University](https://www.lroc.asu.edu/) — lunar surface imagery and location information

The site coordinates and source notes are provided in the application. Consult the original scientific publications and mission documentation before using any values for research or mission decisions.

## Author

**Asma Areesha Hanifi**

- **Live website:** https://asmaareesha.github.io/Lunerlens/
- **GitHub repository:** https://github.com/Asmaareesha/Lunerlens

## License

No license is specified in this README. Unless a license is added to the repository, others should not assume that they have permission to reuse, redistribute, or modify the project. Add a `LICENSE` file if you want to grant permissions under a chosen open-source license.
