## In this project you can create a simple Flask app 

### add flask to your pip in the cmd 
```` 
$ pip install Flask
````

### create a file hello.pyin your work environment

add the folowing to your python file to create a minimal application:

```python 
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()
```
next in the terminal execute the following command
```
$ python hello.py
 * Serving Flask app 'hello' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
You should have somethin like this if you follow the link in the terminal
<img src="pictures\simplestApp.JPG">
You can also add to it and modify it to obtain my results wich is a joke generator 


in order to use the project you need to type 
```
$ python hello.py
 * Serving Flask app 'hello' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
after following the link you need to add http://127.0.0.1:5000/hello/namehere/

and you can obtain the following 
<img src="pictures\jokegenerator.JPG">

a quick explanation of the code 

```python 
@app.route('/hello/<string:name>/')
def getMember(name): # we should add the name since we want to display it 

    jokes = []# this is the jokes list 

    randomNumber = randint(0, len(jokes)-1) #getting a random number every time we refresh the page 
    joke = jokes[randomNumber] # getting the random number related joke 

    return render_template('test.html', **locals()) # we render the template test.html because it contains all the html syntax and it's necessary to put the template into templates folder
    # the html is coded with the help of jinja templates  
```
