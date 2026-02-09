

# D.U.P.A (Data Unity Protection Accessibility)

![Badge Label](https://img.shields.io/badge/<label>-<color>.svg?style=for-the-badge&logo=<logo>&logoColor=<color>) ![Rust](https://img.shields.io/badge/rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Status](https://img.shields.io/badge/status-Alpha-orange?style=for-the-badge)





> "Old laptops aren’t useless — they’re perfect for light server tasks."

**D.U.P.A** is an open-source, security-first personal cloud and distributed file storage solution. Designed for developers and privacy-conscious users, it allows you to regain full control over your data by turning your existing hardware—whether it's a high-end workstation, an old laptop, or a Raspberry Pi—into a resilient, encrypted mesh network.

Inspired by Syncthing, Nextcloud, and IPFS, D.U.P.A ensures that **"your data is your data alone."**

---

## 🚀 Features

### 🔒 End-to-End Encryption

* **Zero-Knowledge Architecture:** All files are encrypted on the client side before they ever touch the disk or network.
* **Transit Security:** All peer-to-peer communication is secured via TLS 1.3 with mutual certificate authentication.
* **At-Rest Protection:** Data is stored as encrypted chunks (AES-256-GCM), protecting your privacy even if the physical drive is stolen.

### 🕸️ Decentralized & Local-First

* **No Central Server:** D.U.P.A runs in a peer-to-peer mesh. You decide which devices hold your data.
* **Content-Addressed Storage:** Files are chunked and hashed (using FastCDC), allowing for efficient deduplication and data integrity verification.
* **Offline Capable:** Sync happens over your LAN when the internet is down.

### 🛡️ Resilient Storage

* **Delete-Protection:** Accidental deletions are captured in a configurable "Trash Bin" and recoverable via version history.
* **Deduplication:** Identical file chunks are stored only once, saving significant space on backups and versioned files.

### ⚡ Hybrid Performance Architecture

* **Rust Storage Engine:** Handles low-level I/O, encryption, and chunking with memory-safe, high-performance code.
* **FastAPI Orchestration:** A modern Python API layer manages authentication, policy, and peer coordination.
* **React + TypeScript UI:** A clean, responsive web dashboard for managing your files and nodes.

---

## 🏗️ Architecture

D.U.P.A uses a layered architecture to maximize performance on modest hardware:

1. **Storage Layer (Rust):** Implements Content-Defined Chunking (FastCDC), encryption, and local metadata indexing (Sled/RocksDB).
2. **API Layer (Python/FastAPI):** Exposes a RESTful API for the CLI and Web UI. Handles complex business logic and coordination.
3. **Presentation Layer (React):** A Single Page Application (SPA) communicating exclusively via the API.

---

## 🛠️ Getting Started

### Prerequisites

* **Rust:** Stable toolchain (`cargo`)
* **Python:** 3.10+ (`uv` or `pip`)
* **Node.js:** 18+ (for building the frontend)

### Installation

1. **Clone the repository:**bash
git clone [https://github.com/your-username/dupa.git](https://www.google.com/search?q=https://github.com/uday68/dupa.git)
cd dupa
```


```


2. **Build the Storage Engine (Rust):**
```bash
cd core
cargo build --release

```


3. **Install Python Dependencies:**
```bash
cd../api
pip install -r requirements.txt

```


4. **Run the D.U.P.A Node:**
```bash
# Starts the Rust core and FastAPI server
python main.py start --data-dir=~/dupa-storage

```


5. **Access the Dashboard:**
Open `http://localhost:8000` in your browser.

---

## 💻 Usage

### Command Line Interface (CLI)

D.U.P.A provides a robust CLI for headless environments.

```bash
# Initialize a new vault
dupa init --path /mnt/storage

# Add a peer device
dupa peer add <device-id>

# List files
dupa ls /Photos

# Sync status
dupa status

```

### API Documentation

Interactive API docs are available at `http://localhost:8000/docs` (Swagger UI) when the daemon is running.

---

## 🗺️ Roadmap

* [ ] **GraphQL API:** For flexible, bandwidth-efficient metadata querying.
* [ ] **S3 Integration:** Optional encrypted backup to S3-compatible buckets.
* [ ] **Mobile Clients:** Native iOS and Android apps.
* [ ] **Advanced Retention Policies:** WORM (Write Once Read Many) and automated purging.

---

## 🤝 Contributing

Contributions are welcome! Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

* **Rust:** Run `cargo fmt` and `cargo clippy` before committing.
* **Python:** We use `black` and `flake8` for formatting and linting.

---

## 📄 License

This project is licensed under the **Apache License 2.0** - see the(LICENSE) file for details.

---

## 💖 Acknowledgments

D.U.P.A takes inspiration from the giants of distributed storage:

* **Syncthing:** For the peer-to-peer connectivity model.
* **Nextcloud:** For usability and the "self-hosting" vision.
* **IPFS:** For content-addressing concepts.
* **SeaweedFS:** For efficient blob storage architecture.

```

This README structure includes standard badges [3, 4], a clear features list derived from the report [1, 5], and installation steps typical for a Rust/Python hybrid project.[6, 7]

```
