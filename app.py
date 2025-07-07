import streamlit as st
import pandas as pd
from core.manager import search_all

st.set_page_config(page_title="Universal Meta-Search", layout="wide")

st.title("Universal Product/Travel/Hotel Meta-Search")

st.sidebar.title("Search Type")
search_type = st.sidebar.selectbox("Select search type", ["Product", "Airfare", "Hotel"])

if search_type == "Product":
    query = st.text_input("Product search (e.g., iPhone 14, Dyson vacuum):", "")
    search_params = {"type": "product", "query": query}
elif search_type == "Airfare":
    from_loc = st.text_input("From (City or Airport Code):", "")
    to_loc = st.text_input("To (City or Airport Code):", "")
    depart_date = st.date_input("Depart Date")
    return_trip = st.checkbox("Return Trip?")
    if return_trip:
        return_date = st.date_input("Return Date")
    else:
        return_date = None
    travel_class = st.selectbox("Class", ["Economy", "Premium Economy", "Business", "First"])
    search_params = {
        "type": "airfare",
        "from": from_loc,
        "to": to_loc,
        "depart_date": str(depart_date),
        "return_date": str(return_date) if return_date else "",
        "travel_class": travel_class
    }
elif search_type == "Hotel":
    destination = st.text_input("Destination (City, Country):", "")
    checkin = st.date_input("Check-in Date")
    checkout = st.date_input("Check-out Date")
    guests = st.number_input("Guests", min_value=1, value=1)
    search_params = {
        "type": "hotel",
        "destination": destination,
        "checkin": str(checkin),
        "checkout": str(checkout),
        "guests": guests
    }
else:
    search_params = {}

if st.button("Search"):
    with st.spinner("Searching across all relevant sources..."):
        results = search_all(search_params)
        if results:
            df = pd.DataFrame(results)
            st.success(f"Found {len(df)} results!")
            st.dataframe(df)
            st.download_button("Export to CSV", df.to_csv(index=False), "results.csv")
        else:
            st.warning("No results found. Try different search criteria.")

with st.expander("❓ Help & Syntax Guide"):
    st.markdown("""
    **Product:**  
    - Enter keywords, brand, model, condition, etc.  
    - E.g.: `iPhone 13`, `Sony headphones new`, `Dyson v15 used`
    
    **Airfare:**  
    - Fill in departure/arrival city or code, select dates and class.
    
    **Hotel:**  
    - Enter city/country, select dates and number of guests.
    """)
