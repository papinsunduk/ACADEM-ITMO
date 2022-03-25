import json


def convert(in_file_path, out_file_path):

    def txt_json(s):
        fdjson = {'spans': [{'text': ''}]}
        ct = 0
        i = 0
        while i < len(s):
            if s[i] == '<' and s[i + 1] != 'l':
                if s[i + 1] != '/':
                    color = '#' + s[i+1:i+7]
                    if i != 0:
                        ct += 1
                        fdjson['spans'].append({'text': ''})
                    fdjson['spans'][ct].update({'color': color})
                    i += 7
                else:
                    ct += 1
                    fdjson['spans'].append({'text': ''})
                    i += 2
            else:
                fdjson['spans'][ct]['text'] += s[i]
            i += 1

        for span in fdjson['spans']:
            while '<ln>' in span['text']:
                i = span['text'].index('<')
                span['text'] = span['text'][:i] + '<' + span['text'][i + 4:]

        return fdjson

    def json_bin():
        pass

    def bin_txt():
        pass

    if in_file_path[-5:] == out_file_path[-5:]:
        file = open(in_file_path, 'r')
        data = file.read()
        with open(out_file_path, 'w') as output:
            output.write(data)

    if in_file_path[-3:] == 'txt':
        file = open(in_file_path, 'r')
        data = file.readlines()
        if data[-1][-1] == '\n':
            data.append('')
        if out_file_path[-4:] == 'json':
            with open(out_file_path, 'w') as output:
                for line in data:
                    json.dump(txt_json(line), output)

