=============================
Widget with an Auxiliary Part
=============================

LabelFrame
----------

Let's try a widget with an auxiliary class such as LabelFrame::

	>>>b=ttk.LabelFrame(None) 
	>>>b.winfo_class()
	'TLabelframe' 
   # you noticed it's a small `f` didn't you, TLabelframe
   
	>>>St.layout('TLabelframe')
	[('Labelframe.border', {'sticky': 'nswe'})]  
	# where is the `label` part then!!!? 
   
	>>>s.layout('TLabelframe.Label')
   #OK I cheated, I knew the answer
		[('Label.fill',
	{'children': [('Label.text', {'sticky': 'nswe'})], 'sticky': 'nswe'})]


How do we know the name of the auxiliary part? It took a bit of web searching 
to find the answer in `Changing Widget Colors <http://wiki.tcl.tk/37973>`_ . 
Strictly the information is for TCL so it may not be totally applicable to 
python ttk, otherwise great information. In order to access all the elements 
of Notebook use TNotebook and TNotebook.Tab, for Treeview use Treeview and 
Heading. (We can optionally use 'Treeview.Heading', it produces the same 
results as for 'Heading'). Be careful with the component names used in the 
Treeview and Heading layouts (yes the Treeview class is simply Treeview)::

	>>>St.layout('Treeview')
	[('Treeview.field',
	{'border': '1',
		'children': [('Treeview.padding',
		{'children': [('Treeview.treearea', {'sticky': 'nswe'})],
			'sticky': 'nswe'})],
		'sticky': 'nswe'})]
      
	>>>s.layout('Heading') # alternative s.layout('Treeview.Heading') 
	[('Treeheading.cell', {'sticky': 'nswe'}),
	('Treeheading.border',
	{'children': [('Treeheading.padding',
		{'children': [('Treeheading.image', {'side': 'right', 'sticky': ''}),
			('Treeheading.text', {'sticky': 'we'})],
			'sticky': 'nswe'})],
		'sticky': 'nswe'})]

This now only leaves PanedWindow, the main class is TPanedwindow, the 
auxiliary class is either Horiontal.Sash or Vertical.Sash.

Rather than find out the class names every time we can use the table 
02ClassNames.csv instead. 

Table Class Names
-----------------

.. raw:: html

   <details>
   <summary><a>Show/Hide <b> Table </b> 02ClassNames.csv </a></summary>

.. csv-table:: 02ClassNames.csv
   :file: /tables/02ClassNames.csv
   :header-rows: 1
   :widths: 20, 30, 25

.. raw:: html

   </details>

|

The main class name is formed from the widget name 
where only the first letter is capitalised prefixed by a capital T, except 
for Treeview that retains its widget name. Remember that those widgets that 
have orientation need to be prefixed by either 'Horizontal.' or 'Vertical.'.
