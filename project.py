import streamlit as st
import locale
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

# Load data
data = pd.read_csv('new_data.csv')

# Display first few rows of the dataset
data.head()

# Separate features (X) and target variable (y)
X = data.drop('price', axis=1)
y = data['price']

# Initialize a Random Forest Regressor
model = RandomForestRegressor()

# Train the Random Forest model
model.fit(X, y)

# Mapping for categorical variables
furnishing_status_mapping = {'Unfurnished': 0, 'Semi-Furnished': 1, 'Fully Furnished': 2}
parking_mapping = {'No': 0, 'Yes': 1}

# Define the Streamlit app
def main():
    st.set_page_config(page_title="House Price Prediction", page_icon=":house_with_garden:", layout="wide")

    # Dark theme
    st.markdown(
        """
        <style>
        body {
            background-color: #1E1E1E;
            color: #FFFFFF;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    area = st.text_input('Area (in sq. ft.)')
    bedrooms = st.number_input('Number of Bedrooms', min_value=0, max_value=3, step=1)
    bathrooms = st.number_input('Number of Bathrooms', min_value=0, max_value=3, step=1)
    stories = st.number_input('Number of Floors', min_value=0, max_value=3, step=1)
    mainroad = st.selectbox('Main Road Access', options=['No', 'Yes'])
    guestroom = st.selectbox('Guest Room', options=['No', 'Yes'])
    basement = st.selectbox('Basement', options=['No', 'Yes'])
    airconditioning = st.selectbox('Air Conditioning', options=['No', 'Yes'])
    furnishing_status = st.selectbox('Furnishing Status', options=['Unfurnished', 'Semi-Furnished', 'Fully Furnished'])
    parking = st.selectbox('Parking Spaces', options=['No', 'Yes'])

    # Convert word inputs to numerical values
    mainroad = 1 if mainroad == 'Yes' else 0
    guestroom = 1 if guestroom == 'Yes' else 0
    basement = 1 if basement == 'Yes' else 0
    airconditioning = 1 if airconditioning == 'Yes' else 0
    parking = parking_mapping[parking]
    furnishing_status = furnishing_status_mapping[furnishing_status]

    # Make prediction
    if st.button('Predict'):
        try:
            area = float(area)  # Convert area to float
            prediction = model.predict([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, airconditioning, furnishing_status, parking, 0]])[0]

            # Format prediction in Indian Rupees
            # locale.setlocale(locale.LC_NUMERIC, 'en_IN')
            formatted_prediction = locale.format_string("%.0f", prediction, grouping=True)

            # Display formatted prediction with bold text and a different background color
            st.success(f'**Predicted Price: ₹ {formatted_prediction}**')
        except ValueError:
            st.error('Please enter a valid number for the area.')

# Run the Streamlit app
if __name__ == '__main__':
    main()
