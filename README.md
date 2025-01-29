<div align="center">

# USpace: Real-Time Space Occupancy Monitoring at EAFIT University

</div>

**USpace** is a web-based application designed to provide real-time monitoring of space occupancy within EAFIT University. By utilizing Internet of Things (IoT) devices, this application allows students, employees, and visitors to easily view available spaces such as desks, cafeterias, study rooms, and other university facilities.

This project aims to improve space management, enhance campus experience, and support efficient resource utilization within the university.

---

## Features

- **Real-Time Space Occupancy**: Monitor the current occupancy of various university spaces.
- **Interactive Map**: View space availability in a dynamic and easy-to-understand map interface.
- **IoT Integration**: Utilizes Raspberry Pi devices for space detection, providing live occupancy data to the application.
- **User-Friendly Interface**: Simple and intuitive interface for students, employees, and visitors to quickly find available spaces.
- **Smart Campus Support**: Contributes to EAFIT University’s smart campus initiative by optimizing space usage and reducing wasted time.

---

## Requirements

Follow these steps to set up the application locally:

### 1. Clone the Repository

Clone the project repository to your local machine:

    git clone https://github.com/srestrep74/P1.git
    

### 2. Set Up a Virtual Environment (Optional but Recommended)
    - Using Python:
        python -m venv venvname
        
    - Using Conda:
        conda create --name venvname
        
Replace the `venvname` with a proper name of the virtual environment, such as `USpace`.

### 3. Install the Dependencies

Navigate to the project directory and install all required Python packages:

    pip install -r requirements.txt

**Note:** If you encounter an error while installing the mysqlclient dependency, use the following command to install mysql-connector-python instead:
   
    pip install mysql-connector-python
   
Then, change the database engine in the USpace/settings.py file (line 95) as follows:
    
    'ENGINE': 'mysql.connector.django'
   
    
### 4. Navigate to the Project Directory
    cd P1

### 5. Run the Development Server
    python manage.py runserver

Once the server is running, open the provided URL (typically http://127.0.0.1:8000/) in your browser to access the application.

## Impact and Benefits

- **Enhanced Campus Experience**: USpace allows students, employees, and visitors to quickly find available spaces, reducing time spent searching for places to work, study, or meet.
- **Optimized Space Usage**: By providing real-time data on space occupancy, the university can better manage its facilities, improving overall resource utilization.
- **Smart Campus Contribution**: The project supports EAFIT University’s initiatives for a smarter campus, helping implement IoT-based solutions for everyday problems.
- **Scalability**: The system can be expanded to monitor more spaces or integrated with other campus services, making it a versatile and long-term solution.



## Contributors

- **Sebastian Restrepo Ortiz** - Lead Developer
- **Juan Manuel Gómez** - IoT Integration Specialist
- **Miguel Ángel Hoyos** - Backend Developer
