import streamlit as st
if "accounts" not in st.session_state:
    st.session_state.accounts = {}
accounts = st.session_state.accounts
st.set_page_config(page_title="Banking System",layout="centered")
st.title("Banking System")



option = st.selectbox("Choose an operation", ["Open Account", "Deposit", "Withdraw", "Check Balance","All accounts"])



def account_open():
    st.subheader("Open Account")
    with st.form(key="Open Account"):
    
        name = st.text_input("Acount Tittle: ",key="account_title_input")
        pin = st.text_input("create a accout pin: pin must be 4 digit: ",max_chars=4,type="password",key="pin_input")
        submitted = st.form_submit_button("Confirm")
        if submitted:
            if pin in accounts:
                st.error("pin is already exist")
            elif len(pin) != 4 or not pin.isdigit():
                st.error("PIN must be exactly 4 digits.")
            elif not name:
                st.error("Account title cannot be empty.")

            else:
                accounts[pin] = {"name":name, "balance": 0}
                st.success("account is successfully created")


def deposite ():
    st.subheader("Deposit")
    with st.form("Deposit Form"):
        pin = st.text_input("Enter your PIN", max_chars=4, type="password")
        amount = st.number_input("Enter amount to deposit")
        submitted = st.form_submit_button("Confirm Deposit")
        if submitted:
            if pin in accounts:
                accounts[pin]["balance"] += amount
                st.success(f"Deposited {amount:.2f} successfully.")
                st.info(f"New Balance: {accounts[pin]['balance']:.2f}")
            else:
                st.error("Invalid PIN.")



def withdraw():
    st.subheader("Withdraw Amount")
    with st.form("Withdraw Money"):
    
        pin = st.text_input("Enter your Pin",max_chars=4,type="password")
        amount = st.number_input("Enter your amount: ")
        submitted = st.form_submit_button("Confirm Withdraw")
        if submitted:
            if pin in accounts:
                
               
                if amount  <= accounts[pin]["balance"]:
                    accounts[pin]["balance"] -= amount
                    st.success(f"Amount withdraw successfully {amount}: ")
                else:
                    st.error(f"Insufficient amount {amount}: ")
            else:
                st.error("Invalid Pin")


def check_balance():
    st.subheader("Check Balance")
    with st.form("Check Balance"):
   
        pin = st.text_input("Enter your Pin",type="password",max_chars=4)
        submitted = st.form_submit_button("Check Balacnce")
        if submitted:
            if pin in accounts:
                name = accounts[pin]["name"]
                balance = accounts[pin]["balance"]
                st.write(f"Account title is {name}\nAccount balance is {balance}")
            else:
                st.error("Invalid Pin")
import time

def check_all_accounts():
    st.subheader("Checking Accounts")

    # Initialize session state variables
    if "attempt_time" not in st.session_state:
        st.session_state.attempt_time = 0
    if "locked_out" not in st.session_state:
        st.session_state.locked_out = False

    with st.form("All Accounts"):
        pin = st.text_input("Enter password:", type="password")
        submitted = st.form_submit_button("Submit")

        if submitted:
            current_time = time.time()
            # Check if user is locked out
            if st.session_state.locked_out:
                if current_time - st.session_state.attempt_time < 900:  # 15 minutes = 900 seconds
                    st.error("Too many attempts. Please try again later.")
                    return
                else:
                    st.session_state.locked_out = False  # Reset lockout after 15 minutes

            if pin == "12ah12":
                st.success("Access granted.")
                st.dataframe(data=accounts)
            else:
                st.error("Invalid Password!")
                st.session_state.locked_out = True
                st.session_state.attempt_time = current_time



if  option ==  "Open Account":
    account_open()
    
elif option == "Deposit":
    deposite()
elif option == "Withdraw":
    withdraw()
elif option == "Check Balance":
    check_balance()
elif option == "All accounts":
    check_all_accounts()