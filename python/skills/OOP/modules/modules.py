# Modules are breaking up one large file into smaller, easier to manage files. These smaller files are called modules.

import converters                   # Call the module by importing it's name (without the .py)

print(converters.kg_to_lbs(25))     # Now just use the function normally
print(converters.lbs_to_kg(75))