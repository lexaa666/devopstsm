Развернуть две ВМ: Server и Store
на Server
1) Установить mysql
 - sudo apt install mysql-server
 - подключаемся к бд : sudo mysql
 - создаем пользователя : CREATE USER 'tsmadmin'@'localhost' IDENTIFIED BY 'password_1';
 - добавляем привелегий : GRANT ALL PRIVILEGES ON * . * TO 'tsmadmin'@'localhost';
 - применяем изменния : FLUSH PRIVILEGES;

2) Создать БД
   - create database test;
   - переключаемся на бд test : use test;
  
     ![](/2.png)
3) Создать несколько таблиц и наполнить данными
	- create table table1()/create table table2()
  
      ![](/3.png)
4) Создать скрипт для бэкапа раз в час ( бэкап в директорию /opt/mysql_backup)
   
     ![](/4.png)
    
 - создаем bash  скрипт mysql_dump.sh
```bash
#!/bin/bash
mysqldump --defaults-extra-file=/etc/mysql/mysqlpassword.cnf -u tsmadmin  test > /opt/mysql_backup/mysql_backup.sql
```
 - добавление в crontab.
```bash
@hourly   /opt/mysql_backup/mysql_dump.sh
```
5) Настроить синхронизацию через rsync в папку /opt/store/mysql на ВМ Store
   
     ![](/5.png)
```console
rsync /opt/mysql_backup/mysql_backup.sql  tsmadmin1@192.168.50.79:/opt/mysql_backup/ 
```

1) Проверить восстановление(предварительно удалив БД)
```console
mysql --defaults-extra-file=/etc/mysql/mysqlpassword.cnf -u tsmadmin -p test < mysql_backup.sql
```

