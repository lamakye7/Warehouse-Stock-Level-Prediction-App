# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pickle
import streamlit as st

# loading the saved model
model = pickle.load(open('stock_level_prediction.pkl', 'rb'))

def main():
    # Giving a title
    st.title("Warehouse Stock Level Prediction App")
    
    # Input Variables
    st.write("Please enter the following information to predict stock level:")
    
    Quantity = st.text_input('Quantity Sold', 'e.g., 100')
    Total = st.text_input('Total Sales', 'e.g., 50.00')
    Temperature = st.text_input("IoT Sensor Temperature of Product", 'e.g., 25.0')
    Unit_price = st.text_input("Unit Price of Product", 'e.g., 10.00')
    hour = st.text_input("Hour of the Day", 'e.g., 14')
    
    # Add a brief description or guide
    st.write("Example inputs are provided in placeholders (e.g., 100, 5000).")
    
    # Prediction Code 
    if st.button('Predict'):
        # Validate and convert input values to integers or floats
        try:
            Quantity = int(Quantity)
            Total = float(Total)
            Temperature = float(Temperature)
            Unit_price = float(Unit_price)
            hour = int(hour)
        except ValueError:
            st.error("Please enter valid numeric values.")
            return
        
        makeprediction = model.predict([[Quantity, Total, Temperature, Unit_price, hour]])
        output = round(makeprediction[0], 2)
        st.success('Predicted Stock Level is {}'.format(output))

if __name__ == '__main__':
    main()
