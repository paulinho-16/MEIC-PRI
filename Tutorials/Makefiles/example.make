SHELL := /bin/bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c

.PHONY: get_pages

get_pages:
	@counter=1;
	while IFS="" read -r p || [ -n "$$p" ]
	do
		mkdir -p "page$${counter}";
		cd "page$${counter}";
		let "counter+=1";
		../get_news_items.sh $$p
		cd ..
	done < example.txt