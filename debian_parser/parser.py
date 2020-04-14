import time
import itertools


class PackagesParser(object):
    def __init__(self, raw_packages_file):
        data_raw = raw_packages_file.splitlines()

        if data_raw[0] != "":
            data_raw.insert(0, "")

        self._data_splitted = data_raw

    def _splitted_lines(self):
        return self._data_splitted.count("")

    def _parse_to_seperated_lists(self):

        # TODO: PLEASE REWRITE THIS IS
        # IS EXTREMELY UGLY
        #
        # It's basically just splitting the .splitlines()
        # into indiv. list seperated by < "" >

        size_of_splitlines = len(self._data_splitted)

        get_new_line_indexes = [
            index + 1
            for index, index_value in enumerate(self._data_splitted)
            if index_value == ""
        ]

        incomplete_data = [
            self._data_splitted[index_to_start:index_to_end]
            for index_to_start, index_to_end in zip(
                [0] + get_new_line_indexes,
                get_new_line_indexes
                + (
                    [size_of_splitlines]
                    if get_new_line_indexes[-1] != size_of_splitlines
                    else []
                ),
            )
        ]

        for sub_list in incomplete_data:
            for element_index, element in enumerate(sub_list):
                if element == "":
                    sub_list.pop(element_index)

        for sub_list_element, sub_list in enumerate(incomplete_data):
            if sub_list == []:
                incomplete_data.pop(sub_list_element)

        self._data = incomplete_data
        return self._data

    def _parse_string(self, string):

        if string == "":
            return False

        selected_string_split = string.split()
        selected_string_top = selected_string_split[0]
        selected_string_top_chars = [x for x in selected_string_top]

        if selected_string_top_chars.count(":") == 1:
            if "http" in selected_string_top:
                return False
            return True

        return False

    def _parse_to_dict(self):
        end_result = []

        for element_list_index, element_list in enumerate(self._data):

            selected_child = []
            for selected_elements_index, selected_element in enumerate(element_list):

                selected_element_check = self._parse_string(selected_element)
                if selected_element_check == True:

                    selected_element_splitted = selected_element.split()
                    selected_element_key = selected_element_splitted[0]
                    selected_element_value = " ".join(selected_element_splitted[1:])

                    # check if the next values should be appended.

                    for inter_step in itertools.count(selected_elements_index + 1):
                        try:
                            selected_element_future = element_list[inter_step]
                            future_index_to_check = self._parse_string(
                                selected_element_future
                            )
                            if future_index_to_check == True:
                                break
                            else:
                                selected_element_value += " " + element_list[inter_step]
                        except IndexError:
                            break

                    selected_child.append(
                        {"tag": selected_element_key, "value": selected_element_value}
                    )
                else:
                    continue

            end_result.append(selected_child)
        return end_result