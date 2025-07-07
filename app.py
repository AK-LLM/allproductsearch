import streamlit as st
import pandas as pd
from core.manager import search_all

st.set_page_config(page_title="Universal Product Price Meta-Search", layout="wide")

st.title("Universal Product Price Meta-Search (POC)")
st.write("""
Type anything—brand, model, type, new/used, even combinations (use `+` to separate, e.g. `"iPhone 14 Pro Max + AirPods used"`).
""")

query = st.text_input("Enter product(s) to search for:", "")

with st.expander("❓ Help / Syntax Guide"):
    st.markdown("""
    - Use `+` to combine multiple products.  
    - Add `used`, `refurbished`, or `new` for condition filtering.
    - Example searches:  
        - `Sony WH-1000XM4 new`
        - `iPhone 13 + MagSafe Charger used`
        - `Nintendo Switch + Animal Crossing`
    - Searches will cast the widest net across all sources and attempt to return **everything** available.
    """)

if st.button("Search 'Everything'"):
    if query.strip():
        with st.spinner("Searching everywhere across the web..."):
            results = search_all(query)
            if results:
                df = pd.DataFrame(results)
                st.success(f"Found {len(df)} results across all sources!")
                st.dataframe(df)
                st.download_button("Export to CSV", df.to_csv(index=False), "results.csv")
            else:
                st.warning("No results found. Try different keywords or broaden your search.")
    else:
        st.info("Please enter something to search for.")
