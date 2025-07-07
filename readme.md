# Universal Product Price Meta-Search (POC)

A modular, extensible proof-of-concept for searching "everything"—all product prices across as many retail, marketplace, and classifieds sources as possible.

## Features

- Search multiple sources in parallel: retail, marketplace, classifieds, and web search fallback
- Supports "everything"—any product, any vendor, new/used, multi-item
- Add your own scrapers by dropping plugins in `sources/` and editing `config/sources.yaml`
- Export results to CSV

## Usage

```bash
git clone https://github.com/YOUR-USER/product_price_search.git
cd product_price_search
pip install -r requirements.txt
streamlit run app.py
