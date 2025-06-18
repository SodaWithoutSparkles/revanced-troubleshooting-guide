# Git Configuration

## .gitignore Setup

The repository now includes a comprehensive `.gitignore` file that handles:

### Python-specific ignores:
- `__pycache__/` and `*.pyc` files
- Virtual environment directories
- Python build artifacts
- Testing and coverage files

### Project-specific ignores:
- **API cache files**: `patches_list.json`, `patches_version.json`
  - These are regenerated on each script run from the ReVanced API
  - No need to track them in git as they contain temporary data
- **State file**: `update.state` **IS tracked** as it contains important state information
  - Tracks last update timestamp and prevents unnecessary updates
  - Required for proper script operation
- **Temporary test files**: `test_temp_*.py`, `test_scratch_*.py`
  - Main test files are kept in git for validation purposes

### Development ignores:
- IDE configuration files (VS Code, IntelliJ, etc.)
- OS-generated files (`.DS_Store`, `Thumbs.db`, etc.)
- Backup and temporary files

### Build/deployment ignores:
- Retype build output (`.retype/`)
- Jekyll/GitHub Pages cache files
- Documentation build artifacts

## Files Removed from Tracking

The following files were removed from git tracking with `git rm --cached`:

```bash
# Python cache files
python/__pycache__/update_versions.cpython-312.pyc

# API cache files (will be regenerated)
.conf/python/patches_list.json
.conf/python/patches_version.json

# Note: .conf/python/update.state was added back to tracking as it's required
```

## What's Still Tracked

✅ **Keep in git:**
- Main Python scripts (`update_versions.py`, test scripts)
- Documentation files (`README.md`, `MIGRATION.md`, etc.)
- Configuration templates and workflows
- Requirements and setup files
- **State file** (`update.state`) for tracking last updates

❌ **Don't track:**
- Generated/cached API data files
- Python bytecode and artifacts
- IDE and OS files
- Temporary test files

This keeps the repository clean while preserving all the important development and documentation files.
