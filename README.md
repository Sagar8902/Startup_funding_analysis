# 📊 Startup Funding Analysis

An exploratory data analysis project focused on understanding **startup funding trends and patterns** using Python and data analysis libraries.

The project works with startup funding datasets to clean, explore, analyze, and visualize information related to startups, funding, investors, industries, and other available attributes.

---

## 🎯 Project Objective

The main objective of this project is to use real-world startup funding data to:

* Understand startup funding patterns
* Explore the characteristics of funded startups
* Analyze funding-related trends
* Identify useful patterns in the dataset
* Practice data cleaning and exploratory data analysis
* Build practical experience with Python and Pandas

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Streamlit**
* **Jupyter / Python**
* **CSV**

---

## 📂 Project Structure

```text
Startup_funding_analysis/
│
├── app.py                  # Streamlit application
├── main.py                 # Main analysis / Python code
├── startup_funding.csv     # Original startup funding dataset
├── startup_cleaned-1.csv  # Cleaned dataset
├── README.md              # Project documentation
└── myenv/                  # Local Python environment
```

> **Note:** The `myenv` folder is a local virtual environment and normally should not be pushed to GitHub. Add it to `.gitignore` if it is not already excluded.

---

## 🔍 Analysis Workflow

The project follows a typical data analysis workflow:

```text
Raw Data
   ↓
Data Loading
   ↓
Data Cleaning
   ↓
Data Exploration
   ↓
Data Analysis
   ↓
Visualization
   ↓
Insights
```

### 1. Data Loading

The startup funding data is loaded from CSV files using Python and Pandas.

### 2. Data Cleaning

The raw dataset is processed to make it more suitable for analysis.

Typical cleaning activities include:

* Handling missing values
* Cleaning column names
* Removing unnecessary records
* Standardizing data
* Preparing columns for analysis

The cleaned dataset is stored separately as:

```text
startup_cleaned-1.csv
```

### 3. Exploratory Data Analysis

The cleaned data is explored to understand:

* Funding patterns
* Startup characteristics
* Investment information
* Industry/sector trends
* Investor-related information
* Other patterns available in the dataset

### 4. Data Visualization

Charts and visualizations are used to make patterns in the data easier to understand.

---

# 🌐 Streamlit Application

The project also includes a Streamlit application through:

```text
app.py
```

Streamlit provides an interactive interface for exploring the startup funding analysis.

To run the application locally:

```bash
streamlit run app.py
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/Sagar8902/Startup_funding_analysis.git
```

Move into the project directory:

```bash
cd Startup_funding_analysis
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv myenv
```

Activate it:

```bash
myenv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv myenv
```

Activate it:

```bash
source myenv/bin/activate
```

## 3. Install Required Libraries

```bash
pip install pandas numpy matplotlib streamlit
```

## 4. Run the Streamlit Application

```bash
streamlit run app.py
```

---

# 📈 Key Learning Outcomes

Through this project, I practiced:

### Python

* Python fundamentals
* Functions
* Loops
* Conditional statements
* File handling

### Pandas

* Reading CSV files
* DataFrame operations
* Data cleaning
* Filtering data
* Grouping and aggregation
* Handling missing values

### Data Analysis

* Exploratory Data Analysis (EDA)
* Finding patterns in data
* Comparing categories
* Generating meaningful insights

### Data Visualization

* Creating charts
* Communicating data insights visually
* Understanding trends and distributions

### Streamlit

* Creating interactive dashboards
* Displaying DataFrames
* Adding user interaction
* Building a simple data analysis web application

---

# 📌 Project Purpose

This is a **learning and portfolio project** created to strengthen practical skills in:

```text
Python
   ↓
Pandas
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Data Visualization
   ↓
Streamlit
```

The project demonstrates how raw data can be transformed into useful information and presented through an interactive application.

---

# 🔮 Future Improvements

Some possible improvements include:

* Add more interactive filters
* Improve dashboard design
* Add more advanced visualizations
* Add investor-level analysis
* Add industry/sector comparisons
* Add funding trend analysis
* Add KPI cards
* Deploy the Streamlit application
* Improve data validation and cleaning
* Add automated data pipelines

---

# 👨‍💻 Author

**Sagar Soni**

GitHub: [@Sagar8902](https://github.com/Sagar8902)

---

## ⭐ If You Find This Project Useful

Feel free to ⭐ **star the repository** and explore the project.
