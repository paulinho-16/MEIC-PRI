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

# Start Solr
run_solr:
	docker build ./solr -t solr
	docker run -p 8983:8983 --name solr solr

# Retrieval Evaluation
evaluation:
	$(PYTHON) evaluation.py

# Remove generated folders
clean:
	rm -rf __pycache__
	rm -rf plots/