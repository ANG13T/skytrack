from rich.console import Console

ICAO_LENGTH = 6           # length of an ICAO designator
TAIL_NUMBER_LENGTH = 6    # maxiumum length of a tail number

ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ" # list of available characters for tail number
NUMBERS = "0123456789"
HEX_VALUES = "0123456789ABCDEF"
CHARACTERS = ALPHABET + NUMBERS
ICAO_PREFIX = 'a' # ICAO designators always start with a

SUFFIX_SIZE = 1 + len(ALPHABET) * (1 + len(ALPHABET)) 
SEGMENT4_SIZE = len(ALPHABET) + len(NUMBERS) + 1
SEGMENT3_SIZE = len(NUMBERS) * SEGMENT4_SIZE + SUFFIX_SIZE
SEGMENT2_SIZE = len(NUMBERS)*(SEGMENT3_SIZE) + SUFFIX_SIZE
SEGMENT1_SIZE = len(NUMBERS)*(SEGMENT2_SIZE) + SUFFIX_SIZE

icao_offset = 0xA00001 # this is the lowest possible number a ICAO designator can have

console = Console()

def generate_icao(prefix, number):
    # This creates an ICAO number in hex from a number and a prefix (works only for US)
    suffix = hex(number)[2:]
    total_length = len(prefix) + len(suffix)
    if total_length > ICAO_LENGTH: # validating ICAO length
        return None
    else:
        return prefix + '0' * (ICAO_LENGTH-total_length) + suffix


def compute_offset_from_suffix(suffix):
    """
    ''   -> 0
    'A'  -> 1
    'AA' -> 2
    'AB' -> 3
    'AC' -> 4
    """
    if len(suffix) == 0:
        return 0
    
    is_valid = True

    if len(suffix) > 2:
        is_valid = False
    else:
        for char in suffix:
            if char not in ALPHABET:
                is_valid = False
                break

    if is_valid == False:
        console.print(f"\n[bold][red] INVALID SUFFIX FOR TAIL NUMBER [/red][/bold]")
        return None

    count = (len(ALPHABET)+1) * ALPHABET.index(suffix[0]) + 1

    if len(suffix) == 2:
        count += ALPHABET.index(suffix[1]) + 1

    return count

def icao_to_tail():
    return

def tail_to_icao(tail_value):
    tail_value = tail_value.upper()

    is_valid = True

    if tail_value[0] != "N" or len(tail_value) == 0 or len(tail_value) > TAIL_NUMBER_LENGTH:
        is_valid = False
    else:
        for char in tail_value:
            if char not in CHARACTERS:
                is_valid = False
                break
        # Ensure that the tail format adheres to standards
        if is_valid and len(tail_value) > 3:
            # middle section of tail number can only be digits
            for val in range(1, len(tail_value) - 2):
                if tail_value[val] in ALPHABET:
                    is_valid = False
                    break

    if is_valid == False:
        console.print(f"\n[bold][red] INVALID TAIL NUMBER [/red][/bold]")
        return
    
    count = 1
    if len(tail_value) > 1:
        tail_value = tail_value[1:] # N is redundant
        for i in range(len(tail_value)):
            if i == 4:
                count += CHARACTERS.index(tail_value[i])+1
            elif tail_value[i] in ALPHABET:
                count += compute_offset_from_suffix(tail_value[i:])
                break
            else:
                # numerical values within tail number
                if i == 0:
                    count += (int(tail_value[i])-1) * SEGMENT1_SIZE
                elif i == 1:
                    count += int(tail_value[i]) * SEGMENT2_SIZE + SUFFIX_SIZE
                elif i == 2:
                    count += int(tail_value[i]) * SEGMENT3_SIZE + SUFFIX_SIZE
                elif i == 3:
                    count += int(tail_value[i]) * SEGMENT4_SIZE + SUFFIX_SIZE

    return generate_icao(ICAO_PREFIX, count)
    
def print_tail_to_icao(tail_value):
    generated_value = tail_to_icao(tail_value)
    if generated_value != None:
        console.print(f"\n[bold][red] ICAO Designation: {generated_value} [/red][/bold]")
    else:
        console.print(f"\n[bold][red] INVALID TAIL NUMBER [/red][/bold]")
