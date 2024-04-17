from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve input values from the form
    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    stories = int(request.form['floors'])
    mainroad = int(request.form['mainroad'])
    guestroom = int(request.form['guestroom'])
    basement = int(request.form['basement'])
    hotwaterheating = int(request.form['hotwaterheating'])
    airconditioning = int(request.form['airconditioning'])
    parking = int(request.form['parking'])
    furnishingstatus = int(request.form['furnishingstatus'])
    
    # Make prediction
    prediction = model.predict([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, furnishingstatus]])[0]
    
    # Pass input values and prediction result to HTML template
    return render_template('index.html', prediction=prediction, area=area, bedrooms=bedrooms, bathrooms=bathrooms, stories=stories, mainroad=mainroad, guestroom=guestroom, basement=basement, hotwaterheating=hotwaterheating, airconditioning=airconditioning, parking=parking, furnishingstatus=furnishingstatus)

if __name__ == '__main__':
    app.run(debug=True)
