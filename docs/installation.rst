Installation Guide
==================

Prerequisites
-------------

* Python 3.8 or higher
* pip package manager
* Git (optional, for cloning the repository)

Step-by-Step Installation
-------------------------

1. **Clone the repository**

   .. code-block:: bash

      git clone https://github.com/YOUR_USERNAME/leonardo-knowledge-graph.git
      cd leonardo-knowledge-graph

2. **Create a virtual environment (recommended)**

   .. code-block:: bash

      # On Windows
      python -m venv venv
      venv\Scripts\activate
      
      # On macOS/Linux
      python3 -m venv venv
      source venv/bin/activate

3. **Install dependencies**

   .. code-block:: bash

      pip install -r requirements.txt

4. **Verify installation**

   .. code-block:: bash

      python -c "import networkx; print('NetworkX version:', networkx.__version__)"
      python -c "import matplotlib; print('Matplotlib version:', matplotlib.__version__)"

Dependencies
------------

The project requires the following Python packages:

* **networkx** (>=3.0): Graph creation and analysis
* **matplotlib** (>=3.5): Data visualization
* **pandas** (>=1.4): Data manipulation
* **numpy** (>=1.21): Numerical operations
* **python-louvain** (>=0.16): Community detection
* **sphinx** (>=5.0): Documentation generation
* **sphinx-rtd-theme** (>=1.0): Documentation theme

Troubleshooting
---------------

**Issue**: `ModuleNotFoundError: No module named 'networkx'`

**Solution**: Install missing dependencies:

.. code-block:: bash

   pip install networkx matplotlib pandas numpy python-louvain

**Issue**: `FileNotFoundError` when running the project

**Solution**: Ensure the data files are in the `data/` directory:

.. code-block:: bash

   mkdir -p data
   # Add your CSV files here

**Issue**: Error with python-louvain

**Solution**: Try alternative installation:

.. code-block:: bash

   pip install community
   # In code, use: import community as community_louvain