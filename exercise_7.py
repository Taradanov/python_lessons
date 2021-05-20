import json


def parse_str(parsed_text, new_dict):
    parsed_text = parsed_text.replace('  ', '')
    parsed_text = parsed_text.replace('\n', '')
    split_text = parsed_text.split(' ')

    org = {'name': split_text[0], 'form': split_text[1], 'profit': int(split_text[2]), 'costs': int(split_text[3])}
    new_dict[split_text[0]] = org


if __name__ == '__main__':
    with open('text_for_ex7.txt', mode='r', encoding='utf-8') as file_1, \
            open('data.json', mode='w', encoding='utf-8') as json_file:
        dict_with_firms = {}
        while True:

            text = file_1.readline()

            if not text:
                break
            if text == '\n':
                continue
            parse_str(text, dict_with_firms)

        average_profit = 0 if len(dict_with_firms) == 0 else sum(
            [val[1]['profit'] - val[1]['costs'] for val in dict_with_firms.items()]) / len(dict_with_firms)

        list_with_data = [
            {key: val['profit'] - val['costs'] for key, val in dict_with_firms.items()},
            {'average_profit': average_profit}
        ]

        print(list_with_data)
        json.dump(list_with_data, json_file)
