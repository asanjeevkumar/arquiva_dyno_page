# Dynamic String Service

A FastAPI-based web service that displays and allows updating a dynamic string without requiring redeployment.

## Features

- Display a dynamic string on a web page
- Update the string through a REST API
- Simple and clean UI
- Input validation using Pydantic
- Unit and system tests
- Code formatting with Black

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies:
```bash
make install
```

## Running the Application

Start the development server:
```bash
make run
```

The application will be available at `http://localhost:8000`

## API Endpoints

- `GET /`: Display the web page with the current string
- `POST /update-string`: Update the string
  - Request body: `{"new_string": "your new string"}`

## Testing

Run the test suite:
```bash
make test
```

## Code Formatting

Format the code using Black:
```bash
make format
```

## Project Structure

```
.
├── app/
│   ├── controllers/
│   │   └── string_controller.py
│   ├── models/
│   │   └── string_model.py
│   ├── templates/
│   │   └── index.html
│   └── main.py
├── tests/
│   ├── test_api.py
│   └── test_string_controller.py
├── Makefile
├── README.md
└── requirements.txt
```

## Development

1. The string is stored in memory in the `StringController` class
2. The UI is built with HTML, CSS, and JavaScript
3. Input validation is handled by Pydantic models
4. Tests are written using pytest

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 