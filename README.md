<div align="center">

# USpace

</div>

This is a web application that allows people within the EAFIT University (students, employees, and visitors) to know the real-time occupations of the spaces within the University.

## Requirements

To use this application you must follow the following steps:

1. Clone the repository.
    ```
    git clone https://github.com/srestrep74/P1.git
    ```

2. Create a virtual environment (optional):
    - Using Python:
        
        ```
        python -m venv venvname
        ```
    - Using Conda:
        
        ```
        conda create --name venvname
        ```
    Replace the `venvname` with a proper name of the virtual environment, such as `USpace`.

3. Install all requirements:
    ```
    pip install -r requirements.txt
    ```

4. Go to the directory where you cloned the project:
    ```
    cd P1
    ```

5. Run the server:
    ```
    python manage.py runserver
    ```

5. You will see in your console a link starting with `https://`. You must copy that link into your browser and then you can start using USpace.
