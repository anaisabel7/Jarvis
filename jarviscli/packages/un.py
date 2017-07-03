from colorama import Fore


def format_information(json_info):
    formated_list = json_info
    return formated_list


def request_information(keyword):
    json_info = keyword
    return json_info


def obtain_keyword(s):
    # keyword must be the 1st word after 'un'
    words = s.strip().split()
    keyword = words[0]
    return keyword


def main(self, s):
    keyword = obtain_keyword(s)

    json_info = request_information(keyword)

    formated_list = format_information(json_info)

    for string in formated_list:
        print_say(string, self, Fore.BLUE)
