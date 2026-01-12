#  Medical Insurance Cost Prediction

This is a simple Machine Learning project where I built a model to predict
medical insurance cost based on user details like age, BMI, smoking habit,
number of children, gender and region.

The project also includes a small web application where users can enter
their details and see the predicted insurance cost instantly.


##  Problem Statement

Insurance companies decide the insurance cost based on many factors.
This project tries to understand those factors and predict the insurance
cost using a Machine Learning model.


##  Tools & Technologies Used

- Python  
- NumPy  
- Pandas  
- Matplotlib  
- Seaborn  
- Scikit-learn  
- Streamlit  


##  Dataset Information

The dataset contains the following columns:
- age  
- sex  
- bmi  
- children  
- smoker  
- region  
- charges (target column)


##  Exploratory Data Analysis (EDA)

During EDA, I:
- Checked the distribution of age, BMI and charges
- Compared insurance cost based on smoker vs non-smoker
- Analyzed how gender, region and children affect insurance cost
- Checked for missing values and data types

This helped me understand which features impact the insurance cost more.


## Machine Learning Model

- Algorithm used: **Linear Regression**
- Target variable: **`charges`**
- Train-test split: **80% training, 20% testing**
- Model performance evaluated using **R² score**

The model learns the relationship between user details and insurance cost.


##  Web Application

I created a simple and clean web app using **Streamlit** where:
- Users can enter their details using sliders and dropdowns
- The model predicts insurance cost in real time
- Results are displayed clearly on the screen


##  Project Structure

- `app.py` → Streamlit web application  
- `insurance.csv` → Dataset  
- `Linear_regression_model.ipynb` → Model training & EDA  
- `requirements.txt` → Required libraries  

## Key Insights

- Smokers have significantly higher insurance costs
- Higher BMI generally leads to higher insurance charges
- Age is directly related to insurance cost
- Region and number of children also affect the final cost

