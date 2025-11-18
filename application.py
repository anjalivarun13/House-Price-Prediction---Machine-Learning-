from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

# Load model and data
model = pickle.load(open('Model\RidgeModel.pkl', 'rb'))
house_data = pd.read_csv('Cleaned_house_data.xls')

@app.route('/', methods=['GET'])
def index():
    locations = sorted(house_data['location'].unique())
    locations.insert(0, 'Select Location')
    return render_template('index.html', locations=locations)

# ,location,total_sqft,bath,price,bhk

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    location = request.form.get('location')
    bhk = int(request.form.get('bhk'))
    bath = int(request.form.get('bathroom'))
    total_sqft = float(request.form.get('total_sqft'))

    # Make DataFrame with column names the model expects
    prediction = model.predict(pd.DataFrame(
        columns=['location', 'bhk', 'bath', 'total_sqft'],
        data=np.array([location, bhk, bath, total_sqft]).reshape(1, 4)
    ))

    # Multiply by 1e5 if the model predicts in lakhs
    prediction_in_rupees = prediction[0] * 1e5

    return str(np.round(prediction_in_rupees,2))

    # # Format with commas
    # formatted_price = "{:,.2f}".format(prediction_in_rupees)

    # return formatted_price

if __name__ == '__main__':
    app.run(debug=True)
