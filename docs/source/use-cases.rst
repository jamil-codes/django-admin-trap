Use Cases
=========

Honeypot Security
-----------------

Place traps on common admin URLs to catch automated attacks and curious attackers:

.. code-block:: python

   urlpatterns = [
       # Common attack targets
       path('admin/', include('django_admin_trap.urls')),
       path('wp-admin/', include('django_admin_trap.urls')),
       path('administrator/', include('django_admin_trap.urls')),
       
       # Your real admin (completely hidden)
       path('c54b2e89-admin/', admin.site.urls),
   ]

Development & Staging
---------------------

Use the fake admin in development environments to avoid setting up real admin users:

.. code-block:: python

   # settings.py
   if DEBUG or STAGING:
       urlpatterns = [
           path('admin/', include('django_admin_trap.urls')),
       ]

Client Demos
------------

Show clients the admin interface without giving them actual access:

.. code-block:: python

   urlpatterns = [
       path('demo/', include('django_admin_trap.urls')),
   ]

Security Through Obscurity
--------------------------

Even though this shouldn't be your only security measure, it adds an extra layer:

.. code-block:: python

   urlpatterns = [
       path('admin/', include('django_admin_trap.urls')),  # Decoy
       path('backend/', admin.site.urls),  # Real admin
   ]

Load Testing
------------

Since it's stateless and lightweight, you can use it for load testing admin login pages without database overhead.