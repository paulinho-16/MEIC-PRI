# Information Search System (PRI, Group 34)

## Run the project

1. **Solr**: Start Solr and upload schema and data
> `docker build ./solr -t solr`
> `docker run -p 8983:8983 --name solr solr`
- prepares Solr and starts running it in the address http://localhost:8983/

## User Interface for the Search System

### Run the Interface:

From the **src/interface** folder of the repository:

```properties
1. npm install
2. npm start
```

The User Interface becomes available in the address http://localhost:3000/