# Odoo 19 CE - Dockerized Setup

Dockerized Odoo 19 Community Edition with PostgreSQL 16, OCA accounting addons, and Nginx reverse proxy.

## Quick Start

### 1. Initial Setup

```bash
# Run the setup script (clones OCA addons)
chmod +x setup.sh
./setup.sh
```

### 2. Configure Environment

Review and update these files:
- `.env` — Database credentials and ports
- `config/odoo.conf` — Odoo server settings (update `admin_passwd`)

### 3. Start Odoo (Development)

```bash
docker compose up -d
```

Access Odoo at: **http://localhost:8069**

### 4. First-Time Database Setup

1. Open http://localhost:8069
2. You'll see the database creation page
3. Fill in:
   - **Master Password**: Value from `admin_passwd` in `odoo.conf` (default: `odoo_admin_master`)
   - **Database Name**: e.g., `odoo19`
   - **Email**: Your admin email
   - **Password**: Your admin password
   - **Language**: English
   - **Country**: Indonesia (or your preference)
   - Check **Demo data** if you want sample data
4. Click **Create Database**

### 5. Install Modules

Go to **Apps** menu and install:

| Module | Search Term |
|--------|-------------|
| Sales | `sale_management` |
| CRM | `crm` |
| Inventory | `stock` |
| Purchase | `purchase` |
| Invoicing | `account` |
| Expenses | `hr_expense` |

> **Note**: Click "Update Apps List" from the Apps menu to see OCA modules.

OCA Financial modules available:
- General Ledger, Trial Balance, Aged Partner Balance
- Journal Ledger, Open Items Report
- Additional financial tools and utilities

---

## Project Structure

```
odoo-testing/
├── docker-compose.yml          # Dev orchestration
├── docker-compose.prod.yml     # Production overrides (Nginx)
├── .env                        # Environment variables
├── .env.example                # Template (safe for git)
├── setup.sh                    # Initial setup script
├── config/
│   └── odoo.conf               # Odoo server configuration
├── addons/                     # Your custom modules
├── oca-addons/                 # OCA modules (auto-cloned)
│   ├── account-financial-reporting/
│   └── account-financial-tools/
├── nginx/
│   └── odoo.conf               # Nginx reverse proxy config
└── README.md
```

---

## Custom Module Development

Create new modules in the `addons/` directory:

```bash
# Standard Odoo module structure
addons/
└── my_module/
    ├── __init__.py
    ├── __manifest__.py
    ├── models/
    │   ├── __init__.py
    │   └── my_model.py
    ├── views/
    │   └── my_model_views.xml
    ├── security/
    │   └── ir.model.access.csv
    └── data/
        └── data.xml
```

After creating a module, restart Odoo and update the apps list:

```bash
docker compose restart odoo
```

Then go to **Apps → Update Apps List** and search for your module.

---

## Common Commands

```bash
# Start services
docker compose up -d

# Stop services
docker compose down

# View logs
docker compose logs -f odoo
docker compose logs -f db

# Restart Odoo (after config/code changes)
docker compose restart odoo

# Access Odoo shell
docker compose exec odoo odoo shell -d <database_name>

# Access PostgreSQL
docker compose exec db psql -U odoo -d <database_name>

# Backup database
docker compose exec db pg_dump -U odoo <database_name> > backup_$(date +%F).sql

# Restore database
cat backup.sql | docker compose exec -T db psql -U odoo <database_name>

# Update a specific module
docker compose exec odoo odoo -d <database_name> -u <module_name> --stop-after-init
```

---

## Production Deployment

### On your VM:

```bash
# Clone the repo
git clone <your-repo-url> /opt/odoo
cd /opt/odoo

# Run setup
./setup.sh

# Update .env with strong passwords
nano .env

# Update odoo.conf for production
# - Set list_db = False
# - Set proxy_mode = True
# - Increase workers (recommended: 2 * CPU cores + 1)
nano config/odoo.conf

# Start with production config
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

### SSL (Let's Encrypt)

1. Update `nginx/odoo.conf` — uncomment SSL sections, set your domain
2. Mount SSL certificates in `docker-compose.prod.yml`
3. Or use a tool like [Certbot](https://certbot.eff.org/) on the VM

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 8069 already in use | Change `ODOO_PORT` in `.env` |
| Database connection error | Check `docker compose logs db` and verify `.env` credentials |
| Modules not appearing | Go to Apps → Update Apps List |
| Permission denied on addons | Run `chmod -R 755 addons/` |
| OCA modules not loading | Verify `oca-addons/` folders exist, re-run `setup.sh` |
