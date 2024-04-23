import streamlit as st
import pickle
import locale

# Load the trained model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Mapping for categorical variables
furnishing_status_mapping = {'Unfurnished': 0, 'Semi-Furnished': 1, 'Fully Furnished': 2}
parking_mapping = {'No': 0, 'Yes': 1}

# Define the Streamlit app
def main():
    st.title('House Price Prediction')

    # Add input fields
    st.header('Input Features')
    area = st.text_input('Area (in sq. ft.)')
    bedrooms = st.number_input('Number of Bedrooms', min_value=0, max_value=3, step=1)
    bathrooms = st.number_input('Number of Bathrooms', min_value=0, max_value=3, step=1)
    stories = st.number_input('Number of Floors', min_value=0, max_value=3, step=1)
    mainroad = st.selectbox('Main Road Access', options=['No', 'Yes'])
    guestroom = st.selectbox('Guest Room', options=['No', 'Yes'])
    basement = st.selectbox('Basement', options=['No', 'Yes'])
    airconditioning = st.selectbox('Air Conditioning', options=['No', 'Yes'])
    parking = st.selectbox('Parking Spaces', options=['No', 'Yes'])

    # Convert word inputs to numerical values
    mainroad = 1 if mainroad == 'Yes' else 0
    guestroom = 1 if guestroom == 'Yes' else 0
    basement = 1 if basement == 'Yes' else 0
    airconditioning = 1 if airconditioning == 'Yes' else 0
    parking = parking_mapping[parking]

    # Make prediction
    if st.button('Predict'):
        try:
            area = float(area)  # Convert area to float
            prediction = model.predict([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, airconditioning, parking, 0]])[0]

            # Format prediction in Indian Rupees
            locale.setlocale(locale.LC_NUMERIC, 'en_IN')
            formatted_prediction = locale.format_string("%.0f", prediction, grouping=True)

            # Display formatted prediction with bold text and a different background color
            st.write('Predicted Price:', f'**{formatted_prediction}**', unsafe_allow_html=True, )
        except ValueError:
            st.error('Please enter a valid number for the area.')

# Run the Streamlit app
if __name__ == '__main__':
    main()
