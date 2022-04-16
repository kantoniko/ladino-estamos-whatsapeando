from yaml import safe_load
import os

def get_messages():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #print(root)
    entries = []
    yaml_files = os.listdir(os.path.join(root, 'text'))
    #print(yaml_files)
    ogg_files = set(os.listdir(os.path.join(root, 'sound')))
    #print(ogg_files)
    for yaml_filename in yaml_files:
        with open(os.path.join(root, 'text', yaml_filename)) as fh:
            data = safe_load(fh)
        ogg_filename = yaml_filename.replace('.yaml', '.ogg')
        if ogg_filename not in ogg_files:
            raise Exception(f"sound file {ogg_filename} does not exist")
        ogg_files.remove(ogg_filename)
        data['filename'] = ogg_filename
        #print(data['text'])
        data['text'] = data['text'].strip()
        entries.append(data)
    if ogg_files:
        raise Exception(f"Some sound files {ogg_files} are not in use")

    return entries


if __name__ == '__main__':
    entries = get_messages()
    #print(entries)

