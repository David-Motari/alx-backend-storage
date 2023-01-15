-- SQL script that creates a function SafeDiv that divides (and returns)
-- the first by the second number or returns 0 if the second number is equal to 0.

DELIMITER //

DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a int, b int)
RETURNS FLOAT
BEGIN
DECLARE outcome FLOAT
IF b = 0 THEN
    SET outcome = 0;
ELSE
    outcome = a / b;
END IF;
RETURN outcome;
END;
//