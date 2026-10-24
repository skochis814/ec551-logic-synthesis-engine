module fpga_top(
    input [4:0] switches,
    output led
);

    synthesized_logic circuit(
        .A(switches[0]),
        .B(switches[1]),
        .C(switches[2]),
        .D(switches[3]),
        .E(switches[4]),
        .F(led)
    );

endmodule