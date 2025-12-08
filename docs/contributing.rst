Contributing
============

We welcome contributions to improve the Leonardo da Vinci Knowledge Graph project!

How to Contribute
-----------------

1. **Fork the repository**
2. **Create a feature branch**
   .. code-block:: bash
   
      git checkout -b feature/your-feature-name
   
3. **Make your changes**
4. **Commit your changes**
   .. code-block:: bash
   
      git commit -m "Add your descriptive commit message"
   
5. **Push to the branch**
   .. code-block:: bash
   
      git push origin feature/your-feature-name
   
6. **Open a Pull Request**

Development Setup
-----------------

1. Clone your fork:
   .. code-block:: bash
   
      git clone https://github.com/YOUR_USERNAME/leonardo-knowledge-graph.git
      cd leonardo-knowledge-graph
   
2. Set up development environment:
   .. code-block:: bash
   
      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate
      pip install -r requirements.txt
      pip install -e .
   
3. Run tests:
   .. code-block:: bash
   
      python -m pytest tests/

Code Style
----------

* Follow PEP 8 guidelines
* Use meaningful variable and function names
* Add docstrings to all functions, classes, and methods
* Write unit tests for new functionality
* Update documentation when changing code

Areas for Contribution
----------------------

1. **Dataset Expansion**
   - Add more concepts from Leonardo's notebooks
   - Refine relationship weights based on historical analysis
   - Add temporal metadata to concepts

2. **Algorithm Implementation**
   - Additional centrality measures
   - Advanced community detection algorithms
   - Graph embedding techniques

3. **Visualization**
   - Interactive visualizations with Plotly
   - 3D graph visualizations
   - Timeline visualizations

4. **Documentation**
   - Improve tutorial content
   - Add more examples
   - Translate documentation to other languages

Reporting Issues
----------------

When reporting issues, please include:

1. Description of the problem
2. Steps to reproduce
3. Expected behavior
4. Actual behavior
5. Environment details (OS, Python version, package versions)

License
-------

This project is licensed under the MIT License. By contributing, you agree that 
your contributions will be licensed under the same license.

Contact
-------

For questions about contributing, please open an issue on GitHub or contact 
the project maintainer.