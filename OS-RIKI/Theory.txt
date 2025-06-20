1.differences between object storage and Distributed Storage

Object storage:
advantage:
1.Scalability:
Object storage is great for storing large amounts of unstructured data, and can easily scale with data growth.
2.Flexibility:
Object storage’s flat approach allows for great flexibility in data management.
3.Cost-effective:
Object storage can be more cost-effective than traditional storage systems, especially when dealing with large amounts of data.
4.Accessibility:
Objects can be accessed from anywhere with an internet connection, making it easy to share and access data.
5.Durability:
Object data can be distributed across multiple geographic locations, ensuring backup and survivability in the event of a failure.
Disadvantages:
1.Complexity:
Working with object storage can be more complex than traditional file systems.
2.Compatibility:
Not all applications are compatible with object storage, especially applications that require fast access to specific files.
3.Locating:
Locating specific objects can be slower than traditional file systems

Distributed Storage:
Advantages:
1.Reliability and Availability:
Distributed storage ensures that data is available even if one of the servers fails.
2.Performance:
Distributed storage can improve performance by spreading the workload across multiple servers.
3.Scalability:
Distributed storage can scale more easily than traditional storage systems.
Disadvantages:
1.Complexity: Distributed storage systems can be more complex to manage.
2.Cost: Distributed storage systems can be more expensive to set up and maintain.
3.Network Dependency: Distributed storage requires a reliable network.

2.what is s3?
S3 is like a giant hard drive in the cloud, which can be used to store all types of files.

3.What is a bucket?
In object storage systems, a bucket is a logical container that stores objects (data files).
Each object is stored within a specific bucket,
and the bucket itself is used to organize and manage the objects.

4.Does the concept of folders exist in S3?
The structure of S3 is flat and not hierarchical like a file system, 
but to compensate for this, 
the console supports the concept of partitions by grouping objects by giving prefixes with a common name to all objects.
In this way, partitions can be created or deleted but without the ability to change their name.
Hence, objects can be uploaded and copied to the partition and even moved between partitions.

5.Are there size limitations? How do they compare to classic filesystem?
In S3, the maximum allowed object size is 5TB. Although the S3 interface resembles a file system, 
it is based on an object model and allows for unlimited scalability in terms of storage capacity and high availability. 
In a classic file system, the maximum size of a file is limited by the operating system and its internal structure, 
and is usually smaller than 5TB.

6.What implementations of S3 are there?
S3 is used for applications that store and access a wide range of data, including content, 
media, software, cloud data, and big data. It is also suitable for backup, disaster recovery, 
archiving, big data analytics, and hybrid cloud storage.

7.
1. first I have to run it in thr terminal:
docker pull minio/minio.
* attached Screenshots:1

and after i put this command:
docker run -p 9000:9000 -p 9001:9001 -e MINIO_ROOT_USER=admin -e MINIO_ROOT_PASSWORD=admin123 -v C:\Users\USER\Desktop\picture\minio:/data minio/minio server /data --console-address ":9001"
* attached Screenshots:2

8.
explain with the update:
In MinIO, versioning allows you to keep a history of all versions of a file. So when updating an object:
MinIO does not delete the previous version, but saves the new file as a new version with a versionId.
This allows you to revert to previous versions, track changes, and prevent accidental data loss.



