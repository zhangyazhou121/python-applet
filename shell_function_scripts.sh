# 批量删除mysql数据库中表名相似的表
echo "show tables like '%wp_41_%'"| mysql -h localhost -u multisite3 -p multisite3 | sed '1d' >> tablelist1
for i in `cat tablelist1`; do echo "drop table "$i"" | mysql -h localhost -u multisite3 -p multisite3; done
