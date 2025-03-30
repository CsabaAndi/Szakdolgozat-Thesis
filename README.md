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



# Webscraper


## Requirements

- node.js 20.19.0 

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
