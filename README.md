# Projeto da Matéria Rede de Computadores
repositório dedicado ao trabalho da matéria de redes de computadores

### Cisco Packet Tracer
O arquivo *.pkt* é referente ao projeto feito no Cisco Packet Tracer da rede de topologia em árvore.

## Referência utilizada:

### Links e repositórios citados no vídeo:
Setup do mininet (Virtual Machine - VM VirtualBox): http://mininet.org/download/#option-3-installation-from-packages

Documentação oficial do mininet com código inicial: https://github.com/mininet/mininet/wiki/Introduction-to-Mininet#creating

Utilizei o código da documentação como ponto de partida, adaptando para as necessidades da rede desenhada no trabalho da matéria (deixo abaixo o código
como registro do ponto inicial de desenvolvimento):

```
#!/usr/bin/python                                                                            
                                                                                             
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1')
        # Python's range(N) generates 0..N-1
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)

def simpleTest():
    "Create and test a simple network"
    topo = SingleSwitchTopo(n=4)
    net = Mininet(topo)
    net.start()
    print( "Dumping host connections" )
    dumpNodeConnections(net.hosts)
    print( "Testing network connectivity" )
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
```

Meu repositório no github com o projeto: este aqui! :)
