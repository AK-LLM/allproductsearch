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

def search_all(params):
    scrapers = load_scrapers()
    results = []
    for scraper in scrapers:
        try:
            matches_type = getattr(scraper, 'handles', None)
            if matches_type and params.get('type') not in matches_type:
                continue  # only run scrapers that handle this type
            result = scraper.search(params)
            if result:
                results.extend(result)
        except Exception as e:
            print(f"[{scraper.name}] Error: {e}")
    return results
