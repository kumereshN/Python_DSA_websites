SELECT name, create_date, last_activity FROM registrations
  WHERE
last_activity
 >=
DATE_ADD
(
create_date
, INTERVAL 30 DAY);
