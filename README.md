<div align="center">

# USpace

</div>

This is a web application that uses IoT devices that allow people within the EAFIT University (students, employees, and visitors) to know the real-time occupations of the spaces within the University.

## Requirements

To use this application you must follow the following steps:

1. **Clone the repository:**
    ```
    git clone https://github.com/srestrep74/P1.git
    ```

2. **Create and activate a virtual environment (optional):**
    - Using Python:
        
        ```
        python -m venv venvname
        ```
    - Using Conda:
        
        ```
        conda create --name venvname
        ```
    Replace the `venvname` with a proper name of the virtual environment, such as `USpace`.

3. **Install all requirements:**
    ```
    pip install -r requirements.txt
    ```

    **Note:** if you have an error trying to install `mysqlclient` dependency, and you cannot fix it, you can replace it with `mysql-connector-python` with the following command:

        pip install mysql-connector-python
    
    And change the database engine (line 95) inside the `USpace/settings.py` file as follows:

        'ENGINE': 'mysql.connector.django'

4. **Go to the directory where you cloned the project:**
    ```
    cd P1
    ```

5. **Run the server:**
    ```
    python manage.py runserver
    ```

6. You will see in your console the following link `http://127.0.0.1:8000/`. You must copy that link into your browser and then you can start using USpace.

## Contributors

- **Juan Manuel Gómez**
- **Miguel Ángel Hoyos**
- **Sebastian Restrepo Ortiz**
