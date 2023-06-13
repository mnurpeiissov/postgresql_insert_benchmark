# Inserting Data to PostgreSQL with Python

This repository contains a benchmark of different methods for inserting data from Python to PostgreSQL. The methods compared include inserting row by row, using the executemany statement, using the execute_batch statement, and using the cur_expert method.

## How to use

You can try and test the every insert method yourself. You will need to create a virtual environment and install the packages in `requirements.txt`. Furthermore, you will need to createte `.env` file and fill out credentials to connect to your postgres database:


`host=`

`port=`

`user=`

`password=`

`database=`



## Methods

The tests are done using 42000 rows csv file. I used Postgresql as database and psycopg2 to connect to postgresql from python. Corresponding python scripts can be found above. 

### Inserting One by One
The first method involves iterating over a CSV file and inserting each row one by one. This approach is the most straightforward but can be inefficient when dealing with large datasets. For each row in the CSV file, a separate SQL INSERT statement is executed, resulting in a high number of individual queries. This method can be time-consuming and resource-intensive.

Benchmark results:

`Time: 33.16 seconds
Max memory: 25.640625 MB
Min memory: 25.453125 MB`

### Inserting with executemany Statement
The executemany statement provided by the Psycopg2 library allows for inserting multiple rows with a single SQL statement. It takes a parameterized SQL statement and a list of tuples containing the values to be inserted. This method is expected to execute the SQL statements in bulk, rather than sending them one by one. However, the performance improvement is not significant compared to inserting row by row.

Benchmark results:

`Time: 31.99 seconds
Max memory: 25.484375 MB
Min memory: 25.328125 MB`

### Inserting with execute_batch Statement
The execute_batch statement is another approach provided by Psycopg2 for bulk insertion of rows. It allows you to execute multiple SQL statements as a batch, reducing the number of round trips to the database. This method provides better performance than both inserting one by one and using the executemany statement.

Benchmark results:

`Time: 3.653 seconds
Max memory: 27.75 MB
Min memory: 27.625 MB`

### Inserting with cur_expert
The cur_expert method is a specialized approach provided by Psycopg2 for efficient bulk insertion of data. It leverages the PostgreSQL COPY command, which is optimized for high-speed insertion of large amounts of data. The cur_expert method allows you to execute the COPY command directly with the data provided as a file-like object or an iterable of strings.

Benchmark results:

`Time: 0.2448 seconds
Max memory: 25.65625 MB
Min memory: 25.46875 MB`

## Conclusion

Based on the benchmark results, the execute_batch and cur_expert methods are the most efficient ways to insert data into PostgreSQL from Python.

The execute_batch statement provides a significant improvement in performance compared to inserting row by row or using the executemany statement. It reduces the number of round trips to the database and executes multiple SQL statements as a batch, resulting in faster insertion times.

The cur_expert method, utilizing the PostgreSQL COPY command, demonstrates the best performance among all the tested methods. It leverages the database's optimized mechanism for bulk data insertion, resulting in the fastest insertion times.
