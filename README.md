# Baku House Price Prediction Project

This is an interactive machine learning application that predicts house prices in Baku, Azerbaijan, based on user inputs via a GUI built with Tkinter. The project uses real housing data, cleans it, and trains a Random Forest model to estimate house prices.

---

## Features

- User-friendly GUI interface with step-by-step inputs.
- Predicts price based on:
  - Area (m²)
  - Number of rooms
  - Title deed status
  - Repair status
  - House category (new/old)
  - Region within Baku
- Data preprocessing and one-hot encoding for regions.
- Random Forest regression for price estimation.

---

## Project Screenshot

![Project Screenshot](https://drive.google.com/uc?export=view&id=1_XQGTMzMKJQozGAAfo-yQPf0Z3InODmA)

---

## Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- tkinter (usually pre-installed with Python)
- Pillow

Install required packages with:

bash
pip install pandas numpy scikit-learn matplotlib seaborn Pillow


## How It Works
1. Loads and preprocesses the dataset (processed_file_new.xlsx).
2. Takes user input through a Tkinter GUI for house features.
3. Converts input into the model’s expected format, including region one-hot encoding.
4. Predicts house price using a trained Random Forest model.
5. Displays the predicted price in a popup message box.

## Usage Instructions
1. Run the main Python script.
2. Input the area in square meters (between 20 and 300).
3. Input the number of rooms (between 1 and 10).
4. Indicate whether the house has a title deed (Yes/No).
5. Indicate whether the house has been repaired (Yes/No).
6. Specify if the house is new or old.
7. Select the region from the options presented.
8. View the predicted price popup.

## File Structure
- `your_script.py` — main Python script with GUI and model.
- `processed_file_new.xlsx` — preprocessed housing dataset.
- `favicon.ico` — application icon.
- `baku_image.png` — background image used in GUI.

## Customization
- Modify model parameters or try different regressors.
- Add more regions or features by updating dataset and GUI.
- Change GUI styling and layout in Tkinter as desired. 

## Troubleshooting
- Ensure all required files are in the same directory as the script.
- If the GUI doesn't appear, check Python and Tkinter installation.
- Verify all Python dependencies are installed.
- Check the console for any error messages.

## License
- This project is open source under the MIT License.
