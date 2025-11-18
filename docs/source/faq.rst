Frequently Asked Questions
==========================

Does this store any data?
-------------------------

**No.** Zero database interactions. Completely stateless. No credentials, IP addresses, or attempt data is stored anywhere.

Can attackers detect this is a trap?
------------------------------------

**It's very difficult.** The trap uses Django's actual admin templates and responses, making it visually and behaviorally identical to a real admin login page until the failed login.

What about performance?
-----------------------

**Minimal impact.** Since it's just template rendering with no database operations, the performance impact is negligible.

Can I use this alongside the real admin?
----------------------------------------

**Yes!** That's the recommended approach. Put your real admin on a different URL path.

.. code-block:: python

   urlpatterns = [
       path('admin/', include('django_admin_trap.urls')),  # Trap
       path('my-secure-admin/', admin.site.urls),  # Real
   ]

Does it work with custom admin templates?
-----------------------------------------

**Yes.** If you have custom admin templates in your project, the trap will use those, maintaining your custom look.

Can I customize the error message?
----------------------------------

**Currently no.** The package is designed to be a perfect mimic, so it uses Django's standard "invalid credentials" message.

Is this a security solution?
----------------------------

**No.** This is a **deterrent and detection tool**, not a security solution. Use it alongside proper security measures like strong passwords, 2FA, and rate limiting.