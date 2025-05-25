.PHONY: install run test format clean

install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload

test:
	pytest tests/

format:
	black .

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete 