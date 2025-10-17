# Kubernetes Overview

Kubernetes (often abbreviated as K8s) is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. It groups containers that make up an application into logical units for easy management and discovery.

## Why Kubernetes?

As applications grow and move towards microservices architectures, managing a large number of containers across various hosts becomes complex. Kubernetes addresses these challenges by providing:

*   **Automated Rollouts and Rollbacks:** Kubernetes can progressively roll out changes to your application or its configuration, and monitor the application's health during the rollout. If something goes wrong, it can roll back the change.
*   **Self-healing:** Kubernetes can detect and restart failed containers, replace unhealthy containers, and kill containers that don't respond to user-defined health checks.
*   **Service Discovery and Load Balancing:** Kubernetes can expose a container using a DNS name or its own IP address. If traffic to a container is high, Kubernetes can load balance and distribute the network traffic so that the deployment is stable.
*   **Storage Orchestration:** Kubernetes allows you to automatically mount a storage system of your choice, such as local storage, public cloud providers (GCP, AWS, Azure, etc.), or a network storage system.
*   **Secret and Configuration Management:** Kubernetes lets you store and manage sensitive information, such as passwords, OAuth tokens, and SSH keys, as well as application configuration, without rebuilding your container images.
*   **Batch Execution:** Kubernetes can manage your batch and CI workloads, replacing failed containers if necessary.
*   **Horizontal Scaling:** Scale your application up and down with a simple command, via a UI, or automatically based on CPU usage.

## Core Kubernetes Components

Kubernetes operates on a cluster of nodes. A Kubernetes cluster consists of at least one master node and multiple worker nodes.

### Master Node Components (Control Plane)

The master node manages the worker nodes and the Pods in the cluster. It consists of several components:

1.  **kube-apiserver:** The front end of the Kubernetes control plane. It exposes the Kubernetes API and is the central hub for all communication.
2.  **etcd:** A consistent and highly available key-value store used as Kubernetes' backing store for all cluster data.
3.  **kube-scheduler:** Watches for newly created Pods with no assigned node, and selects a node for them to run on.
4.  **kube-controller-manager:** Runs controller processes. Controllers watch the shared state of the cluster through the apiserver and make changes attempting to move the current state towards the desired state.
5.  **cloud-controller-manager (Optional):** Integrates Kubernetes with cloud provider-specific APIs (e.g., managing load balancers, virtual machines, and storage volumes).

### Worker Node Components

Worker nodes run the actual containerized applications. Each worker node has the following components:

1.  **kubelet:** An agent that runs on each node in the cluster. It ensures that containers are running in a Pod.
2.  **kube-proxy:** A network proxy that runs on each node and maintains network rules on nodes. These rules allow network communication to your Pods from network sessions inside or outside of the cluster.
3.  **Container Runtime:** The software that is responsible for running containers (e.g., Docker, containerd, CRI-O).

## Key Kubernetes Objects

Kubernetes uses various objects to represent the state of your cluster. These objects describe:

*   What containerized applications are running (and on which nodes).
*   The resources available to those applications.
*   The policies around how those applications behave, such as restart policies, upgrades, and fault-tolerance.

Some common Kubernetes objects include:

*   **Pod:** The smallest deployable unit in Kubernetes. A Pod represents a single instance of a running process in your cluster. Pods can contain one or more containers.
*   **Deployment:** An object that manages a set of identical Pods. It defines the desired state for your application and ensures that the specified number of Pod replicas are running.
*   **Service:** An abstract way to expose an application running on a set of Pods as a network service. Services enable communication between different parts of your application and external users.
*   **Namespace:** A way to divide cluster resources between multiple users or teams. Namespaces provide a scope for names and allow you to manage resources within a logical boundary.
*   **ReplicaSet:** Ensures that a specified number of Pod replicas are running at any given time. Deployments use ReplicaSets to manage Pod scaling and updates.
*   **ConfigMap:** Used to store non-sensitive configuration data in key-value pairs. Applications can consume ConfigMaps as environment variables, command-line arguments, or as configuration files in a volume.
*   **Secret:** Similar to ConfigMap, but designed for storing sensitive data like passwords, tokens, and keys. Secrets are encoded in base64, but not encrypted by default.
*   **Volume:** A directory, accessible to the containers in a Pod. Kubernetes Volumes have a lifetime equal to the Pod that encloses them.

This overview provides a foundational understanding of Kubernetes. For more in-depth learning, explore specific components and objects in detail.
