# 批量删除wordpress mysql数据库中的数据表
for((i=2;i<=17;i++));do echo "show tables like '%wp_"$i"_%'"| mysql -h localhost -u multisite3 -p multisite3 | sed '1d' >> tablelist; done
echo "show tables like '%wp_41_%'"| mysql -h localhost -u multisite3 -p multisite3 | sed '1d' >> tablelist1
for i in `cat tablelist1`; do echo "drop table "$i"" | mysql -h localhost -u multisite3 -p multisite3; done
