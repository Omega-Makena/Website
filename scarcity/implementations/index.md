---
title: "SCARCITY Implementations"
date: "2025-01-01"
description: "Instructions for installing the Python Lib vs the Demo App."
---

# Implementations & Setup

SCARCITY can be used as a standalone Python library for your own projects, or deployed as a full-stack system with a visual dashboard.

## 1. Core Library (Python)
For data scientists and engineers who want to use the **MPIE** (Causal Discovery) or **DRG** (Resource Governor) algorithms in their own scripts.

### Installation
```bash
pip install scarcity
```

### Quick Usage

```python
import scarcity
from scarcity.engine import MPIE

# Initialize the engine
engine = MPIE()

# Feed a data window
results = engine.process(data_window)
print(f"Discovered {len(results.paths)} causal paths")
```

-----

## 2. Full Demo System (Dashboard + Backend)

For running the complete environment with the **React Dashboard** to visualize causal hypergraphs and resource monitoring in real-time.

### Prerequisites

  * **Python 3.11+**
  * **Node.js 18+**

### Backend Setup

The backend serves the API that the dashboard connects to.

```bash
# Clone the repository
git clone https://github.com/Omega-Makena/scarcity.git
cd scarcity/backend

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the API server
uvicorn app.main:app --reload --port 8000
```

### Frontend Setup (Demo UI)

The interactive dashboard for visualizing the system.

```bash
cd scarcity-deep-dive

# Install dependencies
npm install

# Start the development server
npm run dev
```

### Access

  * **Dashboard**: `http://localhost:3000`
  * **API Documentation**: `http://localhost:8000/docs`

<!-- end list -->
