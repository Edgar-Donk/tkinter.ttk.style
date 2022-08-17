Create a Theme
==============

.. sidebar:: ttktheme

   Import ttktheme, then
   find ttktheme under your current python scheme, under the directory 
   ttkthemes found under \Lib\site-packages.

Once individual styles have been tested, we need to to incorporate these into 
a theme that can be called directly from the application with a single import 
and a single call. Obviously it would be foolish to work directly on the 
tkinter.ttk directory. One can concoct a complete standalone python theme 
together with the appropriate images, alternatively use the ttkthemes
module, adding your own theme name. 

Make a New Theme in ttktheme - green
====================================

   1. Create a new directory - give it an expressive name - say green
   2. Choose a ttktheme (*elegance*) and copy its main tcl file and image 
      subdirectory together with their contents to the green directory.  
      As with the original theme, we have a main theme directory now called
      *green*, a main theme file, *elegance.tcl* renamed *green.tcl*, and a 
      subdirectory renamed *green* containing the images.
   3. Edit green.tcl replacing the name of the original theme by the new name
      - so using *elegance* as our example ttktheme::

         namespace eval ::ttk::theme::green {
         package provide ttk::theme::green 0.1
         ....
         LoadImages [file join [file dirname [info script]] green]
         ....
         ::ttk::style theme create green -settings {

4. Copy one of the pkgIndex.tcl files from one of the themes to your main 
   directory, replace the name of the original ttktheme by your chosen name::

      if {![file isdirectory [file join $dir green]]} { return }
      if {![package vsatisfies [package provide Tcl] 8.4]} { return }
      
      package ifneeded ttk::theme::green 0.6.2 \
      [list source [file join $dir green.tcl]]

5. Edit the pkgIndex.tcl found under the parent directory of ttkthemes\themes, 
   add an extra line to the list of theme sources::

      green 0.1
      
6. edit ``_widgets.py`` file, in the main ttkthemes directory, in the 
   section of pixmap_themes add your theme to the list.

.. code-block:: python
   :emphasize-lines: 6
   
      pixmap_themes = [
         "arc",
         "blue",
         "clearlooks",
         "elegance",
         "green",
         "kroc",
         "plastik",
         "radiance",
         "ubuntu",
         "winxpblue
      ]

7. edit __init__.py in the main ttkthemes directory add your theme to the 
   THEMES list.

8. That should do it. Test that everything works after your editing. Now you 
   can start to replace original widgets with your preferred widgets.
