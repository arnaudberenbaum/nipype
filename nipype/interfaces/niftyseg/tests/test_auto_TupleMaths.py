# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..maths import TupleMaths


def test_TupleMaths_inputs():
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
        operand_file1=dict(
            argstr='%s',
            mandatory=True,
            position=5,
            xor=['operand_value1'],
        ),
        operand_file2=dict(
            argstr='%s',
            mandatory=True,
            position=6,
            xor=['operand_value2'],
        ),
        operand_value1=dict(
            argstr='%.8f',
            mandatory=True,
            position=5,
            xor=['operand_file1'],
        ),
        operand_value2=dict(
            argstr='%.8f',
            mandatory=True,
            position=6,
            xor=['operand_file2'],
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
    inputs = TupleMaths.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_TupleMaths_outputs():
    output_map = dict(out_file=dict(), )
    outputs = TupleMaths.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
