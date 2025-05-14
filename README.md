# Overall Approach

My overall approach is to understand the requirements by breaking it into each step.  
Once I get the whole workflow, I structure all the functions/requirements to work properly first.
I will do the planning, designing, development, and the testing to ensure the program runs smoothly.  
Then I will clean up the code into modules for better readablity.

# Design Decisions

Based on my previous experience, I knew I had to use Pandas to read in the data files.  
I would use a groupby method to seperate each category and use arithmetic functions to solve the total transactions, average values, and total quantities.  
I make sure the program does error handlings such as, missing values, missing columns, incorrect formats.

# Run & Test Instructions

### Running the program

Make sure the `sales_data.csv` and the `product_data.json` file exists in the directory.  
In the bstock directory, to run the program:

> `python process_data.py`

Check the terminal messages to see if the program was a success.  
If it was successful, open the `aggregated_report.csv`.

### Testing the program

In the bstock directory, to run the tests:

> `pytest test_data_processing.py`
