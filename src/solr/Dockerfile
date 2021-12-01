FROM solr:8.10

COPY netflix_list.json /data/netflix_list.json

COPY simple_schema.json /data/simple_schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
