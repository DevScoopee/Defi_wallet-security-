import re
import sys

def validate_evm_address(address):
    """
    Validates EVM (Ethereum/BNB) addresses to prevent typo-squatting 
    and basic clipboard-hijacking phishing attempts in DeFi transactions.
    """
    # Standard regex for EVM compatible addresses (0x followed by 40 hex chars)
    pattern = re.compile(r"^0x[a-fA-F0-9]{40}$")
    
    print(f"[*] Analyzing target wallet address: {address}\n")
    
    if pattern.match(address):
        print("[+] STATUS: Valid EVM address format detected.")
        print("[!] Note: This does not guarantee the address belongs to a trusted entity.")
        return True
    else:
        print("[-] CRITICAL WARNING: Invalid address format detected!")
        print("[-] Threat Vector: Potential clipboard hijacking or typo-squatting.")
        print("[-] ACTION REQUIRED: Halt transaction immediately.\n")
        return False

if __name__ == "__main__":
    # Default test vector
    target = "0x71C7656EC7ab88b098defB751B7401B5f6d8976F" 
    
    if len(sys.argv) > 1:
        target = sys.argv[1]
        
    validate_evm_address(target)
      
