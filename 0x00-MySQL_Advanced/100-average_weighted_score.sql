-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes
-- and store the average weighted score for a student.

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN p_user_id INT);

BEGIN
    DECLARE avg_w FLOAT;

    SELECT AVG(score) INTO avg_w
    FROM corrections
    WHERE user_id = p_user_id;

UPDATE users
SET average_score = avg_w
WHERE id = p_user_id;

END;
DELIMITER ;
