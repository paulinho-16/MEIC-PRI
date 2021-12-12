SHELL := /bin/bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c

PYTHON = ../env/Scripts/python.exe

.PHONY: all

all: cleaning scraping exploration

# Data Cleaning
cleaning:
	$(PYTHON) cleaning.py

# Data Scraping
scraping:
	$(PYTHON) scraping.py

# Data Exploration
exploration:
	$(PYTHON) exploration.py

docker:
	docker build . -t meic_solr
	docker run -p 8983:8983 --name solr meic_solr

solr:
	docker exec solr bin/post -c courses /data/simple_schema.json
	docker exec solr bin/post -c courses /data/query1.json

# Remove generated folders
clean:
	rm -rf __pycache__
	rm -rf plots/