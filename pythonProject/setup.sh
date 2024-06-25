#!/bin/bash
# Create the Streamlit configuration directory
mkdir -p ~/.streamlit/

# Create the Streamlit configuration file
echo "\
[server]\n\
port = \$PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml

# Install required packages
pip install -r requirements.txt