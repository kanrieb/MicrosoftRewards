## Overview

A program written in Python that automatically completes the Microsoft Rewards daily searches to get points.
This project was created using Selenium and gekodriver (for Firefox) and implements a headless browser so that your browsing can continue uninterrupted while the program runs. Easily install and set up, then run daily to get all the points possible!
(Note: This project was built and tested on MacOS. Other environments may require different configuration.)

## Installation Instructions

1. Download or clone the repository to your computer
2. Create a `login.json` file with your Microsoft credentials (the JSON format is given in `login.example.json`)
3. Install Selenium (`pip3 install selenium`) and geckodriver (`npm install`)

## Run Instructions

To run the desktop search (runs 30 times + 1 extra so that login registers):
`python3 main.py`

To run the mobile search (runs 21 times):
`python3 main.py --mobile`
