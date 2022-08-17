Lime Notebook
-------------

.. |tn| image:: ../images/lime/tab-nx.png
   :width: 25
   :height: 25

.. |tp| image:: ../images/lime/tab-px.png
   :width: 25
   :height: 25

.. |ta| image:: ../images/lime/tab-hx.png
   :width: 25
   :height: 25

.. |td| image:: ../images/lime/tab-dx.png
   :width: 25
   :height: 25

.. table:: Lime Notebook (alternative)

   ================= ================= ================= =================
   Normal            Pressed           Active             Disabled
   |tn|              |tp|              |ta|               |td|
   ================= ================= ================= =================

The blue notebook has a few configuration lines, and the result is 
disappointing, The ony user feedback occurs when the tab is active. The 
better looking themes have a selected tab that is lighter than the 
background, when the tab is active it lightens also when selected it slightly 
grows in height. The deselected tab darkens. 

.. sidebar:: Initial Attempt

   As in keramik, the right hand side had a line of transparent pixels, 
   this was quickly discarded since the tabs showed a gap between one another.

The methods used by keramik look promising, we'll need four images, three 
being slightly larger and paler. All four images have no lower corners. On 
the normal or disabled tab, there is a band of transparent pixels on the 
upperside and the lowerside is cropped, this gives the effect of resizing.

There is also a method included to expand the tab size after it has been
selected. The parent notebook should have its tabmargins set to allow the 
expansion by the tab.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10notebook.py

   .. literalinclude:: ../examples/10notebook.py

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10lime_notebook.py

   .. literalinclude:: ../examples/10lime_notebook.py
