============
Requirements
============

.. sidebar:: Is your Python upto date?

   If you are using Python 2.7 or later or any of the Python 3 versions then 
   the tkinter version will be 8.5 or later, if we import the ttk module 
   in an active Python session there will be no warning message.

In order to use the scripts developed here, a modern version of Python with
a tkinter version needs to have themed widgets (ttk). If tkinter is 8.6 or 
greater png files can be used directly. Open a python session and import
ttk to confirm all will run. 

.. warning:: Python2 is no longer supported, so unless there are backward
    compatability issues work with Python3.

============================= =============================
 Python3                      Python2
============================= =============================
 ``import tkinter.ttk``        ``import Tkinter.ttk``
============================= =============================

* Windows Directory
   When working in Windows I found it useful to use directories within the
   user working directory ``C:\Users\edgar\programs\python312`` for the
   Python 3.12 installation, ``C:\Users\edgar\python`` for general python 
   scripts and ``C:\Users\edgar\sphinx`` for sphinx specific scripts, this 
   avoids editing issues if the programs were installed in ``C:\Program Files``
   or ``C:\Program Files (x86)``.

* Newer Tkinter 8.6 reference
   `"Tkinter Class API Reference" <https://tkdocs.com/pyref/>`_
* Older Tkinter reference
   download the pdf version of 
   `"Tkinter 8.5 reference a GUI for Python" <https://tkdocs.com/shipman/tkinter.pdf>`_, 
* There is an alternative site 8.5 refrerence
   https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html

.. sidebar:: External Python Modules

   Additional python modules can be installed from a system window,
   in Windows use the command module ``cmd`` found under 
   **C:\Windows\Sytem32\cmd.exe**. Once Python is installed and running open 
   the system window and type in ``pip install module``.

* Themed widgets
   See what has already been done with widgets, view and install the external 
   module ttkthemes::

      pip install ttkthemes 

   found at `"ttkthemes at github" <https://github.com/RedFantom/ttkthemes>`_. 
* Encoding and decoding images
   Using the base64 module. 
* Graphics editor
   Check and edit images.

.. sidebar:: Pillow and PIL

   Ensure that the older version of PIL has been uninstalled, 

   ``pip uninstall PIL``

* PIL (Pillow)
   Used extensively for drawing:: 

      pip install Pillow

* Pretty Print. 
   Better display for some of the output::

      pip install pprint

* colorsys
   Colour conversion between RGB, HLV, etc::

      pip install colorsys

* These words of wisdom
   Go to github `Putting on the Style! <https://github.com/Edgar-Donk/tkinter.ttk.style/tree/master>`_
   clone and unzip in your python playground, make sure that ``examples``, 
   ``tables`` and ``images`` stay at the same level in the directory 
   structure, the other files and images are not relevant if you are viewing
   readthedocs.
   
   If you want to run it as a sphinx example unzip to your sphinx playground,
   then install sphinx and sphinx-rtd-theme.::

      pip install sphinx

      pip install sphinx-rtd-theme

   All the necessary files should be present, so from your os system switch
   to the ``docs`` directory of the unzipped files and run the command
   ``make html``, which should make a new subdirectory ``_build/html``, 
   where you can load ``index.html``.

* Python IDE or code editor
   An IDE is an Integrated Development Environment, used to control projects -
   probably most inexperienced users only need a code editor, certainly they 
   are easier to learn. Idle and Thonny come with the Python installation,
   my choice would be Thonny. A second lightweight code editor is PyScripter
   (only available for Windows). More experienced users require an IDE and
   these are best for the individual to try, judge and select according to
   personal requirements.

