
-- Reseting the tables and the sequence
TRUNCATE TABLE USERS;
ALTER SEQUENCE USERS_CUSTOMUSER_ID_SEQ RESTART WITH 1;

TRUNCATE TABLE POSTS;
ALTER SEQUENCE POSTS_POST_ID_SEQ RESTART WITH 1;

/*
Checking the current order of the sequences
-- auth_user_id_seq
select currval('sequence')
select nextval('sequence')
*/
