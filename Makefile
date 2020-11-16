VERSION := $(shell cat version.py | cut -d "=" -f 2 | tr -d "'")
PWD := $(shell pwd)
BUILD_DIR = $(PWD)/dist
PROG := pymegafon-$(VERSION)-py3-none-any.whl

.PHONY: all version build clean install

build: $(BUILD_DIR) $(BUILD_DIR)/$(PROG)
	@echo "Last steps"

$(BUILD_DIR)/$(PROG):
	@echo target is $@
	python3 setup.py sdist bdist_wheel

install:
	python3 -m pip install --upgrade --user "$(BUILD_DIR)/$(PROG)"

version:
	@echo "Version: $(VERSION)"

clean:
	[ -f "$(BUILD_DIR)/$(PROG)" ] && rm -vf "$(BUILD_DIR)/$(PROG)" || :

$(BUILD_DIR):
	mkdir -p "$(BUILD_DIR)"
