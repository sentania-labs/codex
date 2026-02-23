.PHONY: dev lint api-dev web-dev generate-types

dev:
	docker compose up --build

api-dev:
	cd apps/api && uvicorn app.main:app --reload --port 8000

web-dev:
	npm --workspace @mtg/web run dev

generate-types:
	python apps/api/export_openapi.py
	npm --workspace @mtg/shared run generate

lint:
	cd apps/api && ruff check app
	npm --workspace @mtg/web run lint
