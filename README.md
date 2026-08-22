# 🏡 HomeVista AI

## Data Science Project — House Price Prediction & Property Analytics

HomeVista AI is an end-to-end **Data Science and Machine Learning project** that analyzes residential property data, discovers housing market patterns, recommends properties based on user requirements, and predicts house prices using Machine Learning.

The project combines **data preprocessing, exploratory data analysis, data visualization, feature engineering, machine learning, model evaluation, and an interactive Streamlit dashboard**.

---

## 🌐 Live Demo

Try the deployed HomeVista AI application:

**[🏡 Open HomeVista AI](https://homevista-ai.streamlit.app/)**

The application is deployed using **Streamlit Community Cloud** and provides interactive access to the property analysis, Smart House Finder, market insights, and house price prediction features.

---

---

## 🚀 Key Features

- 📊 Exploratory Data Analysis (EDA)
- 📈 Interactive housing market visualizations
- 🧹 Data preprocessing and cleaning
- 🔧 Feature engineering
- 🤖 House price prediction using Gradient Boosting
- 📐 Model evaluation using R² score
- 🔍 Smart House Finder based on user requirements
- 💰 Property price estimation
- 📊 Interactive Data Science dashboard
- 🏘 Property market insights
- 📍 Location-based analysis
- 🛏 BHK-based analysis
- 📋 Dataset preview and statistical summary

---

## 🧠 Machine Learning

The project uses a **Gradient Boosting Regressor** for house price prediction.

The trained model is saved as:

`model/model.pkl`

The model uses property information such as:

- Area type
- Location
- Total area in square feet
- Number of bathrooms
- Number of balconies
- BHK

The model training workflow includes:

1. Loading the cleaned dataset
2. Separating features and target
3. Identifying numerical and categorical features
4. One-hot encoding categorical features
5. Splitting the data into training and testing sets
6. Training regression models
7. Comparing model performance
8. Evaluating the selected model using regression metrics
9. Saving the trained model with Joblib

---

## 📊 Data Science Workflow

The project follows a practical Data Science workflow:

**Raw Dataset → Data Cleaning → EDA → Feature Engineering → Model Training → Model Evaluation → Saved Model → Streamlit Application**

### Data Cleaning

The project analyzes missing values, duplicate records, data types, and basic dataset statistics.

The original Bengaluru housing dataset contains **13,320 rows and 9 columns**.

The cleaning process includes:

- Checking missing values
- Checking duplicate rows
- Reviewing numerical and categorical features
- Removing the `society` column because of extensive missing values
- Removing rows with remaining missing values

### Feature Engineering

The project creates useful features for Machine Learning.

One important transformation is extracting the numerical **BHK** value from the original `size` column.

The `total_sqft` feature is also converted into a numerical value, including handling ranges such as `1200-1500`.

---

## 📈 Exploratory Data Analysis

The EDA notebook explores the housing dataset using statistical analysis and visualizations.

The analysis includes:

- Missing-value analysis
- House price distribution
- Numerical feature analysis
- Categorical feature analysis
- Outlier exploration
- Relationship between property features and price
- Housing market patterns

---

## 📊 Market Analysis

The Streamlit application provides interactive market analysis.

Users can filter properties by:

- 📍 Location
- 🛏 BHK

The application provides visualizations such as:

- Price distribution
- Price spread
- BHK distribution
- Area type distribution
- Area vs price
- Average price by location
- Correlation heatmap
- Dataset preview

---

## 🔍 Smart House Finder

The **Smart House Finder** allows users to search for properties based on their requirements.

Users can specify:

- 💰 Maximum budget
- 🛏 Bedrooms / BHK
- 🏘 Area type
- 📐 Minimum area
- 🚿 Minimum bathrooms
- 📍 Preferred location

The system filters the available properties and displays matching recommendations.

Recommended properties are sorted by price and the application displays up to 12 matching properties.

---

## 🤖 Price Prediction

The Price Prediction section allows users to enter property details and receive an estimated house price from the trained Machine Learning model.

Input features include:

- Area type
- Location
- Total area
- Bathrooms
- Balconies
- BHK

The application displays:

- 🏷 Estimated price
- 📐 Property area
- 🛏 BHK
- Property summary
- Price category

The prediction is generated using the trained **Gradient Boosting Regressor**.

---

## 📈 Market Insights

The Market Insights section provides a high-level view of the housing market.

It displays:

- Total properties
- Number of locations
- Average property price
- Average property area
- Highest average-price locations
- Budget-friendly locations
- Average price by BHK
- Area type distribution
- Popular locations
- Dataset statistical summary

---

## 🛠️ Technologies Used

### Programming Language

- **Python 3.13.7** — Data Science, Machine Learning, and application logic

### Data Science and Data Processing

- **Pandas** — Data loading, cleaning, transformation, filtering, grouping, and analysis
- **NumPy** — Numerical operations and data processing

### Data Visualization

- **Plotly** — Interactive charts and visualizations in the Streamlit application
- **Matplotlib** — Exploratory Data Analysis visualizations
- **Seaborn** — Statistical data visualization

### Machine Learning

- **Scikit-learn 1.8.0** — Data preprocessing, model training, pipelines, and evaluation
- **GradientBoostingRegressor** — House price prediction
- **OneHotEncoder** — Encoding categorical features
- **ColumnTransformer** — Applying preprocessing to different feature types
- **Pipeline** — Combining preprocessing and Machine Learning steps
- **R² Score** — Model evaluation

### Application Development

- **Streamlit** — Interactive Data Science and Machine Learning dashboard
- **Joblib** — Saving and loading the trained Machine Learning model

### Development Tools

- **Visual Studio Code** — Development environment
- **Jupyter Notebook** — Data cleaning, EDA, feature engineering, and model training
- **Git** — Version control
- **GitHub** — Source code hosting

---

## 📂 Project Structure

The project is organized into the following main components:

- `app.py` — Streamlit application
- `train_model.py` — Machine Learning model training
- `requirements.txt` — Python dependencies
- `README.md` — Project documentation
- `dataset/` — Original and cleaned housing datasets
- `model/` — Trained Machine Learning model
- `notebooks/` — Data cleaning, EDA, feature engineering, and model training notebooks
- `.devcontainer/` — Development container configuration

---

## 📓 Notebooks

### 01 — Data Cleaning

Performs initial dataset inspection and cleaning.

Includes:

- Dataset loading
- Shape and information checks
- Data type inspection
- Missing-value analysis
- Duplicate analysis
- Statistical summaries

### 02 — Exploratory Data Analysis

Explores housing market patterns using:

- Matplotlib
- Seaborn
- Statistical analysis
- Distribution plots
- Feature analysis

### 03 — Feature Engineering

Prepares the data for Machine Learning.

Includes:

- Removing unsuitable columns
- Handling missing values
- Extracting BHK from the `size` column
- Converting `total_sqft` into numerical values
- Preparing the cleaned dataset

### 04 — Model Training

Trains and evaluates regression models using Scikit-learn.

The notebook includes:

- Train/test split
- One-hot encoding
- ColumnTransformer
- Pipeline
- Regression models
- MAE
- MSE
- R² score
- Model saving using Joblib

---

## 📦 Dataset

The project uses a Bengaluru residential property dataset.

The original dataset is stored in the `dataset/` directory.

The processed dataset is also stored in the `dataset/` directory and is used by the Machine Learning model and Streamlit dashboard.

The dataset contains information related to:

- Location
- Area type
- Total area
- BHK
- Bathrooms
- Balconies
- Property price

---

## 💾 Trained Model

The trained Machine Learning model is stored in the `model/` directory.

The Streamlit application loads the saved model using Joblib to generate house price predictions.

---

## ▶️ How to Run

### 1. Clone the Repository

    git clone <your-github-repository-url>

### 2. Open the Project

    cd HomeVista-AI

### 3. Install Dependencies

    pip install -r requirements.txt

### 4. Run the Streamlit Application

    streamlit run app.py

### 5. Open the Application

Streamlit will provide a local URL in the terminal, normally:

    http://localhost:8501

---

## 📋 Requirements

The main Python dependencies used by the project include:

- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Joblib
- Matplotlib
- Seaborn

All required packages are listed in `requirements.txt`.

---

## 💡 Project Workflow

The project can be understood through four major stages.

### Stage 1 — Data Preparation

Raw housing data is loaded, inspected, cleaned, and prepared for analysis.

### Stage 2 — Data Analysis

EDA is performed to understand:

- Price distributions
- Property characteristics
- Locations
- BHK patterns
- Missing values
- Relationships between features

### Stage 3 — Machine Learning

Features are prepared and used to train regression models.

The selected Gradient Boosting model is saved for later use.

### Stage 4 — Interactive Application

The trained model and cleaned dataset are integrated into a Streamlit application containing:

- Home Dashboard
- Market Analysis
- Smart House Finder
- Price Prediction
- Market Insights

---

## 🎯 Project Purpose

The main purpose of HomeVista AI is to demonstrate how **Data Science and Machine Learning can be applied to real-world property data**.

The project combines:

- Data analysis
- Data cleaning
- Data visualization
- Feature engineering
- Machine Learning
- Model evaluation
- Model persistence
- Interactive application development

It provides a practical example of converting raw property data into useful insights and an interactive Machine Learning application.

---

## ⚠️ Disclaimer

The predicted house price is a **Machine Learning estimate** based on the dataset and features provided to the model.

It should not be treated as a guaranteed market price or professional property valuation.

---

## 🚀 Future Improvements

Possible future improvements include:

- Larger and more recent housing datasets
- More advanced feature engineering
- Hyperparameter tuning
- Comparison of additional Machine Learning models
- Improved model accuracy
- More detailed location analysis
- Property price-per-square-foot analysis
- Advanced recommendation ranking
- Deployment as a public web application
- Automated model retraining
- Model performance monitoring
- Additional interactive filters

---

## 🔧 Development

This project was developed as a practical **Data Science and Machine Learning project** using Python.

The development process includes:

- Data cleaning
- Exploratory Data Analysis
- Feature engineering
- Machine Learning
- Model evaluation
- Model persistence
- Interactive application development
- Version control

---

## 📌 Version Control

Git is used for version control during development.

GitHub can be used to store and manage the project source code and documentation.

---

## 👨‍💻 Author

**Lathif Shaik**