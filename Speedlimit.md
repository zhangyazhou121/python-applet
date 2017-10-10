
tc_normal() {
####normal line
tc qdisc del dev $1 root
tc qdisc add dev $1 root handle 1: htb default 30
tc class add dev $1 parent 1:0 classid 1:1 htb rate 5mbit ceil 5mbit burst 40k prio 0
tc class add dev $1 parent 1:0 classid 1:2 htb rate 100mbit ceil 100mbit burst 40k prio 1
tc qdisc add dev $1 parent 1:1 handle 10: sfq perturb 10
tc qdisc add dev $1 parent 1:2 handle 20: sfq perturb 10
tc filter add dev $1 protocol ip parent 1:0 prio 0 u32 match ip dst 0.0.0.0/0 flowid 1:1
tc filter add dev $1 protocol ip parent 1:0 prio 1 u32 match ip dst 211.103.189.114/32 flowid 1:2
}

tc_normal eth0



tc_status() {
tc -s qdisc show dev $1
echo ""
tc class show dev $1
echo ""
tc -s class show dev $1
echo ""
tc filter ls dev $1 parent ffff:
}

tc_status eth0

以T为单位的流量，换成这句
tc class add dev $1 parent 1:0 classid 1:1 htb rate 8mbit ceil 8mbit burst 40k prio 0