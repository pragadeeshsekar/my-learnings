## Inter-Node Ports
* 7000/tcp --> inter-node cluster communication
* 7001/tcp --> SSL inter-node cluster communication
* 7199/tcp --> JMX monitoring port

## Client Ports
* port 9042/tcp --> client port (**CQL**)
* 9160/tcp --> client port (**Thrift** - a legacy RPC Protocol combined with code generation tool)

both the above ports must be allowed by firewall for communication to happen within & outside cassandra.

Normal RDBMS |   Cassandra       | 
------------ | ----------------- | 
Database     |    Keyspace       | 
Table        |    Column         |
Fixed Schema | Flexible Schema   |
Deals with Structured Data | Deals with Unstructured Data |

Each Row in cassandra is identified by Primary Key 
