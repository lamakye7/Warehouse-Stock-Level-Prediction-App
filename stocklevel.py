# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pickle
import streamlit as st

# loading the save model
model = pickle.load(open('stock_level_prediction.pkl','rb'))

def main():
    # giving a title
    st.title("Warehouse Stock Level Prediction App")
    
    # Input Variables
    
    
    Quantity = st.text_input('Quantity Sold')
    Total = st.text_input('Total Sales')
    Temperature = st.text_input("IoT Sensor Temperature of Product")
    Unit_price = st.text_input("Unit Price of Product")
    hour = st.text_input("Hour of the Day")
    
   
        
    
    # Prediction Code 
    if st.button('Predict'):
        makeprediction = model.predict([[Quantity, Total,Temperature,Unit_price,hour]])
        output = round(makeprediction[0],2)
        st.success('Stock Level is {}'.format(output))
        
if __name__ == '__main__':
    main()
        

