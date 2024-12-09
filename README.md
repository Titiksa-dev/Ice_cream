Create a new folder named ice_cream 
create the files inside
          app.py
          models.py
          database.db
          dockerfile
          requirement.txt
          readme.md
add code inside the app.py 
    The code defines a Flask web application with three routes: `/flavors` for adding and retrieving ice cream flavors, `/cart` for adding items to the cart, and `/allergens` for adding allergens. It uses SQLite to store and retrieve data from corresponding tables in a local database (`database.db`).
add code inside the models.py
    The code defines a function `init_db()` that creates four tables (`flavors`, `inventory`, `allergens`, `cart`) in an SQLite database (`database.db`) if they don't already exist. It uses SQLite commands to define the structure of these tables and their relationships, then commits the changes and closes the connection.
add code inside the docker file
    The code is a Dockerfile that creates a Docker image for a Flask application by starting with a slim Python 3.9 base image. It sets the working directory to `/app`, copies the application files into the container, installs Flask using `pip`, and specifies the command to run the `app.py` file when the container starts.
now setup the docker desktop
    install docker desktop from the website according to the laptop configuration 
    once installed configure and setup the account for the docker 
    once the account is setup the docker starts running 
now open the terminal in vs and run the commend |
     python models.py
     python app.py    - this will run on port Running on http://127.0.0.1:5000
build and run the container
    docker build -t ice-cream-parlor .
    docker run -p 5000:5000 ice-cream-parlor
Test the application
    Add a Flavor:  Invoke-RestMethod -Uri http://127.0.0.1:5000/flavors -Method Post -Headers @{ "Content-Type"     ="application/json" } -Body '{"name": "Vanilla", "is_seasonal": false}'
    View Flavors:curl http://127.0.0.1:5000/flavors
    Add to Cart: Invoke-RestMethod -Uri http://127.0.0.1:5000/cart -Method Post -Headers @{ "Content-Type" = "application/json" } -Body '{"flavor_id": 1, "quantity": 2}'
    Add an Allergen:Invoke-WebRequest -Uri http://127.0.0.1:5000/allergens -Method Post -Headers @{ "Content-Type" = "application/json" } -Body '{"name": "Peanuts"}'


