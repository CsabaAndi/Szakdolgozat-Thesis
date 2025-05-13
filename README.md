# Install manual

# Python part

## Requirements

- python 3.12.x

- python3.12 -m venv .venvs/env (in Code folder)
- activate env:
	- linux & macOS: "source .venvs/env/bin/activate"
	- windwos: .venvs\env\Scripts\activate
- pip install -r pie-requirements.txt

or on linux inside Code:

- chmod +x setup-env
- source setup-env.sh

to delete envs:

- chmod +x clean-env.sh
- ./clean-env.sh


## Start

- cd to cakdoga
- activate env:
	- linux & macOS: "source .venvs/env/bin/activate"
	- windwos: .venvs\env\Scripts\activate
- cd to src/
- execute: "python -m main"



# Webscraper Demo


## Requirements

- node.js 20.x.x (20.19.0) 
- Playwright 1.45.0 with chromium 127 (127.0.6533.17)
	- you may need to install chromium for playwright: "npx playwright install-deps chromium"
	- help - https://playwright.dev/docs/browsers

- cd to webscrape-app
- npm install

## Start

- from Python part:
	- only the scraper demo
		- cd to Code/src: 
		- execute: "python -m webscrape_start run_datanode_app"

	- from the streamlit webinterface:
		- cd to Code/src:
		- python -m main
		- navigate to the Data Collection page
		- start Demo

- From webscrape-app:
	- cd to Code/webscrape-app/src
	- execute: "npx ts-node scraper.ts"
		



# User manual/Guide

- will be updated soon

