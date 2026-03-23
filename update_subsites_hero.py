import os
import re

brands = {
    "beet": {"name": "beet music", "color": "#E97132"},
    "kapp": {"name": "kapp mobile apps", "color": "#156082"},
    "kask": {"name": "kask online shop", "color": "#2d5a27"},
    "kovr": {"name": "kovr fashion", "color": "#5a5a2d"},
    "moov": {"name": "moov videos", "color": "#2d2d5a"},
    "klab": {"name": "klab consultancy", "color": "#5a2d5a"},
    "korr": {"name": "korr influencers", "color": "#2d5a5a"},
    "lask": {"name": "lask lawyers", "color": "#5a2d2d"},
    "pai": {"name": "pai ai agents", "color": "#5a5a5a"},
    "simpl": {"name": "simpl wedsites", "color": "#808080"}
}

source_file = "docs/Website/github-pages-deploy/index.html"

with open(source_file, "r") as f:
    content = f.read()

for brand_key, brand_info in brands.items():
    print(f"Updating {brand_key}...")
    
    brand_dir = f"docs/Website/github-pages-deploy/{brand_key}"
    os.makedirs(brand_dir, exist_ok=True)
    
    # Start with the main index.html content
    brand_content = content
    
    # 1. Update the brand wordmark in header (first occurrence)
    first_letter = brand_key[0]
    rest = brand_key[1:]
    colored_brand_display = f'<span style="color: {brand_info["color"]};">{first_letter}</span>{rest}'
    
    # Replace the brand wordmark (slakka) with the initiative name
    brand_content = brand_content.replace(
        '<span class="brand-wordmark" data-slakka-wordmark>sla<span style="color: #E97132;">k</span>ka</span>',
        f'<span class="brand-wordmark" data-slakka-wordmark>{colored_brand_display}</span>'
    )
    
    # 2. Update the hero text h1 to use the initiative name
    # Pattern: <h1><span data-slakka-wordmark>slakka</span> build solutions with awesome simplicity and intelligence.</h1>
    # We want: <h1><span data-slakka-wordmark>[initiative name]</span> build solutions with awesome simplicity and intelligence.</h1>
    # But the initiative name should have the first letter colored
    
    # Extract the initiative name for display in hero text (lowercase, first letter colored)
    initiative_name_lower = brand_key  # e.g., "beet"
    initiative_display = f'<span style="color: {brand_info["color"]};">{initiative_name_lower[0]}</span>{initiative_name_lower[1:]}'
    
    # Replace the hero text
    old_hero_pattern = r'<h1><span data-slakka-wordmark>sla<span style="color: #E97132;">k</span>ka</span> build solutions with awesome simplicity and intelligence\.</h1>'
    new_hero = f'<h1><span data-slakka-wordmark>{initiative_display}</span> build solutions with awesome simplicity and intelligence.</h1>'
    brand_content = re.sub(old_hero_pattern, new_hero, brand_content)
    
    # 3. Update the "Our Offers" section text to be initiative-specific
    # Replace "Stuff made by our sla<span style='color: #E97132;'>k</span>kas that will make you smile."
    # with something like "Stuff made by our [initiative] that will make you smile."
    
    # For the initiative name in the offers text, we want lowercase with first letter colored
    initiative_offer_name = f'<span style="color: {brand_info["color"]};">{initiative_name_lower[0]}</span>{initiative_name_lower[1:]}'
    
    old_offers_text = r'Stuff made by our sla<span style="color: #E97132;">k</span>kas that will make you smile\.'
    new_offers_text = f'Stuff made by our {initiative_offer_name} that will make you smile.'
    brand_content = re.sub(old_offers_text, new_offers_text, brand_content)
    
    # Also update the Services panel text
    old_services_text = r'Things our sla<span style="color: #E97132;">k</span>kas can do to make your life shine\.'
    new_services_text = f'Things our {initiative_offer_name} can do to make your life shine.'
    brand_content = re.sub(old_services_text, new_services_text, brand_content)
    
    # 4. Adjust all paths to be relative from sub-site perspective
    # Since we're now in a subdirectory (/brand/), we need to go up one level for most things
    
    # Assets: change "assets/" to "../assets/"
    brand_content = brand_content.replace('href="assets/', 'href="../assets/')
    brand_content = brand_content.replace('src="assets/', 'src="../assets/')
    
    # Pages: 
    brand_content = brand_content.replace('href="index.html"', 'href="../index.html"')
    brand_content = brand_content.replace('href="about.html"', 'href="../about.html"')
    brand_content = brand_content.replace('href="contact.html"', 'href="../contact.html"')
    brand_content = brand_content.replace('href="products.html"', 'href="../products.html"')
    brand_content = brand_content.replace('href="services.html"', 'href="../services.html"')
    brand_content = brand_content.replace('href="news.html"', 'href="../news.html"')
    
    # 5. Fix the navigation links
    # In the main index.html, we have links like:
    # <a href="beet/index.html">... (link to sub-site)
    # From within the sub-site, this should be just "index.html" (current directory)
    for other_brand in brands.keys():
        if other_brand == brand_key:
            # Link to self: change "beet/index.html" to "index.html"
            brand_content = brand_content.replace(f'href="{other_brand}/index.html"', 'href="index.html"')
        else:
            # Link to other sub-site: change "beet/index.html" to "../other_brand/index.html"
            brand_content = brand_content.replace(f'href="{other_brand}/index.html"', f'href="../{other_brand}/index.html"')
    
    # Write the file
    with open(f"{brand_dir}/index.html", "w") as f:
        f.write(brand_content)

print("All brand sub-sites updated with initiative-specific hero text!")