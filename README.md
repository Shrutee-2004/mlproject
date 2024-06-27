**###Students Marks Predictor and Visualizer**


**##The dataset**: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977

**The goal is to predict marks of a student based on various models as listed below**:
Linear Regression
Lasso
Ridge
K-Neighbors Regressor
Decision Tree 
RandomForestRegressor
XGBRegressor
CatBoosting Regressor
AdaBoost Regressor


**There are 8 independent variables based on which the prediction is made :**

gender : male/female
race/ethnicity : Group A, B,C, D,E
parental level of education : bachelor's degree,some college,master's degree,associate's degree,high school
lunch : having lunch before test (standard or free/reduced)
test preparation course : complete or not complete before test
reading score : any value between 0-100
writing score : any value between 0-100

Target variable : math score(a future test)


**Below are the screenshots attached:**

**1.HOMEPAGE**

![Screenshot 2024-06-28 011043](https://github.com/Shrutee-2004/mlproject/assets/128917059/cc53f989-2b04-4cdd-b42b-061f4d4e446f)



**2.PREDICT EXACT SCORE**(after clicking on predict score button)

![Screenshot 2024-06-28 013604](https://github.com/Shrutee-2004/mlproject/assets/128917059/da83421e-f7a1-4aee-9152-82bf74227253)


**3.ENTERING INFO**

![Screenshot 2024-06-28 013721](https://github.com/Shrutee-2004/mlproject/assets/128917059/1d3afaf3-5174-4e67-a21b-ba6afd4aa379)

**4.PREDICTION OF EXACT MARKS**

![Screenshot 2024-06-28 013736](https://github.com/Shrutee-2004/mlproject/assets/128917059/87512ad8-3592-4e1a-ae45-b2c80edeb9e4)


**5.VISUALIZATION OF DATA**

![Screenshot 2024-06-28 013419](https://github.com/Shrutee-2004/mlproject/assets/128917059/be78bfc5-c3e3-4016-9cc5-a00d24909e0d)


**NOTE:RED DOT SHOWS THE PREDICTED DATA POINT.**


**6.VISUALIZATION OF DATA(BASED ON GENDER)**

![Screenshot 2024-06-28 013432](https://github.com/Shrutee-2004/mlproject/assets/128917059/77712cb5-9560-4ae1-b891-c66306a55bc8)


**7.VISUALIZATION OF DATA(BASED ON RACE/ETHINICITY)**

![Screenshot 2024-06-28 013446](https://github.com/Shrutee-2004/mlproject/assets/128917059/08ffc3f2-26b8-41b8-8e1c-c23c8883b64e)


**8.VISUALIZATION OF DATA(BASED ON PARENTAL LEVEL OF EDUCATION)**

![Screenshot 2024-06-28 013501](https://github.com/Shrutee-2004/mlproject/assets/128917059/1a9f3b8b-53c4-4475-9e02-4e65d0ace24d)



**9.VISUALIZATION OF DATA(BASED ON LUNCH)**

![Screenshot 2024-06-28 013515](https://github.com/Shrutee-2004/mlproject/assets/128917059/6ed991be-0704-410a-891c-5c9f4b91bdf5)



**10.VISUALIZATION OF DATA(BASED ON TEST PREPARATION COURSE)**

![Screenshot 2024-06-28 013527](https://github.com/Shrutee-2004/mlproject/assets/128917059/081ef54a-79e5-471e-98ec-3546d8699f1d)



**####APPOARCH OF THE PROJECT**


**Data Ingestion :**
In Data Ingestion phase the data is first read as csv.
Then the data is split into training and testing and saved as csv file.


**Data Transformation :**
In this phase a ColumnTransformer Pipeline is created.
for Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
This preprocessor is saved as pickle file.


**Model Training :**
In this phase base model is tested . The best model found was catboost regressor.
After this hyperparameter tuning is performed on catboost and knn model.
A final VotingRegressor is created which will combine prediction of catboost, xgboost and knn models.
This model is saved as pickle file.


**Prediction Pipeline :**
This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.


**Flask App creation :**
Flask app is created with User Interface to predict and visualize the marks of a student within Web Application.



**###STEPS TO RUN IN YOUR COMPUTER**

1. CLONE THE REPO IN YOUR LOCAL DEVICE.
2. RUN THE COMMAND : python -u "c:\Users\Lenovo\Desktop\mlproject\app.py" (MODIFY THE PATH AS REQUIRED)
   
**NOTE:THE .venv must be activated.**












