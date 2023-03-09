run:
	start "Sudden Flash Card Event" pythonw ./src/main.pyw --config "./config/cfg.json"

setup: requirements.txt
	pip install -r requirements.txt

clean:
	find ./src/ -type d -name __pycache__ -exec rm -rf {} \;
