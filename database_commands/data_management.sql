
-- Select view for getting the first and last names of each post author
SELECT p.id, u.first_name, u.last_name, p.title, p.post_content, p.posted_on
FROM USERS AS "u" INNER JOIN POSTS AS "p"
ON p.author_id = u.id ORDER BY POSTED_ON DESC;

-- Regular selects
SELECT * FROM USERS ORDER BY ID ASC;

SELECT * FROM POSTS ORDER BY POSTED_ON DESC;

-- Database population
BEGIN TRANSACTION;

INSERT INTO POSTS (TITLE, POST_CONTENT, POSTED_ON, AUTHOR_ID) VALUES ('Look at this post!', 'This is a nice content is it not?', CURRENT_TIMESTAMP, 1);
INSERT INTO POSTS (TITLE, POST_CONTENT, POSTED_ON, AUTHOR_ID) VALUES ('They all look the same', 'Do her posts all look the same?', CURRENT_TIMESTAMP + interval '1 minute', 2);
INSERT INTO POSTS (TITLE, POST_CONTENT, POSTED_ON, AUTHOR_ID) VALUES ('Say something nice', 'Thats me saying a nice thing', CURRENT_TIMESTAMP + interval '2 minute', 1);
INSERT INTO POSTS (TITLE, POST_CONTENT, POSTED_ON, AUTHOR_ID) VALUES ('They all look the same', 'Do her posts all look the same?', CURRENT_TIMESTAMP + interval '3 minute', 2);
INSERT INTO POSTS (TITLE, POST_CONTENT, POSTED_ON, AUTHOR_ID) VALUES ('Am i getting vaccinated?', 'Hopefully tomorrow ill get vaccinated!', CURRENT_TIMESTAMP + interval '4 minute', 1);
INSERT INTO POSTS (TITLE, POST_CONTENT, POSTED_ON, AUTHOR_ID) VALUES ('They all look the same', 'Do her posts all look the same?', CURRENT_TIMESTAMP + interval '5 minute', 2);
INSERT INTO POSTS (TITLE, POST_CONTENT, POSTED_ON, AUTHOR_ID) VALUES ('Missing WOW', 'It was such a good time eh', CURRENT_TIMESTAMP + interval '6 minute', 1);
INSERT INTO POSTS (TITLE, POST_CONTENT, POSTED_ON, AUTHOR_ID) VALUES ('They all look the same', 'Do her posts all look the same?', CURRENT_TIMESTAMP + interval '7 minute', 2);
INSERT INTO POSTS (TITLE, POST_CONTENT, POSTED_ON, AUTHOR_ID) VALUES ('Working hard', 'Maybe in a year ill get the job i want', CURRENT_TIMESTAMP + interval '8 minute', 1);
INSERT INTO POSTS (TITLE, POST_CONTENT, POSTED_ON, AUTHOR_ID) VALUES ('They all look the same', 'Do her posts all look the same?', CURRENT_TIMESTAMP + interval '9 minute', 2);
INSERT INTO POSTS (TITLE, POST_CONTENT, POSTED_ON, AUTHOR_ID) VALUES ('Meaningless post', 'Its doesnt mean anything lol', CURRENT_TIMESTAMP + interval '10 minute', 1);
INSERT INTO POSTS (TITLE, POST_CONTENT, POSTED_ON, AUTHOR_ID) VALUES ('They all look the same', 'Do her posts all look the same?', CURRENT_TIMESTAMP + interval '11 minute', 2);

COMMIT;
