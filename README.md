# ec551-logic-synthesis-engine

## truth table representation

{'inputs': ['A', 'B', 'C'], 'rows': [((0, 0, 0), 0), ((0, 0, 1), 1), ((0, 1, 0), 0), ((0, 1, 1), 1), ((1, 0, 0), 0), ((1, 0, 1), 1), ((1, 1, 0), 1), ((1, 1, 1), 1)]}

## JSON Structure

Accepts a JSON file describing a single-output combinational logic circuit in the following structure:

```
{
    "nodes": [
        {"id": "(gate id)", "type": "(specific logic gate in all caps)", "inputs": ["list of inputs"]},
        ......
    ]
}
```

The gates that it supports are:
- AND
- OR
- NOT
- NAND
- NOR
- XOR
- XNOR