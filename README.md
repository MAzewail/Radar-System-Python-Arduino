# Radar System using Python, Arduino, and OpenCV

Welcome to the Radar System project repository! This project combines Python, Arduino, and an ultrasonic sensor to create a radar-like system that detects and displays the presence of objects in its vicinity. This README file provides an overview of the project and instructions on how to set it up and use it.

![](https://github.com/MAzewail/Radar-System-Python-Arduino/blob/main/Photos/Radar.png)

## Features

- Detects objects using an ultrasonic sensor
- Displays the detected objects on a graphical interface using OpenCV
- Provides real-time information about the objects' distance and position
- Adjustable scanning range and rotation speed
- Supports data logging for further analysis

## Getting Started

To get started with the Radar System, follow these steps:

### Prerequisites

- Python 3.x installed (https://www.python.org/downloads/)
- Arduino IDE installed (https://www.arduino.cc/en/software)
- Required Python packages: `pyserial`, `opencv-python`, `numpy`

### Hardware Setup

1. Connect the ultrasonic sensor to the Arduino board following the manufacturer's instructions.
2. Connect the Arduino board to your computer using a USB cable.

### Software Setup

1. Clone or download this repository to your local machine.
2. Open the Arduino IDE and upload the `arduino_code.ino` sketch from the `arduino` directory to your Arduino board.
3. Install the required Python packages by running the following command:
   ````
   pip install pyserial opencv-python
   ```

### Usage

1. Open a terminal or command prompt and navigate to the project directory.
2. Clone the repo:
   ````
   git clone https://github.com/MAzewail/Radar-System-Python-Arduino.git
   ````
4. Navigate to the project directory:
   ````
   cd Radar-System-Python-Arduino
   ````
6. Check the Port before running the code and edit the COM in the line # 35
   ````
   ![](https://github.com/MAzewail/Radar-System-Python-Arduino/blob/main/Photos/Screenshot%202024-12-05%20111038.png)
   ````
8. Run the Python script using the following command:
   ````
   python Radar_Graph_File.py
   ```
9. The radar system interface will open, displaying the scan area and detected objects in real-time using OpenCV.
10. Adjust the scanning range and rotation speed as desired by modifying the corresponding variables in the Python script.
11. Press Ctrl+C in the terminal or command prompt to stop the program.

### Data Logging

If you want to log the detected object data for further analysis, follow these steps:

1. Create a `data` directory within the project directory.
2. Uncomment the lines related to data logging in the `radar_system.py` script.
3. Run the script as described in the "Usage" section.
4. The detected object data will be logged to a CSV file in the `data` directory.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as permitted by the license.

## Contact

If you have any questions or feedback, please feel free to contact me.

We hope you find this Radar System project both interesting and useful! Thank you for your interest and support.

Happy coding!
