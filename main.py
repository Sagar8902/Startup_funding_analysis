import streamlit as st
import pandas as pd
import time

#########################################
## Text Utility


# title
st.title("Startup Dashbaord")

# header
st.header("Startup funding-2024")

# subheader
st.subheader("Overview of indian startup ecosystem")

# write - to write normal text
st.write("we provide detailed understanding of indian startup ecosystem")

# markdown - to write list
st.markdown("""
### funding overview
- market size
- valuation
- funding
- customer base
""")

# code - to display code on page
st.code("""
def foo(num):
    return num**2

foo(2)
"""
        )

# latex - to display mathematics formulas
st.latex("a^2 + b ^2 = 2ab")

###############################################
## Display Elements
df = pd.DataFrame({
    "name": ["zudio", "danzo", "zepto"],
    "valuation": ["1.5b", "1.4b", "5b"]
})
df.set_index("name", inplace=True)

# dataframe - to display dataframe / table
st.dataframe(df)

# matric - to display card / kpi
st.metric("Revenue", "30l", "+10%")

# json - display json file
st.json({
    "name": ["zudio", "danzo", "zepto"],
    "valuation": ["1.5b", "1.4b", "5b"]
})

###################################
## Display media - image/video

# image - to display image
st.image("download.jpg")
st.video("2637-161442811_tiny.mp4")

#########################################
## Creating Layouts

# sidebar - create sidebar in the page
st.sidebar.title("Naya India")

# column - organize info in column - side by side
col1, col2 = st.columns(2)  # segregate into multiple columns

with col1:
    st.image("download.jpg")

with col2:
    st.image("download.jpg")

############################################
## Showing status

# messages -- show messages based on conditions
st.error("incorrect password")
st.success("login successful")
st.info("enter details here")
st.warning("not enter this - $E$#^")

# process bar -- to show progess
bar = st.progress(0)

for i in range(1, 101):
    # time.sleep(0.1)
    bar.progress(i)

########################################
## user input

# text input, number input, date input
st.text_input("Enter Email here:")
st.number_input("Enter your age here:")
st.date_input("Enter company's incorporation date here:")

# button
import streamlit as st

email = st.text_input("Enter email")
password = st.text_input("Enter password")
gender = st.selectbox("gender", ["male", "female", "other"])

btn = st.button("login")

if btn:
    if email == "startup@gmail.com" and password == "1234":
        st.balloons()
        st.write(gender)
    else:
        st.error("incorrect details")

import streamlit as st
import pandas as pd

# file uploader
file = st.file_uploader("upload csv file here")

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())


