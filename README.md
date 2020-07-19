This repository is used for sharing the number of solved problems on LeetCode and plot the historical data for a group of people. 

## Environment 
- Python >= 3.7  
- Scrapy  
- Jupyter Notebook

## Additional file required
- profile_urls.txt
A list of LeetCode profile URLs (e.g. https://leetcode.com/gdkou90/) as the entry point of the crawler

## Run it
```
Scrapy crawl profiles
```
Or simply run the Jupyter Notebook `Visualize_solved_problems.ipynb` directly.