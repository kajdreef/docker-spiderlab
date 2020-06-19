DOCKER_FILE=Dockerfile
image=spider-container
tag=latest

build:
	docker build -f ${DOCKER_FILE} -t ${image}:${tag} .

rebuild:
	docker build --no-cache -f ${DOCKER_FILE} -t ${image}:${tag} .

tag: build
	docker tag ${image}:${tag} kajdreef/${image}:${tag}

push: tag
	docker push kajdreef/${image}:${tag}

check:
	docker run --rm -i hadolint/hadolint hadolint - < Dockerfile

run:
	docker run -t -i ${image}:${tag} bash