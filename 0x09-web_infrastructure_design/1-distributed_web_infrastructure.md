Description:


Server 2 (Application Server): Adding a second application server allows for redundancy and load distribution. If one application server fails or is overwhelmed, the load balancer can direct traffic to the other server.
Load Balancer (HAproxy): The load balancer evenly distributes incoming traffic between the two application servers, improving the website's performance, fault tolerance, and scalability.
Load Balancer Distribution Algorithm:
The load balancer is configured with a Round Robin distribution algorithm. It cycles through the available servers in a sequential order, ensuring that each server receives an equal share of incoming requests.

Active-Active vs. Active-Passive Setup:
The load balancer is enabling an Active-Active setup. In an Active-Active setup, both application servers are actively serving traffic, sharing the load equally. An Active-Passive setup would have one application server actively serving traffic while the other remains on standby until needed.

Primary-Replica (Master-Slave) Database Cluster:
In this setup, the MySQL database is configured as a Primary-Replica (Master-Slave) cluster. The Primary node (Master) handles read and write operations, while the Replica node (Slave) replicates data from the Primary node and can handle read operations to offload the Primary node.

Difference between Primary and Replica Nodes for the Application:

Primary Node: Handles both read and write operations. Application servers write data to the Primary node, and it is responsible for maintaining the most up-to-date data.
Replica Node: Handles read operations, providing a copy of the data from the Primary node. This offloads read traffic from the Primary node, improving its performance and scalability.
Issues with the Infrastructure:

Single Point of Failure (SPOF):

The load balancer is a single point of failure. If it goes down, traffic won't be distributed properly.
The primary database node is also a potential SPOF. If it fails, the replica node can't take over for write operations.
Security Issues:

There's no mention of a firewall, which exposes the servers and database to potential security risks.
HTTPS (SSL/TLS encryption) is missing, potentially compromising data security during transmission.
No Monitoring:

Lack of monitoring tools means you won't be able to promptly identify and address issues, impacting overall system health and performance.