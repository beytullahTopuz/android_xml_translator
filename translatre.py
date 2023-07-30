import xml.etree.ElementTree as ET
from googletrans import Translator

# XML dosyası adı
folder_path = "C:\\Users\\beytu\\Desktop\\python\\"
xml_file_name = "strings.xml"
language_code = 'es'
translated_file = xml_file_name + language_code

# XML dosyasını ağaç yapısına yükle
tree = ET.parse(folder_path + xml_file_name)
root = tree.getroot()

# Google Translate API'si için çeviri aracını oluştur
translator = Translator()

itemCount = 0
# Her bir metin dizisi için Felemenkçe çeviri yap
for string in root.iter('string'):
    print(itemCount)
    itemCount = itemCount + 1
    original_text = string.text

    # Skip translating if the translateable property is false
    if string.get('translatable') == 'false':
        print("Translation skipped for string -translatable=false :", original_text)
        continue

    try:
        translated_text = translator.translate(original_text, dest = language_code).text
        string.text = translated_text
        print("data : " + original_text + " | " + translated_text)
    except Exception as e:
        print("Error:", e)
        # In case of error, skip translation keeping the original text
        string.text = original_text
        print("Translation skipped for string:", original_text)


#Create a new XML with translated texts
tree.write((folder_path + translated_file), encoding="utf-8", xml_declaration=True)
print(translated_file +" is created")