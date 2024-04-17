from flask import Flask, render_template, request
import pickle
import locale

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
    airconditioning = int(request.form['airconditioning'])
    parking = int(request.form['parking'])
    furnishingstatus = int(request.form['furnishingstatus'])
    
    # Make prediction
    prediction = model.predict([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, airconditioning, parking, furnishingstatus]])[0]

    # Format prediction in Indian Rupees without paisa units
    locale.setlocale(locale.LC_NUMERIC, 'en_IN')
    formatted_prediction = locale.format_string("%.0f", prediction, grouping=True)
    
    # Pass input values and formatted prediction result to HTML template
    return render_template('index.html', prediction= formatted_prediction, area=area, bedrooms=bedrooms, bathrooms=bathrooms, stories=stories, mainroad=mainroad, guestroom=guestroom, basement=basement, airconditioning=airconditioning, parking=parking, furnishingstatus=furnishingstatus)

if __name__ == '__main__':
    app.run(debug=True)