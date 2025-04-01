# Install manual

# Cakdoga

## Requirements

- python 3.12.x (3.12.9)

- python -m venv .venvs/env (in cakdoga folder)
- activate env:
	- linux & macOS: "source .venvs/env/bin/activate"
	- windwos: .venvs\env\Scripts\activate
- pip install -r requirements-cakdoga.txt


## Start

- cd to cakdoga
- activate env:
	- linux & macOS: "source .venvs/env/bin/activate"
	- windwos: .venvs\env\Scripts\activate
- cd to src/
- execute: "python -m main"
- for args use: "--help"



# Webscraper


## Requirements

- node.js 20.x.x (20.19.0) 
- Playwright 1.45.0 with chromium 127 (127.0.6533.17)
	- you may need to install chromium for palywright: "npx playwright install-deps chromium"
	- help - https://playwright.dev/docs/browsers

- cd to webscrape-app/datanode
- npm install

## Start

- from .py file , only the scraer
	- From Cakdoga: 
		- cd to src/
		- execute: "python -m webscrape_start run_datanode_app"
	- From datanode
		- cd to cakdoga/webscrape-app/datanode/src
		- execute: "npx ts-node scraper.ts"
		
- from the streamlit webinterface:
	- cd to src/
	- python -m main
	- navigate to the webscrape section
	- start DataNode
	- (Terminate DataNode)


# User manual


- TBD