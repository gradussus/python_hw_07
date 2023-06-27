import os
import re
import shutil

extensions = {
    'images': ('jpeg', 'png', 'jpg', 'svg'),
    'videos': ('avi', 'mp4', 'mov', 'mkv'),
    'documents': ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'),
    'music': ('mp3', 'ogg', 'wav', 'amr'),
    'archives': ('zip', 'gz', 'tar')
    }

unknown_extensions = set()
known_extensions = set()

def goClean():
    initial_directory = os.getcwd()
    walk(initial_directory, initial_directory)

    print('{:^30}{}'.format('Unknown_extensions:', unknown_extensions))
    print('{:^30}{}'.format('Known_extensions:', known_extensions))


    if os.path.exists(os.path.join(initial_directory, 'images')):
        print('{:^30}{}'.format('Images:', os.listdir(os.path.join(initial_directory, 'images') )))

    if os.path.exists(os.path.join(initial_directory, 'videos')):
        print('{:^30}{}'.format('Videos:', os.listdir(os.path.join(initial_directory, 'videos') )))

    if os.path.exists(os.path.join(initial_directory, 'documents')):
        print('{:^30}{}'.format('Documents:', os.listdir(os.path.join(initial_directory, 'documents') )))

    if os.path.exists(os.path.join(initial_directory, 'music')):
        print('{:^30}{}'.format('Music:', os.listdir(os.path.join(initial_directory, 'music') )))

    if os.path.exists(os.path.join(initial_directory, 'archives')):
        print('{:^30}{}'.format('Archives:', os.listdir(os.path.join(initial_directory, 'archives') )))

    if os.path.exists(os.path.join(initial_directory, 'other')):
        print('{:^30}{}'.format('Other:', os.listdir(os.path.join(initial_directory, 'other') )))

def transliteration (text):

    dict = {

        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
        'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
        'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
        'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
        'Ц': 'C', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E',
        'Ю': 'YU', 'Я': 'YA', 'Ї': 'YI', 'ї': 'yi', 'Є': 'YE', 'є': 'ye', 'І': 'I', 'і': 'i'
    }
    newName = ''
    for letter in text:
        if re.match(r'[a-zA-Z0-9.]', letter):
            newName += letter
        elif letter in dict:
            newName += dict[letter]
        else:
            newName += '_'
    return newName

def move_file(old_folder, filename, init_path ):
 

    if filename.endswith(extensions['images']):
         
        known_extensions.add(filename.split('.')[-1])
            
        old_file = os.path.join(old_folder, filename)
        new_file = os.path.join(init_path, 'images' , transliteration(filename))

        if not os.path.exists(os.path.join(init_path, 'images')):
            os.makedirs(os.path.join(init_path, 'images'))
                
        os.rename(old_file, new_file)

    elif filename.endswith(extensions['videos']):
         
        known_extensions.add(filename.split('.')[-1])
            
        old_file = os.path.join(old_folder, filename)
        new_file = os.path.join(init_path, 'videos' , transliteration(filename))

        if not os.path.exists(os.path.join(init_path, 'videos')):
            os.makedirs(os.path.join(init_path, 'videos'))
    
        os.rename(old_file, new_file)

    elif filename.endswith(extensions['documents']):
         
        known_extensions.add(filename.split('.')[-1])
            
        old_file = os.path.join(old_folder, filename)
        new_file = os.path.join(init_path, 'documents' , transliteration(filename))

        if not os.path.exists(os.path.join(init_path, 'documents')):
            os.makedirs(os.path.join(init_path, 'documents'))

        os.rename(old_file, new_file)

    elif filename.endswith(extensions['music']):
         
        known_extensions.add(filename.split('.')[-1])
            
        old_file = os.path.join(old_folder, filename)
        new_file = os.path.join(init_path, 'music' , transliteration(filename))

        if not os.path.exists(os.path.join(init_path, 'music')):
            os.makedirs(os.path.join(init_path, 'music'))

                
        os.rename(old_file, new_file)

    elif filename.endswith(extensions['archives']):
        known_extensions.add(filename.split('.')[-1])

        shutil.unpack_archive((os.path.join(old_folder, filename)), (os.path.join(init_path, 'archives', transliteration(filename).split('.')[0])) )

    else:
        unknown_extensions.add(filename.split('.')[-1])

        old_file = os.path.join(old_folder, filename)
        new_file = os.path.join(init_path, 'other' , transliteration(filename))

        if not os.path.exists(os.path.join(init_path, 'other')):
            os.makedirs(os.path.join(init_path, 'other'))

                
        os.rename(old_file, new_file)

def walk (path, init_path):
    if os.listdir(path) == []:
        os.rmdir(path)

    else:

        for item in os.listdir(path):
            if item in extensions or item == 'other':
                continue
            
            if os.path.isdir(os.path.join(path, item)):
                walk(os.path.join(path, item), init_path)

            else:
                move_file(path, item, init_path)

