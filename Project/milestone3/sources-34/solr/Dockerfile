FROM solr:8.10

COPY netflix_list.json /data/netflix_list.json

COPY query1.json /data/query1.json

COPY query2.json /data/query2.json

COPY query3.json /data/query3.json

COPY query4.json /data/query4.json

COPY query5.json /data/query5.json

COPY schema.json /data/schema.json

COPY synonyms.txt /data/mysynonyms.txt

COPY solrconfig.xml /data/config.xml

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
