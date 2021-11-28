from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the pickle file that contains the prediction logic
model = pickle.load(open('iris.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

# Taking User input using forms and passing the values to the predictor
@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    arr = np.array([[data1, data2, data3, data4]])
    pred = model.predict(arr)
    return render_template('result.html', pred=pred)

if __name__ == "__main__":
    app.run(debug=True)