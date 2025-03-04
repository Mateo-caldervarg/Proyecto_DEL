# Define the reactant and product SMILES
def rxn_to_smarts(rxn_file):
    # Load reaction from RXN file
    with open(rxn_file_path, "r") as file:
        rxn_block = file.read()
    
    reaction = rdChemReactions.ReactionFromRxnBlock(rxn_block)
    
    if reaction is None:
        raise ValueError("Invalid RXN file or unable to parse.")
    
    # Convert to SMARTS notation
    smarts_notation = rdChemReactions.ReactionToSmarts(reaction)
    
    return smarts_notation

# Example Usage:
rxn_file_path = "ketcher.rxn"  # Replace with your actual RXN file path
smarts = rxn_to_smarts(rxn_file_path)
print("SMARTS Notation:", smarts)
