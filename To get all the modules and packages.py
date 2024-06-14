import sys
import pkgutil

# List all modules and packages
modules = list(pkgutil.iter_modules())
print(len(modules))

# Display the names of the modules
for module in modules:
    print(module.name)
