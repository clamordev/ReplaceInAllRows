import re
import argparse

def __replace_in_all_rows(row, replacements) -> str:
    for replacement in replacements:
        old_value = replacement[0]
        new_value = replacement[1] if len(replacement) > 1 else ''
        row = row.replace(old_value, new_value)

    if delims:
        row = re.sub(r"([\-_.:,;|/\\?&@#%^*!~()\[\]]){2,}", lambda m: m.group(0)[0], row)

    if remove_edge_delims:
        row = row[1:] if row and row[0] in '-_.:,;|/\\?&@#%^*!~()[]' else row
        row = row[:-1] if row and row[-1] in '-_.:,;|/\\?&@#%^*!~()[]' else row
    
    return row.strip()

def main() -> None:
    """
    Main function to perform text replacement in all given rows based on input and 
    replacement files. This script reads input rows from a file and applies a series 
    of text replacements defined in another file. It supports optional collapsing of 
    delimiters and removal of edge delimiters.
    Arguments:
        -r, --remove-edge-delims : A flag to indicate whether to remove delimiters
            from the edges of the rows. Defaults to False.
        -c, --collapse-delims : A flag to collapse multiple consecutive matches
            of any common delimiter into a single one. Defaults to False.
    """
    parser = argparse.ArgumentParser(description="Replace text in rows. Use an empty string for deletion.")
    parser.add_argument('-r', '--remove-edge-delims', action='store_true', 
                        help="Remove delimiters from the edges of the rows.")
    parser.add_argument('-c', '--collapse-delims', action='store_true', 
                        help="Collapse multiple consecutive matches of delimiters into one.")
    args = parser.parse_args()

    global delims, remove_edge_delims
    delims = args.collapse_delims if args.collapse_delims else False
    remove_edge_delims = args.remove_edge_delims if args.remove_edge_delims else False

    print('*********************************')
    print('*     BEGIN Replace in Rows     *')
    print('*********************************')

    with open('input.txt', 'r') as input_file:
        input = [line.strip() for line in input_file if not line.strip().startswith('#')]
        input_file.close()
    with open('replacements.txt', 'r') as replacements_file:
        replacements = [line.split() for line in replacements_file if not line.strip().startswith('#')]
        replacements_file.close()
    
    if not input:
        print('No input data found.')
        return
    if not replacements:
        print('No replacements found.')
        return

    print('\nInput:', *(f"  [{row}]" for row in input), sep='\n')
    print('\nReplacements:', *(f"  {row}" for row in replacements), sep='\n')

    print('\nProcessing replacements...')
    output = list(map(lambda row: __replace_in_all_rows(row, replacements), input))
    print('Processing replacements OK.')

    print('\nWriting output to "output.txt"...')
    with open('output.txt', 'w') as output_file:
        for row in output:
            output_file.write(row + '\n')
        output_file.close()
    print('Writing output OK.\n')

    print('*********************************')
    print('*      END Replace in Rows      *')
    print('*********************************')


if __name__ == '__main__':
    main()
