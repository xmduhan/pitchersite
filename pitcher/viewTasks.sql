select * from pitcher_ticketcountlog
where "departureTime" = '09:30'
  and "departure" = '邮轮中心厦鼓码头'
  and "arrival" = '三丘田码头'
  order by "logTime";

--
select  "departureTime",count(*)*3 "机会时间(秒)"
from pitcher_ticketcountlog
where 1 = 1
  and "departureTime" >= '08:10' and "departureTime" <= '10:30'
  and "departure" = '邮轮中心厦鼓码头'
  and "arrival" = '三丘田码头'
  and "ticketCount" > 0
  group by "departureTime"
  order by "departureTime";