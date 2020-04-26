## App Definitions
#### AIENGINE

Running the Scraper
```
> cd backend/AIEngine/webscraper
> scrapy crawl crawler
```

## Setting Up

## PostMan Link
https://www.getpostman.com/collections/da06eda18e51229afe8c
```
Download Postman.
Under File tab. Select Import. (Ctrl + O)
Use the above link to "import from link".
```

## Database Diagrams and Working with PyDot
```
# to create model diagram for given specific Apps.
> python manage.py graph_models AIEngine coreEngine > sabar_db.dot
OR
# to create model diagram for complete project definitions
> python manage.py graph_models -a > sabar_db.dot
> dot -Tpng sabar_db.dot -o sabar_db.png
OR
# to directly create a png (graphviz isn't installed, pydot is defined in req.txt)
python manage.py graph_models --pydot  -a -g -o sabar_db.png
```
A dot file and PNG files will be created to view the models defined.

### Backend-Dependencies - Setting Up
```
Folder Structure
-sabar 
    - sabar //git clone here
    - sabar_venv //to hold all python dependencies 
```

```
Via Anaconda Prompt:
    # Install this in ubuntu ONLY IF req.txt fails.
    > sudo apt-get install graphviz libgraphviz-dev graphviz-dev python-pygraphviz

	> virtualenv --python=python3 . (Requires Python 3)
	> source bin/activate

	> pip install -r backend/requirements.txt
	> python backend/manage.py runserver

<!-- DATABASE POPULATION -->
> python backend/manage.py loaddata <fixturename>.json

To access admin dashboard (only if backend/db.sqlite3 file is not present, else use the given credentials)
	> python backend/manage.py createsuperuser
	> enter user - admin, p/w - admin
	> Access localhost:8000/admin
```

### Frontend-Dependencies - Setting Up
```
1. THE PROJECT ECOSYSTEM (npm, bower)
	<!-- Install Node Js -->
	> https://nodejs.org/en/download/

	<!-- Check version using  -->
	> node -v
	v10.16.3

2. JS Framework (Angular)
	> npm install -g @angular/cli
	> ng --version (TO VERIFY)

3. SETUP DEPENDENCY MANAGERS FOR PROJECT
	> cd frontend
	> npm install (from package.json)

	<!-- INFO  -->
	* npm install will install all dependencies mentioned in package.json

4. RUNNING THE FRONTEND
	> Open a new terminal
	> cd speech-recognizer\Master\frontend>
	> npm start

<!-- Other Commands -->
ng generate component dashboard
```	

## Design - API

## Design - Databases

### References: