/* root 계정으로 접속, scof 데이터베이스 생성, scof 계정 생성 */
/* MySQL Workbench에서 초기화면에서 +를 눌러 root connection을 만들어 접속한다. */
DROP DATABASE IF EXISTS  scof;
DROP USER IF EXISTS  scof@localhost;
create user scof@localhost identified WITH mysql_native_password  by 'root';
create database scof;
grant all privileges on scof.* to scof@localhost with grant option;
commit;

/* madang DB 자료 생성 */
USE scof;

CREATE TABLE test_login(
	num		INTEGER	PRIMARY	KEY NOT NULL AUTO_INCREMENT,
    ID		VARCHAR(20),
    PW		VARCHAR(20)
);

INSERT INTO test_login (ID, PW) VALUES ('scof', 'sejong');
