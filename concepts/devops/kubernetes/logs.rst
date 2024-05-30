If the pod has been terminated but not yet deleted, you can access its logs using the --previous flag with kubectl logs:
kubectl logs <pod-name> --previous

Using a Persistent Logging Solution
To ensure that you always have access to logs, even after pods are deleted, you should set up a persistent logging solution. 
Popular logging solutions for Kubernetes include:

ELK Stack (Elasticsearch, Logstash, Kibana)
EFK Stack (Elasticsearch, Fluentd, Kibana)
Loki with Grafana
Prometheus with Grafana
These solutions typically involve deploying logging agents (like Fluentd or Filebeat) on each node, which collect logs and 
send them to a central logging backend.

Accessing Logs from Persistent Storage
If you have configured your logging agents to store logs on persistent volumes, you can access logs directly from the storage. 
For example, if using Fluentd with a persistent volume:

Identify the persistent volume associated with Fluentd or your logging agent.
Access the logs stored on the persistent volume, either by using a kubectl command or by directly accessing the storage backend.

sing Kubernetes Events and Audit Logs
Kubernetes events and audit logs can provide additional insights into what happened to a pod. 
These logs include information about pod creation, deletion, and any errors that occurred:

# Get events for a specific namespace
kubectl get events -n <namespace>

# Get all events
kubectl get events --all-namespaces

# Describe the pod to see events related to it
kubectl describe pod <pod-name> -n <namespace>

If a pod in your Kubernetes cluster has crashed, you can still access its logs using the kubectl logs command with the --previous flag.
kubectl logs <pod-name> --previous

Retrieve logs from the previous instance of the container:
kubectl logs my-app-pod -c my-app-container --previous -n my-namespace