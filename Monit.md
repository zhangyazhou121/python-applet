1. 安装nettraffic

cd /usr/local/
wget http://zbx.shoplex.cn:8666/nettraffic.tar.bz2
tar -jxvf nettraffic.tar.bz2
chown -R root:staff nettraffic
cd nettraffic
python3 setup.py --install

修改配置文件config.py
网卡名称：
周期变更时间；
总带宽(GB):

设定周期内已经使用的流量值（Gb）
sudo netset -u 100

sudo /etc/init.d/nettraffic start
sudo systemctl status nettraffic 

2. 安装falcon agent

cd /usr/local
mkdir falcon
cd falcon
wget http://zbx.shoplex.cn:8666/open-falcon-v0.2.1.tar.gz
tar -zxf open-falcon-v0.2.1.tar.gz
sed -i "s/0.0.0.0:6030/221.229.173.150:6030/g" agent/config/cfg.json
sed -i "s/0.0.0.0:8433/221.229.173.150:8433/g" agent/config/cfg.json
./open-falcon start agent

3. 安装自定义push脚本

cd /usr/local/falcon
mkdir scripts
cd scripts
wget http://zbx.shoplex.cn:8666/push.py
chmod +x push.py

echo "*/1 * * * * /usr/bin/python2.7 /usr/local/falcon/scripts/push.py >/tmp/aa 2>&1" >> /var/spool/cron/crontabs/root
chmod 0600 /var/spool/cron/crontabs/root
/etc/init.d/cron restart

