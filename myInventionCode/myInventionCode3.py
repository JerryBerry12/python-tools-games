# By Micah
# Here is a better way to search for Eric Liddel
# Cause of error: wikipedia module is not that great.
# Fix: Uses wikipedia-api instead of wikipedia.


import wikipediaapi
from make_colors import make_colors

wiki_wiki = wikipediaapi.Wikipedia('The Three Pythoneers Team (pythoneers-team@jssources.com)', 'en')

page_py = wiki_wiki.page('Eric Liddel')

print(make_colors(page_py.title, 'white', 'black'))
print(make_colors(page_py.summary, 'green', 'black'))