import importlib
import yaml
import os

def load_scrapers(config_path='config/sources.yaml'):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    scrapers = []
    for src in config['sources']:
        if not src.get('enabled', True):
            continue
        module = importlib.import_module(f"sources.{src['module']}")
        scraper_class = getattr(module, src['class'])
        scrapers.append(scraper_class())
    return scrapers

def search_all(query):
    scrapers = load_scrapers()
    results = []
    for scraper in scrapers:
        try:
            result = scraper.search(query)
            if result:  # Non-empty
                results.extend(result)
        except Exception as e:
            print(f"[{scraper.name}] Error: {e}")
    return results
