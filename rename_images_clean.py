from pathlib import Path

mapping = {
    'interior-home-painting.jpg': 'berkley-mi-interior-painting.jpg',
    'interior-metamora.webp': 'beverly-hills-mi-interior-painting.webp',
    'interior-painting-2-700x809-1.webp': 'bingham-farms-mi-interior-painting.webp',
    'interior-rochester-hills.webp': 'birmingham-mi-interior-painting.webp',
    'kitchen-painting-rochester-hills.webp': 'bloomfield-hills-mi-interior-kitchen-painting.webp',
    'exterior-shelby-township.jpg': 'clawson-mi-exterior-painting.jpg',
    'before-painting-rochester-hills.png': 'clinton-township-mi-exterior-before-painting.png',
    'after.jpg': 'franklin-mi-after-painting.jpg',
    'Metamora Home with Exterior Painting.webp': 'grosse-pointe-farms-mi-exterior-painting.webp',
    'dfd6c3b2-6061-4c22-b6d2-0708df2de25f.jpeg': 'grosse-pointe-mi-painting.jpeg',
    'd64f374c-1186-4cbb-ab12-5cfddb3d5542.jpeg': 'grosse-pointe-shores-mi-painting.jpeg',
    '3170f64c-f6d6-4d73-9191-77652509a359.jpeg': 'grosse-pointe-woods-mi-painting.jpeg',
    '2b0b564b-7b5d-4ce9-b471-741c2aca30b5.jpeg': 'huntington-woods-mi-painting.jpeg',
    '40b033c6-6ad1-4340-9eff-f2f274476c78.jpeg': 'lake-orion-mi-painting.jpeg',
    '6c7f9afc-a373-4556-8c35-1a7532120b3f.jpeg': 'lathrup-village-mi-painting.jpeg',
    '7cb24696-b86b-4d83-9b94-8366f7f300b8.jpeg': 'macomb-township-mi-painting.jpeg',
    '807f3e7f-43f0-40ff-ae6b-dc7496adf15e.jpeg': 'metamora-mi-painting.jpeg',
    '75df44c5-ed96-4a41-a1c1-6a44fcee0833.jpeg': 'new-baltimore-mi-painting.jpeg',
    '9dae1d62-12d7-4fe5-9bb7-c213a5efe4d5.jpeg': 'oakland-township-mi-painting.jpeg',
    '7254bc44-cd5f-4132-abd1-a201d90644a0.jpeg': 'orchard-lake-mi-painting.jpeg',
    '518954623_674558782253543_4372270863981000647_n.jpg': 'oxford-mi-painting.jpg',
    '660450000_1253721433616946_8894774063789859336_n.jpg': 'pleasant-ridge-mi-painting.jpg',
    '697065598_914404568268962_5420312407982393630_n.jpg': 'rochester-hills-mi-painting.jpg',
    '697196527_914404811602271_4944136717320278659_n.jpg': 'rochester-mi-painting.jpg',
    '457161063_442534468789310_1526689513949087024_n.jpg': 'romeo-mi-painting.jpg',
    '477254987_1129838969152447_1914040403052451525_n.jpg': 'royal-oak-mi-painting.jpg',
    '529949469_694257273617027_6124888373376448099_n.jpg': 'shelby-township-mi-painting.jpg',
    '3423baa3-1138-4688-8258-47d0aa472bba.jpeg': 'sterling-heights-mi-painting.jpeg',
    '23bd54b6-8c47-479a-961f-808117fd732c.jpeg': 'sylvan-lake-mi-painting.jpeg',
    '06c058d2-a868-4562-94c1-cc957b060019.jpeg': 'troy-mi-painting.jpeg',
    '5b26406d-e9e7-4b8d-b48c-ee4df89eebd8.jpeg': 'utica-mi-painting.jpeg',
    '14cfd8c4-d902-4189-b972-e1fa45eaa4e9.jpeg': 'washington-township-mi-painting.jpeg'
}

img_dir = Path('images')
for old, new in mapping.items():
    old_path = img_dir / old
    new_path = img_dir / new
    if not old_path.exists():
        raise FileNotFoundError(f'Missing source image: {old_path}')
    if new_path.exists():
        raise FileExistsError(f'Target already exists: {new_path}')

html_files = list(Path('.').glob('*.html'))
for hf in html_files:
    text = hf.read_text(encoding='utf-8')
    new_text = text
    for old, new in mapping.items():
        new_text = new_text.replace(f'images/{old}', f'images/{new}')
    if new_text != text:
        hf.write_text(new_text, encoding='utf-8')

for old, new in mapping.items():
    (img_dir / old).rename(img_dir / new)

print('Renamed', len(mapping), 'image files')
