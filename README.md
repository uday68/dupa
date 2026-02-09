##D.U.P.A (Data Unity Protection Accessibility)
D.U.P.A is an open-source, security-first personal cloud and distributed file storage solution. It is designed for developers and privacy-conscious users—especially those running older or low-powered machines—who want full control over their data. Inspired by projects like Syncthing and Nextcloud, D.U.P.A ensures that “your data is your data alone”
 by keeping all files on user-owned devices with no central server. All communication is end-to-end encrypted (using TLS) and stored data is encrypted at rest
. The system also includes safeguards like versioning and a recoverable “trash bin” so that accidental deletions are not catastrophic. As one user demonstrated by repurposing an old laptop for Nextcloud, “old laptops aren’t useless — they’re perfect for light server tasks” and give “total control over your data”
. D.U.P.A exists to meet these needs by providing a lightweight, resilient personal cloud that anyone can run on modest hardware.
Features
End-to-End Encryption: All files are encrypted by the client before storage and transferred over TLS. This matches Nextcloud’s “military-grade encryption” approach and Syncthing’s use of TLS certificates
. No unencrypted data ever leaves your machine.
Decentralized & Local-First: D.U.P.A runs in a peer-to-peer fashion with no cloud servers. You decide which devices hold your data, just as Syncthing ensures “none of your data is ever stored anywhere else other than on your computers”
. Files are content-addressed (chunked and hashed) much like IPFS, so that any participating node with a copy can serve the data
.
Delete-Protected Storage: The system uses versioning and a configurable “trash bin” so that deleted files can be recovered. This mirrors MooseFS’s “transparent trash bin” which retains deleted files for a set period
. By default, files are not immediately purged, preventing accidental data loss.
Content Chunking & Deduplication: Files are broken into smaller chunks, each cryptographically hashed to form unique content IDs
. Chunks may be compressed and stored only once, enabling deduplication and efficient use of space. When files change, only the new chunks are stored, making incremental syncing fast.
Metadata Indexing & Search: A local index of file metadata (names, types, timestamps, etc.) is maintained for quick lookup. This allows the CLI or API to search and navigate files efficiently. (Future versions may add tagging or full-text search capabilities.)
Command-Line & API Access: D.U.P.A provides both a CLI tool and a REST API for all operations. You can list, upload, download, or sync files via the command line, script, or any HTTP client. The API layer is built on FastAPI, a “modern, fast (high-performance)” Python framework
, ensuring responsive interactions.
Cross-Platform & Lightweight: The core engine is written in Rust for speed and safety, allowing it to run on Linux, Windows, macOS, or even Raspberry Pi. The FastAPI service and CLI have minimal dependencies. Together, they make D.U.P.A suitable for older computers and low-end servers without sacrificing performance.
How It Works
D.U.P.A is organized in layered components that separate concerns for efficiency and flexibility:
Rust Storage Engine: The heart of the system is a Rust-based engine that manages disk I/O and security. It handles splitting files into chunks, compressing and encrypting data, and tracking metadata in an embedded database. Rust’s memory safety prevents crashes and leaks, while its performance makes these operations fast even on modest hardware.
FastAPI Orchestration: Sitting atop the storage core is a Python FastAPI server. This layer exposes RESTful endpoints that the CLI, front-end, or other clients use. FastAPI is chosen for its “high performance” and async capabilities
. It coordinates actions like file uploads/downloads, handles authentication, and translates HTTP requests into storage engine operations.
GraphQL Interface (Planned): In the roadmap, D.U.P.A will add a GraphQL API to allow clients to query file metadata more flexibly. This will enable the future UI and clients to request exactly the data they need (e.g. filtered file lists) without multiple REST calls.
Web Front-End (React+TypeScript): A web-based UI is built with React and TypeScript. Currently it offers a minimal file browser and status dashboard, but it will be expanded to manage sync jobs, view logs, and configure policies. This front-end communicates via the FastAPI or (in the future) GraphQL interface. Eventually, native mobile and desktop clients will plug into the same APIs.
The architecture allows each layer to be developed and scaled independently. For example, the FastAPI server can be scaled horizontally or secured behind a reverse proxy, while the Rust engine can be embedded into other tools. This layered design is similar in spirit to systems like SeaweedFS, which separates metadata and data services for scalability
.
Use Cases
D.U.P.A’s flexible design supports many scenarios:
Home & Personal Cloud: Run D.U.P.A on a home server or old laptop to store family photos, documents, and media. This creates a self-hosted private cloud that gives “total control over your data”
. Automatic syncing means your files are available on all your devices, without trusting any third party.
Team Collaboration: Small development or creative teams can use D.U.P.A to share project files securely. Because everything is local and encrypted, it’s ideal for sensitive codebases or research data. Versioned file storage ensures everyone can recover previous versions of a document or code.
Remote & Offline Work: For field research, IoT deployments, or intermittent connectivity scenarios, D.U.P.A can run on edge hardware (e.g. Raspberry Pi) to collect and store data. When connectivity returns, it can sync encrypted data to other nodes or the cloud.
Secure Backup & Archival: Use D.U.P.A as an encrypted backup solution. The chunked, deduplicated store is efficient for backups, and the delete-protection ensures old data isn’t lost unless explicitly purged. It works with modest hardware, avoiding expensive high-end storage.
Each of these use cases emphasizes privacy and resilience. By keeping data local or on user-chosen devices, D.U.P.A avoids the risks of public cloud services. As one experience with Nextcloud put it: turning an old PC into a personal cloud is “surprisingly easy, cost-free, and gives you total control over your data”
.
Roadmap
The initial MVP of D.U.P.A focuses on secure local storage and basic CLI/API operations. Looking ahead, planned enhancements include:
Cloud Sync Integrations: Add optional syncing or backup to cloud services like OneDrive, Amazon S3, or generic S3-compatible storage. These connections will still use end-to-end encryption, so providers never see plaintext.
GraphQL API & Clients: Implement the GraphQL layer for more powerful queries, and develop native clients for desktop and mobile that use these APIs.
Advanced Deletion Logic: Introduce object reference tracking and lifecycle policies. For example, enable setting retention periods, automatic purging of unreferenced data, or write-once protections for immutable storage.
Enhanced UI & Policy Controls: Expand the React web UI to manage users, permissions, and encryption keys. Expose admin controls to define storage quotas, encryption settings, and sharing policies.
Client Tools & Extensions: Build additional tools like a FUSE filesystem driver to mount D.U.P.A storage locally, integration with backup software, or plugins for development environments.
This roadmap is driven by community needs. Contributions are welcome for any of these features.
Testing
D.U.P.A includes a suite of automated tests to ensure reliability:
Unit & Integration Tests: The Rust core has cargo test coverage of storage logic (encryption, chunking, indexing) and the FastAPI layer has pytest (or equivalent) tests for API endpoints and CLI functions. Contributors should add tests for any new functionality.
Continuous Integration: The project uses CI pipelines (e.g. GitHub Actions) to run lint checks and all tests on every commit. Code formatting and static analysis tools (Rust’s Clippy, Python linters, type checkers) help maintain code quality.
Documentation and Examples: Key workflows are documented in the repository’s docs/ directory. Example configurations and usage scenarios guide new users. All CLI commands have help text, and the API is self-documented via OpenAPI/Swagger.
Testing focuses on encryption correctness, data integrity (no silent corruption), and multi-node synchronization scenarios. Before each release, a full end-to-end test is performed to verify that files encrypted on one machine can be decrypted on another.
Contributing
Contributions are very welcome! See the CONTRIBUTING guide for details. In summary:
Open Source: D.U.P.A is developed openly on GitHub. Feel free to open issues for bugs or feature requests, or submit pull requests.
Coding Standards: Follow the existing code style. For Rust code, run cargo fmt and cargo clippy. For the Python API, use black, flake8, or similar. Ensure all tests pass before submitting.
Code of Conduct: Please adhere to the project’s Code of Conduct. Treat all contributors with respect.
Discussion: Development discussions happen on GitHub Discussions and issues. Feedback on design and roadmap is welcome on these channels.
Whether it’s improving documentation, optimizing performance, or adding new features (e.g. plugins, backends, UI enhancements), we encourage community participation. Together we can make D.U.P.A stronger and more versatile.
License
D.U.P.A is released under the Apache License 2.0. See the LICENSE file for full terms. All contributions are licensed under Apache-2.0 by default. This permissive open-source license ensures D.U.P.A can be freely used and extended by individuals and organizations alike. References: This project takes inspiration and best practices from systems like Syncthing
, Nextcloud
, IPFS
, SeaweedFS
, and MooseFS
, each providing insights into secure, distributed storage design. These influence D.U.P.A’s emphasis on encryption, decentralization, and delete-protection in a user-owned cloud.
Citations

Syncthing

https://syncthing.net/

Syncthing

https://syncthing.net/

Nextcloud encryption and hardening

https://nextcloud.com/encryption/

How I Built a Home Cloud Server Using an Old Laptop and Nextcloud - DEV Community

https://dev.to/neil_brown/how-i-built-a-home-cloud-server-using-an-old-laptop-and-nextcloud-30k

How I Built a Home Cloud Server Using an Old Laptop and Nextcloud - DEV Community

https://dev.to/neil_brown/how-i-built-a-home-cloud-server-using-an-old-laptop-and-nextcloud-30k

IPFS Storage Explained: How It Works

https://filebase.com/blog/ipfs-storage-explained-how-it-works/

Moose File System - Wikipedia

https://en.wikipedia.org/wiki/Moose_File_System

FastAPI

https://fastapi.tiangolo.com/

GitHub - seaweedfs/seaweedfs: SeaweedFS is a fast distributed storage system for blobs, objects, files, and data lake, for billions of files! Blob store has O(1) disk seek, cloud tiering. Filer supports Cloud Drive, xDC replication, Kubernetes, POSIX FUSE mount, S3 API, S3 Gateway, Hadoop, WebDAV, encryption, Erasure Coding. Enterprise version is at seaweedfs.com.

https://github.com/seaweedfs/seaweedfs

Nextcloud encryption and hardening

https://nextcloud.com/encryption/
All Sources

syncthing

nextcloud

dev

filebase

en.wikipedia

fastapi.tiangolo

githu
