Master nodes host the K8s control plane components. The master node will hold configuration and state data used to maintain the desired 
state. The control plane maintains communication with the worker nodes in order to schedule containers efficiently. 

Worker nodes are so-called because they run pods. Pods are usually single instances of an application. 
Containers run inside pods, Pods run on a node. 

Master Node Components
API server (kube-apiserver)
The REST API acts as a front door to the control plane. Any requests for modifications to the cluster come through the API, 
as well as any requests from worker nodes. If the requests are valid the API server executes them. 
Communications with the cluster occurs either via the REST API, or command-line tools like kubeadm or kubectl.

Scheduler (kube-scheduler)
The scheduler determines where resources will be deployed on which nodes within the K8s cluster. 
It does this by scheduling pods of containers across nodes and makes these decisions based on monitoring resource utilization. 
It places the resources on healthy nodes that can fulfill the requirements of the application.

Controller (kube-controller-manager)
The controller runs a number of background processes and also initiates any requested changes to the state. 
It ensures that the cluster state remains consistent. 
The controller can identify failed nodes and take action, and also runs jobs as required (jobs are one-time tasks). 
Also when a new namespace is created, this controller creates default accounts and API access tokens.

Etcd (key-value store)
Configuration data about the state is stored in a key-value store that all nodes can access in the cluster. 
It is a critical component that is distributed and fault-tolerant. 
Etcd can be a target for malicious actors as it provides effective control over the cluster and should be secured.

Cloud Controller Manager (cloud-controller-manager)
An optional component, the cloud controller manager can be used to link the K8s API to the cloud providers API. 
Once linked, it can enable the cluster to scale horizontally. 
Components that interact with the cloud providers are separated from those that only interact with the K8s API to optimize performance.

Worker Node Components
Pods & Containers
Worker nodes are so-called because they run pods that do the work. Pods are usually single instances of the application itself. 
Containers run inside pods, Pods run on a node. If more resource is needed in the K8s cluster to run the workloads, 
more nodes can be added to the cluster.

Kubelet
Each worker node runs a small application called the kubelet, which enables communication with the control plane. 
If the control plane needs to make any changes on the worker nodes, the request will go via the kubelet.

Kube-proxy
Each worker node also runs a component to control the networking, within and outside the cluster, called kube-proxy. 
Traffic can be forwarded independently or using the Operating systems packet filtering layer. 
It acts as a load balancer and forwards requests from the control plane to the correct pods.

Calico implements the Kubernetes Container Network Interface (CNI) as a plug-in and provides agents for Kubernetes to provide networking 
for containers and pods. Calico creates a flat layer-3 network and assigns a fully routable IP address to every pod.

What does the Calico-node do?
Calico Reference Architecture | VMware Tanzu Developer Center
calico-node

It is responsible for 2 pieces of functionality: 
Route programming: Based on known routes to pods in the Kubernetes cluster, configure the Linux host to facilitate routing accordingly. 
Route sharing: Based on pods running on this host, provide a mechanism to share known routes with other hosts.

What is the difference between k8s Calico and Istio?
Istio policies apply to the communication between the services (both internal and external to the mesh). 
Kubernetes Network Policies (implemented via Calico) control communication between pods. 
These policies are applied regardless if the pods belong to the Istio mesh or not.

Istio is a service mesh technology that allows developers to secure, connect, run, control, and monitor distributed microservices architectures 
regardless of the vendor or platform. It manages interactions between services in container-based and virtual machine-based workloads.
Istio manages traffic flows between services, enforces access policies, and aggregates telemetry data, all without requiring changes to 
application code.
Istio is the path to load balancing, service-to-service authentication, and monitoring – with few or no service code changes. 
Its powerful control plane brings vital features, including: Secure service-to-service communication in a cluster with TLS encryption, 
strong identity-based authentication and authorization.
An Istio service mesh is logically split into a data plane and a control plane. 
The data plane is composed of a set of intelligent proxies (Envoy ) deployed as sidecars. 
These proxies mediate and control all network communication between microservices. 
They also collect and report telemetry on all mesh traffic.

A service mesh is a dedicated infrastructure layer built into an application that controls service-to-service communication in a 
microservices architecture. It controls the delivery of service requests to other services, performs load balancing, encrypts data, and 
discovers other services.

Load Balancer
Having a load balancer also gives ability to load balance the traffic across multiple replicas of ingress controller pods. 
When you use ingress controller the traffic comes from the loadBalancer to the ingress controller and then gets to backend POD IPs based 
on the rules defined in ingress resource
Load balancers in K8S can be implemented by using a cloud provider-specific load balancer such as Azure Load Balancer, 
AWS Network Load Balancer (NLB), or Elastic Load Balancer (ELB) that operates at the Network Layer 4 of the OSI model.

Cloud-specific Ingress controllers that can operate at the Application Layer 7, include Application Gateway on Azure, or ELB or 
Application Load Balancer (ALB) on AWS. 
To use ingress, an Ingress controller must be installed on the cluster, as they are not included out of the box with K8S.
Popular ingress controllers include NGINX, HAProxy, Istio Ingress, and Traefik

There are two types of  layer 4 load balancer types in Kubernetes – internal and external.
Internal load balancer — routes traffic only within the cluster and does not allow any external traffic.
External load balancer — exposes the application to external users or services outside the cluster.

Ingress
Ingress in K8S is an object that allows access to services within your cluster, from outside your cluster.
Traffic routing is defined by rules specified on the Ingress resource.

Ingress, LoadBalancer, and NodePort are all ways of exposing services within your K8S cluster for external consumption.
NodePort and LoadBalancer let you expose a service by specifying that value in the service’s type.

With a NodePort, K8S allocates a specific port on each node to the service specified. 
Any request received on the port by the cluster simply gets forwarded to the service.

With a LoadBalancer, there needs to be an external service outside of the K8S cluster to provide the public IP address. 
In Azure, this would be an Azure Application Gateway in front of your Azure Kubernetes Service (AKS) cluster. 
In AWS, this would be an Application Load Balancer (ALB) in front of your Elastic Kubernetes Service (EKS), and in Google cloud, 
this would be a Network Load Balancer in front of your Google Kubernetes Engine (GKE) cluster.

To set up Ingress in K8S, you need to configure an Ingress controller. 
These do not come as default with the cluster and must be installed separately. 
An ingress controller is typically a reverse web proxy server implementation in the cluster.

Taints and tolerations help prevent your pods from scheduling to undesirable nodes.
If there are no errors during the verification, the pod will be scheduled on the node. 
If the conditions of the verification aren’t satisfied, then your pods will be put in a Pending state, you may experience sometime.

The scheduler looks at the nodes, and if there are taints that the pods can’t tolerate, it doesn’t schedule the pod to that node.
one can add taint to your nodes with the following command:
# kubectl taint nodes <node name> <taint key>=<taint value>:<taint effect>
The three taint effects are:
NoSchedule: 
A strong effect where the system lets the pods already scheduled in the nodes run, but enforces taints from the subsequent pods.
PreferNoSchedule: 
A soft effect where the system will try to avoid placing a pod that does not tolerate the taint on the node.
NoExecute: 
A strong effect where all previously scheduled pods are evicted, and new pods that don’t tolerate the taint will not be scheduled.

Node Affinity
Node affinity is a set of rules used by the scheduler to determine where a pod can be placed. 
The rules are defined using custom labels on nodes and label selectors specified in pods. 
Node affinity allows a pod to specify an affinity (or anti-affinity) towards a group of nodes it can be placed on.

Node affinity is a property of Pods that attracts them to a set of nodes (either as a preference or a hard requirement). 
Taints are the opposite -- they allow a node to repel a set of pods. 
Tolerations are applied to pods. Tolerations allow the scheduler to schedule pods with matching taints.

Pod affinity/anti-affinity allows you to constrain which nodes your pod is eligible to be scheduled on based on the labels on other pods.
Node Affinity ensures that pods are hosted on particular nodes. Pod Affinity ensures two pods to be co-located in a single node.

Labels and Selectors are the standard method to group things together in Kubernetes.
We can filter the objects based on the criteria like class, kind, and functions. 
Labels are the properties attached to each item/object. 
Selector helps us to filter the items/objects which have labels attached to them.
The label selector is the core grouping primitive in Kubernetes. 
The API currently supports two types of selectors: equality-based and set-based. 
A label selector can be made of multiple requirements which are comma-separated.
Simple selectors (select elements based on name, id, class) 
Combinator selectors (select elements based on a specific relationship between them) 
Pseudo-class selectors (select elements based on a certain state)