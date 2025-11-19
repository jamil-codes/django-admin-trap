Installation
============

PyPI Installation
-----------------

.. code-block:: bash

   pip install django-admin-trap

Django Configuration
--------------------

Add to your ``INSTALLED_APPS`` in ``settings.py``:

.. code-block:: python

   INSTALLED_APPS = [
       # ... your other apps
       'django_admin_trap',
   ]

Add to your ``urls.py``:

.. code-block:: python

   urlpatterns = [
       path('admin/', include('django_admin_trap.urls')),  # Fake admin trap
       path('real-admin/', admin.site.urls), # Your real admin
   ]


No migrations needed! The package is completely stateless.

Requirements
------------

* Python 3.7+
* Django 3.2+

Compatible with all modern Django versions. No additional dependencies.