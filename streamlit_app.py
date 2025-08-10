import streamlit as st

# Set title of the app
st.title("Simple Calculator")

# User inputs
num1 = st.number_input("Enter the first number", format="%.2f")
num2 = st.number_input("Enter the second number", format="%.2f")

# Dropdown for selecting operation
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform calculation based on selected operation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

# Display result
st.write("Result:", result)
