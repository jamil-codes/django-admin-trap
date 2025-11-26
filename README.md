# Django Admin Trap 🔐

A completely fake Django admin login page that mimics the real Django admin perfectly. Ideal for security-through-obscurity setups, basic deception traps, or simply confusing automated scanners and attackers.

**Warning**: This is a trap. It looks exactly like the Django admin, but it never logs anyone in.

---

## 🚀 Features

- **Perfect Disguise** – Identical to Django’s real admin login
- **Stateless by Design** – Zero database access, no data written
- **No Logging** – Does not store credentials, attempts, or IPs
- **Always Rejects** – Every login attempt returns “invalid credentials”
- **Plug & Play** – Configure once, done in minutes
- **Django Native** – Uses Django’s official admin templates

---

## 📦 Installation

```bash
pip install django-admin-trap
````

---

## ⚡ Quick Setup

### 1. Add to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    'django_admin_trap',
]
```

### 2. Add to your `urls.py`:

#### **A. Replace the default admin (recommended for traps)**

```python
urlpatterns = [
    path('admin/', include('django_admin_trap.urls')),
]
```

#### **B. Use alongside the real admin**

```python
urlpatterns = [
    path('admin/', include('django_admin_trap.urls')),  # Fake
    path('real-admin/', admin.site.urls),              # Real
]
```

#### **C. Multiple trap endpoints**

```python
urlpatterns = [
    path('admin/', include('django_admin_trap.urls')),
    path('wp-admin/', include('django_admin_trap.urls')),
    path('administrator/', include('django_admin_trap.urls')),
    path('real-admin/', admin.site.urls),
]
```

---

## 🎯 How It Works

* Any URL under a trap path displays the fake admin login
* All login attempts fail with the correct Django error message
* Non-staff authenticated users see their username (mirrors real behavior)
* Uses Django's own admin template system for perfect mimicry
* Fully stateless — no data saved, no credentials processed

---

## 🛡️ Use Cases

### 1. Honeypot-Style Decoys

```python
urlpatterns = [
    path('admin/', include('django_admin_trap.urls')),
    path('wp-admin/', include('django_admin_trap.urls')),
    path('real-admin/', admin.site.urls),
]
```

### 2. Development Mock (No risk of accidental changes)

```python
if DEBUG:
    urlpatterns = [
        path('admin/', include('django_admin_trap.urls')),
    ]
else:
    urlpatterns = [
        path('admin/', admin.site.urls),
    ]
```

### 3. Client Demos Without Access

```python
urlpatterns = [
    path('demo-admin/', include('django_admin_trap.urls')),
]
```

---

## 🔧 Configuration

No configuration required.

### Optional: Custom Template

To override the login page:

1. Create `templates/admin_trap/login.html`
2. Extend Django’s admin login:

```html
{% extends "admin/login.html" %}
```

---

## ❓ FAQ

### **Does this store any data?**

No. Zero logging. Zero database writes.

### **Is it detectable?**

It uses the real Django admin template and response flow, so it’s extremely difficult to distinguish.

### **Will this slow down my app?**

No — it only renders a template.

### **Can I run this with my real admin?**

Yes. Just place the real admin under a different URL.

---

# 🔍 Why No Logging?

Django Admin Trap is intentionally **stateless**.

A real honeypot that collects IPs, attempts, or credentials requires:

* background workers
* rate-limit logic
* storage pruning
* SIEM or log aggregation
* protection from database flooding during brute-force attacks

This package is **not** meant to do any of that.

Brute-force bots can generate thousands or millions of login attempts.
Storing those attempts inside your Django database is:

* inefficient
* expensive
* potentially dangerous
* and not Django’s job at all

Logging belongs to your **firewall, CDN, WAF, Nginx access logs, or gateways**, where traffic should be rate-limited and monitored properly.

The trap’s only job is **deception**, nothing more.

If you need a real honeypot that stores attempts, use:

* other logging-focused security tools

Django Admin Trap will always remain lightweight, simple, and stateless.

---

# 🚨 Security Notes

* This is a **deception layer**, not a security control
* Always secure your real admin: strong passwords, 2FA, hidden URLs
* Combine with proper upstream protections (Cloudflare, Fail2ban, WAF, etc.)
* If you need logging, do it outside Django — not inside this trap

---

## 📄 License

MIT License.

---

## 🔗 Links

* **PyPI** – [https://pypi.org/project/django-admin-trap/](https://pypi.org/project/django-admin-trap/)
* **GitHub** – [https://github.com/jamil-codes/django-admin-trap](https://github.com/jamil-codes/django-admin-trap)
* **Documentation** – [https://django-admin-trap.jamilcodes.com/](https://django-admin-trap.jamilcodes.com/)

