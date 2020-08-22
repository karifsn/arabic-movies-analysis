## This script uses google's search package to query a movie name with its' release data (with the addition of the keyword 'elcinema') to acquire a link to that movie on elcinema's website.

import pandas as pd
from googlesearch import search

movies_dataset = pd.read_csv('1940s_movies_release_date_expanded.csv')

number_of_rows = movies_dataset.shape[0]

for row in range(number_of_rows):
    search_input = 'elcinema '
    search_input += date_expanded_dataset.iloc[row,0] 
    search_input += ' '
    search_input += date_expanded_dataset.iloc[row,16]
        
    link = None
    for search_result in search(search_input, tld="co.in", num=1, stop=1, pause=2): 
        link = search_result
    
    with open('links.txt', 'a') as file:
        file.write(link)
        file.write('\n')
        file.close()