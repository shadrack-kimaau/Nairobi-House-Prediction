# Nairobi House Prediction
# To be filled with project details

.PHONY: help setup install clean test run-app run-dashboard

help:
	@echo "Available commands:"
	@echo "  make setup          - Set up the project environment"
	@echo "  make install        - Install dependencies"
	@echo "  make clean          - Remove temporary files"
	@echo "  make test           - Run tests"
	@echo "  make run-app        - Run Streamlit app"
	@echo "  make run-dashboard  - Run dashboard"

setup:
	bash setup.sh

install:
	pip install -r requirements.txt

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +

test:
	pytest tests/ -v

run-app:
	streamlit run app/app.py

run-dashboard:
	python dashboard/dashboard.py
