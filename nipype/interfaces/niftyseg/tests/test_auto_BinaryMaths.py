# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..maths import BinaryMaths


def test_BinaryMaths_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='%s',
            mandatory=True,
            position=2,
        ),
        operand_file=dict(
            argstr='%s',
            mandatory=True,
            position=5,
            xor=['operand_value', 'operand_str'],
        ),
        operand_str=dict(
            argstr='%s',
            mandatory=True,
            position=5,
            xor=['operand_value', 'operand_file'],
        ),
        operand_value=dict(
            argstr='%.8f',
            mandatory=True,
            position=5,
            xor=['operand_file', 'operand_str'],
        ),
        operation=dict(
            argstr='-%s',
            mandatory=True,
            position=4,
        ),
        out_file=dict(
            argstr='%s',
            name_source=['in_file'],
            name_template='%s',
            position=-2,
        ),
        output_datatype=dict(
            argstr='-odt %s',
            position=-3,
        ),
    )
    inputs = BinaryMaths.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_BinaryMaths_outputs():
    output_map = dict(out_file=dict(), )
    outputs = BinaryMaths.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
