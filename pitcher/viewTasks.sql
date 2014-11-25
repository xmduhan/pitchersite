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



1、刷票日志记录，支持刷票后余票（潜力）。(ok)
2、是否尝试去掉DEBUG，看看是否能解决内存问题。
3、修改刷票配置表数据结构，支持同航班号多次配置，如何人性化支持选择。
4、增加crontab配置。
5、一次订多张票的测试。

