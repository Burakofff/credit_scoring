
**Description**
Our task is to predict the target variable based on various characteristics of clients - whether the client was overdue for 90 days or more or not (and if he was, the bank will not issue a loan to this client, otherwise it will be)

You can try this app [here](https://credit-scoring-ml-service.streamlit.app/)!

**Files**:
- `app.py`: streamlit app file
- `model.ipynd`:  a notebook with our model
- `model.pickle`:  pre-trained model
- `credit_scoring.csv`: data file
- `requirements.txt`: package requirements files


To do this, we used the credit_scoring dataset, the description of which you can see below
**Target variable**
- `SeriousDlqin2yrs`: the client was overdue for 90 days or more


**Features**
- `RevolvingUtilizationOfUnsecuredLines`: total balance on credit cards and personal lines of credit except real estate and no installation debt
like car loans divided by the sum of credit limits)
- `age`: age of the borrower
- `NumberOfTime30-59DaysPastDueNotWorse`: how many times in the last 2 years there has been a delay of 30-59 days
- `DebtRatio': monthly expenses (payment of debts, alimony, living expenses) divided by monthly income
- `MonthlyIncome`: monthly income
- `NumberOfOpenCreditLinesAndLoans`: the number of open loans (e.g. car loan or mortgage) and credit cards
- `NumberOfTimes90DaysLate`: how many times there was a delay (90 days or more)
- `RealEstateLoansOrLines`: the encoded number of loans (including secured housing) - the larger the letter code, the more loans
- `NumberOfTime60-89DaysPastDueNotWorse`: how many times in the last 2 years has the borrower delayed payment by 60-89 days
- `NumberOfDependents`: the number of dependents in care (spouses, children, etc.)
- `GroupAge`: encoded age group - the larger the code, the greater the age
