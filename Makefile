.PHONY: order-check
order-check:
	dagger call pyright --root_dir . --project order-service

.PHONY: order-test
order-test:
	dagger call pytest --root_dir . --project order-service

.PHONY: common-check
common-check:
	dagger call pyright --root_dir . --project common

.PHONY: common-test
common-test:
	dagger call pytest --root_dir . --project common
