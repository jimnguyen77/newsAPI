### Project instructions
Your task is to create a simple API that interacts with a public news API for fetching articles. For the back-end, you can use the language and framework of your choice. For example, you can use the GNews API (https://gnews.io/) and then create your own API service, with documentation, that interacts with this API for fetching articles.

Your API should have a few basic methods like, fetching N news articles, finding a news article with a specific title or author, and searching by keywords. Include a cache in your API service as well so users are not fetching the same things over and over.

### How to use

# To run this simple news API:

1. Install python3
2. Install pip
3. Install the virtual environment: 
	- on MacOS/Linux: `python3 -m venv venv`
	- on Windows: `py -3 -m venv venv`
4. Activate the virtual environment:
	- on MacOS/Linux: type `. venv/bin/activate` from within the project directory
	- on Windows: type `venv\Scripts\activate` from within the project directory
5. In the project directory, run: `pip install -r requirements.txt`
	- this installs the project dependencies
6. Run the server by typing: `flask --app app run`

# To use the API: 

Once the server is running (typically it runs on localhost:5000), you will have the following functionality:

1. To get the latest N articles, you can use the following path:
	`/api/latest/<N (quantity)>` e.g. `/api/latest/25` will return 25 of the latest articles

2. To search* the articles for anything:
	`/api/search/<keywords>` e.g. `/api/search/puppies` will return all relevant articles about puppies

3. To search* by title:
	`/api/search/title/<title>` e.g. `/api/search/title/trains` will return all relevant articles with "trains" in the title

4. To search* by description:
	`/api/search/desc/<description>` e.g. `/api/search/desc/planes` will return all relevant articles with planes in the description.

5. To search* by content:
	`/api/search/content/<content>` e.g. `/api/search/content/president` will return all relevant articles with presidents in the content

* Note: the default number of articles that are sent back is 10; if you wish to change that value, you can simply append the quantity at the end of the url string; e.g., for title, the path would be: `/api/search/title/trains/5` and it will return only 5 articles.  The free accounts limit to a maximum of 100 articles.