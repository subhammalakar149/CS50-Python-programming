    # TODO: Check for command-line usage
if len(sys.argv) != 3:
    print("Usage: python dna.py csv_file txt_file.", file=sys.stderr)
    sys.exit(1)

csv_file_name = sys.argv[1]
txt_file_name = sys.argv[2]

    # TODO: Read database file into a variable
try:
    with open(csv_file_name, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        ref = [row for row in csv_reader]
except (OSError, PermissionError, FileNotFoundError) as e:
    print(e)
    sys.exit(1)

    # TODO: Read DNA sequence file into a variable
try:
    with open(txt_file_name, "r") as txt_file:
        contents = txt_file.read()
        contents_length = len(contents)
except (OSError, PermissionError, FileNotFoundError) as e:
    print(e)
    sys.exit(1)

count = {k:0 for k in ref[0][1::]}

for key in count.keys():
    local_count = 0
    i = 0
    while i < contents_length:
        step = 1
        flag = False
        key_length = len(key)
        seq_end = i + key_length
        if seq_end < contents_length and key == contents[i:seq_end]:
            local_count = local_count + 1
            step = key_length
        else:
            if local_count > count[key]:
                count[key] = local_count
            local_count = 0
        i = i + step

    # TODO: Find longest match of each STR in DNA sequence
max_count = [str(v) for _, v in count.items()]

    # TODO: Check database for matching profiles
for r in ref[1::]:
    if r[1::] == max_count:
        print(r[0])
        break
    elif r == ref[-1]:
        print("No match")
