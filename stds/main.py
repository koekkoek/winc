# Do not modify these lines
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Add your code after this line
import sys


def main():
    if len(sys.argv) != 2:
        print("Exactly two arguments required")
        sys.exit()

    # TODO: read text from stdin
    text = sys.stdin.read()

    # TODO: Filter character given as an argument from the text
    try:
        extract = sys.argv[1]
    except IndexError:
        pass

    extract_count = text.count(extract)
    new_text = text.replace(extract, "")

    # TODO: Print the result to stdout
    sys.stdout.write(new_text)

    # TODO: Print the total number of removed characters to stderr
    sys.stderr.write(str(extract_count))


if __name__ == "__main__":
    main()
