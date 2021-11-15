SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c

.PHONY: all

all: cleaning scraping exploration

cleaning:
    python cleaning.py

scraping: cleaning
    python scraping.py

exploration: scraping
    python exploration.py

clean:
    rm -rf __pycache__
    rm plots/