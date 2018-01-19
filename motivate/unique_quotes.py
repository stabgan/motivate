#!/usr/bin/env python3
from database import data
import json

quotes = []
quotes += json.load(quote_file)['data']

unique_quotes = []
seen_quotes = set()
for x in quotes:
    if x['quote'] not in seen_quotes:
        unique_quotes.append(x)
        seen_quotes.add(x['quote'])		

with open('data_unique/unique_quotes.json', 'w') as unique_quotes_file:
    json.dump({'data': list(unique_quotes)}, unique_quotes_file, indent=4, ensure_ascii=False)
    unique_quotes_file.write('\n')
