Setup Guide
===========

URL Configuration
-----------------

Choose one of these patterns for your ``urls.py``:

Option A: Replace Real Admin (Recommended for Traps)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from django.urls import include, path

   urlpatterns = [
       path('admin/', include('django_admin_trap.urls')),  # Fake admin
       # ... your other URLs
       # Your real admin is hidden on a different path
       path('hidden-admin/', admin.site.urls),
   ]

Option B: Multiple Trap Endpoints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   urlpatterns = [
       # Common admin URLs as traps
       path('admin/', include('django_admin_trap.urls')),
       path('wp-admin/', include('django_admin_trap.urls')),
       path('administrator/', include('django_admin_trap.urls')),
       path('login/', include('django_admin_trap.urls')),
       
       # Your actual admin (well hidden)
       path('my-secure-admin-panel/', admin.site.urls),
   ]

Option C: Development Mock
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # settings.py
   if DEBUG:
       urlpatterns = [
           path('admin/', include('django_admin_trap.urls')),  # Fake for dev
       ]
   else:
       urlpatterns = [
           path('admin/', admin.site.urls),  # Real for production
       ]

Verification
------------

Visit your trap URL (e.g., ``/admin/``) and you should see a perfect Django admin login page. Try logging in - it will always fail with "invalid credentials".

.. note::

   The trap uses Django's actual admin templates, so it's visually identical to the real admin login.