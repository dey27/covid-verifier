### App Definitions
```

```

## Setting Up

## PostMan Link

```
Download Postman.
Under File tab. Select Import. (Ctrl + O)
Use the above link to "import from link".
```

## DBDiagram Link

```
```

### Backend-Dependencies - Setting Up
```
Via Anaconda Prompt:
	> virtualenv . (Requires Python 3)
	> .\Scripts\activate

	> change to Master folder ("cd master")
	> pip install -r requirements.txt
	> python backend\manage.py runserver

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