
import os
import sys
import datetime
from tabulate import tabulate

import pandas as pd
import numpy as np

import config
# from sympy.sets import conditionset
# from aifc import data

def main():
#     default project directory path
    project_directory_path = os.path.dirname(sys.argv[0])  

#     test missing data file path
    missing_data_path = os.path.join(project_directory_path, config.TEST_MISSING_DATA)  
    
#     test data no missing file path
    no_missing_data_path = os.path.join(project_directory_path, config.TEST_NO_MISSING_DATA)  
    
#     HERE ARE SOME POSSIBLE STEPS:
#     1. REMOVE DUPLICATES (WITH AND WITHOUT CONDITIONS)
#     2. FIND AND REPLACE MESSING DATA
#     3. FIND AND REPLACE DIRT DATA
        
#     1. IMPORT TITANIC DATA FILE
    df_missing_data = pd.read_csv(missing_data_path, sep=",")    
    print(df_missing_data)    
#     print(tabulate(df_missing_data, headers='keys', tablefmt='rst'))

    df_missing_data.head(5)
    
# #     2. GET NUMBER OF ROWS AND COLUMNS
    result = df_missing_data.shape
    print(result)
     
# #     3. GET INDEX, DATATYPE AND MEMORY INFORMATION
    result = df_missing_data.info()
    print(result)
    
#     show summary descriptive stats for numerical columns
    result = df_missing_data.describe()
    print(result)
    
#     frequency distribution values for "four" column
    result = df_missing_data["four"].value_counts()
    print(result)
    
#     check missing values
    result = df_missing_data.apply(lambda x: sum(x.isnull()), axis = 0) 
    print(result)
     
# #     4. REMOVE DUPLICATES ROWS
#     identify which observations are duplicates
    result = df_missing_data.duplicated()
    print(result)   
     
# #     drop duplicates for all columns and keep first
# #     inplace : boolean, default False. Modify the DataFrame in place (do not create a new object)
    result = df_missing_data.drop_duplicates(keep = "first")
    print(result)
     
# #     drop duplicates for column "one" and keep first
# #     result = df_missing_data.drop_duplicates(["one"], keep = "first")
# #     print(result)
#     
# #     drop duplicates for all columns and keep nothing
# #     result = df_missing_data.drop_duplicates(keep=False)    
# #     print(result)
#     
# #     5. FILL NAN VALUES (MEAN, MEDIAN, DEFAULTS, ETC)
    result = df_missing_data.fillna(df_missing_data.mean()["one":"two"], inplace = True)
    print(result)
    
#     or
#     df_missing_data['one'].fillna(df_missing_data['one'].mean(), inplace=True)
     
    result = df_missing_data.fillna(df_missing_data.median()[:"three"], inplace = True)
    print(result)
    
    df_missing_data["four"] = df_missing_data["four"].fillna("club")    
    print(df_missing_data)    
#     or
#     df_missing_data['four'].fillna("club",inplace=True)    
     
    df_missing_data["five"] = df_missing_data["five"].fillna(True)
    print(df_missing_data)     
          
    now = datetime.datetime.now().strftime('%m/%d/%Y')
    df_missing_data["timestamp"] = df_missing_data["timestamp"].fillna(str(now))
    print(df_missing_data)     
      
#     6. REMOVE ROWS BY COLUMNS CONDITIONS
    df_missing_data = df_missing_data[(df_missing_data["four"] == "bar") | (df_missing_data["four"] == "club")]
    print(df_missing_data)
      
    df_missing_data.set_index("one", inplace = True)
    df_missing_data.to_csv(no_missing_data_path)
        
if __name__ == '__main__':
    main()