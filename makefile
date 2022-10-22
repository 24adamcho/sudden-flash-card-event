run:
	run.bat

setup: requirements.txt
	pip install -r requirements.txt

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} \;