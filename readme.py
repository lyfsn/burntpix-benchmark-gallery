import os

def generate_readme(img_folder, readme_path):
    img_files = [f for f in os.listdir(img_folder) if f.endswith('.svg')]
    
    img_files.sort()
    
    with open(readme_path, 'w') as readme:
        readme.write('# Image Gallery\n\n')
        
        num_per_row = 4
        for i in range(0, len(img_files), num_per_row):
            readme.write('<p align="center">\n')
            for img_file in img_files[i:i+num_per_row]:
                readme.write(f'  <img src="imgs/{img_file}" width="200" />\n')
            readme.write('</p>\n\n')

def main():
    img_folder = 'imgs'
    readme_path = 'README.md'
    
    generate_readme(img_folder, readme_path)
    print(f'Generated {readme_path} with {len(os.listdir(img_folder))} images.')

if __name__ == '__main__':
    main()