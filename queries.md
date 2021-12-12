## Queries

### Query 1

http://localhost:8983/solr/shows/query?q=english&q.op=AND&defType=edismax&indent=true&debugQuery=false&qf=language%5E2%20summary&rows=20&tie=1

### Query 2

http://localhost:8983/solr/shows/query?q=title:Doing%20originCountry:%22United%20States%22%20startYear:%5B2017%20TO%202021%5D&q.op=AND&defType=edismax&indent=true&tie=1

### Query 3

http://localhost:8983/solr/shows/select?defType=edismax&indent=true&q.op=AND&q=rating%3A%5B7%20TO%20*%5D%20startYear%3A%5B2010%20TO%20*%5D%20endYear%3A%5B*%20TO%202020%5D%20episodes%3A%5B10%20TO%20*%5D%20certificate%3A%22Australia%22&rows=100&sort=rating%20DESC&tie=1

### Query 4

http://localhost:8983/solr/shows/select?indent=true&q.op=AND&q=rating%3A%5B7%20TO%20*%5D%20startYear%3A%5B2010%20TO%20*%5D%20endYear%3A%5B*%20TO%202020%5D%20episodes%3A%5B10%20TO%20*%5D%20(certificate%3AR%C3%BAssia%20OR%20certificate%3APortugal)&sort=numVotes%20DESC

rating:[7 TO *] startYear:[2010 TO *] endYear:[* TO 2020] episodes:[10 TO *] (certificate:Rússia OR certificate:Portugal)

### Query 5

http://localhost:8983/solr/shows/select?indent=true&q.op=OR&q=(cast%3A%22DB%22%20cast%3A%22Lesley%20Ann%22%20cast%3A%22jk%22%20cast%3AMatt)%20AND%20genres%3A%22Action%22&rows=30&sort=episodes%20ASC