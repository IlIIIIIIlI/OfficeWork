!pip install PyPDF2
import PyPDF2

def extract_annotations_from_pdf(pdf_path, output_txt_path):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        with open(output_txt_path, 'w', encoding='utf-8') as output:
            for page in reader.pages:
                if page.get('/Annots'):
                    for annotation_ref in page['/Annots']:
                        annotation = annotation_ref.get_object()
                        content = annotation.get('/Contents')
                        if content:
                            output.write(content + "\n")

pdf_path = './LLL.pdf'
output_txt_path = 'output_comments.txt'
extract_annotations_from_pdf(pdf_path, output_txt_path)
