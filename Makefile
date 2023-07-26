# Define the directories and files to be checked by Flake8
SRC_DIR := pyhelpmixin
TEST_DIR := pyhelpmixin/tests
FILES := $(wildcard $(SRC_DIR)/*.py) $(wildcard $(TEST_DIR)/*.py)

# Define the Flake8 command and its options
FLAKE8 := flake8
FLAKE8_OPTIONS :=   # --exclude=

# Target for linting Python files using Flake8
lint:
    $(FLAKE8) $(FLAKE8_OPTIONS) $(FILES)