#!/bin/bash

curl=$(which curl)
url=$(echo $1)
outfile="output.txt"

function get_page() {
    $curl -s -o $outfile $url
    check_errors
}

function get_items() {
    sed -e 's/<item>\(.*\)<\/item>/\1/' output.txt | sed 's/<item>/\n<item>/' | sed 's/<\/item>/<\/item>\n/' | sed '0,/<item>/s//\n<item>/' | tac | awk '!f && /<\/item>/ { f=1 }; f' | tac | awk '!f && /<item>/ { f=1 }; f' > all_items.txt
}

function create_html() {
    tr -d '\r' < all_items.txt | awk '{print > ("item" ++CNT ".html")}' RS=""
}

function check_errors() {
    [ $? -ne 0 ] && echo "Error downloading page..." && exit -1
}

get_page
get_items
create_html
rm output.txt
rm all_items.txt