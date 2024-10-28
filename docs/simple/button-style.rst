==============
Button - Style
==============

Use the button widget as our first example and run the following queries 
interactively in Python. 

.. sidebar:: Import ttk
    
    Older versions of python work with ``import ttk``, newer versions use
    ``import tkinter.ttk as ttk``

Find the class name::

   >>>import ttk
   >>>St = ttk.Style()  
   # Style is used to call the classic theme
   >>>St.theme_use('classic')
   # step 1 using the widget name of *Button*
   >>>but = ttk.Button(None, text='Righto') 
 
   # step 2 
   >>>butClass = but.winfo_class() 
   # find the class name using the Button handle "but"
   >>>butClass
      TButton

The class name is 'TButton'. Using layout find the element name(s), 
the elements are preceded by the component name, in this case **'Button.**::

	# step 3
	>>> layout = St.layout('TButton')
   # find the Button component names as used by the classic theme
	>>> layout 
	[('Button.highlight', {'children': [('Button.border', {'border':
	'1', 'children': [('Button.padding', {'children': [('Button.label',
	{'sticky': 'nswe'})], 'sticky': 'nswe'})], 'sticky': 'nswe'})],
	'sticky': 'nswe'})]

It creates quite an output, but don't be put off. We have found 4 element 
names - highlight, border, padding and label. Compare to :ref:`Button Elements`.

.. sidebar:: layout

    Older versions of python display this layout as::
    
        [('Button.highlight', {'children': [('Button.border', {'border':
        '1', 'children': [('Button.padding', {'children': [('Button.label',
        {'sticky': 'nswe'})], 'sticky': 'nswe'})], 'sticky': 'nswe'})],
        'sticky': 'nswe'})]
        
    Newer versions will display as::

        [('Button.highlight',
            {'children': [('Button.border',
                 {'border': '1',
                  'children': [('Button.padding',
                                {'children': [('Button.label',
                                               {'sticky': 'nswe'})],
                                 'sticky': 'nswe'})],
                  'sticky': 'nswe'})],
        'sticky': 'nswe'})]

Be careful to use the correct element name with right theme. That's just 
completed the third step. As a help in determining the element names for 
every widget check out the table 02elements.csv. See how the names change 
not only with the widgets, but may also change with the theme. 

Table Theme Layout Names
------------------------

.. raw:: html

   <details>
   <summary><a>Show/Hide <b> Table </b> 02names.csv </a></summary>

.. csv-table:: 02names.csv
   :file: /tables/02names.csv
   :header-rows: 1
   :delim: ;
   :widths: 20, 15

.. raw:: html

   </details>

|


Now onto the element options::

	# step 4 
	>>>d = St.element_options('Button.highlight') # find the element attributes
	>>> d
	('-highlightcolor', '-highlightthickness') 
   # 2 elements in this component
   
	# step 5 
	>>>St.lookup('Button.highlight', 'highlightthickness')
	1 
   # the highlight is 1 pixel thick
   
	# step 5 repeated for the other element
	>>> St.lookup('Button.highlight', 'highlightcolor')
	'#d9d9d9' 
   # highlight has a default or normal colour #d9d9d9 which is grey

Button is a fairly straightforward widget, but some such as Progressbar, 
Scale and Scrollbar have an orientation, whereas LabelFrame, Notebook and 
Treeview have a main and auxiliary class name. Lastly PanedWindow has both 
orientation and an auxiliary part. 

Table Theme Elements
----------------------

.. raw:: html

   <details>
   <summary><a>Show/Hide <b> Table </b> 02elements.csv </a></summary>

.. csv-table:: 02elements.csv
   :file: /tables/02elements.csv
   :header-rows: 1
   :delim: ;
   :widths: 15, 45, 45, 45, 45

.. raw:: html

   </details>

|

.. note:: 

   Widgets with an auxiliary part will have two entries.

