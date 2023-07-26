# Define the Flake8 command and its options
FLAKE8 := flake8
FLAKE8_OPTIONS := --count --show-source # --benchmark --statistics

# Target for linting Python files using Flake8
lint:
	$(FLAKE8) $(FLAKE8_OPTIONS)
