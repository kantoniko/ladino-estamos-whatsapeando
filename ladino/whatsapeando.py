from yaml import safe_load
import datetime
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
    img_files = set(os.listdir(os.path.join(root, 'img')))
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
        img_filename = yaml_filename.replace('.yaml', '.jpeg')
        if img_filename in img_files:
            data['img'] = img_filename
        #print(data['text'])
        if 'text' in data:
            data['teksto'] = [{
                'ladino': data['text'].strip(),
                'ebreo': '',
            }]
            entries.append(data)
        elif 'teksto' in data:
            for entry in data['teksto']:
                assert 'ladino' in entry, f"ladino field is missing in file {yaml_filename}"
                assert 'ebreo' in entry, f"ebreo field is missing in file {yaml_filename}"
            entries.append(data)
        else:
            raise Exception('No text and no teksto')

        assert re.search(r'^\d\d\d\d\.\d\d\.\d\d$', data['data'], re.ASCII)
        match = re.search(r'^(\d\d\d\d\.\d\d\.\d\d)( \d\d:\d\d:\d\d)?$', data['pub'], re.ASCII)
        assert match
        data['date'] = match.group(1)

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
    print(f"All read properly.")
    print(f"Last published:   {entries[-1]['pub']}")
    print(f"Today is          {str(datetime.date.today()).replace('-', '.')}")

