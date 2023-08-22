# Super Store Dashboard using Streamlit
The growth of supermarkets in most populated cities are increasing and market competitions are also high. In this dashboard we'll give it a try and turn everything into a readable visualizations.

**Designed by:**
 <br>@mohamedyosef101 : https://linkedin.com/in/mohamedyosef101
 <br>
 
 **Deployed on:**
 <br> Streamlit: https://super-dashboard.streamlit.app

## About the dataset
The dataset is one of the historical sales of supermarket company which has recorded in 3 different branches for 3 months data.
[Visit Data Source](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales)


### Versioning
- Based on Streamlit 1.25.0
- Analysed by Pandas 2.0.3
- Visualized by Plotly 5.16.1
- Made with Python 3.11

<hr>

# I've changed the database a little

### **Add four years to the date**

```sql
UPDATE superSales
SET Order_date = DATEADD(YEAR, 4, Order_date)
WHERE YEAR(Order_date) = 2019
```

### **Change cities**

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

# What to I've done with Streamlit
### Page settings

```python
st.set_page_config(page_title="Super Store Dashboard", 
page_icon="URL",
layout="centered",
initial_sidebar_state= "expand",
)
```

### The layout variables

```python
hero = st.container()
col1, col2 = st.columns([2, 1])
```

### Editing the sidebar

```python
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
```

### Using a selectbox

```python
# Choosing the Product Line
    Product_lines = superSales['Product_line'].unique()
    line = st.selectbox('',['Choose the Product Line'] + list(Product_lines))
    if line == 'Choose the Product Line':
        chosen_line = superSales
    else:
        chosen_line = superSales[superSales['Product_line'] == line]
```
<div></div>

<hr>

<p>&copy; All rights reserved. MohamedYosef101</p>#
