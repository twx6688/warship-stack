import streamlit as st

# Configure the main page settings: title and layout style.
st.set_page_config(page_title="Warship", layout="wide")

# Define the pages for the application.
# The file paths should point to the correct locations of your Streamlit pages.
dashboard = st.Page("pages/dashboard.py", title="Dashboard", default=True)
tsr = st.Page("pages/tsr.py", title="TSR Prep")
wh = st.Page("pages/wh.py", title="Warehouse")

# Set up the navigation structure.
# I group pages under different sections.
# - "Summary" contains the Dashboard page.
# - "Shipping" contains the TSR Prep page.
# - "Warehouse" contains the Warehouse page.
pg = st.navigation(
    {
        "Summary": [dashboard],
        "Shipping": [tsr],
        "Warehouse": [wh],
    }
)

# Run the navigation, which will render the appropriate page based on user selection.
pg.run()
