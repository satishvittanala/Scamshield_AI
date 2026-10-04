import re
import glob

for f in sorted(glob.glob('frontend/*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Extract nav
    nav_match = re.search(r'<nav[^>]*>.*?</nav>', content, re.DOTALL)
    if nav_match:
        nav_html = nav_match.group(0)
        items = re.findall(r'<li class="nav-item">(.*?)</li>', nav_html, re.DOTALL)
        print(f, f"({len(items)} items)")
        for it in items:
            href_m = re.search(r'href="([^"]*)"', it)
            href = href_m.group(1) if href_m else 'None'
            is_active = 'active' in re.search(r'class="([^"]*)"', it).group(1) if re.search(r'class="([^"]*)"', it) else False
            text = re.sub(r'<[^>]*>', '', it).strip()
            print(f"   [{ 'ACTIVE  ' if is_active else 'inactive' }] {text} -> {href}")
        print()
    else:
        print(f, "NO NAVBAR\n")
