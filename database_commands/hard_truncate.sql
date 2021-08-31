/*
NOTICE:  truncate cascades to table "auth_user_groups"
NOTICE:  truncate cascades to table "auth_user_user_permissions"
NOTICE:  truncate cascades to table "django_admin_log"
*/

-- Starting the transaction
begin transaction;

-- Reseting the tables and the sequence
TRUNCATE TABLE USERS_CUSTOMUSER;
ALTER SEQUENCE USERS_CUSTOMUSER_ID_SEQ RESTART WITH 1;

TRUNCATE TABLE posts_post;
ALTER SEQUENCE posts_post_id_seq RESTART WITH 1;

-- Commiting
commit;

/*
Checking the current order of the sequences
-- auth_user_id_seq
select currval('sequence')
select nextval('sequence')
*/
