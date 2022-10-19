from flask import Flask, render_template
from random import randint


app = Flask(__name__)


@app.route('/')
def index():
    return 'Flask App'


@app.route('/hello/<string:name>/')
def getMember(name):

    jokes = ["'Why did an old man fall in a well? Because he couldn t see that well!'", "'Why did the actor fall through the floorboards? They were going through a stage!'", "'Why did a scarecrow win a Nobel prize? He was outstanding in his field!'", "'Why are peppers the best at archery? Because they habanero!'", "'What did the duck say after she bought chapstick? Put it on my bill!'",
             "'What do you call a fake noodle? An impasta!'", "'What did the three-legged dog say when he walked into a saloon? “I’m looking for the man who shot my paw!”'", "'How do you tell the difference between a bull and a cow? It is either one or the udder!'", "'What’s red and smells like blue paint? Red paint!'", "'What’s the difference between a hippo and a Zippo? One is very heavy, the other is a little lighter!'"]

    randomNumber = randint(0, len(jokes)-1)
    joke = jokes[randomNumber]

    return render_template('test.html', **locals())


if __name__ == '__main__':
    app.run()
