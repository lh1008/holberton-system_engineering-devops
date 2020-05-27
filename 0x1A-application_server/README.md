# 0x1A. Application server

### Tasks

_**0. Set up development with Python**_
Git clone `AirBnB_clone_v2`, configure `web_flask/0-hello_route.py`.

_**1. Set up production with Gunicorn**_
Install `Gunicorn`

_**2. Serve a page with Nginx**_
Building on your work in the previous tasks, configure `Nginx` to serve your page from the route `/airbnb-onepage/`

_**3. Add a route with query parameters**_
Building on what you did in the previous tasks, let’s expand our web application by adding another service for `Gunicorn` to handle. In `AirBnB_clone_v2/web_flask/6-number_odd_or_even`, the route `/number_odd_or_even/<int:n>` should already be defined to render a page telling you whether an integer is odd or even. You’ll need to configure `Nginx` to proxy HTTP requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to a `Gunicorn` instance listening on port `5001`.

_**4. Let's do this for your API**_
Let’s serve what you built for `AirBnB clone v3 - RESTful API` on `web-01`.

_**5. Serve your AirBnB clone**_
Let’s serve what you built for `AirBnB clone - Web dynamic` on `web-01`.
