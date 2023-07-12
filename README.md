# Unit Testing for Telecommunication Billing Data Pipeline

<h3>Background Information</h3>
You are working on a project related to telecommunication billing data. As part of the project, a
data pipeline has been provided to you. The data pipeline is responsible for extracting data from
a CSV file, performing transformations using pandas, and storing the transformed data in
another CSV file. Your task is to write unit tests for the functions in the data pipeline using the
<b>unittest</b> framework.

<h3>Problem Statement</h3>
Your goal is to develop robust unit tests for the three functions in the data pipeline:
data_extraction, data_transformation, and data_loading. These tests ensure the data
pipeline functions correctly and handle various scenarios and edge cases.

<h3>Guidelines</h3>
● Use the unittest framework to create test cases for each function in the data pipeline.
<br>● Write at least three test cases for each function, covering different scenarios and edge
cases.
<br>● Ensure that your tests are independent and do not rely on each other.
<br>● Name your test methods descriptively to indicate the scenario being tested.
<br>● Use assertions to validate the expected behavior of each function.
<br>● Provide informative error messages when assertions fail to aid in debugging.

<h3>Solution</h3>
Unit test .py file : 
Run the tests on cli using the command : python telco_test.py
Requirements - 2 csv files are needed in same directory:
1- test_data.csv ... this contains the source telco data
2- empty_data.csv ... blank csv needed for the data_extraction test case 2

When all tests successful you get OK message as seen below:

C:\Users\Joe Kibera\venv>python telco_test.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.015s

OK


