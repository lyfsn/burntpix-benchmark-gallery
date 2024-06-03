import os
import random
import subprocess

def generate_random_parameters():
    uint32_seed = random.randint(0, 2**32 - 1)
    # uint256_iter = random.randint(0, 2**256 - 1)
    uint256_iter = random.randint(100000, 1000000)
    return uint32_seed, uint256_iter

def to_hex_string(value, length):
    return f'{value:0{length}x}'

def run_command_and_save_svg(uint32_hex, uint256_hex):
    input_data = f'0xa4de9ab4{uint32_hex}{uint256_hex}'
    
    command = (
        f'./evm run --prestate ./genesis.json --receiver 0x49206861766520746F6F206D7563682074696D65 '
        f'--input {input_data} | tail -c +131 | sed \'s/[0]*$//\' | xxd -r -p > imgs/{uint32_hex}_{uint256_hex}.svg'
    )
    
    subprocess.run(command, shell=True)

def main():
    os.makedirs('imgs', exist_ok=True)
    
    for _ in range(100): 
        uint32_seed, uint256_iter = generate_random_parameters()
        uint32_hex = to_hex_string(uint32_seed, 64)
        uint256_hex = to_hex_string(uint256_iter, 64)
        print(f'[{uint32_hex}, {uint256_hex}]')
        run_command_and_save_svg(uint32_hex, uint256_hex)

if __name__ == '__main__':
    main()