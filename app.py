import streamlit as st
import pandas as pd
import plotly.express as px

# the layout Variables
st.set_page_config(page_title="Super Store Dashboard", 
                   page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Map-circle-blue.svg/1024px-Map-circle-blue.svg.png",
                   initial_sidebar_state="expanded",
                   )

hero = st.container()
topRow = st.container()
midRow = st.container()
chartRow = st.container()
footer = st.container()

# Load the data
superSales = pd.read_csv('data/superSales.csv')

# CSS styles
# Custom styling for top and down
st.markdown(
    """
    <style>
    .top-stats {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin: 12px 0 40px 0;
        width: 100%;
        height: 40px;
    }
    .subheader {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .stat {
        flex: 1; 

        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        background-color: #111;

        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    .stat p {
        padding-top: 8px;
    }
    .stat p {
        color: #bbb;
        font-size: 12px;
    }
    .stat span {
        color: #ddd;
        font-size: 24px;
        font-family: serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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

# The Hero Section
with hero:
    # the logo
    st.markdown("""<div style="position:relative; margin: auto; text-align: center;">
              <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Map-circle-blue.svg/1024px-Map-circle-blue.svg.png" width=56>
            </div>""", unsafe_allow_html=True)

    # the header
    st.markdown('<h1 style="text-align:center; position:relative; top:40%;">Super Store DATA</h1>', unsafe_allow_html=True)


# The Rows
with topRow:

    # Calculate the total number of invoices
    total_invoices = chosen_line.shape[0]

    # Calculate the average rating and number of ratings
    average_rating = chosen_line['Rating'].mean()

    # Find the most active time for invoices
    most_active_time = chosen_line['Order_time'].mode()[0]
    # the result is 2:14 PM so I'll type it by hand for now.
    st.markdown(
        """
        <div class="subheader">Top Stats</div>
        <div class="top-stats">
            <div class="stat">
                <p>Total Invoices<br><span> %d </span></p>
            </div>
            <div class="stat">
                <p>Average Rating<br><span> %.2f </span></p>
            </div>
            <div class="stat">
                <p>Most Active Time<br><span> %s </span></p>
            </div>
        </div>
        """ % (total_invoices, average_rating, most_active_time),
        unsafe_allow_html=True
    )
    
    
with midRow:
    # Calculate the total income, costs, and profit
    depts_income = chosen_line['Total_price'].sum()
    depts_costs = chosen_line['costs'].sum()
    depts_profit = depts_income - depts_costs

    st.markdown(
        """
        <div class="top-stats">
            <div class="stat" style="background-color: #093b09;">
                <p>Income<br><span>&pound; %.1f</span></p>
            </div>
            <div class="stat" style="background-color: #4e0000;">
                <p>Costs<br><span>&pound; %.1f</span></p>
            </div>
            <div class="stat" style="background-color: #000062;">
                <p>Profit<br><span>&pound; %.1f</span></p>
            </div>
        </div>
        """ % (depts_income, depts_costs, depts_profit),
        unsafe_allow_html=True
    )



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


with footer:
    st.markdown("---")
    st.markdown(
        """
        <style>
            p {
                font-size: 16px;
                text-align: center;
            }
            a {
                text-decoration: none;
                color: #00a;
                font-weight: 600;
            }
        </style>
        <p>
            &copy; Designed by <a href="https://linkedin.com/in/mohamedyosef101">Mohamed Yosef</a>.
        </p>
        """, unsafe_allow_html=True
        )