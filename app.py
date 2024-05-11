import pandas as pd
import streamlit as st
from PIL import Image
import pickle


def process_main_page():
  show_main_page()
  process_side_bar_inputs()


def show_main_page():
  image = Image.open('data/good-credit-score.jpg')

  resized_image = image.resize((image.width // 2, image.height // 2))

  st.set_page_config(
    layout="wide",
    initial_sidebar_state="auto",
    page_title="credit-score",
    page_icon=resized_image,

  )

  st.write(
    """
    # Machine learning service for predicting the risk of payment delinquency of a bank customer
    #### We determine which of the clients will be overdue for their loan for 90 days or more.
    """
  )

  st.image(resized_image)

def sidebar_input_features():
  age = st.sidebar.slider("Age", min_value=1, max_value=110, value=18,
                          step=1)
  DebtRatio = st.sidebar.number_input("Monthly expenses:", value=0)

  MonthlyIncome = st.sidebar.number_input("Monthly income:", value=0)

  NumberOfOpenCreditLinesAndLoans = st.sidebar.number_input("Number of open credit lines and loans:", value=0)

  RevolvingUtilizationOfUnsecuredLines = st.sidebar.number_input("Total balance on credit cards:", value=0)

  NumberOfDependents = st.sidebar.number_input("Number of dependents :", value=0)


  NumberOfTime30_59DaysPastDueNotWorse = st.sidebar.slider("How many times has there been a delay of 30-59 days in the last 2 years", min_value=0, max_value=100, value=1,
                          step=1)
  NumberOfTimes90DaysLate = st.sidebar.slider("How many times has there been a delay of 90 and more days in the last 2 years", min_value=0, max_value=100, value=1,
                          step=1)
  NumberOfTime60_89DaysPastDueNotWorse = st.sidebar.slider("How many times has there been a delay of 60-89 days in the last 2 years", min_value=0, max_value=100, value=1,
                          step=1)


  if NumberOfOpenCreditLinesAndLoans < 3:
    RealEstateLoansOrLines = 0
  elif NumberOfOpenCreditLinesAndLoans < 6:
    RealEstateLoansOrLines = 1
  elif NumberOfOpenCreditLinesAndLoans < 15:
    RealEstateLoansOrLines = 2
  elif NumberOfOpenCreditLinesAndLoans < 25:
    RealEstateLoansOrLines = 3
  else:
    RealEstateLoansOrLines = 4


  if age <21:
    group_age = 0
  elif age <35:
    group_age = 1
  elif age < 50:
    group_age = 2
  elif age < 65:
    group_age = 3
  else:
    group_age = 4


  data = {
    'RealEstateLoansOrLines': RealEstateLoansOrLines,
    'GroupAge': group_age,
    'RevolvingUtilizationOfUnsecuredLines': RevolvingUtilizationOfUnsecuredLines,
    'age': age,
    'NumberOfTime30-59DaysPastDueNotWorse': NumberOfTime30_59DaysPastDueNotWorse,
    'DebtRatio': DebtRatio,
    'MonthlyIncome': MonthlyIncome,
    'NumberOfOpenCreditLinesAndLoans': NumberOfOpenCreditLinesAndLoans,
    'NumberOfTimes90DaysLate': NumberOfTimes90DaysLate,
    'NumberOfTime60-89DaysPastDueNotWorse': NumberOfTime60_89DaysPastDueNotWorse,
    'NumberOfDependents': NumberOfDependents
  }
  df = pd.DataFrame(data, index=[0])

  return df

def write_user_data(df):
  st.write("## Your data")
  st.write(df)

def write_prediction(prediction):
  st.write("## Prediction")
  st.write(f'The probability of delayed payments: {prediction *100}%')
  if prediction < 0.5:
    image = Image.open('data/approved.jpg')

  else:
    image = Image.open('data/not-approved.jpg')

  resized_image = image.resize((image.width // 2, image.height // 2))
  st.image(resized_image)

def process_side_bar_inputs():
  st.sidebar.header('User-defined parameters')
  user_input_df = sidebar_input_features()
  write_user_data(user_input_df)

  with open('model.pickle', 'rb') as f:
    model = pickle.load(f)
    pred = model.predict_proba(user_input_df)[:, 1]

    write_prediction(pred)


if __name__ == "__main__":
    process_main_page()
