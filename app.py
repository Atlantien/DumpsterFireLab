from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll')
def roll_dice():
    result = random.randint(1, 6)
    
    if result in [1, 3, 5]:  # Odd numbers
        state = "It's a dumpster fire! 🔥"
        on_fire = True
    else:  # Even numbers
        state = "It's safe! 👍"
        on_fire = False
    
    return jsonify({'result': result, 'state': state, 'on_fire': on_fire})

if __name__ == '__main__':
    app.run()