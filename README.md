# Super Store Dashboard using Streamlit
The growth of supermarkets in most populated cities are increasing and market competitions are also high. In this dashboard we'll give it a try and turn everything into a readable visualizations.

![top stats](https://github.com/mohamedyosef101/Super-Dashboard/assets/118842452/5438b91a-cb6c-499e-a95b-402c076cbbf8)


**Designed by:** [@mohamedyosef101](https://github.com/mohamedyosef101)
<br> 
 **Deployed on:** [Streamlit](https://super-dashboard.streamlit.app)
<hr>
<div><br></div>

# About the dataset
The dataset is one of the historical sales of supermarket company which has recorded in 3 different branches for 3 months data.
<br> [Visit Data Source](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales)


### Versioning
- Based on Streamlit 1.25.0
- Analysed by Pandas 2.0.3
- Visualized by Plotly 5.16.1
- Made with Python 3.11

<hr>
<div><br></div>

# I've changed the database a little
Since this is a visualization work, I've a freedom to change the database to make my job easier.
<div><br></div>

### **Add four years to the date**
Actually and for the first time, I worked with SQL not pandas.

```sql
UPDATE superSales
SET Order_date = DATEADD(YEAR, 4, Order_date)
WHERE YEAR(Order_date) = 2019
```
<div><br></div>

### **Add cities**
Before: each branch has a unique identifier A, B, C
Now: besides this id we also have a city name to be more clear about where the branch live.

```sql
Update superSales
set City = case Branch
		WHEN 'A' THEN 'Plymouth'
		WHEN 'B' THEN 'Bristol'
		WHEN 'C' THEN 'Glasgow'
		END;
select City from superSales;
```

<hr>
<div><br></div>

# Building The Dashboard with Streamlit
> These are some highlights from the code not the whole code.
<div><br></div>

### 1. Importing the libraries
We’ll need core data analysis libraries like Pandas, NumPy as well as plotting libraries like Plotly Express. Streamlit is imported as st.

```python
import streamlit as st
import pandas as pd
import plotly.express as px
```
<div><br></div>

### 2. Getting Ready
I loaded a supermarket sales CSV file using Pandas, did some preprocessing like setting page config as well as creating the layout variables.

```python
# Load the data
superSales = pd.read_csv('data/superSales.csv')

# Setting page config
st.set_page_config(page_title="Super Store Dashboard", 
                   page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Map-circle-blue.svg/1024px-Map-circle-blue.svg.png",
                   initial_sidebar_state="expanded",
                   )

# the layout Variables
hero = st.container()
topRow = st.container()
midRow = st.container()
chartRow = st.container()
footer = st.container()
```
<div><br></div>

### 3. Editing the sidebar
Sidebars in Streamlit provide an easy way to add filters that users can tweak to update the dashboard.


```python
# Sidebar
with st.sidebar:
    st.markdown(f'''
        <style>
        section[data-testid="stSidebar"] {{
                width: 500px;
                background-color: #000b1a;
                }}
        section[data-testid="stSidebar"] h1 {{
                color: #e3eefc;
                }}
        section[data-testid="stSidebar"] p {{
                color: #ddd;
                text-align: left;
                }}
        section[data-testid="stSidebar"] svg {{
                fill: #ddd;
                }}
        </style>
    ''',unsafe_allow_html=True)
    st.title(":anchor: About the dataset")
    st.markdown("The growth of supermarkets in most populated cities are increasing and market competitions are also high. In this dashboard we'll give it a try and turn everything into a readable visualizations.")
```
<div><br></div>

### 4. I also added selectbox filters to choose Product Line….

<img width="560" alt="sidebar" src="https://github.com/mohamedyosef101/Super-Dashboard/assets/118842452/79912ea2-6c1a-4ba0-adb6-c36f99d05365">


```python
# The Selectbox
    Product_lines = superSales['Product_line'].unique()
    line = st.selectbox('',['Choose the Product Line'] + list(Product_lines))
    if line == 'Choose the Product Line':
        chosen_line = superSales
    else:
        chosen_line = superSales[superSales['Product_line'] == line]

    # Customizing the select box
    st.markdown(f'''
    <style>
        .stSelectbox div div {{
                background-color: #fafafa;
                color: #333;
        }}
        .stSelectbox div div:hover {{
                cursor: pointer
        }}
        .stSelectbox div div .option {{
                background-color: red;
                color: #111;
        }}
        .stSelectbox div div svg {{
                fill: black;
        }}
    </style>
    ''', unsafe_allow_html=True)
```
<div><br></div>

### 5. The most importan part: THE CHART

<img width="560" alt="main chart" src="https://github.com/mohamedyosef101/Super-Dashboard/assets/118842452/3df137ad-b4f0-4af7-8ecc-3464c5ed858f">

```python
with chartRow:
    # Filter for the month
    superSales['Order_date'] = pd.to_datetime(superSales['Order_date'])
    mar_data = (superSales['Order_date'].dt.month == 3)
    lineQuantity = chosen_line[(mar_data)]

    # Quantity for each day
    quantity_per_day = lineQuantity.groupby('Order_date')['Quantity'].sum().reset_index()

    # some space
    st.markdown('<div></div>', unsafe_allow_html=True)
    
    # Create a line chart for Quantity over the last month using Plotly
    fig_quantity = px.line(
        quantity_per_day, 
        x='Order_date', 
        y='Quantity', 
        title='Quantity Sold over the Last Month'
    )
    fig_quantity.update_layout(
        margin_r=100,
    )
    st.plotly_chart(fig_quantity)

```
<div><br></div>

### 6. Deploying the Dashboard
Once ready, I deployed the app using Streamlit sharing which provides free hosting for Streamlit apps!

This allows me to share the interactive dashboard with anyone.

For more about the deployment: https://youtu.be/B0MUXtmSpiA

<div><br></div>

<hr>
🔔 Follow me for more <b>Product Data Science</b> work.
<hr>
<p>&copy; Created by MohamedYosef101 | <a href="https://github.com/mohamedyosef101"> GitHub</a> &centerdot; <a href="https://linkedin.com/in/mohamedyosef101">LinkedIn</a> &centerdot; <a href="https://kaggle.com/mohamedyosef101">Kaggle</a></p>
