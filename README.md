# MolEncoder

MolEncoder is a Python package for molecular representations and encodings. It provides tools for working with SMILES, SELFIES, molecular fingerprints, and various encoding methods.

## Installation

```bash
pip install molencoder
```

## Usage

```python
from molencoder import canonicalize_smiles, smiles_to_selfies, morgan_fingerprint, one_hot_encoding

# Example usage
smiles = "CC(=O)Nc1ccc(O)cc1"
print(canonicalize_smiles(smiles))
print(smiles_to_selfies(smiles))
print(morgan_fingerprint(smiles))
print(one_hot_encoding(smiles, ['C', '(', ')', '=', 'O', 'N', 'c', '1', 'O']))
```

For more examples, see the `examples/` directory.