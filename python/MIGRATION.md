# Migration Guide: From checkReVancedVersion.py to update_versions.py

This guide helps you migrate from the old `checkReVancedVersion.py` script to the new `update_versions.py` system.

## Overview of Changes

### Old System (checkReVancedVersion.py)
- Used ReVanced API v2 (deprecated)
- Required complex configuration files
- Used template-based file generation
- Limited git integration
- Manual branch management

### New System (update_versions.py)
- Uses ReVanced API v4 (current)
- Simplified configuration
- Direct placeholder replacement in files
- Automatic git branch management
- Better error handling and logging

## Migration Steps

### 1. Backup Current Configuration
```bash
# Backup existing configuration
cp -r .conf .conf.backup
cp checkReVancedVersion.py checkReVancedVersion.py.backup
```

### 2. Update GitHub Actions Workflow

Replace the current `.github/workflows/version-and-lastCheck-bump.yml` with the new workflow:

```bash
# Backup existing workflow
cp .github/workflows/version-and-lastCheck-bump.yml .github/workflows/version-and-lastCheck-bump.yml.backup

# Copy new workflow
cp python/new-workflow.yml .github/workflows/update-versions.yml
```

### 3. Create Required Branches

The new system requires a `docs-base` branch for development and commits to `main` for production:

```bash
# Create docs-base branch from main
git checkout main
git checkout -b docs-base
git push origin docs-base

# The workflow will handle switching between branches automatically
```

### 4. Test the New System

```bash
# Test API connectivity
python3 python/test_api.py

# Dry-run test
python3 python/test_dry_run.py

# Test with wrapper script
./python/run_updater.sh --dry-run
```

### 5. Disable Old Workflow

Comment out or disable the old workflow to prevent conflicts:

```yaml
# In .github/workflows/version-and-lastCheck-bump.yml
name: "[DISABLED] Bump version and last modified time"
# Add this at the top to disable
```

## Configuration Changes

### Files No Longer Needed
- Most of the complex `.conf/python/` configuration files
- The template system (replaced with direct placeholder replacement)

### Files Still Used
- `.conf/python/update.lut.json` - Package name to common name mapping
- `.conf/python/update.state` - State tracking for updates

### New Files
- `python/update_versions.py` - Main updater script
- `python/requirements.txt` - Python dependencies
- `python/run_updater.sh` - Convenient wrapper script

## Placeholder System Changes

### Old System
Used template files with `{table}`, `{date}`, `{footnote}` placeholders that were processed to generate complete files.

### New System
Direct replacement of placeholders in existing markdown files:
- `${YT_VERSION}` → Latest YouTube version (e.g., "20.12.46")
- `${LAST_UPDATE}` → Timestamp (e.g., "2025-06-18 15:37:15 UTC")

## Workflow Differences

### Old Workflow
1. Run `checkReVancedVersion.py`
2. Generate template files
3. Manual git operations
4. Trigger rebuilds manually

### New Workflow
1. Ensure on `docs-base` branch
2. Fetch latest API data
3. Update placeholders in all markdown files
4. Commit changes to `main` branch
5. Return to `docs-base` branch
6. Automatically trigger website rebuild

## Rollback Plan

If you need to rollback to the old system:

```bash
# Restore old files
cp checkReVancedVersion.py.backup checkReVancedVersion.py
cp -r .conf.backup/* .conf/

# Restore old workflow
cp .github/workflows/version-and-lastCheck-bump.yml.backup .github/workflows/version-and-lastCheck-bump.yml

# Remove new workflow
rm .github/workflows/update-versions.yml

# Switch back to main branch
git checkout main
```

## Testing Checklist

Before going live with the new system:

- [ ] API connectivity test passes
- [ ] Dry-run test completes successfully
- [ ] Git branches are set up correctly (`docs-base` and `main`)
- [ ] GitHub Actions has proper permissions
- [ ] Discord webhook is configured (if using notifications)
- [ ] Old workflow is disabled
- [ ] New workflow can be triggered manually

## Benefits of Migration

1. **Future-proof**: Uses current API v4 instead of deprecated v2
2. **Simpler**: Less configuration, more direct approach
3. **Automated**: Better git integration and branch management
4. **Robust**: Improved error handling and recovery
5. **Maintainable**: Cleaner, more readable code
6. **Flexible**: Easy to extend for new features

## Support

If you encounter issues during migration:

1. Check the workflow logs in GitHub Actions
2. Run the test scripts to isolate problems
3. Use the dry-run mode to safely test changes
4. Refer to the README.md for detailed documentation
