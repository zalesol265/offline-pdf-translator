# import sys  
# import json  

# arguments = sys.argv[1:]

# name = arguments[0]
# arg1 = arguments[1]
# arg2 = arguments[2]

# # Create sentences
# sentence1 = "Hello, {}! Greetings from Python!".format(name)
# sentence2 = "The first arg is {} and the second is {}".format(arg1, arg2)
# # Create a dictionary to represent the JSON object
# json_data = {
#     "greeting": sentence1,
#     "arguments": sentence2
# }

# # Convert the dictionary to JSON format
# json_output = json.dumps(json_data)

# # Print the JSON output
# print(json_output)

import sys
import argostranslate.package
import argostranslate.translate
# from translation import argos_translate, download_argos_language

def download_argos_language(from_code, to_code):
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())


def argos_translate(input_text, input_lang, output_lang):
    translatedText = argostranslate.translate.translate(input_text, input_lang, output_lang)
    return translatedText


def translate(args):
    input_text = args[2]
    input_lang = args[3]
    output_lang = args[4]
    response = argos_translate(input_text, input_lang, output_lang)
    print(response)


def add_language(args):
    input_lang = args[2]
    output_lang = args[3]
    download_argos_language(input_lang, output_lang)


def process_option_c():
    print("Processing option C")


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py [option]")
        sys.exit(1)

    option = sys.argv[1]

    # Define a mapping between options and functions
    options_mapping = {
        'translate': translate,
        'add_language': add_language,
        'C': process_option_c,
    }

    # Check if the provided option is in the mapping
    if option in options_mapping:
        # Call the corresponding function
        options_mapping[option](sys.argv)
    else:
        print(f"Invalid option: {option}")

if __name__ == "__main__":
    print("starting test.py...")
    main()
