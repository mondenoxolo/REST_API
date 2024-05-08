# Color Description API

The Color Description API is a simple REST API built from scratch using Python. It generates random colors and provides a description of each color.

## Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/your-username/color-description-api.git
    ```

2. Navigate to the project directory:

    ```
    cd color-description-api
    ```

3. Create and activate a virtual environment (optional but recommended):

    ```
    virtualenv venv
    source venv/bin/activate   # for Unix/MacOS
    venv\Scripts\activate      # for Windows
    ```

4. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Start the server:

    ```
    python app.py
    ```

2. Once the server is running, you can access the API endpoints using HTTP requests.

    - To generate the colors and its description:
    
        ```
        GET /color
        ```
    
    - Example response:
    
        ```json
        {
            "color": "Red",
            "description": "This color is a vibrant shade of orange-red."
        }
        ```

## API Endpoints

- `GET /color`: Generates a random color and its description.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
