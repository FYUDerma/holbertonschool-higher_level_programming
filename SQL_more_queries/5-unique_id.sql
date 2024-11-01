-- Creates table `unique_id` with `id and `name` fields. DB in args.
CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
