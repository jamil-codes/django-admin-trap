Security Notes
==============

.. warning::

   **Important Security Considerations**

Purpose
-------

**django-admin-trap** is designed for:

* **Deterrence**: Waste attackers' time
* **Obscurity**: Hide your real admin endpoint

What It Is NOT
--------------

This package is **NOT**:

* A replacement for proper authentication
* A security barrier
* A logging/monitoring solution
* A replacement for security best practices

Recommended Security Practices
------------------------------

1. **Keep Django Updated**: Always run the latest secure Django version
2. **Strong Admin Path**: Use unpredictable URLs for your real admin
3. **Strong Passwords**: Enforce strong admin user passwords
4. **Two-Factor Authentication**: Implement 2FA for admin users
5. **Rate Limiting**: Use rate limiting on admin endpoints
6. **IP Whitelisting**: Restrict admin access to specific IPs if possible
7. **Monitoring**: Monitor your traps for suspicious activity

Example Secure Setup
--------------------

.. code-block:: python

   # urls.py - Hidden real admin
   urlpatterns = [
       # Traps for common URLs
       path('admin/', include('django_admin_trap.urls')),
       path('wp-admin/', include('django_admin_trap.urls')),
       
       # Real admin - well hidden
       path('c54b2e89-secure-admin-panel/', admin.site.urls),
   ]

   # Use environment variables for the real admin path
   # REAL_ADMIN_URL = os.getenv('REAL_ADMIN_URL', 'c54b2e89-secure-admin-panel')

Monitoring
----------

Since django-admin-trap doesn't log anything, consider:

* Server access logs for trap URLs
* Django's built-in logging for high traffic to trap endpoints
* External monitoring services

Remember
--------

This package is one tool in your security toolbox. **Defense in depth** is the key to good security practices.