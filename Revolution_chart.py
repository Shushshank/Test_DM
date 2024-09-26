import streamlit as st
import pandas as pd
import pickle

# Load the trained model
filename = 'trained_model.pkl'
model = pickle.load(open(filename, 'rb'))

# Create the Streamlit app
st.title("Revolution Chart Revenue Predictor")

# Get user input for independent variables
# Replace 'variable_name' with the actual names of your independent variables from your DataFrame
independent_variables = ['number_of_products', 'average_order_value', 'customer_acquisition_cost', 'customer_lifetime_value'] 
input_data = {}
for variable in independent_variables:
    input_data[variable] = st.number_input(f"Enter {variable}", value=0.0)

# Create a DataFrame from the user input
input_df = pd.DataFrame([input_data])

# Make a prediction using the loaded model
if st.button("Predict Monthly Revenue"):
    prediction = model.predict(input_df)[0][0]
    st.write(f"Predicted Monthly Revenue: {prediction:.2f}") 
