Standalone Theme - orange
=========================

The alternative to the above is to create a standalone package. Here the 
package will need to replicate what a tcl based ttktheme 
does but using python. 

We can use the script for `plastik_theme.py <https://github.com/enthought/Python
-2.7.3/blob/master/Demo/tkinter/ttk/plastik_theme.py>`_ as a basis for our 
standalone - this should shortcut a lot of the work. The script uses 
Style.theme_create and follows the pattern already seen in 
:ref:`03combobox.py<combobox themes>` for theme_settings. Copy the plastik 
image files found in ttkthemes to a subdirectory, called *plastik*, at your 
test location, these will eventually be replaced by new file names of your 
own choice.

Convert the plastik_theme.py script from python2 to 3. 

We can test plastik_theme.py by running the script 06treeview.py directly 
from your os system. First **import plastik_theme** then we call 
**plastik_theme.install('plastik')**, notice that it has *'plastik'* as a 
variable, so *'plastik'* is the subdirectory where the images from plastik 
have been copied to.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 06treeview.py

   .. literalinclude:: ../examples/06treeview.py
      :lines: 94-112

When that works, rename the *plastik* directory and subdirectory, to your 
theme name, say *orange*, then wherever we find *plastik* referenced in 
plastik_theme.py we should change it to our theme name *orange*, using
orange_theme.py. ::

	style.theme_create("orange", "default", settings={
	.....
	style.theme_use("orange") # right at the end

We now have both an extra theme in ttkthemes controlled by tcl files or we 
have a standalone theme running under python. Associated with these 
control files is a subdirectory of image files. Either system is as valid as 
the other, the choice is yours. 

The method of working for both is similar, after creating a good quality 
working widget with all the required states, either replace the  
widget in green.tcl or orange.py, change the references to any images, alter 
the border sizes as necessary, then add replacement images to the image 
subdirectory. When everything works satisfactorily delete the unused images 
found in the green or orange image directories. 

Occasionaly it may be necessary to change the widget layout. In both methods 
we normally need to translate between tcl and python, use the files plastik.tcl 
and plastik.py to help spot the differences and similarities between the two 
languages.

Translating between TCL and Python
----------------------------------

We have been already automatically translating between TCL and Python, 
probably without our knowledge, most of the Style() commands have
done just that. All of the standard themes are programmed in TCL, but the
output of our queries is in Python. We could equally query the ttkthemes 
module, but in this case use ``themed_style.ThemedStyle()`` as opposed to
plain ``Style()``. The commands used are exactly the same in both modules. 
Open an interactive session.::

   import ttkthemes as ts
   s = ts.themed_style.ThemedStyle()
   s.theme_use('ubuntu')
   s.layout('TButton')
   
   Out[4]:
   [('Button.focus',
  {'sticky': 'nswe',
   'children': [('Button.button',
     {'sticky': 'nswe',
      'children': [('Button.padding',
        {'sticky': 'nswe',
         'children': [('Button.label', {'sticky': 'nswe'})]})]})]})]

   # Notice that there is no longer a ``border``, it was used for the image

Let's try with a horizontal scale.::

   s.layout('Horizontal.TScale')
   Out[5]:
   [('Horizontal.Scale.trough',
  {'sticky': 'nswe',
   'children': [('Horizontal.Scale.slider', {'side': 'left', 'sticky': ''})]})]
   
   s.element_options('Horizontal.Scale.slider')
   Out[6]: ()

No output for the element options - which should come as no surprise, since
the slider is also an image. (This result is the same with the Windows vista
theme).
