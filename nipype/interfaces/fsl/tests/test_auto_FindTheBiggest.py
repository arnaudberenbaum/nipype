# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..dti import FindTheBiggest


def test_FindTheBiggest_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_files=dict(
            argstr='%s',
            mandatory=True,
            position=0,
        ),
        out_file=dict(
            argstr='%s',
            genfile=True,
            hash_files=False,
            position=2,
        ),
        output_type=dict(),
    )
    inputs = FindTheBiggest.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_FindTheBiggest_outputs():
    output_map = dict(out_file=dict(argstr='%s', ), )
    outputs = FindTheBiggest.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
