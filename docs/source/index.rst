Django Admin Trap 🔐
====================

.. image:: https://img.shields.io/pypi/v/django-admin-trap.svg
    :target: https://pypi.org/project/django-admin-trap/
    :alt: PyPI Version

.. image:: https://readthedocs.org/projects/django-admin-trap/badge/?version=latest
    :target: https://django-admin-trap.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

A completely fake Django admin login page that mimics the real Django admin perfectly. Perfect for security through obscurity, honeypots, or just confusing attackers.

.. warning::

   **This is a trap!** It looks exactly like the real Django admin but doesn't actually log anyone in.

.. rubric:: Features

* **Perfect Disguise**: Looks identical to the real Django admin login
* **No Database**: Zero database interactions - completely stateless
* **No Logging**: Doesn't store any credentials or attempt data
* **Always Fails**: Every login attempt shows "invalid credentials" error
* **Plug & Play**: Setup in 2 minutes
* **Django Native**: Uses Django's actual admin templates and styling

Quick Start
-----------

.. code-block:: bash

   pip install django-admin-trap

Add to your ``urls.py``:

.. code-block:: python

   urlpatterns = [
       path('admin/', include('django_admin_trap.urls')),  # Fake admin trap
       path('real-admin/', admin.site.urls),  # Your real admin
   ]

.. toctree::
   :maxdepth: 2
   :caption: Documentation

   installation
   setup
   use-cases
   how-it-works
   faq
   security

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`