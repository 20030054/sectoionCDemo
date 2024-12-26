import streamlit as st

def main():
    st.title("Simple Calculator Application")
    
    # Input fields
    st.header("Enter Numbers")
    number1 = st.number_input("First Number", value=0.0, step=0.1, format="%.2f")
    number2 = st.number_input("Second Number", value=0.0, step=0.1, format="%.2f")
    
    # Operation selection
    st.header("Select Operation")
    operation = st.radio(
        "Operation",
        ("Addition", "Subtraction", "Multiplication", "Division")
    )

    # Perform calculation
    result = None
    if st.button("Calculate"):
        if operation == "Addition":
            result = number1 + number2
        elif operation == "Subtraction":
            result = number1 - number2
        elif operation == "Multiplication":
            result = number1 * number2
        elif operation == "Division":
            if number2 != 0:
                result = number1 / number2
            else:
                st.error("Division by zero is not allowed.")
        
        if result is not None:
            st.success(f"The result is: {result}")

if __name__ == "__main__":
    main()
