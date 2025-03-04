# Project Title: Code2Pseudo2Code

## Overview
Code2Pseudo2Code is a Streamlit application that allows users to convert pseudocode into C++ code and vice versa. This project leverages advanced models to facilitate the translation between these two programming representations, making it easier for developers and learners to understand and implement algorithms.

## Features
- Convert C++ code to pseudocode.
- Convert pseudocode to C++ code.
- User-friendly interface built with Streamlit.
- Utilizes pre-trained models for accurate code translation.

## Project Structure
```
code2pseudo2code
├── app.py                  # Main entry point for the Streamlit application
├── models                  # Contains model logic for code conversion
│   ├── __init__.py
│   ├── code_to_pseudo.py   # Logic for converting C++ code to pseudocode
│   └── pseudo_to_code.py   # Logic for converting pseudocode to C++ code
├── utils                   # Utility functions for tokenization and preprocessing
│   ├── __init__.py
│   ├── tokenizer_utils.py   # Functions for handling tokenization
│   └── preprocessing.py     # Functions for preprocessing input data
├── assets                  # Contains static assets like CSS
│   └── style.css           # Styles for the Streamlit application
├── requirements.txt        # Project dependencies
├── .gitignore              # Files and directories to ignore in Git
└── README.md               # Documentation for the project
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd code2pseudo2code
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the Streamlit application:
   ```
   streamlit run app.py
   ```
2. Open your web browser and go to `http://localhost:8501` to access the application.
3. Use the provided input fields to enter either pseudocode or C++ code and generate the corresponding output.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.