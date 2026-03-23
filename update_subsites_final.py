import os
import re

brands = {
    "beet": "#E97132",
    "kapp": "#156082",
    "kask": "#2d5a27",
    "kovr": "#5a5a2d",
    "moov": "#2d2d5a",
    "klab": "#5a2d5a",
    "korr": "#2d5a5a",
    "lask": "#5a2d2d",
    "pai": "#5a5a5a",
    "simpl": "#808080"
}

source_file = "docs/Website/github-pages-deploy/index.html"

with open(source_file, "r") as f:
    content = f.read()

for brand, color in brands.items():
    print(f"Updating {brand}...")
    
    # Create brand directory
    brand_dir = f"docs/Website/github-pages-deploy/{brand}"
    os.makedirs(brand_dir, exist_ok=True)
    
    # Start with the main index.html content
    brand_content = content
    
    # 1. Update the brand wordmark in header (first occurrence)
    # Find the brand wordmark and replace with colored initiative name
    first_letter = brand[0]
    rest = brand[1:]
    colored_brand_name = f'{first_letter.upper()}{rest}'  # Keep first letter capitalized for display?
    # Actually looking at the examples, it seems like they want the full name lowercase with first letter colored
    # Like: <span style="color: #E97132;">b</span>eet
    colored_brand_display = f'<span style="color: {color};">{first_letter}</span>{rest}'
    
    # Replace the brand wordmark (slakka) with the initiative name
    # We need to be careful to only replace the one in the header
    brand_content = brand_content.replace(
        '<span class="brand-wordmark" data-slakka-wordmark>sla<span style="color: #E97132;">k</span>ka</span>',
        f'<span class="brand-wordmark" data-slakka-wordmark>{colored_brand_display}</span>'
    )
    
    # 2. Adjust all paths to be relative from sub-site perspective
    # Since we're now in a subdirectory (/brand/), we need to go up one level for most things
    
    # Assets: change "assets/" to "../assets/"
    brand_content = brand_content.replace('href="assets/', 'href="../assets/')
    brand_content = brand_content.replace('src="assets/', 'src="../assets/')
    
    # Pages: 
    # - index.html -> ../index.html (to go back to main site)
    # - about.html -> ../about.html
    # - contact.html -> ../contact.html
    # - products.html -> ../products.html
    # - services.html -> ../services.html
    # - news.html -> ../news.html
    brand_content = brand_content.replace('href="index.html"', 'href="../index.html"')
    brand_content = brand_content.replace('href="about.html"', 'href="../about.html"')
    brand_content = brand_content.replace('href="contact.html"', 'href="../contact.html"')
    brand_content = brand_content.replace('href="products.html"', 'href="../products.html"')
    brand_content = brand_content.replace('href="services.html"', 'href="../services.html"')
    brand_content = brand_content.replace('href="news.html"', 'href="../news.html"')
    
    # 3. Fix the navigation links
    # In the main index.html, we have links like:
    # <a href="beet/index.html">... (link to sub-site)
    # From within the sub-site, this should be just "index.html" (current directory)
    for other_brand in brands.keys():
        if other_brand == brand:
            # Link to self: change "beet/index.html" to "index.html"
            brand_content = brand_content.replace(f'href="{other_brand}/index.html"', 'href="index.html"')
        else:
            # Link to other sub-site: change "beet/index.html" to "../other_brand/index.html"
            brand_content = brand_content.replace(f'href="{other_brand}/index.html"', f'href="../{other_brand}/index.html"')
    
    # Write the file
    with open(f"{brand_dir}/index.html", "w") as f:
        f.write(brand_content)

print("All brand sub-sites updated!")