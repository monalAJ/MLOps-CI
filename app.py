import streamlit as st

st.title("Power Calculator")
st.write("Enter the number to calculate the square,cube and fifth power")

n = st.number_input("Enter An Integer",value = 1, step=1)

square = n ** 2
cube = n ** 3
fifth_power = n ** 5

st.write(f"The square of {n} is : {square}")
st.write(f"The Cube of {n} is : {cube}")
st.write(f"The fith_power of {n} is : {fifth_power}")




