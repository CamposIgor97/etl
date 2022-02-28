create database eventdb;
use eventdb;
CREATE TABLE queue_event
(
    time String,
    type String,
    correlation_id String,
    site_id String
) ENGINE = Kafka('my-release-kafka:9092', 'event', 'group1')
SETTINGS
    kafka_format = 'JSONEachRow',
    kafka_num_consumers = 1;

-- Should be revisited I've tried converting the string directly on the SQL from the view
-- Used DateTime and DateTime64(9) as type formats and parseDateTimeBestEffort(time)
-- but it always inserted as 1970-01-01 00:00:00
CREATE TABLE event
(
    time String,
    type String,
    correlation_id String,
    site_id String
) ENGINE = MergeTree()
ORDER BY (time, type, correlation_id, site_id);

CREATE materialized view queue_to_event TO event AS select * from queue_event;

INSERT INTO event VALUES('2021-01-22T18:20:42.159246','serve','357d1bc4-3502-4592-8355-874b1c31f1a0','0faf8b64-a33d-4db8-aaee-aa165d13cff6');
INSERT INTO event VALUES('2021-01-22T18:20:42.159246','serve','357d1bc4-3502-4592-8355-874b1c31f1a1','0faf8b64-a33d-4db8-aaee-aa165d13cff6');
INSERT INTO event VALUES('2021-01-22T18:20:42.159246','serve','357d1bc4-3502-4592-8355-874b1c31f1a2','0faf8b64-a33d-4db8-aaee-aa165d13cff6');
INSERT INTO event VALUES('2021-01-22T18:20:42.159246','serve','357d1bc4-3502-4592-8355-874b1c31f1a3','0faf8b64-a33d-4db8-aaee-aa165d13cff6');
INSERT INTO event VALUES('2021-01-22T18:20:42.159246','serve','357d1bc4-3502-4592-8355-874b1c31f1a3','0faf8b64-a33d-4db8-aaee-aa165d13cff6');
INSERT INTO event VALUES('2021-01-22T18:20:42.159246','solve','357d1bc4-3502-4592-8355-874b1c31f1a0','0faf8b64-a33d-4db8-aaee-aa165d13cff6');
INSERT INTO event VALUES('2021-01-22T18:20:42.159246','solve','357d1bc4-3502-4592-8355-874b1c31f1a1','0faf8b64-a33d-4db8-aaee-aa165d13cff6');
INSERT INTO event VALUES('2021-01-22T18:20:42.159246','solve','357d1bc4-3502-4592-8355-874b1c31f1a2','0faf8b64-a33d-4db8-aaee-aa165d13cff6');