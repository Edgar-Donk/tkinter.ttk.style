=================
Widgets General
=================

All the widgets previously found in tkinter remain, ttk has many of the 
original widgets and the class Style(). Two of the widgets in ttk, Combobox 
and Treeview are new, whereas some widgets only exist in tkinter. 

.. note:: Spinbox has been added to ttk - see the latest documentation.
   If your Python is 3.7 or later then everything should work, if you have 
   an earlier release then change the import statements and import Spinbox 
   from tkinter. 

Where widgets are duplicated be aware that  
property options do not correspond between tkinter and ttk. For instance ttk 
Button has a 
single option ``style`` instead of 24 additional property options in tkinter, 
the remaining 10 property options are common to both Button widgets. Use
`"Tkinter 8.5 reference a GUI for Python" <https://www.hsg-kl.de/faecher/inf/python/tkinter/tkinter.pdf>`_
to find out which property options are used on all the widgets. 

.. topic:: Property Options

   For example in Label the option ``text`` is one of its property options 
   ``w = Label(root, text="Hello, world!")`` .

.. sidebar:: File Referencing

   Code examples, tables and figures will be prefixed by their chapter number.

The example 01Label_config.py shows the differences in property 
configurations found in the older tkinter and newer ttk Label.

Script 01Label_config.py
------------------------

To view or hide the code just click on the arrow.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 01Label_config.py
       
   .. literalinclude:: ../examples/01Label_config.py

The script displays the attributes available in tkinter and ttk, there are
fewer attributes in ttk as the
missing attributes are replaced by the options for the style attribute, this
should be useful when multiple widgets are used in a project.
Later it will be seen just how flexible ttk is. 