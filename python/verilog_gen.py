from .minimization import minimize

def generate_verilog(truth_table):
    minimized = minimize(truth_table, False)
    inputs = truth_table["inputs"]

    lines = []
    lines.append(
        "module synthesized_logic(input "
        + ", ".join(inputs)
        + ", output F);"
    )

    inverted = []
    for term in minimized:
        for i in range(len(term)):
            if term[i] == "0" and inputs[i] not in inverted:
                inverted.append(inputs[i])

    for variable in inverted:
        lines.append("wire inv_" + variable + ";")

    term_outputs = []
    gates = []

    for i in range(len(minimized)):
        signals = []

        for j in range(len(minimized[i])):
            if minimized[i][j] == "1":
                signals.append(inputs[j])
            elif minimized[i][j] == "0":
                signals.append("inv_" + inputs[j])

        if len(signals) == 0:
            term_outputs.append("1'b1")
        elif len(signals) == 1:
            term_outputs.append(signals[0])
        else:
            output = "term_" + str(i)
            lines.append("wire " + output + ";")
            gates.append(
                "and (" + output + ", " + ", ".join(signals) + ");"
            )
            term_outputs.append(output)

    for variable in inverted:
        lines.append("not (inv_" + variable + ", " + variable + ");")

    lines.extend(gates)

    if len(term_outputs) == 0:
        lines.append("assign F = 1'b0;")
    elif len(term_outputs) == 1:
        lines.append("assign F = " + term_outputs[0] + ";")
    else:
        lines.append("or (F, " + ", ".join(term_outputs) + ");")

    lines.append("endmodule")

    with open("generated.v", "w") as file:
        file.write("\n".join(lines))