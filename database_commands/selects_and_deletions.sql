-- SELECT * FROM USERS_CUSTOMUSER_GROUPS

-- SELECT * FROM USERS_CUSTOMUSER_USER_PERMISSIONS

SELECT * FROM USERS_CUSTOMUSER ORDER BY ID ASC;

SELECT * FROM POSTS_POST ORDER BY POSTED_ON DESC;

-- Select view for getting the first and last names of each post author
SELECT p.id, u.first_name, u.last_name, p.title, p.post_content, p.posted_on
FROM USERS_CUSTOMUSER AS "u" INNER JOIN POSTS_POST AS "p"
ON p.author_id = u.id ORDER BY POSTED_ON DESC;
