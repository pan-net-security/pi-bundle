BUNDLE_NAME          = pi-bundle
BUNDLE_VERSION      ?= 0.2.5
IMAGE_TAG            = pannet/$(BUNDLE_NAME):$(BUNDLE_VERSION)

.PHONY: docker docker-clean docker-shell docker-fresh

docker: Dockerfile .dockerignore
	docker build --rm -t $(IMAGE_TAG) .

docker-clean:
	docker rmi -f `docker images -q $(IMAGE_TAG)` || true

docker-shell:
	docker run --rm -it $(IMAGE_TAG) sh

docker-fresh: docker-clean docker
