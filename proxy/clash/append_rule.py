# open the file for reading

# clash configuration file to be modified
# conf_file = "v2club.yaml"
conf_file = "/Users/hongde/.config/clash/v2club.yaml"

# custom rules maintained by myself
custom_rule_file = "custom_rule.yaml"

# define the pattern to match
pattern = "    - 'GEOIP,CN,"


def read_custom_rule(custom_rule_file):
    # Open the file for reading
    with open(custom_rule_file, "r") as f:
        # Read the contents of the file into a string variable
        custom_rule = f.read()
    # Print the file contents
    print(">>> custom rules: \n")
    print(custom_rule)
    return custom_rule


def modify_configuration_file(custom_rule, pattern):
    with open(conf_file, "r") as f:
        content = f.read()

    # trailing comment
    begin_comment = "\n    # ########## custom rule begin ##########\n"
    end_comment = "\n    # ########## custom rule end ##########\n\n"
    custom_rule = "{}{}{}".format(begin_comment, custom_rule, end_comment)
    # insert the variables before the pattern
    new_content = content.replace(pattern, f"{custom_rule}{pattern}")

    print(">>> modified rules: \n")
    print(new_content)

    # open the file for writing and write the new content
    with open(conf_file, "w") as f:
        f.write(new_content)
        pass


custom_rule = read_custom_rule(custom_rule_file)
modify_configuration_file(custom_rule, pattern)

# copy modified rules
# python3 append_rule.py | grep -A 1000000 ">>> modified rules" | grep -v "modified rules" | pbcopy