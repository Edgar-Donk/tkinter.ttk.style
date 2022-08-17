Lime Treeview
-------------

.. |thn| image:: ../images/lime/slider-hn.png
   :width: 25
   :height: 21

.. |thp| image:: ../images/lime/slider-hp.png
   :width: 25
   :height: 21

.. |tha| image:: ../images/lime/slider-ha.png
   :width: 25
   :height: 21

.. table:: Lime Treeview

   ================= ================= ================= 
   Normal            Active            Pressed         
   |thn|              |tha|              |thp|             
   ================= ================= ================= 

The treeview heading has three different images that were the same as those 
used in scrollbar thumb. It is probably not possible to use selected, the
headings do not react interactively and only the treeview body reacts to
binding.

Notice the extra bit of mapping to enable the row selection being highlighted.

.. container:: toggle

   .. container:: header

       *Show/Hide Code* 10lime_treeview.py

   .. literalinclude:: ../examples/10lime_treeview.py
