.. _04images:

======================
04 Working with Images
======================

.. sidebar:: tkinter version

	If your version of tkinter is 8.6 or higher then PhotoImage also works 
	with png files directly.

Using PhotoImage tkinter and ttk work with gif, pgm or ppm images and use xbm 
with BitmapImage. (PhotoImage and BitmapImage are both imported
using tkinter). 

.. table:: Display Images in tkinter

   =============== ========== ===========
   tkinter version PhotoImage BitmapImage
   =============== ========== ===========
    all versions     gif         xbm
    all versions     pgm
    all versions     ppm
    8.6 or higher    png
   =============== ========== ===========

You can check out the tkinter version as follows::

   import tkinter
   print(tkinter.TkVersion)

Some widgets have a property option called image (it is shown in 
`Tkinter 8.5 reference: a GUI for Python <https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/tkinter.pdf>`_) 
so once the image file is initiated in PhotoImage it can be loaded directly 
onto the widget. 

.. note:: All the images used with the examples will be found in the 
	directory "images". and the programs can be run using the same directory 
	structure on your computer.

.. toctree::
    :maxdepth: 3

    button-image