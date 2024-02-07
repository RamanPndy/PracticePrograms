class JSONParser:
    '''
    JSONParser class provides a static method parse to parse a JSON string into a Python dictionary.
    The parser iterates over each character in the JSON string and builds the corresponding dictionary.
    It uses a stack to keep track of nested objects.
    It handles key-value pairs, nested objects, and simple values.
    '''
    @staticmethod
    def parse(json_string):
        stack = []
        current_object = {}
        key = None
        value = ""
        for char in json_string:
            if char == "{":
                if key:
                    current_object[key] = value.strip()
                stack.append(current_object)
                current_object = {}
                key = None
                value = ""
            elif char == "}":
                if key:
                    current_object[key] = value.strip()
                if stack:
                    parent = stack.pop()
                    parent.update(current_object)
                    current_object = parent
                key = None
                value = ""
            elif char == ":":
                key = value.strip()
                value = ""
            elif char == ",":
                if key:
                    current_object[key] = value.strip()
                key = None
                value = ""
            else:
                value += char
        return current_object
    
    def parse(self, json_string):
        self.json_string = json_string
        self.index = 0
        return self.parse_value()

    def parse_value(self):
        current_char = self.json_string[self.index]

        if current_char == '{':
            return self.parse_object()
        elif current_char == '[':
            return self.parse_array()
        elif current_char == '"':
            return self.parse_string()
        elif current_char.isdigit() or current_char == '-':
            return self.parse_number()
        elif current_char == 't':
            return self.parse_true()
        elif current_char == 'f':
            return self.parse_false()
        elif current_char == 'n':
            return self.parse_null()
        else:
            raise ValueError("Invalid JSON")

    def parse_object(self):
        obj = {}
        self.index += 1
        while self.json_string[self.index] != '}':
            key = self.parse_string()
            self.index += 1  # skip the colon
            value = self.parse_value()
            obj[key] = value
            if self.json_string[self.index] == ',':
                self.index += 1
        self.index += 1  # skip the closing brace
        return obj

    def parse_array(self):
        arr = []
        self.index += 1
        while self.json_string[self.index] != ']':
            value = self.parse_value()
            arr.append(value)
            if self.json_string[self.index] == ',':
                self.index += 1
        self.index += 1  # skip the closing bracket
        return arr

    def parse_string(self):
        start_index = self.index
        self.index += 1
        while self.json_string[self.index] != '"':
            self.index += 1
        end_index = self.index
        self.index += 1  # skip the closing quote
        return self.json_string[start_index + 1:end_index]

    def parse_number(self):
        start_index = self.index
        while self.json_string[self.index].isdigit() or self.json_string[self.index] in ['-', '.', 'e', 'E']:
            self.index += 1
        end_index = self.index
        return float(self.json_string[start_index:end_index])

    def parse_true(self):
        self.index += 4
        return True

    def parse_false(self):
        self.index += 5
        return False

    def parse_null(self):
        self.index += 4
        return None

# Example usage
if __name__ == "__main__":
    json_string = '{"name": "John", "age": 30, "city": "New York"}'
    parsed_json = JSONParser.parse(json_string)
    print(parsed_json)
