-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a student.

DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users, 
    (SELECT users.id, SUM(score * weight) / SUM(weight) AS weight_avg 
    FROM users
    JOIN corrections ON users.id = corrections.user_id 
    JOIN projects ON corrections.project_id = projects.id 
    GROUP BY users.id)
  AS WeightAverage
  SET users.average_score = WeightAverage.weight_avg 
  WHERE users.id = WeightAverage.id;
END;
//