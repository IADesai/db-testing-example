DROP DATABASE testing_example_prod;
CREATE DATABASE testing_example_prod;
\c testing_example_prod;

DROP TABLE IF EXISTS message;

CREATE TABLE message (
    message_id INT GENERATED ALWAYS AS IDENTITY,
    message_text VARCHAR(100)
);

DROP DATABASE testing_example_test;
CREATE DATABASE testing_example_test;
\c testing_example_test;

DROP TABLE IF EXISTS message;

CREATE TABLE message (
    message_id INT GENERATED ALWAYS AS IDENTITY,
    message_text VARCHAR(100)
);