# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pickle
import streamlit as st

# loading the save model
model = pickle.load(open("C:/Users/LENOVO/Desktop/Stock Level Prediction/stock_level_prediction.pkl",'rb'))

def main():
    # giving a title
    st.title("Warehouse Stock Level Prediction App")
    
    # Input Variables
    
    
    Quantity = st.text_input('Quantity')
    Total = st.text_input('Total')
    Temperature = st.text_input("temperature")
    Unit_price = st.text_input("unit_price")
    hour = st.text_input("hour")
    day_of_month = st.text_input("day_of_month")
    customer_type_No_Sale = st.text_input("customer_type_No Sale")
    customer_type_basic = st.text_input("customer_type_basic")
    customer_type_gold = st.text_input("customer_type_gold")
    customer_type_nonmember = st.text_input("customer_type_nonmember")
    customer_type_premium = st.text_input("customer_type_premium")
    customer_type_standard = st.text_input("customer_type_standard")
    category_baby_products = st.text_input("category_baby products")
    category_baked_goods = st.text_input("category_baked goods")
    category_baking = st.text_input("category_baking")
    category_beverages = st.text_input("category_beverages")
    category_canned_foods= st.text_input("category_canned foods")
    category_cheese = st.text_input("category_cheese")
    category_cleaning_products = st.text_input("category_cleaning products")
    category_condiments_sauces = st.text_input("category_condiments and sauces")
    category_dairy = st.text_input("category_dairy")
    category_frozen = st.text_input("category_frozen")
    category_fruit = st.text_input("category_fruit")
    category_kitchen = st.text_input("category_kitchen")
    category_meat = st.text_input("category_meat")
    category_medicine = st.text_input("category_medicine")
    category_packaged_foods = st.text_input("category_packaged foods")
    category_personal_care = st.text_input("category_personal care")
    category_pets = st.text_input("category_pets")
    category_refrigerated_items = st.text_input("category_refrigerated items")
    category_seafood = st.text_input("category_seafood")
    category_snacks = st.text_input("category_snacks")
    category_spices_herbs = st.text_input("category_spices and herbs")
    category_vegetables = st.text_input("category_vegetables")
    dayname_Friday = st.text_input("dayname_Friday")
    dayname_Monday = st.text_input("dayname_Monday")
    dayname_Saturday = st.text_input("dayname_Saturday")
    dayname_Sunday = st.text_input("dayname_Sunday")
    dayname_Thursday= st.text_input("dayname_Thursday")
    dayname_Tuesday = st.text_input("dayname_Tuesday")
    dayname_Wednesday = st.text_input("dayname_Wednesday")
        
    
    # Prediction Code 
    if st.button('Predict'):
        makeprediction = model.predict([[Quantity, Total,Temperature,Unit_price,hour, day_of_month,customer_type_No_Sale,customer_type_basic
                                         ,customer_type_gold,customer_type_nonmember,customer_type_premium,customer_type_standard,category_baby_products,category_baked_goods,category_baking,
                                         category_beverages,category_canned_foods,category_cheese,category_cleaning_products,category_condiments_sauces,category_dairy,category_frozen,category_fruit,category_kitchen,category_meat,
                                         category_medicine,category_packaged_foods,category_personal_care,category_pets,category_refrigerated_items,category_seafood,category_snacks,category_spices_herbs,category_vegetables,
                                         dayname_Friday,dayname_Monday,dayname_Saturday,dayname_Sunday,dayname_Thursday,dayname_Tuesday,dayname_Wednesday]])
        output = round(makeprediction[0],2)
        st.success('Stock Level is {}'.format(output))
        
if __name__ == '__main__':
    main()
        

