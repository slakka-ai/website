import os
import re

# Define the root directory
root_dir = "docs/Website/github-pages-deploy"

# List of subdirectories (brands)
brands = ["beet", "kapp", "kask", "klab", "korr", "kovr", "lask", "moov", "pai", "simpl"]

def get_header(root_path):
    with open(os.path.join(root_dir, "header.html"), "r") as f:
        content = f.read()
    # Replace placeholders if any (though header.html seems to use absolute paths)
    return content

def get_footer(root_path):
    with open(os.path.join(root_dir, "footer.html"), "r") as f:
        content = f.read()
    # Inject root_path if needed, but for now assuming it uses root_path format
    return content.replace("{root_path}", root_path)

# Process all files
all_files = [os.path.join(root_dir, "index.html")]
for brand in brands:
    all_files.append(os.path.join(root_dir, brand, "index.html"))
    all_files.append(os.path.join(root_dir, brand, "about.html"))
    all_files.append(os.path.join(root_dir, brand, "products.html"))

for file_path in all_files:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, "r") as f:
        content = f.read()
        
    # Determine root_path
    if "index.html" == os.path.basename(file_path) and os.path.dirname(file_path) == root_dir:
        root_path = ""
    else:
        root_path = "../"
        
    new_header = get_header(root_path)
    new_footer = get_footer(root_path)
    
    content = re.sub(r'<header class="site-header">.*?</header>', new_header, content, flags=re.DOTALL)
    content = re.sub(r'<footer class="site-footer">.*?</footer>', new_footer, content, flags=re.DOTALL)
    
    with open(file_path, "w") as f:
        f.write(content)
    print(f"Updated {file_path}")
