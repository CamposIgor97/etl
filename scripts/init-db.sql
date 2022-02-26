create database eventdb;
use eventdb;
CREATE TABLE queue_event
(
    time String,
    type String,
    correlation_id String,
    site_id String
) ENGINE = Kafka('kafka:9092', 'event', 'group1')
SETTINGS
    kafka_format = 'JSONEachRow',
    kafka_num_consumers = 1;

CREATE TABLE event
(
    time String,
    type String,
    correlation_id String,
    site_id String
) ENGINE = MergeTree()
ORDER BY (time, type, correlation_id, site_id);

CREATE materialized view queue_to_event TO event AS select * from queue_event;

-- CREATE ROLE reader;
-- GRANT select on eventdb.* TO reader;
-- CREATE USER reader_user2 IDENTIFIED WITH sha256_password BY 'qwerty' DEFAUlT ROLE reader;