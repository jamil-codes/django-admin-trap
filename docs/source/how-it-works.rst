How It Works
============

Technical Overview
------------------

**django-admin-trap** is incredibly simple by design:

1. **URL Routing**: Any request to the trap URLs is routed to a fake login view
2. **Template Rendering**: Uses Django's actual ``admin/login.html`` template
3. **Form Handling**: Processes login attempts but always returns "invalid credentials"
4. **Stateless**: No data is stored, logged, or processed

The Magic
---------

.. code-block:: python

   # Simplified version of what happens:
   def fake_login(request):
       if request.method == 'POST':
           # Always show error, regardless of credentials
           return render(request, 'admin/login.html', {
               'error_message': 'Invalid credentials'
           })
       return render(request, 'admin/login.html')

Key Characteristics
-------------------

* **No Database**: Zero database queries or models
* **No Authentication**: Never calls Django's auth system
* **No Logging**: No files, databases, or external services store data
* **Perfect Mimicry**: Uses the same templates, CSS, and form structure as real admin

Performance Impact
------------------

Minimal! The trap only:

1. Handles HTTP request
2. Renders a template
3. Returns response

No database operations, authentication checks, or external API calls.

.. note::

   Since it's just template rendering, the performance impact is negligible - perfect for high-traffic honeypots.