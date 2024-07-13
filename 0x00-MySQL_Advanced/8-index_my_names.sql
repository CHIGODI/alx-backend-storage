-- SQL script that creates an index idx_name_first on the table names
-- and the first letter of name.

ALTER TABLE names
ADD COLUMN first_letter CHAR(1)
SET first_letter = SUBSTR(name, 1, 1);

CREATE INDEX idx_name_first ON names (first_letter);