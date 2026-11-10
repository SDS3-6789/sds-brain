.PHONY: check index status sqlite

check:
	python3 scripts/brain.py validate
	python3 scripts/brain.py index --check
	python3 scripts/check_repository.py --manifest
	python3 -m unittest discover -s tests
	python3 scripts/acceptance.py
	python3 scripts/verify_offline_knowledge.py
	python3 scripts/vendor_grafana.py --check
	python3 scripts/check_plugin_layout.py
	python3 plugins/team-brain/mcp-servers/launch.py --check
	python3 scripts/sqlite_brain.py check --fresh

index:
	python3 scripts/brain.py index

status:
	python3 scripts/brain.py status

sqlite:
	python3 scripts/sqlite_brain.py build
