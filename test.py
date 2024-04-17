import streamlit as st
import pickle

# Load the trained model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the Streamlit app
def main():
    st.title('House Price Prediction')

    # Add input fields
    area = st.number_input('Area', min_value=0.0, step=0.1)
    bedrooms = st.number_input('Number of Bedrooms', min_value=0, step=1)
    bathrooms = st.number_input('Number of Bathrooms', min_value=0, step=1)
    stories = st.number_input('Number of Floors', min_value=0, step=1)
    mainroad = st.selectbox('Main Road', [0, 1])
    guestroom = st.selectbox('Guest Room', [0, 1])
    basement = st.selectbox('Basement', [0, 1])
    airconditioning = st.selectbox('Air Conditioning', [0, 1])
    parking = st.number_input('Parking Spaces', min_value=0, step=1)
    furnishingstatus = st.selectbox('Furnishing Status', [0, 1, 2])

    # Make prediction
    if st.button('Predict'):
        prediction = model.predict([[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, airconditioning, parking, furnishingstatus]])
        st.write('Predicted Price:', prediction[0])

# Run the Streamlit app
if __name__ == '__main__':
    main()
