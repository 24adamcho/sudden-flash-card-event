run:
	run.bat

setup: requirements.txt
	pip install -r requirements.txt

clean:
	find . -type d -name a -prune -exec rm -rf {} \;