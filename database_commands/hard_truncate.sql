/*
NOTICE:  truncate cascades to table "auth_user_groups"
NOTICE:  truncate cascades to table "auth_user_user_permissions"
NOTICE:  truncate cascades to table "django_admin_log"
*/

-- Starting the transaction
begin transaction;

-- Reseting the table and the sequence
truncate table auth_user cascade;
alter sequence auth_user_id_seq restart with 1;
alter sequence auth_user_groups_id_seq restart with 1;
alter sequence auth_user_user_permissions_id_seq restart with 1;
alter sequence django_admin_log_id_seq restart with 1;

ALTER SEQUENCE posts_post_id_seq RESTART WITH 1;

-- Commiting
commit;

/*
Checking the current order of the sequences

-- auth_user_id_seq
select currval('auth_user_id_seq')
select nextval('auth_user_id_seq')

-- auth_user_groups_id_seq
select currval('auth_user_groups_id_seq')
select nextval('auth_user_groups_id_seq')

-- auth_user_user_permissions_id_seq
select currval('auth_user_user_permissions_id_seq')
select nextval('auth_user_user_permissions_id_seq')

-- django_admin_log_id_seq
select currval('django_admin_log_id_seq')
select nextval('django_admin_log_id_seq')
*/
