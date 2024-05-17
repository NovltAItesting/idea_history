import streamlit as st
import json
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to history.json in the parent directory
json_file_path = os.path.join(current_dir, '..', 'mainhistory.json')

with open(json_file_path, 'r') as file:
    existing_json_data = json.load(file)
    st.json(existing_json_data,expanded=False)