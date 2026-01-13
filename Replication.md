# Replication steps

Requirements: Python3 (scrapy library), Codeforces API acces (https://codeforces.com/apiHelp).
The following outlines steps to recreate the data collection procedure:

1. Get list of contests and store in files (https://codeforces.com/api/contest.list)
    - Store as "contests.json"
2. Access API to get list of hacking attempt for each contest: "2) Process get contest information.ipynb"
For each contest, the successful hacks are stored in a json file.
    - Follow steps in "2.1) Extract all relevant hacking attempts.ipynb" to extract all hacks for the dataset
3. Run "3) Problems with hacks.ipynb" to extract problems with hacks. These will be stored in "Problems.txt" and are used for scraping problem descriptions.
4. Crawl problem descriptions (scrape.py).
Use command "scrapy runspider scrape.py -o descriptions.json" to append to existing file, "scrapy runspider scrape.py -o descriptions.json" to overwrite existing file.
"descriptions.json" is used to store the crawling results. Different file names can be used.
Alternatively, the "Parsing.ipynb" can be used. This extracts information from local html files.

5. There are 50 problems that do not follow the common layout and need to be crawled with adapted scripts.
    1. You can run /scraping/missing.py to find the respective urls (stored in missing.txt)
    2. After manaul inspection the files can be divided in: 
        - interactive problems with input descriptions (28 problems, stored in "interactiveInput.txt")
        - interactive problems without input descriptions (13 problems, stored in "interactiveNoInput.txt")
        - standard problems with different layout (2 problems)
    
    3) Run the following commands to crawl the remaining probles:
        - scrapy runspider scrape_1220C.py -o descriptions.json
        - scrapy runspider scrape_837G.py -o descriptions.json
        - scrapy runspider scrapeInteractive.py -o descriptions.json
        - scrapy runspider scrapeInteractiveNoInput.py -o descriptions.json

6. Correct the formatting in "descriptions.json": Each of the scraping script appends result as a json object, encapsulated by "[ ... ]". Running multiple scraping scripts therefore requires the removal of additional brackets in the file. Brackets should remain in the first and last line of the file, all others should be removed.

7. Crawl submission urls: Follow the instructions "4) Crawl Submission URLS.ipynb".

8. Obtain source code submissions from Code4Bench (https://github.com/code4bench/Code4Bench)
    - Downlad code4bench dataset
    - Install mysql
    - Start mysql server
    - Create a database (e.g., code4bench)
    - Load "source.sql" and "testcases.sql"
    - Follow steps in "5) SQL matching.ipynb"