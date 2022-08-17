Documentation
=============

Create a directory ``myproject`` with two subdirectories ``docs`` and ``scripts``.
Assuming that we are in myproject/docs obtain documentation, which includes 
an index that works, a module index and search page, there are a few 
important pre-requisites. It is often useful 
to have separate source and build directories, so when using the 
``sphinx-quickstart`` on the first question, asking whether to build a 
separate source directory, say yes and not the default [n].

Edit the ``conf.py`` file to show the path to the ``scripts`` directory. Add
to the extensions sphinx.ext.autodoc, and sphinx.ext.napoleon, then within 
the body add the napoleon directives. Depending on your preference either 
activate google or numpy docstrings::

    # uncomment the following, change path to where scripts is
    # path is relative to config.py
    import os
    import sys
    sys.path.insert(0, os.path.abspath('../../scripts/'))
    html_theme = "pydata_sphinx_theme"
    html_sidebars = {
    "contributing": ["sidebar-search-bs.html", "custom-template.html"],
    "changelog": [],
    }
    ## older version
    '''
    html_sidebars = {
        '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html'
        ]
    ]
    '''
    # add the dependancies within extensions for autodoc and napolean
    extensions =["sphinx.ext.autodoc",
        'sphinx.ext.napoleon',
        "sphinx.ext.autosummary",
        #"numpydoc", # creates loads of warnings
        'sphinx.ext.mathjax'
    ]
    # add napolean directives - using numpy style docstrings
    napoleon_google_docstring = False
    napoleon_numpy_docstring = True

Autodoc is now setup to look in the directory scripts, which will contain
all the python scripts which should include all the necessary docstrings. It
is best to ensure that all variables, functions, methods and classes are 
correctly  formatted according to PEP8 using pylint. If the directory has
subdirectories add __init__.py. 

Set up the project with all the normal rst, example and image files, (include
source.rst in the main index) then run a test with ``make html``. When in 
good shape start autogenerating the docstrings.
Run ``~my_project\docs>sphinx-apidoc -o ./source ../scripts``. This creates
two files scripts.rst and modules.rst in the source directory. ``modules.rst``
is the index for ``scripts.rst``, they can be used as they stand, but we 
will modify this.  

Check the main index.rst file, just before `Indices and Tables` heading we 
need a toctree pointing at `modules.rst`::

    Sources
    =======

    .. toctree::
        :maxdepth: 3
    
        source/modules

Each python script will become our modules, so we require separate rst files
for each of the modules within the source directory. Each module file will 
look a bit like part of the original `scripts.rst`::

    Tree Class Module
    ==================

    tree\_class class
    ----------------------

    .. automodule:: tree_class
       :members:
       :undoc-members:
       :show-inheritance:

.. note:: In the heading escape any underscores.

``.. Automodule::`` is used to trigger autodocumenting and points towards
tree_class.py located in the scripts directory. Make `scripts.rst` into the
local index, by adding toctree from modules.rst which can now be deleted.
The original scripts.rst had a ``Module contents``, which is no longer
required. Within the scripts directory add any local import file required. If
these are not part of the documentation do not include them as a module.

``make clean`` before re-running ``make html``.

.. toctree::
   :maxdepth: 4

   roundrect
   tools
