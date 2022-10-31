# DS2002-Project1

Skye Jung (hsj5sn)

## Data File

The Students Performance in Exams dataset was found on Kaggle, and it includes information on the average exam scores for math, reading, and writing, alongside demographics of each observation. There are 8 columns and 1000 records, with the variables being the following: gender, race/ethnicity, parental level of education, lunch type (standard or free/reduced), completion of test preparation, math score, reading score, and writing score.

data link: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

## Data Processor

The code takes in the file (CSV of the students performance dataset) and converts the original data set into a JSON file (attached, named examsjson). Then it modifies the data set and adds two new columns: average total test score for each record and whether the each record has a total average above or below the average of all the records' exam scores. Then, it prints out a brief summary of the data set, including the number of columns, rows, and the first ten observations of the dataset. The last section uses try/except statements to produce informative errors if the program is unable to complete an operation. The user inputs a gender and racial group and the program outputs the total average exam score for the given demographics. If the user inputs an invalid gender or racial group (not included in the data), it outputs an error message.

## Benchmarks 

1. Retrieves a remote data file by URL
2. Converts the general format and data structure of the data source
3. Modifies the number of columns from the source to the destination
4. Generates a brief summary of the data file ingestion after it has processed and output it to the user
5. Produces informative errors should it be unable to complete an operation
