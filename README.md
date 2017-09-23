## twitpilvi


Attempts to get data based on certain hashtag/search terms and then generate a simple word cloud based on the data. Obtains at max 100 items from twitter but
continues until query doesn't return anything. (NB! T's data limits might appear with any larger sets, but should be fine for smaller ones.)

_Python file_ gets the data and stores it to a .csv file (which is overwrites without warning)

_.r file_ utilizes r's nifty  modules, calculates word frequencies and shows the wordcloud image

## Todo 

  * save also the image file to a file
  * paramtereize the first part (query, output filename)
  * etc.
  
## Acknowledgements

  * python file adapted from  original from https://github.com/ideoforms/python-twitter-examples


