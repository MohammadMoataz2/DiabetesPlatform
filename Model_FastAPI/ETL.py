import pandas as pd
import numpy as np
import pickle



def ETL_final(feature_list,int_age = 5):

    loaded_model = pickle.load(open(r"catboost_model.pkl", 'rb'))

    df = {
        "Pregnancies":[feature_list[0]],
        "Glucose":[feature_list[1]],
        "BloodPressure":[feature_list[2]],
        "SkinThickness":[0],
        "Insulin":[feature_list[3]],
        "BMI":[feature_list[4]],
        "DiabetesPedigreeFunction":[0],
        "Age":[feature_list[5]],

    }
    df = pd.DataFrame(df)


    df_interval = df.copy()
    df_interval


    max = 81
    min = 21
    interval_jump = int_age

    list_interval_Age = []

    for i in range(min,max+1,interval_jump):
        if i == (max - (interval_jump)):
            list_interval_Age.append(f"{i}-{max}")
            break

        if i == min:
            list_interval_Age.append(f"{i}-{i + interval_jump -1}")
            continue
            
        list_interval_Age.append(f"{i}-{i+interval_jump-1}")

   

    if interval_jump == 5:
        cutoff_Age = [20,25,30,35,40,45,50,55,60,65,70,75,81]

    if interval_jump == 10:
        cutoff_Age = [20,30,40,50,60,70,81]

    df_interval['Age_interval'] = pd.cut(df['Age'],bins = cutoff_Age,labels = list_interval_Age)




    cutoff_Blood = [0,59,79,89,119,300]

    list_interval_Blood = ['Low Blood Preasure (dangerous)','Normal or Elevated','High Blood Preasure Stage 1',"High Blood Preasure Stage 2","Hypertensive Crisis"]
    df_interval['BloodPressure_interval'] = pd.cut(df['BloodPressure'],bins = cutoff_Blood,labels = list_interval_Blood)




    cutoff_Glucose= [0,139,199]

    list_interval_Glucose = ['Normal Diabetes ( > 140 )','Pre Diabetes ( 140-199 )']
    df_interval['Glucose_interval'] = pd.cut(df['Glucose'],bins = cutoff_Glucose,labels = list_interval_Glucose)
    


    cutoff_BMI= [0,18.4,24.5,29.9,34.9,100]

    list_interval_BMI = ['UNDERWEIGHT','NORMAL',"OVERWEIGHT","OBESE","EXTREMELY OBESE"]
    df_interval['BMI_interval'] = pd.cut(df['BMI'],bins = cutoff_BMI,labels = list_interval_BMI)



    


    return loaded_model.predict(df_interval[loaded_model.feature_names_])[0]



