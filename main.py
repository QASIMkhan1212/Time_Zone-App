# import required lib
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
# list of available timezones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Australia/Sydney",
    "Asia/Tokyo",
    "America/Los_Angeles",
    "Asia/Dubai",
    "Europe/Paris",
    "Asia/Kolkata",
]
# title of the app
st.title("Time Zone App")

# created a multiselect widget to select multiple timezones
selected_time_zone = st.multiselect("**Select Time Zones**", TIME_ZONES,default = ["UTC", "Asia/Karachi"])

# Display current time of selected timezones
st.subheader("Selected Time Zones")
for tz in selected_time_zone:
    
    # Get the current time of selected timezone with AM/PM
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")

    st.write(f"**{tz}**: {current_time}")
# Created a Sub-header for converting timezones between timezones
st.subheader("Convert Time Zone Between Timezones")

# Created a time input widget to get the current time
current_time = st.time_input("Current Time", value = datetime.now().time())

from_tz = st.selectbox("From Time Zone", TIME_ZONES , index = 0)

# Created a selectbox widget to select the from timezone
to_tz = st.selectbox("To Time Zone", TIME_ZONES , index = 1)

# Created a button to trigger the time conversion
if st.button("Convert Time"):
    
    # Combine the current time with the selected timezone
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    
    # Convert the time to the selected timezone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
    
    # Displaying the current time
    st.success(f"Converted Time: {converted_time}")
    