# QR Code Generator
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6%2B-brightgreen)
![Libraries](https://img.shields.io/badge/dependencies-Pillow%20%7C%20Requests-orange)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)
![API](https://img.shields.io/badge/API-goqr.me-lightblue)

A simple GUI-based QR code generator built with Python's `tkinter` library. This application allows users to create QR codes quickly by entering custom data and dimensions.

---

## Features

- **User-Friendly Interface**: Intuitive design with clear input fields.
- **Customizable Dimensions**: Specify the dimensions of the QR code (e.g., `300x300`).
- **Instant QR Code Generation**: Generates a QR code and displays it instantly within the application.
- **Save to File**: Automatically saves the generated QR code as a PNG file.
- **Error Handling**: Provides clear error messages for invalid inputs or network issues.

---

## Requirements

- Python 3.6 or later
- Libraries:
  - `tkinter`
  - `Pillow`
  - `requests`

To install the required libraries, run:
```bash
pip install Pillow requests
```

---

## How to Use

1. Clone or download the repository.
2. Navigate to the project directory and run the script:
   ```bash
   python main.py
   ```
3. Enter the desired data into the **Enter Data** field.
4. Specify the dimensions in the **Enter Dimensions** field (e.g., `300x300`). Maximum size allowed is `750x750`.
5. Click the **Generate QR Code** button to create your QR code.
6. The generated QR code will be displayed in the app and saved as `qrcode.png` in the current directory.

---

## Example

- **Input Data**: `https://github.com`
- **Dimensions**: `300x300`
- **Output**: A 300x300 QR code linking to GitHub, saved as `qrcode.png`.

---

### Main Interface:
The main screen has fields for data entry, dimensions, and a button to generate the QR code.

### QR Code Display:
Generated QR codes are displayed within the app. They will also be saved to your local machine.

---

## Error Messages

- **Empty Data**: Displays an error if the data field is empty.
- **Invalid Dimensions**: Ensures dimensions are in the format `widthxheight` and within the acceptable range.
- **Network Issues**: Handles errors if the QR code API request fails.

---

## Contributing

Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request. Suggestions and bug reports are appreciated via the Issues section.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

- QR Code API: [goqr.me](https://goqr.me/)
- Python Libraries: `tkinter`, `Pillow`, `requests`

