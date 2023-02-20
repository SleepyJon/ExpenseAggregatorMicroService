# ExpenseAggregatorMicroService

## Communication Contract:

### How to REQUEST data:
- The Expense Aggregator microservice is requested by looking for a file named 'bank.csv' in the same directory as the microservice .py files. It can be requested by the intial load of the 'bank.csv' in the directory. It can also be requested if the 'bank.csv' is modified (i.e. an updated bank statement is loaded).

### How to RECEIVE data:
- When the Expense aggregator microservice is requested, the microservice aggregates the 'bank.csv' by category and saves the results to the 'bank_by_category.csv" which is saved in the same directory as the 'bank.csv'.
