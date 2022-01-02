# Information Search System (PRI, Group 34)

### Create the virtual environment and install the requirements
From the **src** folder of the repository:

#### Ubuntu
```properties
1. python3 -m venv env
2. source env/bin/activate
3. pip3 install -r ../requirements.txt
```

#### Windows
```properties
1. py -m venv env
2. .\env\Scripts\activate.bat
3. pip install -r ..\requirements.txt
```
***

## Run the project

1. **Data Cleaning**: Generate the clean data from the original Netflix dataset
> `make cleaning`
- outputs datasets/cleaning.csv

2. **Data Scraping**: Apply scraping to the dataset, completing missing or invalid values
> `make scraping` 
- outputs datasets/final_netflix_list.csv

3. **Data Exploration**: Explore the dataset by generating some relevant graphs and analyzing statistics
> `make exploration`
- outputs many plots and a statistics table in the **plots** folder

4. **Solr**: Start Solr and upload schema and data
> `make run_solr`
- prepares Solr and starts running it in the address http://localhost:8983/

5. **Clean Cache**: Empty the Python cache folders (\_\_pycache\_\_) and the **plots** folder
> `make clean`

## User Interface for the Search System

### Run the Interface:

```properties
1. npm install
2. npm start
```

The User Interface becomes available in the address http://localhost:3000/