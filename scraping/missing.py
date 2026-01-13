import json
seenURLS = set()
f = open('descriptions.json')
data = json.load(f)
for entry in data:
    seenURLS.add(entry["p_url"])
p = [tuple(l.split()) for l in open("../Problems.txt", 'r').read().splitlines()]
all_urls = [f'https://codeforces.com/contest/{nr}/problem/{letter}' for nr,letter in p]

start_urls = []
for url in all_urls:
    if url in seenURLS:
        continue
    else:
        print (url)
        start_urls.append(url)
#print (len(start_urls))