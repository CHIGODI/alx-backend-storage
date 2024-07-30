-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes
-- and store the average weighted score for a student.

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN p_user_id INT)
BEGIN
    DECLARE weighted_sum FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;
    DECLARE weighted_average FLOAT;

    -- Calculate the weighted sum of scores and total weight
    SELECT
        SUM(c.score * p.weight),
        SUM(p.weight)
    INTO
        weighted_sum,
        total_weight
    FROM
        corrections c
    JOIN
        projects p ON c.project_id = p.id
    WHERE
        c.user_id = p_user_id;

    -- Calculate the weighted average
    SET weighted_average = weighted_sum / total_weight;

    -- Update the users table with the calculated weighted average
    UPDATE
        users
    SET
        average_score = weighted_average
    WHERE
        id = p_user_id;
END$$

DELIMITER ;