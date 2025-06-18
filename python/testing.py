import sys
sys.path.append('python')
from new_update_versions import ReVancedVersionUpdater
import json

updater = ReVancedVersionUpdater()
patches_data, version_data = updater.fetch_api_data()
package_versions = updater.parse_patches_data(patches_data)

# Read state file
with open('.conf/python/update.state', 'r') as f:
    last_updated = int(f.readline().strip())
    last_result = f.read().strip()

# Generate current result
current_result = json.dumps(package_versions, sort_keys=True)

print('=== CURRENT DATA ===')
print(current_result[:200] + '...')
print()
print('=== STATE FILE DATA ===') 
print(last_result[:200] + '...')
print()
print('=== EQUAL? ===')
print(current_result == last_result)
print()
print('=== LENGTH COMPARISON ===')
print(f'Current: {len(current_result)}')
print(f'State: {len(last_result)}')