import streamlit as st
import requests
# Replace 'YOUR_API_KEY' with your actual API key
api_key = '91hg5lFfluglrylERjyMK8CHZ+POM7JqKvdcSIHxwcb+kEm3DLb7/q/3p+IUgvGOY'

# Define the headers with the API key
headers = {
    'Authorization': f'Bearer {api_key}',
}
st.title("Counter App")
st.sidebar.header("Options")

if st.sidebar.button("Increment"):
    # Send an API request to increment the counter in your web-based database
    # Use the requests library to make the API call
    response = requests.post("d_2aioq7yi81pv787mwofptc547-t_60peshkr7nyx8w7b4a7irxi0c@mail.alpha.workspace.gov.sg")
    if response.status_code == 200:
        st.success("Counter increase successful")
    else:
        st.error("Failed to increase counter")
if st.sidebar.button("Decrement"):
    # Send an API request to decrement the counter in your web-based database
    # Handle the response as needed
#buttons to reset counter
if st.sidebar.button("Reset"):
    # Send an API request to reset the counter in your web-based database
    # Handle the response as needed
  #display counter
  response = requests.get("d_2aioq7yi81pv787mwofptc547-t_60peshkr7nyx8w7b4a7irxi0c@mail.alpha.workspace")
if response.status_code == 200:
    counter_value = response.json()["counter_value"]
    st.write(f"Counter Value: {counter_value}")
else:
    st.error("Failed to fetch counter value")
