import sys

def cd(current_path, new_path):
    # Split the paths into parts
    current_parts = current_path.split('/')
    new_parts = [part for part in new_path.split('/') if part != '']

    # Process each part of the new path
    for part in new_parts:
        if part == '..':  # Move up in the directory tree
            if len(current_parts) > 1:  # Can't move up from root
                current_parts.pop()
        elif part != '.':  # Current directory, do nothing
            current_parts.append(part)

    # Reconstruct the new valid path
    new_valid_path = '/' + '/'.join(current_parts)
    return new_valid_path

# Read paths from command line arguments
if len(sys.argv) == 3:
    current_dir = sys.argv[1]
    new_dir = sys.argv[2]
    print(cd(current_dir, new_dir))
else:
    print("Error: Two path strings are required.")