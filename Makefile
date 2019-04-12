build: check
	docker build -t spiderlab .

tag: build
	docker tag spiderlab:latest kajdreef/spiderlab:latest

push: tag
	docker push kajdreef/spiderlab:latest

check:
	docker run --rm -i hadolint/hadolint hadolint - < Dockerfile