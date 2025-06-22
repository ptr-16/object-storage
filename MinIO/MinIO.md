docker run -p 9000:9000 -p 9001:9001 `
--name minio `
-v ${PWD}\ minio \data:/data `
-e "MINIO_ROOT_USER=TAMARITZ" `
-e "MINIO_ROOT_PASSWORD=TATITA123" `
quay.io/ minio / minio server /data --console-address ":9001"

When versioning is not enabled, if you upload a new file with the same name (key) as an existing file, the system simply replaces the previous file.
There is no way to recover the old file—it is permanently deleted.

 Update with Versioning enabled
When versions are enabled In a bucket :
1.	Every time you upload a file with a name that already exists, a new version number is created .
2.	All versions are saved – both previous and new .
3.	Given :
o	Restore an old version .
o	Delete only a specific version .
o	Track changes .

