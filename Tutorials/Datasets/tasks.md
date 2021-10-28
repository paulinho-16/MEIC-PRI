### Task 1:
`in2csv example.xlsx > example.csv`

### Task 2:
`awk -F, '{print $NF}' example.csv`

### Task 3:
```
ROWS=$(csvsql --query "SELECT * FROM example WHERE Team LIKE '%y%'" example.csv)
echo $ROWS
echo $(($(echo $ROWS | wc -l)-1))
```