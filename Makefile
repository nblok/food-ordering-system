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

.PHONY: run_zookeeper
run_zookeeper:
	docker-compose -f 'projects/infrastructure/docker-compose/common.yml' -f 'projects/infrastructure/docker-compose/zookeeper.yml' up

.PHONY: run_kafka
run_kafka:
	docker-compose -f 'projects/infrastructure/docker-compose/common.yml' -f 'projects/infrastructure/docker-compose/kafka_cluster.yml' up

.PHONY: init_kafka
init_kafka:
	docker-compose -f 'projects/infrastructure/docker-compose/common.yml' -f 'projects/infrastructure/docker-compose/init_kafka.yml' up
