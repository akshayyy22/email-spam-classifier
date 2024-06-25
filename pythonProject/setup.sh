#!/bin/bash

# Create the Streamlit configuration directory
mkdir -p ~/.streamlit/

# Create or overwrite the Streamlit configuration file
cat <<EOF > ~/.streamlit/config.toml
[server]
port = $PORT
enableCORS = false
headless = true
EOF

# Install required packages
pip install -r requirements.txt