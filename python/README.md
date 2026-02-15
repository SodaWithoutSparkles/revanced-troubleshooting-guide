# ReVanced Version Updater

This directory contains scripts for updating ReVanced version information using the new v4 API.

## Files

- `update_versions.py` - Main script that updates versions and manages git branches
- `run_updater.sh` - Bash wrapper script for easier execution
- `test_api.py` - Test script to verify API connectivity and parsing
- `test_dry_run.py` - Dry-run test that simulates the update process
- `requirements.txt` - Python dependencies
- `github-actions-template.yml` - Template for GitHub Actions workflow
- `new-workflow.yml` - Complete replacement workflow for the old system
- `MIGRATION.md` - Detailed migration guide from old to new system
- `list.json` - Sample response from patches list API (for reference)
- `version.json` - Sample response from patches version API (for reference)

## Main Script: `update_versions.py`

### Features

- Fetches data from ReVanced API v4 endpoints
- Parses patch compatibility information
- Finds the latest supported YouTube version
- Replaces placeholders in markdown files:
  - `20.14.43` → Latest YouTube version (e.g., "20.12.46")
  - `2026-02-15 23:17:23 UTC` → Timestamp of last update (e.g., "2025-06-18 16:11:26 UTC")
  - APKMirror URLs → Automatically updates hardcoded dashed versions (e.g., "youtube-19-43-41-release" → "youtube-20-12-46-release")
- Manages git branches (works on `docs-base`, commits to `main`)
- Exports outputs for GitHub Actions

### API Endpoints Used

- `https://api.revanced.app/v4/patches/list` - List of all patches with compatibility info
- `https://api.revanced.app/v4/patches/version` - Latest patches version

### Usage

```bash
# Using the wrapper script (recommended)
./python/run_updater.sh           # Normal run
./python/run_updater.sh --dry-run # Test without making changes
./python/run_updater.sh --force   # Force update

# Or run directly
cd /path/to/repository
pip install -r python/requirements.txt
python3 python/update_versions.py
```

### Environment Variables

- `GITHUB_ACTIONS=true` - Enables GitHub Actions mode
- `GITHUB_OUTPUT` - File path for GitHub Actions outputs
- `EVENT=workflow_dispatch` - Forces update when manually triggered
- `FORCE=1` - Forces update in local mode

### Git Workflow

1. Ensures it's running on `docs-base` branch
2. Fetches latest data from API
3. Updates placeholders in all markdown files
4. Commits changes to `main` branch
5. Returns to `docs-base` branch

### Outputs (GitHub Actions)

- `modified` - Whether files were updated (`true`/`false`)
- `youtube_version` - Latest supported YouTube version
- `last_update` - Timestamp of the update

## Testing

### Test API connectivity:
```bash
python3 test_api.py
```

### Dry-run test (no file modifications):
```bash
python3 test_dry_run.py
```

## Migration from checkReVancedVersion.py

The new script (`update_versions.py`) replaces `checkReVancedVersion.py` with these improvements:

1. **Updated API**: Uses v4 API instead of deprecated v2
2. **Simplified structure**: Cleaner, more maintainable code
3. **Git integration**: Handles branch management automatically
4. **Better error handling**: More robust error handling and logging
5. **Flexible placeholders**: Supports multiple placeholder types
6. **Modern Python**: Uses timezone-aware datetime objects

## Configuration Files

The script uses the existing configuration structure:

- `.conf/python/update.state` - Tracks last update and data
- `.conf/python/update.lut.json` - Package name to common name lookup
- `.conf/python/update.template` - Template for version table (legacy)

## Dependencies

- `requests` - For API calls
- `packaging` - For version comparison
- `git` - Must be available in PATH for git operations

## GitHub Actions Integration

### Quick Setup
1. Copy `new-workflow.yml` to `.github/workflows/update-versions.yml`
2. Disable the old workflow (`version-and-lastCheck-bump.yml`)
3. Ensure `docs-base` branch exists
4. Configure secrets if using Discord notifications

### Workflow Features
- **Automatic scheduling**: Runs every 30 minutes (configurable)
- **Manual triggering**: Can be triggered manually with force option
- **Branch management**: Automatically handles `docs-base` ↔ `main` workflow
- **Website rebuilding**: Triggers retype rebuild when versions change
- **Notifications**: Discord webhook support for updates and failures
- **Error handling**: Creates GitHub issues for failures

### Required Secrets (Optional)
- `DISCORD_WEBHOOK` - For Discord notifications

## Migration from Old System

See `MIGRATION.md` for detailed instructions on migrating from `checkReVancedVersion.py` to the new system.
