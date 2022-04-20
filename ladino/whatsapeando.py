from yaml import safe_load
import re
import os

def get_messages():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #print(root)
    entries = []
    yaml_files = os.listdir(os.path.join(root, 'text'))
    #print(yaml_files)
    ogg_files = set(os.listdir(os.path.join(root, 'sound')))
    #print(ogg_files)
    pubs = set()
    for yaml_filename in yaml_files:
        with open(os.path.join(root, 'text', yaml_filename)) as fh:
            data = safe_load(fh)
        ogg_filename = yaml_filename.replace('.yaml', '.ogg')
        if ogg_filename not in ogg_files:
            raise Exception(f"sound file {ogg_filename} does not exist")
        ogg_files.remove(ogg_filename)
        data['filename'] = ogg_filename
        data['page'] = yaml_filename.replace('.yaml', '')
        #print(data['text'])
        data['text'] = data['text'].strip()
        entries.append(data)
        assert re.search(r'^\d\d\d\d\.\d\d\.\d\d$', data['data'], re.ASCII)
        assert re.search(r'^\d\d\d\d\.\d\d\.\d\d$', data['pub'], re.ASCII)

        if data['pub'] in pubs:
            raise Exception(f"Duplicate publication date {data['pub']}")
        pubs.add(data['pub'])

        assert len(data['titulo']) > 5
    if ogg_files:
        raise Exception(f"Some sound files {ogg_files} are not in use")

    return sorted(entries, key=lambda entry: entry['pub'])


if __name__ == '__main__':
    entries = get_messages()
    #print(entries)
    print(f"All read properly. Last published: {entries[-1]['pub']}")

