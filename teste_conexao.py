#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel


class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."

    def build(self, n=2):
	    core_switch = self.addSwitch("c1")
        aggregation_switch_1 = self.addSwitch("a1")
        aggregation_switch_2 = self.addSwitch("a2")
        edge_switch_1 = self.addSwitch("e1")
        edge_switch_2 = self.addSwitch("e2")
        edge_switch_3 = self.addSwitch("e3")
        edge_switch_4 = self.addSwitch("e4")
	    host1 = self.addHost("h1")
        host2 = self.addHost("h2")
        host3 = self.addHost("h3")
        host4 = self.addHost("h4")
        host5 = self.addHost("h5")
        host6 = self.addHost("h6")
        host7 = self.addHost("h7")
        host8 = self.addHost("h8")
	    self.addLink( host1, edge_switch_1, bw=10, delay="5ms", loss=2, max_queue_size=1000, use_htb=True )
        self.addLink( host2, edge_switch_1, bw=10, delay="5ms", loss=2, max_queue_size=1000, use_htb=True )
        self.addLink( host3, edge_switch_2, bw=10, delay="5ms", loss=2, max_queue_size=1000, use_htb=True )
        self.addLink( host4, edge_switch_2, bw=10, delay="5ms", loss=2, max_queue_size=1000, use_htb=True )
        self.addLink( host5, edge_switch_3, bw=10, delay="5ms", loss=2, max_queue_size=1000, use_htb=True )
        self.addLink( host6, edge_switch_3, bw=10, delay="5ms", loss=2, max_queue_size=1000, use_htb=True )
        self.addLink( host7, edge_switch_4, bw=10, delay="5ms", loss=2, max_queue_size=1000, use_htb=True )
        self.addLink( host8, edge_switch_4, bw=10, delay="5ms", loss=2, max_queue_size=1000, use_htb=True )
        self.addLink( edge_switch_1, aggregation_switch_1, bw=10, delay="5ms", loss=2, max_queue_size=1000, use_htb=True )
        self.addLink( edge_switch_2, aggregation_switch_1, bw=10, delay="5ms", loss=2, max_queue_size=1000, use_htb=True )
        self.addLink( edge_switch_3, aggregation_switch_2, bw=10, delay="5ms", loss=2, max_queue_size=1000, use_htb=True )
        self.addLink( edge_switch_4, aggregation_switch_2, bw=10, delay="5ms", loss=2, max_queue_size=1000, use_htb=True )
        self.addLink( aggregation_switch_1, core_switch, bw=10, delay="5ms", loss=2, max_queue_size=1000, use_htb=True )
        self.addLink( aggregation_switch_2, core_switch, bw=10, delay="5ms", loss=2, max_queue_size=1000, use_htb=True )



def testaConexoes():
    "Create network and run simple performance test"
    topo = SingleSwitchTopo( n=8 )
    net = Mininet( topo=topo, host=CPULimitedHost, link=TCLink )
    net.start()
    print( "Dumping host connections" )
    dumpNodeConnections( net.hosts )
    print( "Testing network connectivity" )
    net.pingAll()
    print( "Testing bandwidth between hosts" )
    h1, h2, h3, h4, h5, h6, h7, h8 = net.get( "h1", "h2" , "h3", "h4", "h5", "h6", "h7" , "h8")
    net.iperf( (h1, h2) )
    net.iperf( (h3, h4) )
    net.iperf( (h5, h6) )
    net.iperf( (h7, h8) )
    net.stop()

if __name__ == "__main__":
    setLogLevel( "info" )
    testaConexoes()
