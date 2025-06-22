Research:

Briefly research the key differences between object storage and other forms of distributed storages. Make note of advantages and disadvantages of each.

Object Storage:
Unlike file systems, object storage is not built on a hierarchy of folders and subfolders.

Each data unit—called an object—exists on a flat structure.

An object contains data and a unique identifier, allowing direct access by ID instead of physical location on disk.

This enables fast access to each object by using its unique key.

Advantages:

Virtually unlimited scalability: Thanks to the flat structure, enormous amounts of data can be stored.

Rich metadata usage: Enables fast search and retrieval based on object attributes, without scanning all the data.

High reliability: Data is replicated and distributed across multiple nodes, so even in case of failure, it can be recovered.

Cost efficiency: Object storage systems don’t require expensive storage servers and often use low-cost hard drives.

Disadvantages:

Slower data access: Especially when frequent processing or updates are required.

Costly with frequent access: When frequent data retrieval is needed or when storing large data volumes.

Security risks: With cloud storage, sensitive data is exposed and requires high-level security.

Vendor lock-in: Makes migration to other providers or systems difficult.

Distributed Storage:
A distributed system consists of nodes that are physically dispersed and may be located in different geographic regions.
They connect through a network, and each node has its own memory and processor. The nodes cooperate in data processing.

Advantages:

Scalability: Nodes can be added as needed to handle growing data or performance demands.

Resilience: If a node or component fails, the system continues by redistributing tasks.

Performance: Enhanced through parallel processing across nodes, enabling higher throughput.

Flexibility: Nodes can be dynamically added or removed as needed.

Cost efficiency: Resource utilization is improved by distributing workloads across multiple low-cost nodes.

Robustness: Distributed systems adapt well to changes and failures.

Disadvantages:

Complexity: Beyond individual computer speed, network communication may affect performance.

Security: Due to node communication over networks, high-level security is required.

System heterogeneity: Different OS versions, software, and hardware make system management harder.

Unpredictable behavior: The system's response depends on overall load and network traffic, so one response time cannot predict the next.

Summary of Differences:
Object storage excels at long-term storage of large data volumes and efficient searching,
but is less suitable for frequent processing or high performance.
Distributed storage is designed to deliver performance, resilience, and flexibility, but requires complex maintenance and advanced infrastructure.

2. What is S3?
S3 is Amazon Web Services’ cloud storage service.
It is based on object storage with a flat structure—each object is identified by a unique key defined by the user.
Main features include high scalability, high availability, advanced security, and more.

3. What is a bucket?
In S3, a bucket is a storage container where objects are stored.
Each object has a unique identifier within the bucket.
The bucket uses a flat (non-hierarchical) structure—you cannot create a bucket inside another bucket.
It is the basic unit of management—you can define permissions, storage policies, and security settings on it.

4. Does the concept of folders exist in S3?
S3 has no true directory hierarchy.
Storage is based on flat object structure. However, you can simulate folders by using keys that contain slashes (/) to represent folder-like paths.

5. Are there size limitations? How do they compare to classic filesystems?
In S3, each object can be up to 5TB.
Direct upload is limited to 5GB, but multipart upload enables larger files.
You can store an unlimited number of objects.

6. What implementations of S3 are there?
S3 is used for many purposes:

Backups

Disaster recovery

Low-cost archival storage

Content distribution

Development, testing, and more

7. Deploy a working instance of MinIO using Docker.
I ran MinIO using Docker through VS Code.
This is the terminal output:

bash
Copy
Edit
PS C:\הנדסת תוכנה 1 תשפ''ה\פרקטיקום\משימות\task3\object-storage> docker run -p 9000:9000 -p 9001:9001