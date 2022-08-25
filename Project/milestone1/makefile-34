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

# Remove generated folders
clean:
	rm -rf __pycache__
	rm -rf plots/