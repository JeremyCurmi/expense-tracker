## [ERR-20260320-001] docker_missing

**Logged**: 2026-03-20T05:20:00Z
**Priority**: high
**Status**: pending
**Area**: infra

### Summary
Docker CLI not available in the environment

### Error
```
sh: 1: docker: not found
```

### Context
- Command: `docker --version`
- Needed to run docker compose and seed/test endpoints locally

### Suggested Fix
Install Docker in the runtime environment or run compose on a host with Docker.

### Metadata
- Reproducible: yes
- Related Files: docker-compose.yml

---
