### The Twelve Factors
- [x] **Codebase** (One codebase tracked in revision control, many deploys) - GitHub
- [x] **Dependencies** (Explicitly declare and isolate dependencies) - uses requirements.txt
- [x] **Config** (Store config in the environment) - uses .env files
- [ ] **Backing services** (Treat backing services as attached resources)
- [ ] **Build, release, run** (Strictly separate build and run stages)
- [X] **Processes** (Execute the app as one or more stateless processes) - Thanks Docker!
- [X] **Port binding** (Export services via port binding) - 8000 & 55432
- [ ] **Concurrency** (Scale out via the process model)
- [ ] **Disposability** (Maximize robustness with fast startup and graceful shutdown)
- [ ] **Dev/prod parity** (Keep development, staging, and production as similar as possible)
- [ ] **Logs** (Treat logs as event streams)
- [X] **Admin processes** (Run admin/management tasks as one-off processes) - manage.py