!pip install pdf2image
import os
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# 设置PDF和图片文件的目录
pdf_folder = './docs'
output_folder = './result/'

# 创建一个用于保存所有文本的列表
all_text = []

# 遍历文件夹内所有PDF文件
for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder, filename)
        print(f'正在处理文件: {pdf_path}')

        # 使用pdf2image库将PDF文件的所有页转为PNG图片
        images = convert_from_path(pdf_path)
        for i, image in enumerate(images):
            image_path = os.path.join(output_folder, f'{filename.replace(".pdf", "")}_{i}.png')
            image.save(image_path, 'PNG')
            print(f'图片已保存至: {image_path}')

            # 使用pytesseract库将图片识别为文本
            img = Image.open(image_path)
            text = pytesseract.image_to_string(img, lang='eng')

            # 保存文本文件
            text_path = os.path.join(output_folder, f'{filename.replace(".pdf", "")}_{i}.txt')
            with open(text_path, 'w') as f:
                f.write(text)
            print(f'文本已保存至: {text_path}')

            # 将文本添加到列表中
            all_text.append(text)

# 创建一个新的TXT文件，将所有文本写入到这个文件中
combined_text_path = os.path.join(output_folder, 'combined.txt')
with open(combined_text_path, 'w') as f:
    f.write('\n'.join(all_text))
print(f'所有文本已合并并保存至: {combined_text_path}')



# Also, save the combined text to a .md file
combined_md_path = os.path.join(output_folder, 'combined.md')
with open(combined_md_path, 'w') as md_file:
    md_file.write('\n'.join(all_text))
print(f'All text combined and saved to MD file: {combined_md_path}')
