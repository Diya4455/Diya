import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Function to open an image file dialog
def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        display_image(file_path)

# Function to display the selected image
def display_image(image_path):
    image = Image.open(image_path)
    image = image.resize((300, 300))
    photo = ImageTk.PhotoImage(image)
    
    # Update the label widget to display the new image
    image_label.config(image=photo)
    image_label.image = photo

# Function to analyze the image based on selected type and generate autocompleted text
def analyze_image():
    selected_type = image_type_var.get()
    diagnostic_result = ""

    if selected_type == "USG":
        diagnostic_result = "YOUR USG IMAGES ARE NORMAL."
    elif selected_type == "PET SCAN":
        diagnostic_result = "PET SCAN REPORT: No significant abnormalities detected."
    elif selected_type == "XRAY":
        diagnostic_result = "X-RAY REPORT: No fractures or anomalies detected."
    elif selected_type == "MRI":
        diagnostic_result = "MRI REPORT: No abnormal findings observed."
    elif selected_type == "CT SCAN":
        diagnostic_result = "CT SCAN RESULTS: Normal brain scan."

    # Display the generated diagnostic result in uppercase
    result_label.config(text=diagnostic_result.upper())

# Create the main application window
root = tk.Tk()
root.title("AI-Based Diagnostic Assistance")

# Create labels and input fields for patient information
patient_id_label = tk.Label(root, text="Patient ID:")
patient_id_label.pack()
patient_id_entry = tk.Entry(root)
patient_id_entry.pack()

patient_name_label = tk.Label(root, text="Patient Name:")
patient_name_label.pack()
patient_name_entry = tk.Entry(root)
patient_name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

sex_label = tk.Label(root, text="Sex:")
sex_label.pack()
sex_entry = tk.Entry(root)
sex_entry.pack()

mobile_label = tk.Label(root, text="Mobile No:")
mobile_label.pack()
mobile_entry = tk.Entry(root)
mobile_entry.pack()

# Create a dropdown menu for image type selection
image_type_label = tk.Label(root, text="Select Image Type:")
image_type_label.pack()
image_types = ["USG", "PET SCAN", "XRAY", "MRI", "CT SCAN","ECG","EEG","EMG","EHR" ]
image_type_var = tk.StringVar(root)
image_type_var.set(image_types[0])  # Set the default image type
image_type_menu = tk.OptionMenu(root, image_type_var, *image_types)
image_type_menu.pack()

# Create buttons to open an image, analyze it, and display results
open_button = tk.Button(root, text="Open Image", command=open_image)
analyze_button = tk.Button(root, text="Analyze Image", command=analyze_image)
open_button.pack(pady=10)
analyze_button.pack(pady=10)

# Create a label to display the image and another label for the analysis result
image_label = tk.Label(root)
result_label = tk.Label(root, text="", wraplength=300)
image_label.pack()
result_label.pack(pady=10)

# Save patient information to a text file
def save_patient_info():
    patient_info = f"Patient ID: {patient_id_entry.get()}\n"
    patient_info += f"Patient Name: {patient_name_entry.get()}\n"
    patient_info += f"Age: {age_entry.get()}\n"
    patient_info += f"Sex: {sex_entry.get()}\n"
    patient_info += f"Mobile No: {mobile_entry.get()}\n"
    
    with open("patient_info.txt", "w") as file:
        file.write(patient_info)

# Create a button to save patient information
save_button = tk.Button(root, text="Save Patient Info", command=save_patient_info)
save_button.pack(pady=10)

# Start the main GUI loop
root.mainloop()
