# Dynamic String Service

A FastAPI-based web service that displays and allows updating a dynamic string without requiring redeployment.

## Features

- Display a dynamic string on a web page
- Update the string through a REST API
- Simple and clean UI
- Input validation using Pydantic
- Unit and system tests
- Code formatting with Black
- Infrastructure as Code with Terraform
- CI/CD with GitHub Actions

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Terraform 1.5.0 or higher
- AWS CLI configured with appropriate credentials

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

## Infrastructure Deployment

### Prerequisites

1. AWS CLI installed and configured
2. Terraform installed
3. S3 bucket for Terraform state (create manually)
4. DynamoDB table for state locking (create manually)

### Required AWS Resources

1. S3 bucket for Terraform state:
```bash
aws s3api create-bucket \
    --bucket arqiva-dyno-page-terraform-state \
    --region eu-west-2 \
    --create-bucket-configuration LocationConstraint=eu-west-2
```

2. DynamoDB table for state locking:
```bash
aws dynamodb create-table \
    --table-name terraform-state-lock \
    --attribute-definitions AttributeName=LockID,AttributeType=S \
    --key-schema AttributeName=LockID,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --region eu-west-2
```

### Local Deployment

1. Initialize Terraform:
```bash
cd terraform
terraform init
```

2. Plan the deployment:
```bash
terraform plan
```

3. Apply the changes:
```bash
terraform apply
```

### Environment Variables

The following environment variables are required for deployment:

- `AWS_ACCESS_KEY_ID`: Your AWS access key
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret key
- `AWS_DEFAULT_REGION`: AWS region (default: eu-west-2)

### Optional Variables

You can customize the deployment by setting these variables:

- `environment`: Environment name (default: dev)
- `domain_name`: Custom domain name (optional)
- `route53_zone_id`: Route 53 hosted zone ID (required if domain_name is set)

Example:
```bash
terraform apply -var="environment=prod" -var="domain_name=example.com" -var="route53_zone_id=Z1234567890"
```

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
├── terraform/
│   ├── main.tf
│   └── variables.tf
├── tests/
│   ├── test_api.py
│   └── test_string_controller.py
├── .github/
│   └── workflows/
│       └── terraform.yml
├── Makefile
├── README.md
└── requirements.txt
```

## Development

1. The string is stored in memory in the `StringController` class
2. The UI is built with HTML, CSS, and JavaScript
3. Input validation is handled by Pydantic models
4. Tests are written using pytest
5. Infrastructure is managed with Terraform
6. CI/CD is handled by GitHub Actions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 