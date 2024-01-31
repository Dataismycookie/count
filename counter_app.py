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

# Increment the counter
if st.sidebar.button("Increment"):
    response = requests.post("d_2aioq7yi81pv787mwofptc547-t_60peshkr7nyx8w7b4a7irxi0c@mail.alpha.workspace", headers=headers)
    if response.status_code == 200:
        st.success("Counter increased successfully")
    else:
        st.error("Failed to increase counter")

# Decrement the counter
if st.sidebar.button("Decrement"):
    response = requests.post("d_2aioq7yi81pv787mwofptc547-t_60peshkr7nyx8w7b4a7irxi0c@mail.alpha.workspace", headers=headers)
    if response.status_code == 200:
        st.success("Counter decreased successfully")
    else:
        st.error("Failed to decrease counter")

# Reset the counter
if st.sidebar.button("Reset"):
    response = requests.post("d_2aioq7yi81pv787mwofptc547-t_60peshkr7nyx8w7b4a7irxi0c@mail.alpha.workspace", headers=headers)
    if response.status_code == 200:
        st.success("Counter reset successfully")
    else:
        st.error("Failed to reset counter")

# Fetch and display the counter value
response = requests.get("d_2aioq7yi81pv787mwofptc547-t_60peshkr7nyx8w7b4a7irxi0c@mail.alpha.workspace", headers=headers)
if response.status_code == 200:
    counter_value = response.json()["counter_value"]
    st.write(f"Counter Value: {counter_value}")
else:
    st.error("Failed to fetch counter value")
