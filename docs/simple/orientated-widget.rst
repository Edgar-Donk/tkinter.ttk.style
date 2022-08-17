=======================
Widget with Orientation
=======================

Scale - Style
-------------

When we have a widget with an orientation, such as Scale, see what changes.
Continue with your interactive session.::

	>>>b = ttk.Scale(None)
	>>>b.winfo_class()
	'TScale'    # class name
   >>> layout = St.layout('Vertical.TScale') 
   # It won't work if you use just TScale
   
	>>>layout
	[('Vertical.Scale.trough',
	{'children': [('Vertical.Scale.slider', {'side': 'top', 'sticky': ''})],
	'sticky': 'nswe'})] 
   # we found 2 components, trough and slider

Now try the Horizontal orientation::

	>>>layout = St.layout('Horizontal.TScale') 
	>>>layout
	[('Horizontal.Scale.trough',
	{'children': [('Horizontal.Scale.slider', {'side': 'left', 'sticky': ''})],
		'sticky': 'nswe'})]  
   # notice the changes that are specific to orientation
   
	>>>d = St.element_options('Horizontal.Scale.trough') 
   # using the component name
	>>>d
	('borderwidth', 'troughcolor', 'troughrelief')  
   # to find the element values
	>>>St.lookup('Horizontal.Scale.slider', 'troughcolor')
	'#c3c3c3'

That wasn't too bad, once we knew that the widget had orientation which had
a capitalised first letter. 