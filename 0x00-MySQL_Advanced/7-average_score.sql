-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and
-- store the average score for a student. 
-- Note: An average score can be a decimal

DELIMITER //
 DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
 CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id int)
 BEGIN
 UPDATE users
 DECLARE average_score float
 SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
 WHERE id = user_id;
 END;
 //