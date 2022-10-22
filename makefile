run:
	run.bat

setup: requirements.txt
	pip install -r requirements.txt

clean:
	find ./src/ -type d -name __pycache__ -exec rm -rf {} \;
